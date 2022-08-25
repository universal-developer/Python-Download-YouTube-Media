import scrapetube
from pytube import YouTube
import youtube_dl

def main():
	choice = int(input('What are you want to download?:\n1) YouTube Video\n2) All YouTube Videos from channel\n3) Thumbnail\n-----\n'))

	if choice == 1: 
		download_video()
	elif choice == 2:
		download_videos()
	elif choice == 3:
		download_thumbnail()


def download_video():
	get_video_link = str(input('Paste link on youtube video here: '))

	yt = YouTube(get_video_link)

	yt.streams.get_highest_resolution().download(get_video_link)

	print('Video downloaded')


def download_videos():
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


def download_thumbnail():
	get_video_link = str(input('Paste video link here: '))

	video = YouTube(get_video_link).thumbnail_url

	print(video)


main()