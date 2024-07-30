# Highlight Generation

Highlight Generation is a tool for Twitch streamers looking to pinpoint exciting moments in their live streams. 
By utilizing Selenium for automated chat data CSV retrieval, NumPy for chat message frequency analysis, NLTK/VADER for sentiment analysis, and yt_dlp
for local vod/clip downloads, highlight generation takes what is usually a fully manual process and speeds it up by simply asking the user to input a
link to their Twitch VOD.

* Locally downloads the input twitch VOD using a UUID unique ID via yt_dlp. 
* Downloads chat data as a CSV utilizing Selenium to automate the web process of
  entering a stream link to https://www.twitchchatdownloader.com/.
* Analyzes chat message frequency through message times in order to determine when
  exciting moments happen in the stream (Threshold is 3.5X the normal stream average frequency).
* Extracts 30 second clips surround periods of high chat activity and downloads them to a folder.
* Performs sentiment analysis using VADER lexicon analysis to report sentiment statistics and
  plots sentiment over time.

## Demo

## Languages and Libaries Used
* [Python](https://www.python.org/)
* NLTK/VADER
* Selenium
* NumPy
* Matplotlib
* yt_dlp



