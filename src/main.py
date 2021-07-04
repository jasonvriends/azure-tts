import os, datetime
from azure.cognitiveservices.speech import AudioDataStream, SpeechConfig, SpeechSynthesizer, SpeechSynthesisOutputFormat
from azure.cognitiveservices.speech.audio import AudioOutputConfig
from pydantic import BaseSettings

# Settings management
class Settings(BaseSettings):
    KEY: str = ""
    REGION: str = ""
    class Config:
        env_file = ".env"

settings = Settings()

# Set output filename
OUTPUT_FILE = os.path.join(os.path.dirname(__file__),'output',datetime.datetime.today().strftime("%Y-%m-%d")+'-announcements.mp3')
OUTPUT_FOLDER = os.path.dirname(__file__),'output'

# Create output folder is not exist
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

# Configure Azure Cognitive Services
speech_config = SpeechConfig(subscription=settings.KEY, region=settings.REGION)
speech_config.set_speech_synthesis_output_format(SpeechSynthesisOutputFormat["Audio24Khz160KBitRateMonoMp3"])
audio_config = AudioOutputConfig(filename=OUTPUT_FILE)
synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

# Read tts.xml
ttsfilename = os.path.join(os.path.dirname(__file__),'tts.xml')
with open(ttsfilename,'r') as f:
    content = f.read()

# Generate audio
synthesizer.speak_ssml_async(content)