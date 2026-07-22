class LLMManager:

    def __init__(self):
        self.model = "Not Connected"

    def connect(self, model_name):
        self.model = model_name
        print(f"[✓] AI Model Connected : {self.model}")

    def status(self):
        print("\n========== AI MODEL ==========")
        print(f"Current Model : {self.model}")
        print("==============================")