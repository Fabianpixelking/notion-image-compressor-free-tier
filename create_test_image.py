from PIL import Image
import os
import random

def create_large_image(filename):
    # Create a large image (e.g., 4000x4000) with random noise to ensure it's not easily compressible by default
    # and has some size.
    width, height = 5000, 5000
    img = Image.new('RGB', (width, height), color='red')
    
    # Add some noise or details to make it larger in file size
    pixels = img.load()
    for i in range(0, width, 10):
        for j in range(0, height, 10):
            pixels[i, j] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            
    # Save with high quality to ensure large size
    if not os.path.exists('input'):
        os.makedirs('input')
        
    path = os.path.join('input', filename)
    img.save(path, quality=100)
    print(f"Created {path} with size {os.path.getsize(path) / (1024*1024):.2f} MB")

if __name__ == "__main__":
    create_large_image("test_large.jpg")
