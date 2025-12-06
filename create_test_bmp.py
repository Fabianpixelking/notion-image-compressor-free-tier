from PIL import Image
import os
import random

def create_large_bmp(filename):
    width, height = 2000, 2000 # BMPs are uncompressed usually, so this will be big. 2000*2000*3 bytes approx 12MB.
    img = Image.new('RGB', (width, height), color='blue')
    
    pixels = img.load()
    for i in range(0, width, 10):
        for j in range(0, height, 10):
            pixels[i, j] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            
    if not os.path.exists('input'):
        os.makedirs('input')
        
    path = os.path.join('input', filename)
    img.save(path)
    print(f"Created {path} with size {os.path.getsize(path) / (1024*1024):.2f} MB")

if __name__ == "__main__":
    create_large_bmp("test_large.bmp")
