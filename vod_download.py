import yt_dlp
import uuid

"""
Downloads a twitch vod from a given url locally
"""
def download_vod(vod_url):
    
    #generates a unique file_id
    file_id = uuid.uuid4()
    local_filename = f"vod_{file_id}.mp4"
    
    # params for download
    ydl_opts = {
        'outtmpl': local_filename,
        'format': 'bestvideo+bestaudio/best',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([vod_url])

    print(f"Video downloaded as {local_filename}")

if __name__ == '__main__':
    download_vod('https://www.twitch.tv/videos/917374678')
