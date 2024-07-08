# YouTube Transcript Summariser

## Overview

The YouTube Transcript Summariser is a Chrome extension that extracts transcripts from YouTube videos and generates summaries of varying lengths. Users can choose from three summary lengths: short, medium, and long. The application uses a Flask backend to handle transcript extraction and summary generation, leveraging the YouTube Transcript API and Google's Generative AI model.

## Features

- Extracts transcripts from YouTube videos playing currently.
- Generates summaries in three different lengths: short (100 words), medium (500 words), and long (1000 words).
- Handles errors such as invalid YouTube URLs and disabled transcripts.


## Prerequisites

- Python 3.x
- Flask
- youtube-transcript-api
- google.generativeai
- dotenv

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/your-username/youtube-transcript-summariser.git
    cd youtube-transcript-summariser
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the project root and add your Google API key:
    ```
    GOOGLE_API_KEY=your_google_api_key
    ```

## Usage

1. Run the Flask application:
    ```
    python app.py
    ```

2. Open your Web Browser. Click on the three dots in the right hand corner. Select Extensions-> Manage extensions from the menu. Select developer mode in right hand corner of the web page that appears. Select Load Unpacked and choose the files from the location they were cloned into.  

4. To get a summary: play video and use the extensio from the browser.
   //127.0.0.1:5000/summary?url=https://www.youtube.com/watch?v=dQw4w9WgXcQ&length=medium
    ```

## Error Handling

The application handles the following error cases:

- **Invalid YouTube URL:** Returns a 400 status code with a message indicating that the URL is invalid.
- **Transcripts Disabled:** Returns a 400 status code with a message indicating that transcripts are disabled for the video.
- **No Transcript Found:** Returns a 404 status code with a message indicating that no transcript was found for the video.
- **General Errors:** Returns a 500 status code with a message indicating an internal server error.

## Acknowledgements

- [YouTube Transcript API](https://github.com/jdepoix/youtube-transcript-api)
- [Google Generative AI](https://ai.google/tools/)
- [Flask](https://flask.palletsprojects.com/)


