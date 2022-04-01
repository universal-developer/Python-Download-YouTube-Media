import scrapetube
from pytube import YouTube
import youtube_dl

def main():
    
    get_channel_link = str(input('Paste YouTube channels link here: '))
    videos = scrapetube.get_channel(f"{get_channel_link}")

    youtube_videos_id = []

    for video in videos:
        youtube_videos_id.append(video['videoId'])

    print(youtube_videos_id)

    for i in range(len(youtube_videos_id)):
        yt = YouTube(f'https://www.youtube.com/watch?v={youtube_videos_id[i]}')
        yt.streams.get_highest_resolution().download(f'https://www.youtube.com/watch?v={youtube_videos_id[i]}')
        print(i)


main()
