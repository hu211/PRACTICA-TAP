from agents.minecraft_agent import MinecraftAgent
import time

class OracleBot(MinecraftAgent):
    def __init__(self):
        super().__init__()
        self.answering = False  # Flag to control answering loop

    def command_iniciar_oraculo(self):
        """Start the OracleBot and greet players."""
        self.post_to_chat("¡Hola! Soy el oráculo. ¿Qué quieres saber?")
        self.start_answering()

    def start_answering(self):
        """Respond to player questions in the chat."""
        self.answering = True
        while self.answering:
            chat_posts = self.mc.events.pollChatPosts()
            for post in chat_posts:
                question = post.message.strip().lower()
                answer = self.get_answer(question)
                self.post_to_chat(answer)
            time.sleep(1)  # Avoid busy-waiting

    def stop_answering(self):
        """Stop the answering loop."""
        self.answering = False

    def get_answer(self, question):
        """Generate an answer based on the player's question."""
        if "tiempo" in question:
            return "El tiempo está soleado."
        elif "nombre" in question:
            return "Mi nombre es OracleBot."
        elif "creador" in question:
            return "Fui creado por el profesor."
        elif "propósito" in question:
            return "Mi propósito es responder a tus preguntas."
        else:
            return "No entiendo tu pregunta. Prueba con 'tiempo', 'nombre', 'creador' o 'propósito'."

if __name__ == "__main__":
    oracle_bot = OracleBot()
    oracle_bot.command_iniciar_oraculo()