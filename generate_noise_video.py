import imageio_ffmpeg
import subprocess
import os

exe = imageio_ffmpeg.get_ffmpeg_exe()

cmd = [
    exe, '-y',
    '-f', 'lavfi',
    '-i', 'nullsrc=s=1280x720:d=5',
    '-vf', 'geq=random(1)*255:128:128',
    '-c:v', 'libx264',
    '-preset', 'ultrafast',
    '-b:v', '10M',
    'input/noise.mp4'
]

subprocess.run(cmd)
print("Generated input/noise.mp4")
