from PIL import Image
import os
import random

def create_large_png(filename):
    width, height = 3000, 3000
    img = Image.new('RGB', (width, height), color='green')
    
    pixels = img.load()
    for i in range(0, width, 5):
        for j in range(0, height, 5):
            pixels[i, j] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            
    if not os.path.exists('input'):
        os.makedirs('input')
        
    path = os.path.join('input', filename)
    img.save(path)
    print(f"Created {path} with size {os.path.getsize(path) / (1024*1024):.2f} MB")

if __name__ == "__main__":
    create_large_png("test_large.png")
