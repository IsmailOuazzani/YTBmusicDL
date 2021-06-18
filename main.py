import subprocess as sb
import os
import shutil


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
