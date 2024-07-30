import yt_dlp
import uuid

"""
Downloads a twitch vod from a given url locally
"""

IDS = {}
def download_vod(vod_url) -> dict:
    
    file_id = uuid.uuid4()
    local_filename = f"vod_{file_id}.mp4"
    if vod_url not in IDS:
        IDS[vod_url] = file_id
    else:
        print(f"Video already downloaded as {local_filename}")
        return {
        'local_filename': local_filename,
        'vod_url': vod_url
    }
    
    # params for download
    ydl_opts = {
        'outtmpl': local_filename,
        'format': 'bestvideo+bestaudio/best',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([vod_url])

    print(f"Video downloaded as {local_filename}")

    #returns the unique file name
    return {
        'local_filename': local_filename,
        'vod_url': vod_url
    }


