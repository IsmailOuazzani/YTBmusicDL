# YTBmusicDL
Python script using youtube-dl to automate mp3 downloading with relevant settings (metadata for titles, album, author ...)

# Disclaimer
This project was done for education purposes only. Please do not use it to download content you are not allowed to download.  
The author of this program is not responsible for how you use it.

# Features
- Download files as mp3 at the best quality available
- Add a title, album and the author in the files' metadata  
- Add an Album cover to the file (the thumbnail of the video) 
- Place all the files in a 'Music' directory  
- Delete previous 'Music' folder and the files it contains when starting the program (can be disabled by creating the folder manually and removing line 82)
- History file that stores previously downloaded songs (can be disabled by removing line 92). The script will not download these songs again (can be disabled by removing line 86).


# Installation
Download main.py and playlist.txt and put them in the same folder.  

 Install youtube-dl by typing in the cmd:
 ```sh
 pip install youtube-dl  
```
 
 Download [ffmpeg](https://www.gyan.dev/ffmpeg/builds/), unzip it and open: ffmpeg(YOUR VERSION)/bin  
 Move ffmpeg, ffplay, ffprobe into the folder where you previously put main.py and playlist.txt 

# Use
Place youtube urls in the 'playlist.txt' document (1 url each line).  
Start the program by typing in the cmd:
``` sh
python main.py
```  

Note: to get the title, album, author correctly, the video needs to have these information in the description. [Example](https://youtu.be/CICIOJqEb5c)

# Modification
[youtube-dl documentation](https://github.com/ytdl-org/youtube-dl/blob/master/README.md#developer-instructions)  
Please feel free to send me suggestions / ask questions, I would be happy to help if I can.
