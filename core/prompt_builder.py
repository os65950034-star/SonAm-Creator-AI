class PromptBuilder:

    def build_script_prompt(self, topic):

        prompt = f"""
You are a professional YouTube Script Writer.

Write a highly engaging script about:

Topic:
{topic}

The script should:
- Be easy to understand
- Have a strong hook
- Keep audience engaged
- End with a powerful conclusion
"""

        return prompt