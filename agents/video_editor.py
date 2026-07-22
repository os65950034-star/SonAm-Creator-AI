from moviepy import VideoFileClip, TextClip, CompositeVideoClip


class VideoEditor:

    def edit(self, video_path):

        print("\n========== VIDEO EDITOR ==========\n")

        video = VideoFileClip(video_path)

        subtitle = TextClip(
            text="Created with SonAm Creator AI",
            font_size=40,
            color="white",
            duration=video.duration
        ).with_position(("center", "bottom"))

        final = CompositeVideoClip([video, subtitle])

        final.write_videofile(
            "output/final_video.mp4",
            codec="libx264",
            audio_codec="aac"
        )

        print("Video Edited Successfully.\n")