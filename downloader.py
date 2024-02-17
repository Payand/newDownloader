from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        print("downloading in progress... please wait...")
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")


link = input("Enter the YouTube video URL: ")
Download(link)