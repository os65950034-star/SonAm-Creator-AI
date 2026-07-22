class ContentPipeline:

    def __init__(self):
        self.steps = [
            "Research",
            "Script Writing",
            "Voice Generation",
            "Video Editing",
            "Thumbnail Creation",
            "SEO Optimization",
            "Social Media Upload"
        ]

    def show_pipeline(self):
        print("\n========== CONTENT PIPELINE ==========")

        for i, step in enumerate(self.steps, start=1):
            print(f"{i}. {step}")

        print("======================================")