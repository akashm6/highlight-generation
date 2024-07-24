import csv
import numpy as np

def seconds_to_mmss(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes:02}:{seconds:02}"

def get_chat_excitement(chat_csv_path, segment_duration=30) -> str:

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
        if count >= average_count * 2:
            start_segment = seconds_to_mmss(segments[i])
            end_segment = seconds_to_mmss(segments[i + 1])
            exciting_segments.append((start_segment, end_segment, count))

    if exciting_segments:
        result = "Segments with message frequency meeting or exceeding the average:\n" + "\n".join(
            [f"From {start} to {end}: {count} messages (Average: {average_count:.2f})" for start, end, count in exciting_segments]
        )
    else:
        result = "No segments met or exceeded the average message frequency."

    return result


