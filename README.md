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

## 🛠️ Installation & Usage (Beginner Guide)

Follow these steps to get started, even if you've never used Python before.

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

### 3. Install Dependencies
1.  Open the folder where you extracted the files.
2.  Double-click the **`install_dependencies.bat`** file.
3.  A black window will appear and install the necessary software. Press any key when it says "Press any key to continue...".

### 4. Compress Your Images
1.  **Add Images**: Create a folder named `input` inside the tool's folder and put your large images there.
2.  **Run Tool**: Double-click **`run_compressor.bat`**.
3.  **Wait**: The tool will process your images.
4.  **Done**: Open the `output` folder to find your compressed images!

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
