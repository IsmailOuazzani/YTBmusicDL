# YTBmusicDL
Python script using youtube-dl to automate mp3 downloading with relevant settings (metadata for titles, album, author ...).


# Installation:
Download main.py and playlist.txt and put them in the same folder.  

 Install youtube-dl by typing in the cmd:  
 pip install youtube-dl  
 
 Download ffmpeg: https://www.gyan.dev/ffmpeg/builds/  
 Unzip it and copy the files in ffmpeg(YOUR VERSION)/bin in the folder with main.py and playlist.txt  
 
 If you get an error with ffmpeg, use:  
 pip install ffmpeg  
 pip install ffprobe  

# Use:
Place youtube urls in the 'playlist.txt' document (1 url each line)  
Start the program by doing: python main.py  

# Modification
youtube-dl documentation: https://github.com/ytdl-org/youtube-dl/blob/master/README.md#developer-instructions
