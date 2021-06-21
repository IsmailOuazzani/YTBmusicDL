import subprocess as sb
import os
import shutil

PLAYLIST = "playlist.txt"
HISTORY = "history.txt"
FOLDER = "Music"

# Creates a music folder if it does not exist
def makefolder():
    if os.path.exists(FOLDER):
        shutil.rmtree(FOLDER)

    os.mkdir(FOLDER)

# Create a history file if it does not exist
# Returns all the past urls
def gethistory():
    f = open(HISTORY, 'r')
    history_list = f.read()
    f.close()
    return history_list

# Remove urls that are already in the history
def filterplaylist():
    history_list = gethistory()
    playlist_list = open(PLAYLIST, 'r').read().replace(' ', '').splitlines()

    os.remove(PLAYLIST)
    f = open(PLAYLIST, 'a+') #open (or create if it doesnt exist) the file for appending

    url_count = 0

    for url in playlist_list:
        if url not in history_list:
            f.write(url)
            url_count += 1
        else:
            print(url + " already in history")
    
    # Check that the playlist isnt empty after filtering
    if url_count == 0:
        print("Playlist empty or only contains urls in history.")
        quit()
    else:
        print("Downloading " + str(url_count) + " song(s).")

    f.close()
    return

# Save the downloaded urls to the history file
def save_to_history():
    playlist_list = open(PLAYLIST, 'r').readlines()
    os.remove(PLAYLIST)

    history_file = open(HISTORY, 'a')
    for url in playlist_list:
        history_file.write(url + " \n")
    # Recreate the playlist file
    f = open(PLAYLIST, 'a+')
    f.close()

    return
    
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
    # Retry infinitely in case someting is wrong
    Command.append("--retries infinite")
    # Wait 1s before giving up and try again
    Command.append("--socket-timeout 1")
    # Clean the 'Musique' folder
    makefolder()
    # Place songs in 'Musique' folder 
    Command.append("-o " + FOLDER + "/%(title)s.%(ext)s")
    # Remove songs that have already been downloaded
    filterplaylist()

    # Run youtube-dl command
    sb.run(" ".join(Command))

    # Save urls to history
    save_to_history()
    return


if __name__ == '__main__':
    download(PLAYLIST)
