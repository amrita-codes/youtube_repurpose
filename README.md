## This converts any YouTube video to LinkedIn post

### How it works?
- First fetches the transcript of the YouTube video
- Uses the transcript, settings.py and prompt in prompts.py file to generate a response from Claude AI (Anthropic)
- Stores the response in response.txt and transcript in transcript.txt

### How to install and run?
- Create a .env file
- Add your ANTHROPIC_API_KEY in it (get it from here: https://console.anthropic.com/settings/keys)
- Run ```pip3 install requrirements.txt``` in the terminal
- Run ```python3 transcript_to_linkedin.py``` in the terminal
