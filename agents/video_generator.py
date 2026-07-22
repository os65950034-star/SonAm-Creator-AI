from moviepy import ImageClip, AudioFileClip
import os


class VideoGenerator:

    def generate(self, script):

        print("\n========== VIDEO GENERATOR ==========\n")

        os.makedirs("output", exist_ok=True)

        image_path = "assets/background.jpg"
        audio_path = "output/voice.mp3"
        output_path = "output/video.mp4"

        audio = AudioFileClip(audio_path)

        video = (
            ImageClip(image_path)
            .with_duration(audio.duration)
            .with_audio(audio)
        )

        video.write_videofile(
            output_path,
            fps=24,
            codec="libx264",
            audio_codec="aac"
        )

        print("Video Generated Successfully.")