from config.settings import Settings
from agents.voice_generator import VoiceGenerator
from agents.video_editor import VideoEditor
from agents.video_generator import VideoGenerator
from agents.thumbnail_generator import ThumbnailGenerator
from api.openrouter_client import OpenRouterClient

from core.prompt_builder import PromptBuilder
from agents.research_agent import ResearchAgent
from agents.script_writer import ScriptWriter
from workflows.content_pipeline import ContentPipeline
from api.llm_manager import LLMManager
from core.mission_control import MissionControl
from agents.agent_manager import AgentManager
from database.memory import Memory
from database.database_manager import DatabaseManager


# =========================
# Mission Control
# =========================
mission = MissionControl()
mission.start()


# =========================
# Agent Manager
# =========================
manager = AgentManager()

manager.register("Script Writer AI")
manager.register("Video Editor AI")
manager.register("Thumbnail AI")

manager.show_agents()


# =========================
# Memory
# =========================
memory = Memory()

memory.save("Project", "SonAm Creator AI")
memory.save("Owner", "Raman")

memory.show()


# =========================
# Database
# =========================
db = DatabaseManager()
db.create_tables()


# =========================
# LLM Status
# =========================
llm = LLMManager()

llm.connect("GPT-4.1 Mini")
llm.status()


# =========================
# Content Pipeline
# =========================
pipeline = ContentPipeline()
pipeline.show_pipeline()


# =========================
# Research
# =========================
research = ResearchAgent()
research.research("How AI Will Change The Future")


# =========================
# Script Writer
# =========================
writer = ScriptWriter()
writer.generate("How AI Will Change The Future")


# =========================
# Prompt Builder
# =========================
builder = PromptBuilder()

prompt = builder.build_script_prompt(
    "How AI Will Change The Future"
)

print("\n========== GENERATED PROMPT ==========")
print(prompt)


# =========================
# OpenRouter
# =========================
client = OpenRouterClient()

client.connect()

response = client.generate(prompt)

print("\n========== AI RESPONSE ==========\n")
print(response)


# =========================
# Video Generator
# =========================
video = VideoGenerator()
video.generate(response)


# =========================
# Video Editor
# =========================
editor = VideoEditor()
editor.edit("output/video.mp4")


# =========================
# Voice Generator
# =========================
voice = VoiceGenerator()
voice.generate(response)


# =========================
# Settings
# =========================
Settings.show()
thumbnail = ThumbnailGenerator()
thumbnail.generate()