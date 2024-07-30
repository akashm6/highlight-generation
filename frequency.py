import csv
import numpy as np
import uuid
import os
import subprocess

def seconds_to_mmss(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes:02}:{seconds:02}"

def extract_clip(vod_file_path, start_time, clips_directory, segment_duration=30):
    
    os.makedirs(clips_directory, exist_ok=True)
    
    file_id = uuid.uuid4()
    local_filename = os.path.join(clips_directory, f"clip_{file_id}.mp4")
    
    command = [
        'ffmpeg', '-ss', str(start_time), '-i', vod_file_path, '-t', str(segment_duration),
        '-c', 'copy', local_filename
    ]

    subprocess.run(command, check=True)
    
    print(f"Clip extracted as {local_filename}")

def get_chat_excitement(chat_csv_path, vod_file_path, clips_directory, segment_duration=30) -> str:
    with open(chat_csv_path, newline='') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]

    timestamps = [int(row['time']) for row in data]
    
    if not timestamps:
        return "No chat data available."

    start_time = min(timestamps)
    end_time = max(timestamps)
    segments = np.arange(start_time, end_time + segment_duration, segment_duration)

    message_counts = [0] * (len(segments) - 1)
    for ts in timestamps:
        for i in range(len(segments) - 1):
            if segments[i] <= ts < segments[i + 1]:
                message_counts[i] += 1
                break

    average_count = np.mean(message_counts)
    exciting_segments = []
    
    for i, count in enumerate(message_counts):
        if count >= average_count * 4:
            start_segment = segments[i]
            end_segment = segments[i + 1]
            exciting_segments.append((start_segment, end_segment, count))

            extract_clip(vod_file_path, start_segment, clips_directory, segment_duration)

    if exciting_segments:
        result = "Segments with message frequency meeting or exceeding the average:\n" + "\n".join(
            [f"From {seconds_to_mmss(start)} to {seconds_to_mmss(end)}: {count} messages (Average: {average_count:.2f})" 
             for start, end, count in exciting_segments]
        )
    else:
        result = "No segments met or exceeded the average message frequency."

    return result
