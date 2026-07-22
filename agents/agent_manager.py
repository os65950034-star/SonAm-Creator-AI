class AgentManager:

    def __init__(self):
        self.agents = []

    def register(self, agent_name):
        self.agents.append(agent_name)
        print(f"[✓] {agent_name} Registered")

    def show_agents(self):
        print("\n========== ACTIVE AI AGENTS ==========")

        if not self.agents:
            print("No agents registered.")

        for i, agent in enumerate(self.agents, start=1):
            print(f"{i}. {agent}")

        print("======================================")