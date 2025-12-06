import imageio_ffmpeg
import subprocess
import os

exe = imageio_ffmpeg.get_ffmpeg_exe()
print(f"FFmpeg exe: {exe}")

if not os.path.exists("input"):
    os.makedirs("input")

# Generate a 10 second video
# ffmpeg -f lavfi -i testsrc=duration=10:size=1280x720:rate=30 -c:v libx264 -b:v 10M input/test_large.mp4
# 10M bitrate should result in ~12MB file, which is > 5MB.

cmd = [
    exe, '-y',
    '-f', 'lavfi',
    '-i', 'testsrc=duration=10:size=1280x720:rate=30',
    '-c:v', 'libx264',
    '-b:v', '10M',
    'input/test_large.mp4'
]

subprocess.run(cmd)
print("Generated input/test_large.mp4")
