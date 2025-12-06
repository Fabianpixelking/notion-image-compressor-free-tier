import os
import math
import subprocess
from PIL import Image

# Try to import imageio_ffmpeg to get the binary path
try:
    import imageio_ffmpeg
    FFMPEG_EXE = imageio_ffmpeg.get_ffmpeg_exe()
except ImportError:
    FFMPEG_EXE = None
    print("Warning: imageio-ffmpeg not found. Video compression will not work.")

def get_size_mb(file_path):
    """Returns the file size in megabytes."""
    return os.path.getsize(file_path) / (1024 * 1024)

def check_video_duration(file_path):
    """Returns the duration of the video in seconds using ffmpeg."""
    if not FFMPEG_EXE:
        return 0
    
    cmd = [FFMPEG_EXE, '-i', file_path]
    # ffmpeg prints info to stderr
    result = subprocess.run(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    
    # helper to parse "Duration: 00:00:05.12"
    for line in result.stderr.split('\n'):
        if "Duration" in line:
            # Example: "  Duration: 00:00:05.12, start: 0.000000, bitrate: 14785 kb/s"
            try:
                time_str = line.split("Duration:")[1].split(",")[0].strip()
                h, m, s = time_str.split(':')
                return float(h) * 3600 + float(m) * 60 + float(s)
            except:
                pass
    return 0

def compress_video(file_path, output_path, max_size_mb=4.9):
    """
    Compresses a video to be under the max_size_mb using ffmpeg.
    Target bitrate = (target_size_bits / duration_seconds) - audio_bitrate_allowance
    """
    if not FFMPEG_EXE:
        print(f"Skipping {os.path.basename(file_path)} (ffmpeg not found)")
        return

    current_size = get_size_mb(file_path)
    if current_size <= max_size_mb:
        print(f"Skipping {os.path.basename(file_path)} (already {current_size:.2f} MB)")
        # For video, copying might range from instant (copy) to slow-ish, 
        # but shutil.copy is better than re-encoding.
        import shutil
        shutil.copy2(file_path, output_path)
        return

    print(f"Compressing {os.path.basename(file_path)} ({current_size:.2f} MB)...")

    duration = check_video_duration(file_path)
    if duration <= 0:
        print(f"  -> Could not determine duration, skipping simple compression logic.")
        return

    # Algorithm to calculate bitrate
    # Target size in bits = MB * 1024 * 1024 * 8
    target_total_bits = max_size_mb * 1024 * 1024 * 8
    
    # We leave some headroom (e.g. 10%) because bitrate control isn't perfect
    target_total_bits *= 0.90
    
    total_bitrate = target_total_bits / duration # bits per second
    
    # Reasonable minimum bitrate (so we don't destroy short videos usually, but for 5MB limit we must adhere)
    # If the video is very long, bitrate will be tiny -> unwatchable.
    # But we must satisfy the requirement.
    
    # Let's clean up audio logic. Allocate 96k or 128k for audio if possible?
    # Actually, for very small files, we might need to go lower on audio.
    # Let's allocate ~10% to audio or fixed 64k/96k depending on total.
    
    audio_bitrate = 96 * 1000 # 96 kbps
    if total_bitrate < 200000: # If total allowed is < 200k, reduce audio
        audio_bitrate = 48 * 1000
    
    video_bitrate = total_bitrate - audio_bitrate
    
    if video_bitrate < 10000: # Extremely low bitrate safety
         # If we can't even give 10kbps to video, it's probably too long for the size target.
         # But let's try anyway or just cap minimum.
         video_bitrate = 10000
         
    # ffmpeg expects bits per second or k/M suffixes.
    
    cmd = [
        FFMPEG_EXE, '-y', # overwrite
        '-i', file_path,
        '-b:v', str(int(video_bitrate)),
        '-maxrate', str(int(video_bitrate)),
        '-bufsize', str(int(video_bitrate * 2)),
        '-b:a', str(int(audio_bitrate)),
        '-preset', 'medium', # 'slow' gives better quality for size but slower
        output_path
    ]
    
    # Suppress verbose output
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    new_size = get_size_mb(output_path)
    print(f"  -> Done! New size: {new_size:.2f} MB")


def compress_image(file_path, output_path, max_size_mb=4.9):
    """
    Compresses an image to be under the max_size_mb.
    """
    try:
        img = Image.open(file_path)
    except Exception as e:
        print(f"Error opening {file_path}: {e}")
        return

    # Check if file is already small enough
    if get_size_mb(file_path) <= max_size_mb:
        print(f"Skipping {os.path.basename(file_path)} (already {get_size_mb(file_path):.2f} MB)")
        img.save(output_path)
        return

    print(f"Compressing {os.path.basename(file_path)} ({get_size_mb(file_path):.2f} MB)...")

    file_ext = os.path.splitext(file_path)[1].lower()
    has_alpha = False
    if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
        has_alpha = True

    if file_ext in ['.png', '.bmp', '.tiff', '.tif']:
        if has_alpha:
            img_format = 'WEBP'
            output_path = os.path.splitext(output_path)[0] + '.webp'
            print(f"  -> Converting to WEBP to preserve transparency...")
        else:
            img_format = 'JPEG'
            output_path = os.path.splitext(output_path)[0] + '.jpg'
            img = img.convert('RGB')
            print(f"  -> Converting to JPEG to preserve resolution...")
    else:
        format_mapping = {'.jpg': 'JPEG', '.jpeg': 'JPEG', '.webp': 'WEBP'}
        img_format = format_mapping.get(file_ext, 'JPEG')

    quality = 95
    min_quality = 10
    
    while quality >= min_quality:
        img.save(output_path, format=img_format, quality=quality, optimize=True)
        current_size = get_size_mb(output_path)
        
        if current_size <= max_size_mb:
            print(f"  -> Done! New size: {current_size:.2f} MB (Quality: {quality})")
            return
        
        quality -= 5
    
    print(f"  -> Quality reduction insufficient, resizing...")
    scale = 0.9
    while True:
        new_width = int(img.width * scale)
        new_height = int(img.height * scale)
        if new_width < 100 or new_height < 100:
            print("  -> Could not compress enough.")
            break
            
        resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        resized_img.save(output_path, format=img_format, quality=min_quality, optimize=True)
        
        if get_size_mb(output_path) <= max_size_mb:
            print(f"  -> Done! New size: {get_size_mb(output_path):.2f} MB (Resized)")
            return
        
        scale *= 0.9

def main():
    input_folder = "input"
    output_folder = "output"

    if not os.path.exists(input_folder):
        print(f"Error: Folder '{input_folder}' does not exist.")
        return

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    img_exts = {'.jpg', '.jpeg', '.png', '.webp', '.bmp', '.tiff', '.tif'}
    vid_exts = {'.mp4', '.mov', '.avi', '.mkv', '.webm'}
    
    files = os.listdir(input_folder)
    
    if not files:
        print(f"No files found in '{input_folder}'.")
        return

    processed_count = 0
    for file in files:
        file_ext = os.path.splitext(file)[1].lower()
        input_path = os.path.join(input_folder, file)
        output_path = os.path.join(output_folder, file)
        
        if file_ext in img_exts:
            processed_count += 1
            compress_image(input_path, output_path)
        elif file_ext in vid_exts:
            processed_count += 1
            compress_video(input_path, output_path)

    if processed_count == 0:
        print("No supported image or video files found.")
    else:
        print("\nAll done! Check the 'output' folder.")

if __name__ == "__main__":
    main()
