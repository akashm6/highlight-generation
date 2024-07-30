import csv
import nltk
import numpy as np
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer

#nltk.download('vader_lexicon')

def seconds_to_mmss(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes:02}:{seconds:02}"

def analyze_sentiments(chat_csv_path):
    analyzer = SentimentIntensityAnalyzer()
    results = []

    with open(chat_csv_path, newline='') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]

    for row in data:
        message = row.get('message')
        timestamp = int(row.get('time'))
        if message:
            scores = analyzer.polarity_scores(message)
            scores['time'] = timestamp
            results.append(scores)

    return results

def sentiment_over_time(sentiments, segment_duration=60):
    if not sentiments:
        return "No sentiment data available."

    start_time = min(sentiments, key=lambda x: x['time'])['time']
    end_time = max(sentiments, key=lambda x: x['time'])['time']
    segments = np.arange(start_time, end_time + segment_duration, segment_duration)

    average_sentiments = []
    for i in range(len(segments) - 1):
        segment_scores = [s['compound'] for s in sentiments if segments[i] <= s['time'] < segments[i + 1]]
        if segment_scores:
            average_sentiments.append(np.mean(segment_scores))
        else:
            average_sentiments.append(0)

    return segments, average_sentiments

def plot_sentiment_over_time(segments, average_sentiments):
    segment_labels = [seconds_to_mmss(seg) for seg in segments[:-1]]
    plt.figure(figsize=(12, 6))
    plt.plot(segment_labels, average_sentiments, marker='o')
    plt.xlabel('Time (MM:SS)')
    plt.ylabel('Average Sentiment')
    plt.title('Sentiment Over Time')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
