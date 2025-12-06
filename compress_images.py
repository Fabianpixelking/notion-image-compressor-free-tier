import os
from PIL import Image
import math

def get_size_mb(file_path):
    """Returns the file size in megabytes."""
    return os.path.getsize(file_path) / (1024 * 1024)

def compress_image(file_path, output_path, max_size_mb=4.9):
    """
    Compresses an image to be under the max_size_mb.
    """
    # Open the image
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

    # Initial quality
    quality = 95
    
    # Save to a temporary buffer or file to check size? 
    # We'll just save to the output path and check size.
    
    # Convert to RGB if necessary (e.g. for PNGs we might want to convert to JPG if we really need to compress, 
    # but let's try to keep format if possible. However, compressing PNGs by quality isn't always straightforward 
    # with save(). JPG is better for lossy compression.
    # The user didn't specify format conversion, but usually "compress to X MB" implies lossy.
    # Let's assume we keep the format if supported, but for PNG, 'quality' param works differently or not at all for some.
    # If it's a PNG and too big, we might need to resize or convert to JPEG. 
    # Let's try to stick to the original format first, but if it's PNG, we might have to resize.
    
    file_ext = os.path.splitext(file_path)[1].lower()
    format_mapping = {
        '.jpg': 'JPEG', '.jpeg': 'JPEG', 
        '.png': 'PNG', 
        '.webp': 'WEBP', 
        '.bmp': 'BMP', 
        '.tiff': 'TIFF', '.tif': 'TIFF'
    }
    img_format = format_mapping.get(file_ext, 'JPEG')

    if img_format == 'PNG':
        # PNG compression is lossless usually, optimizing it is harder. 
        # If we really need to hit a target size, resizing is the main lever, or reducing colors (quantization).
        # For this script, let's try resizing if it's too big.
        pass
    
    # Iterative compression
    min_quality = 10
    
    while quality >= min_quality:
        img.save(output_path, format=img_format, quality=quality, optimize=True)
        if get_size_mb(output_path) <= max_size_mb:
            print(f"  -> Done! New size: {get_size_mb(output_path):.2f} MB (Quality: {quality})")
            return
        quality -= 5
    
    # If quality reduction isn't enough, we start resizing
    print("  -> Quality reduction insufficient, resizing...")
    scale = 0.9
    while True:
        new_width = int(img.width * scale)
        new_height = int(img.height * scale)
        if new_width < 100 or new_height < 100:
            print("  -> Could not compress enough without making it too small.")
            break
            
        resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        resized_img.save(output_path, format=img_format, quality=min_quality, optimize=True)
        
        if get_size_mb(output_path) <= max_size_mb:
            print(f"  -> Done! New size: {get_size_mb(output_path):.2f} MB (Resized to {new_width}x{new_height})")
            return
        
        scale *= 0.9

def main():
    input_folder = "input"
    output_folder = "output"

    if not os.path.exists(input_folder):
        print(f"Error: Folder '{input_folder}' does not exist.")
        print(f"Please create a folder named '{input_folder}' and place your images inside.")
        return

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    supported_exts = {'.jpg', '.jpeg', '.png', '.webp', '.bmp', '.tiff', '.tif'}
    
    files = [f for f in os.listdir(input_folder) if os.path.splitext(f)[1].lower() in supported_exts]
    
    if not files:
        print(f"No image files found in '{input_folder}'.")
        return

    print(f"Found {len(files)} images.")
    
    for file in files:
        input_path = os.path.join(input_folder, file)
        output_path = os.path.join(output_folder, file)
        compress_image(input_path, output_path)

    print("\nAll done! Check the 'output' folder.")

if __name__ == "__main__":
    main()
