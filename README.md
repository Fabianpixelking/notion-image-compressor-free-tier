# Notion Image & Video Compressor for Free Tier (Under 5MB)

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.x-blue.svg)

**Bypass Notion's 5MB upload limit** with this free, open-source image and video compression tool.

**Notion Image Compress for Free Tier** is a powerful Python utility designed to automatically compress and resize your images to fit perfectly within the Notion Free Tier's 5MB file size restriction. Whether you are a student, blogger, or productivity enthusiast, this tool ensures your high-quality visuals make it into your workspace without errors.

## ⚡ Quick Start

1.  **Download**: Click **Code** > **Download ZIP** and extract it.
2.  **Install**: Double-click **`Setup.bat`** to create the shortcuts and icons.
3.  **Add Images**: Place your images in the **`input`** folder.
4.  **Run**: Double-click **`Start Compressor`**.
5.  **Done**: Get your optimized images from the **`output`** folder.
6.  **Cleanup**: Double-click **`Reset & Clear`** to empty the folders for next time.

---

## 📋 Table of Contents

-   [Features](#-features)
-   [Installation & Detailed Usage](#-installation--detailed-usage)
-   [How It Works](#-how-it-works)
-   [Troubleshooting](#-troubleshooting)
-   [Contributing](#-contributing)
-   [License](#-license)

---

## 🚀 Features

-   **Notion 5MB Limit Solver**: Specifically tuned to keep files under 4.9MB.
-   **Bulk Image Compression**: Process hundreds of photos in seconds.
-   **Smart Optimization**: Intelligently reduces quality first, then resizes only if necessary to preserve maximum detail.
-   **Multi-Format Support**: Works with **Images (JPG, PNG, WEBP, etc.)** and **Videos (MP4, MOV, AVI, etc.)**.
-   **Zero Cost**: Completely free alternative to paid image optimizers.
-   **Privacy Focused**: Runs locally on your computer—no uploading images to third-party servers.

## 🛠️ Installation & Detailed Usage

If the Quick Start wasn't enough, here is the step-by-step guide.

### 1. Install Python
1.  Go to the [Python Download Page](https://www.python.org/downloads/).
2.  Download the latest version for Windows.
3.  Run the installer. **IMPORTANT**: On the first screen, check the box that says **"Add Python to PATH"**.
4.  Click "Install Now".

### 2. Download the Tool
1.  Scroll to the top of this page.
2.  Click the green **Code** button.
3.  Select **Download ZIP**.
4.  Extract the ZIP file to a folder on your computer (e.g., on your Desktop).

### 3. Compress Your Images
1.  **Add Images**: Open the **`input`** folder inside the tool's directory. Drag and drop all your large images here.
2.  **Run Tool**: Double-click **`Start Compressor`**.
3.  **Wait**: The tool will process your images (first time might take a moment to set up).
4.  **Done**: Open the **`output`** folder to find your compressed images!

## ⚙️ How It Works

This script uses the advanced **Pillow (PIL)** library to optimize file size:
1.  **Analysis**: Checks if the image exceeds the 4.9MB threshold.
2.  **Format Conversion**: If the file is a lossless format (PNG, BMP, TIFF), it first tries converting to JPEG (or WEBP) to reduce size while **preserving resolution**.
3.  **Quality Optimization**: Iteratively reduces quality (95% -> 10%) to reduce size without visible loss.
4.  **Smart Resizing**: If quality reduction isn't enough, it incrementally scales down the image dimensions until it fits.

## ❓ Troubleshooting

**"Python is not recognized..."**
-   You likely didn't check **"Add Python to PATH"** during installation. Reinstall Python and make sure to check that box.

**The window closes immediately**
-   Try running `install_dependencies.bat` first. If that doesn't work, open a command prompt in the folder and run `python compress_images.py` manually to see the error message.

**My PNG became a JPG**
-   This is intentional! To get under 5MB without shrinking the image dimensions (resolution), we convert lossless formats like PNG to efficient formats like JPEG.

## 🤝 Contributing

We welcome contributions! If you have ideas for better compression algorithms or new features, please submit a Pull Request or open an Issue.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---
*Keywords: notion image resize, compress image for notion, notion 5mb limit, free tier notion hack, bulk image compressor python, reduce image size, optimize images for web, free image optimizer.*
