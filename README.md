# Highlight Generation <img src="https://gamequitters.com/wp-content/uploads/twitch-logo-transparent.png" width="50" height = "50" title="logo">

Highlight Generation is a tool for Twitch streamers looking to automate the process of pinpointing exciting moments in their live streams. 

By utilizing:
* Selenium for automated chat data CSV retrieval
* NumPy for chat message frequency analysis
* NLTK/VADER for sentiment analysis
* and yt_dlp for local vod/clip downloads,

Highlight generation takes what is usually a fully manual process and speeds it up by simply asking the user to input a
link to their Twitch VOD.

## How it Works
* Locally downloads the input twitch VOD using a UUID via yt_dlp. 
* Downloads chat data as a CSV utilizing Selenium to automate the web process of
  entering a stream link to [Twitch Chat Downloader](https://www.twitchchatdownloader.com/).
* Analyzes chat message frequency through message times in order to determine when
  exciting moments happen in the stream (Threshold is 3.5X the normal stream average frequency).
* Extracts 30 second clips surrounding periods of high chat activity and locally downloads them to your machine.
* Performs sentiment analysis using VADER lexicon analysis to report sentiment statistics and
  plots sentiment over time.

## Demo

Coming Soon!

## Dependencies Applied
* [Python](https://www.python.org/)
* [NLTK/VADER](https://www.nltk.org/_modules/nltk/sentiment/vader.html)
* [Selenium](https://www.selenium.dev/)
* [NumPy](https://numpy.org/)
* [Matplotlib](https://matplotlib.org/)
* [yt_dlp](https://github.com/yt-dlp/yt-dlp)



