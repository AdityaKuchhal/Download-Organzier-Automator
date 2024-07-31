# Download Organizer Automator

This script automatically organizes files in your download directory into specific folders based on their file type.

## Requirements
- Python 3.x
- watchdog library

## Installation
1. Install Python: Ensure you have Python 3 installed on your system. You can download it from python.org.

2. Install watchdog: Use pip to install the watchdog library.

```bash
pip install watchdog
```
## Usage
1. Clone or download the repository: Ensure you have the fileAutomator.py script in your desired location.

2. Edit the script:

  - Open the fileAutomator.py script in a text editor.
  - Set the source_dir to the directory you want to monitor (e.g., your Downloads folder).
  - Set the dest_dirs dictionary to specify the destination directories for different file types.

3. Run the script:

- Execute the script using Python.
```bash
python fileAutomator.py
```

## How It Works
- The script monitors the specified source_dir for any modifications.
- When a file is added or modified in the source_dir, the script checks the file extension and moves it to the appropriate directory in dest_dirs.
- If a file with the same name already exists in the destination directory, the script generates a unique name to avoid overwriting.
## Logging
- The script logs all file movements, including the source file name and its new location.
- Logs are displayed in the console with timestamps.
## File Types Supported
- **Audio**: .m4a, .flac, .mp3, .wav, .wma, .aac
- **Video**: .webm, .mpg, .mp2, .mpeg, .mpe, .mpv, .ogg, .mp4, .mp4v, .m4v, .avi, .wmv, .mov, .qt, .flv, .swf, .avchd
- **Image**: .jpg, .jpeg, .jpe, .jif, .jfif, .jfi, .png, .gif, .webp, .tiff, .tif, .psd, .raw, .arw, .cr2, .nrw, .k25, .bmp, .dib, .heif, .heic, .ind, .indd, .indt, .jp2, .j2k, .jpf, .jpx, .jpm, .mj2, .svg, .svgz, .ai, .eps, .ico
- **Documents**: .doc, .docx, .odt, .pdf, .xls, .xlsx, .ppt, .pptx
## Customization
- You can add more file types and corresponding directories by editing the file_extensions dictionary and dest_dirs dictionary in the script.
## License
This project is open-source and available under the MIT License.
