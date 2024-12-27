import pytube

video_url = input("Enter your youtube url: ")
try:
    video = pytube.YouTube(video_url).streams.first()
    video.download("D://source")
    print("Download successful...")
except:
    print("Error: there might be some issue")
