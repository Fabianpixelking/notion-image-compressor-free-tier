from PIL import Image
import os

def create_large_png(filename):
    width, height = 3000, 3000
    # 3000*3000*3 = ~27MB raw.
    data = os.urandom(width * height * 3)
    img = Image.frombytes('RGB', (width, height), data)
    
    if not os.path.exists('input'):
        os.makedirs('input')
        
    path = os.path.join('input', filename)
    img.save(path)
    print(f"Created {path} with size {os.path.getsize(path) / (1024*1024):.2f} MB")

if __name__ == "__main__":
    create_large_png("test_large_noise.png")
