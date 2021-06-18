import subprocess as sb
import os
import shutil

# Installation:
# Install youtube-dl by typing in the cmd: pip install youtube-dl
# If you get an error with ffmpeg, do: pip install ffmpeg
#                                      pip install ffprobe

# Use:
# Place youtube urls in the 'playlist.txt' document (1 url each line)
# Start the program by doing: python main.py

# Modification
# youtube-dl documentation: https://github.com/ytdl-org/youtube-dl/blob/master/README.md#developer-instructions

FOLDER = "Music"

def makefolder():
    if os.path.exists(FOLDER):
        shutil.rmtree(FOLDER)

    os.mkdir(FOLDER)

def download(files):
    Command = []
    # Dl a playlist:
    Command.append("youtube-dl -a" + files)
    # Dl audio only (mp3)
    Command.append("-x --audio-format mp3")
    # Dl audio in best quality
    Command.append("--audio-quality 0")
    # Add metadata
    Command.append("--add-metadata")
    # Add thumbnail
    Command.append("--embed-thumbnail")
    # Clean the 'Musique' folder
    makefolder()
    # Place songs in 'Musique' folder 
    Command.append("-o " + FOLDER + "/%(title)s.%(ext)s")

    sb.run(" ".join(Command))
    return


if __name__ == '__main__':
    download("playlist.txt")
