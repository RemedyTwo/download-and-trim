import os, re, subprocess, sys
from typing import List

FFMPEG_PATH = '"tools/ffmpeg.exe"'
FFPROBE_PATH = '"tools/ffprobe.exe"'
YOUTUBE_DL_PATH = '"tools/youtube-dl.exe"'

def main(link: str, beggining_timestamp: List[int], closing_timestamp: List[int]) -> None:
    id = re.search(".*(?:(?:youtu\.be\/|v\/|vi\/|u\/\w\/|embed\/)|(?:(?:watch)?\?v(?:i)?=|\&v(?:i)?=))([^#\&\?]*).*", link).group(1)
    print("ID: " + id)
    youtube_dl_command = YOUTUBE_DL_PATH + " -f22 -o " + id + ".mp4 " + link
    ffmpeg_command = FFMPEG_PATH + " -ss " + beggining_timestamp + " -to " + closing_timestamp + " -i " + id + ".mp4 tmp.mp4"
    print(youtube_dl_command)
    subprocess.call(youtube_dl_command, creationflags=subprocess.CREATE_NEW_CONSOLE)
    print(ffmpeg_command)
    subprocess.call(ffmpeg_command, creationflags=subprocess.CREATE_NEW_CONSOLE)
    os.remove(id + ".mp4")
    os.rename("tmp.mp4", id + ".mp4")

if __name__ == "__main__":
    if (len(sys.argv) > 1):
        link = sys.argv[1]
        beggining_timestamp = sys.argv[2]
        closing_timestamp = sys.argv[3]
        print("YouTube link: " + link + 
        "\nBeggining timestamp: " + beggining_timestamp +
        "\nClosing timestamp: " + closing_timestamp)
    else:
        link = input("Enter YouTube link: ")
        beggining_timestamp = input("Enter beginning timestamp: ")
        closing_timestamp = input("Enter closing timestamp: ")

    print(link)
    
    main(link, beggining_timestamp, closing_timestamp)