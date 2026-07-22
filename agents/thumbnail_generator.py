import shutil
import os

class ThumbnailGenerator:

    def generate(self):

        print("\n========== THUMBNAIL ==========\n")

        os.makedirs("output", exist_ok=True)

        shutil.copy(
            "assets/background.jpg",
            "output/thumbnail.jpg"
        )

        print("Thumbnail Generated Successfully.")