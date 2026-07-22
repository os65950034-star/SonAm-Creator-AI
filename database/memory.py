class Memory:

    def __init__(self):
        self.data = {}

    def save(self, key, value):
        self.data[key] = value
        print(f"[✓] Saved : {key}")

    def get(self, key):
        return self.data.get(key, "Not Found")

    def show(self):
        print("\n========== MEMORY ==========")

        if not self.data:
            print("Memory Empty")

        for key, value in self.data.items():
            print(f"{key} : {value}")

        print("============================")