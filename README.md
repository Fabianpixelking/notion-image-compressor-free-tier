# Notion Image Compressor for Free Tier (Under 5MB)

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.x-blue.svg)

**Bypass Notion's 5MB upload limit** with this free, open-source image compression tool.

**Notion Image Compress for Free Tier** is a powerful Python utility designed to automatically compress and resize your images to fit perfectly within the Notion Free Tier's 5MB file size restriction. Whether you are a student, blogger, or productivity enthusiast, this tool ensures your high-quality visuals make it into your workspace without errors.

## 🚀 Why Use This Tool?

-   **Notion 5MB Limit Solver**: Specifically tuned to keep files under 4.9MB.
-   **Bulk Image Compression**: Process hundreds of photos in seconds.
-   **Smart Optimization**: Intelligently reduces quality first, then resizes only if necessary to preserve maximum detail.
-   **Multi-Format Support**: Works with **JPG, JPEG, PNG, WEBP, BMP, and TIFF**.
-   **Zero Cost**: Completely free alternative to paid image optimizers.
-   **Privacy Focused**: Runs locally on your computer—no uploading images to third-party servers.

## 🛠️ Installation & Quick Start

Get started in minutes. No coding knowledge required.

### Prerequisites
-   [Python](https://www.python.org/downloads/) (Version 3.6 or higher)

### Step-by-Step Guide

1.  **Download the Tool**: Clone this repository or download the ZIP file.
2.  **Install Requirements**:
    Open your terminal/command prompt in the folder and run:
    ```bash
    pip install Pillow
    ```
3.  **Add Your Images**:
    Create a folder named `input` and drag all your large images into it.
4.  **Run Compression**:
    -   **Windows**: Double-click the `run_compressor.bat` file.
    -   **Mac/Linux**: Run `python compress_images.py` in your terminal.
5.  **Done!**: Find your optimized, Notion-ready images in the `output` folder.

## ⚙️ How It Works

This script uses the advanced **Pillow (PIL)** library to optimize file size:
1.  **Analysis**: Checks if the image exceeds the 4.9MB threshold.
2.  **Quality Optimization**: Iteratively reduces JPEG quality (95% -> 10%) to reduce size without visible loss.
3.  **Smart Resizing**: If quality reduction isn't enough, it incrementally scales down the image dimensions until it fits.

## 🤝 Contributing

We welcome contributions! If you have ideas for better compression algorithms or new features, please submit a Pull Request or open an Issue.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---
*Keywords: notion image resize, compress image for notion, notion 5mb limit, free tier notion hack, bulk image compressor python, reduce image size, optimize images for web, free image optimizer.*
