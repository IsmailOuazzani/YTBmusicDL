# Rename files that do not have a section in the description
# with the information about the song (title, author, album ...)
import os
from mutagen.easyid3 import EasyID3

# Remove the author name, usally in the form 
# AUTHOR - TITLE ...
# If the file does not have this, it will probable not feature parenthesis that are not part of the title,
# so we will not do further modifications (returns "none").
# If it does, it will change the title of the song and make sure that the author in the mp3 file and the title
# is the same.
def dash_filter(title, author):
    separators = [' - ', ' – ', ' | '] #somehow some songs contain '-' and others '–' which are different 
    for sep in separators:
        if sep in title:
            title_components = title.split(sep)
            filtered_title = title_components[1]
            filtered_author = title_components[0]
            if author not in filtered_author and filtered_author not in author:
                return filtered_title, filtered_author
            return filtered_title, "noModification"
    
    return "noModification", "noModification"

# Remove the parenthesis part, usually in the form
# TITLE - (Official Video) or TITLE - (Lyrics) etc
def remove_parenthesis(title):
    if '(' in title:
        title_components = title.split(' (')
        return title_components[0]

    return title

# Update the file metadata if necessary
def update_file_info(file, title, author, FOLDER):
    if title != "noModification":
        music = EasyID3(FOLDER + '/' + file)
        if author != "noModification":
            music['title'] = title
            music['artist'] = author
        else:
            music['title'] = title
        print("Updating " + file)
        music.save()
    return


def renamefiles(FOLDER):
    for dirpath, dirnames,files in os.walk(FOLDER):
        for file in files:

            # Get the author to compare with author in title
            # Because if the video does not contain the music info,
            # youtube-dl will take the channel as the author
            music = EasyID3(FOLDER + '/' + file)
            default_title = music['title'][0]
            default_author = music['artist'][0]
            music.save()

            title, author = dash_filter(default_title, default_author)
            title = remove_parenthesis(title)
            update_file_info(file, title, author, FOLDER)

    return
