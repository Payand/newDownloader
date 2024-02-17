import yt_dlp

link = ["https://www.youtube.com/watch?v=JJEKPqSlXvk","https://www.youtube.com/watch?v=ZJJHm_bd9Zo"]
ydl_opts = {
    'format': 'best',
    'outtmpl': 'allDownload/%(title)s.%(ext)s',

}

with yt_dlp.YoutubeDL(ydl_opts) as yld:
    yld.download(link)
