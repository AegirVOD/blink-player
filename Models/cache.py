import youtube_dl

def download(target_videoId):
    target_link = "https://www.youtube.com/watch?v=" + target_videoId
    ydl_opts = {
        'outtmpl': ('%(id)s.%(ext)s'),
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([target_link])
