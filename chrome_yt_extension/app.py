from dotenv import load_dotenv
from flask import Flask, request
from youtube_transcript_api import YouTubeTranscriptApi
import os
import google.generativeai as genai

app = Flask(__name__)

load_dotenv()  # Load all the environment variables
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt = """You are a YouTube video summarizer. You will be taking the transcript text
and summarizing the entire video, providing the important summary in points
within 500 words. Please provide the summary of the text given here: """

@app.route('/summary', methods=['GET'])
def summary_api():
    url = request.args.get('url', '')
    video_id = url.split('=')[1]
    transcript_text = extract_transcript_details(video_id)
    summary = get_summary(transcript_text, prompt)
    return summary, 200

# Getting the transcript data from YouTube videos
def extract_transcript_details(video_id):
    try:
        transcript_data = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = " ".join([item["text"] for item in transcript_data])
        return transcript
    except Exception as e:
        raise e

def get_summary(transcript_text, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt + transcript_text)
    return response.text



if __name__ == '__main__':
    app.run()
