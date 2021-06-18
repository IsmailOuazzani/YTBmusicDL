# YTBmusicDL
Python script using youtube-dl to automate mp3 downloading with relevant settings (metadata for titles, album, author ...)

# Disclaimer
This project was done for education purposes only. Please do not use it to download content you are not allowed to download.  

# Features
- Download files as mp3 at the best quality available
- Add a title, album and the author in the files' metadata  
- Add an Album cover to the file (the thumbnail of the video) 
- Place all the files in a 'Music' directory  
- Delete previous 'Music' folder and the files it contains when starting the program (can be disabled by creating the folder manually and removing line 27)


# Installation:
Download main.py and playlist.txt and put them in the same folder.  

 Install youtube-dl by typing in the cmd:  
 pip install youtube-dl  
 
 Download ffmpeg: https://www.gyan.dev/ffmpeg/builds/  
 Unzip it and open ffmpeg(YOUR VERSION)/bin  
 Move ffmpeg.exe, ffplay.exe, ffprobe.exe in the folder where you previously put main.py and playlist.txt
 
 
 
 If you get an error with ffmpeg, use:  
 pip install ffmpeg  
 pip install ffprobe  

# Use:
Place youtube urls in the 'playlist.txt' document (1 url each line)  
Start the program by doing: python main.py  

# Modification
youtube-dl documentation: https://github.com/ytdl-org/youtube-dl/blob/master/README.md#developer-instructions
