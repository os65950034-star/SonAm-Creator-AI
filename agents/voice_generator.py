import os
import asyncio
import edge_tts


class VoiceGenerator:

    def generate(self, script):

        print("\n========== VOICE GENERATOR ==========\n")

        os.makedirs("output", exist_ok=True)

        async def create_voice():
            communicate = edge_tts.Communicate(
                text=script,
                voice="en-US-GuyNeural"
            )

            await communicate.save("output/voice.mp3")

        asyncio.run(create_voice())

        print("Voice Generated Successfully.")