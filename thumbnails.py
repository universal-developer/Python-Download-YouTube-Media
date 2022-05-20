from pytube import YouTube

def main():
    get_video_link = str(input('Paste video link here: '))

    video = YouTube(get_video_link).thumbnail_url

    print(video)
    
main()
