
from flask import Flask, request
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from dotenv import load_dotenv
import os
import google.generativeai as genai

app = Flask(__name__)

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt_templates = {
    "short": "Provide a short summary in 100 words exactly, give number of words at the end: ",
    "medium": "Provide a medium-length summary in 500 words exactly,give number of words at the end: ",
    "long": "Provide a detailed summary in 1000 words exactly, give number of words at the end: "
}

@app.route('/summary', methods=['GET'])
def summary_api():
    url = request.args.get('url', '')
    length = request.args.get('length', '')
    video_id = url.split('v=')[1] if 'v=' in url else None
    if not video_id:
        return "Invalid YouTube URL.", 400
    try:
        transcript_text = get_transcript(video_id)
    except TranscriptsDisabled:
        return "Transcripts are disabled for this video.", 400
    except Exception as e:
        return str(e), 500

    if length not in prompt_templates:
        return jsonify(error="Invalid summary length. Choose 'short', 'medium', or 'long'."), 400

    prompt = prompt_templates[length]
    summary = get_summary(transcript_text, prompt)
    return summary, 200


def get_transcript(video_id):
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
    transcript = ' '.join([d['text'] for d in transcript_list])
    return transcript

def get_summary(transcript, prompt):
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt + transcript)
        return response.text
    except Exception as e:
        raise e

if __name__ == '__main__':
    app.run()
