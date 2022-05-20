import scrapetube
from pytube import YouTube

def main():
    
    get_video_link = str(input('Paste link on youtube video here: '))

    yt = YouTube(get_video_link)

    yt.streams.get_highest_resolution().download(get_video_link)

    print('Video downloaded')

main()
