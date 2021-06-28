import youtube_dl
ydl_opts={'format':'bestaudio/best','outtmpl':'/video/%(title)s.%(ext)s','format':'bestaudio/best','postprocessors':[{'key':'FFmpegExtractAudio','preferredcodec':'mp3','preferredquality':'192'}]}                   
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://youtu.be/xfNYHWeQfHo'])