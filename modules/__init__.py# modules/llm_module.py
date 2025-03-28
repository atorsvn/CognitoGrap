import ollama

class LLMModule:
    def __init__(self):
        # Initialize the Ollama client (using default settings)
        self.client = ollama.Client()

    def generate_text(self, prompt, params=None):
        """
        Uses ollama.py to generate a text completion.
        """
        result = self.client.generate(prompt, params=params)
        return result

    def multi_turn_conversation(self, conversation_history):
        """
        Concatenates conversation history into a prompt and generates text.
        """
        prompt = "\n".join(conversation_history)
        return self.generate_text(prompt)
