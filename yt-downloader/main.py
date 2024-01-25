from pytube import YouTube

video_url = "https://www.youtube.com/shorts/I9PchMLY5yg"
yt = YouTube(video_url)

yt.streams.filter(progressive=True, file_extension="mp4").order_by(
    "resolution"
).desc().first().download()
