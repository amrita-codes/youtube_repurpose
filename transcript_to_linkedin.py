from youtube_transcript_api import YouTubeTranscriptApi
import re
import prompts
import settings
import requests

import os
from dotenv import load_dotenv

load_dotenv()

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")
print(ANTHROPIC_API_KEY)

import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key=ANTHROPIC_API_KEY
)
def getClaudeResponse(prompt):
    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    # print(message.content)
    response = message.content[0].text
    return response


def getTranscript():
    """Get transcript from YouTube video URL and output it"""
    try:
        # Take input of video_id from the user
        video_id = input('Enter the video id: ')
        if not video_id:
            return {"error": "Invalid YouTube Video Id"}

        # Get transcript
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        
        # Combine transcript text
        full_transcript = " ".join([entry['text'] for entry in transcript_list])
        
        # Basic cleaning
        full_transcript = re.sub(r'\s+', ' ', full_transcript)  # Remove extra whitespace
        full_transcript = full_transcript.strip()
        
        # save the transcript in a new txt file
        with open('transcript.txt', 'w') as f:
            f.write(full_transcript)
        
        return {
          "data": {
              "success": True,
              "video_id": video_id,
              "full_transcript": full_transcript,
              "transcript_length": len(full_transcript)
          }
        }
        
    except Exception as e:
        error_message = str(e)
        if "TranscriptsDisabled" in error_message:
            return {"error": "Transcripts are disabled for this video"}
        elif "NoTranscriptAvailable" in error_message:
            return {"error": "No transcript available for this video"}
        else:
            return {"error": f"An error occurred: {error_message}"}

def transcriptToLinkedin():
    transcript = getTranscript()
    if "error" in transcript:
        print(transcript["error"])
        return
    
    linkedin_prompt = prompts.convertToLinkedinPrompt(
        transcript["data"]["full_transcript"]
    )

    response = getClaudeResponse(linkedin_prompt)

    # store the output in a txt file
    with open('response.txt', 'w') as f:
        f.write(str(response))

    

# Run the transcriptToLinkedin function in main function of python
if __name__ == "__main__":
    print('run main')
    transcriptToLinkedin()
