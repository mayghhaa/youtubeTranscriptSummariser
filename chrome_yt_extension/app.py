from flask import Flask, request
from youtube_transcript_api import YouTubeTranscriptApi
from dotenv import load_dotenv
import os
import google.generativeai as genai


app = Flask(__name__)


# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt = """You are a YouTube video summarizer. You will be taking the transcript text
and summarizing the entire video, providing the important summary in points
within 500 words. Please provide the summary of the text given here: """

@app.route('/summary', methods=['GET'])
def summary_api():
    url = request.args.get('url', '')
    video_id = url.split('=')[1]
    transcript_text = get_transcript(video_id)
    summary = get_summary(transcript_text, prompt)
    return summary, 200  # Return plain text response

def get_transcript(video_id):
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = ' '.join([d['text'] for d in transcript_list])
        return transcript
    except Exception as e:
        raise e

def get_summary(transcript, prompt):
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt + transcript)
        return response.text
    except Exception as e:
        raise e

if __name__ == '__main__':
    app.run()
