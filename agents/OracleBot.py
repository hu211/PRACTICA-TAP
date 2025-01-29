from agents.minecraft_agent import MinecraftAgent
import time

class OracleBot(MinecraftAgent):
    def __init__(self):
        super().__init__()
        self.commands = {
            "iniciar": self.start_answering,
            "detener": self.stop_answering
        }
        self.responses = {
            "tiempo": lambda: "El tiempo está soleado.",
            "nombre": lambda: "Mi nombre es OracleBot.",
            "creador": lambda: "Fui creado por el profesor.",
            "propósito": lambda: "Mi propósito es responder a tus preguntas."
        }

    def command_iniciar_oraculo(self):
        """Iniciar el oráculo."""
        self.post_to_chat("¡Hola! Soy el oráculo. Pregunta sobre 'tiempo', 'nombre', 'creador' o 'propósito'.")
        self.start_answering()

    def start_answering(self):
        """Responder preguntas en el chat usando programación funcional y reflexión."""
        while True:
            chat_posts = self.mc.events.pollChatPosts()
            questions = map(lambda post: post.message.strip().lower(), chat_posts)
            valid_questions = filter(lambda q: q in self.responses, questions)

            for question in valid_questions:
                self.post_to_chat(self.responses[question]())  # Reflexión: ejecuta la función de respuesta

            self.listen_for_commands()
            time.sleep(1)

    def stop_answering(self):
        """Detener el bot."""
        self.post_to_chat("¡Oráculo apagado!")
        exit()

    def listen_for_commands(self):
        """Escuchar comandos en el chat usando reflexión."""
        chat_posts = self.mc.events.pollChatPosts()
        commands = filter(lambda post: post.message.strip().lower() in self.commands, chat_posts)

        for post in commands:
            command = post.message.strip().lower()
            getattr(self, f"{command}_answering")()  # Reflexión: ejecuta el comando dinámicamente

if __name__ == "__main__":
    oracle_bot = OracleBot()
    oracle_bot.command_iniciar_oraculo()
