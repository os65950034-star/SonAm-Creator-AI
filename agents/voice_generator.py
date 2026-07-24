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

        try:
            asyncio.run(create_voice())

            if os.path.exists("output/voice.mp3"):
                print("[✓] Voice Generated Successfully.")
            else:
                raise Exception("voice.mp3 was not created.")

        except Exception as e:
            print("\nVOICE GENERATOR ERROR:")
            print(e)
            input("\nPress Enter to Exit...")
            raise
