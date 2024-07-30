from auth import get_parameters
from vod_download import download_vod
from chat_pull import download_chat_data
from frequency import get_chat_excitement
from sentiment import analyze_sentiments, sentiment_over_time, plot_sentiment_over_time


def main():
    vod_url = str(input('Input the URL of the Twitch VOD you would like to analyze: '))
    print('Downloading VOD...')
    vod_file = download_vod(vod_url).get('local_filename')
    output_file = str(input('Name your chat data file: '))
    print('Fetching chat data from the web...')
    chat_path = download_chat_data(vod_url, output_file)
    print('Analyzing chat data and downloading clips...')
    get_chat_excitement(chat_path, vod_file, './clips')
    print('Clips downloaded into \"clips\" directory!')
    while True:
        response = str(input('Would you like sentiment data? Y/N: '))
        if response.lower() != 'y' and response.lower() != 'n':
            continue
        break
    if response.lower() == 'y':
        print('Retrieving chat sentiment analysis data...')
        sentiments = analyze_sentiments(chat_path)
        segments, average_sentiments = sentiment_over_time(sentiments)
        print('Plotting sentiment data...')
        plot_sentiment_over_time(segments, average_sentiments)
    print('Thank you for using highlight generation!')
    return

if __name__ == '__main__':
    main()