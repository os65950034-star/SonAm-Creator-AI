from dotenv import load_dotenv

load_dotenv()
import os

OPENAI_API_KEY = os.getenv
import os

class Settings:

    PROJECT_NAME = "SonAm Creator AI"

    OPENAI_MODEL = "gpt-4.1-mini"

    VIDEO_ENGINE = "ComfyUI"

    TTS_ENGINE = "Kokoro"

    THUMBNAIL_ENGINE = "Flux"

    OUTPUT_FOLDER = "output"

    @staticmethod
    def show():

        print("\n========== SETTINGS ==========\n")

        print("Project :", Settings.PROJECT_NAME)
        print("LLM :", Settings.OPENAI_MODEL)
        print("Video :", Settings.VIDEO_ENGINE)
        print("Voice :", Settings.TTS_ENGINE)
        print("Thumbnail :", Settings.THUMBNAIL_ENGINE)
        print("Output :", Settings.OUTPUT_FOLDER)