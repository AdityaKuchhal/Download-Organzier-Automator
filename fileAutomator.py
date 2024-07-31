import os
import logging
from shutil import move
from time import sleep
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Directories
source_dir = "C:/Users/adity/Downloads"
dest_dirs = {
    "audio_sfx": "D:/O Downloads/Sound",
    "music": "D:/O Downloads/Music",
    "video": "D:/O Downloads/Videos",
    "image": "D:/O Downloads/Images",
    "documents": "D:/O Downloads/Docs"
}

# File extensions
file_extensions = {
    "audio": [".m4a", ".flac", ".mp3", ".wav", ".wma", ".aac"],
    "video": [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
              ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"],
    "image": [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", 
              ".arw", ".cr2", ".nrw", ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", 
              ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"],
    "documents": [".doc", ".docx", ".odt", ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]
}


def make_unique(dest, name):
    filename, extension = os.path.splitext(name)
    counter = 1
    while os.path.exists(os.path.join(dest, name)):
        name = f"{filename}({counter}){extension}"
        counter += 1
    return name


def move_file(dest, entry, name):
    # Ensure the destination directory exists
    if not os.path.exists(dest):
        os.makedirs(dest)

    if os.path.exists(os.path.join(dest, name)):
        name = make_unique(dest, name)
    move(entry.path, os.path.join(dest, name))


class MoverHandler(FileSystemEventHandler):
    def on_modified(self, event):
        with os.scandir(source_dir) as entries:
            for entry in entries:
                if entry.is_file():
                    name = entry.name
                    self.check_and_move_file(entry, name)

    def check_and_move_file(self, entry, name):
        ext = os.path.splitext(name)[1].lower()
        for category, extensions in file_extensions.items():
            if ext in extensions:
                if category == "audio":
                    dest = dest_dirs["audio_sfx"] if entry.stat().st_size < 10_000_000 or "SFX" in name else dest_dirs["music"]
                else:
                    dest = dest_dirs[category]
                move_file(dest, entry, name)
                logging.info(f"Moved {category} file: {name}")
                break


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, source_dir, recursive=True)
    observer.start()
    try:
        while True:
            sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
