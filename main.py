from pytube import YouTube

while True:
    userInput = input("\n\nEnter URL for video: ")
    ytVidLink = str(userInput)
    yt = YouTube(f'{ytVidLink}')
    stream = yt.streams.get_by_itag(22)
    print(f'Downloading: "{yt.title}"...')
    stream.download()
    print("Downloaded!")