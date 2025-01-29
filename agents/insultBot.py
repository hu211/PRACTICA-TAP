from agents.minecraft_agent import MinecraftAgent
import random
import time
import sys
from functools import partial

class InsultBot(MinecraftAgent):
    def __init__(self):
        super().__init__()
        self.insulting = False
        self.commands = {
            "start": self.start_insulting,
            "stop": self.stop_insulting
        }

    def insult(self):
        """Genera un insulto aleatorio y lo envía al chat (función pura)."""
        insults = ["loser", "jerk", "noob", "dork", "dummy", "nerd"]
        return random.choice(insults)

    def start_insulting(self, interval=5):
        """Inicia la acción de insultar a los jugadores en el chat."""
        self.insulting = True
        self.post_to_chat("¡Empezando a insultar!")
        while self.insulting:
            players = self.mc.getPlayerEntityIds()
            list(map(self.insult_player, players))  # Uso de map() funcional
            time.sleep(interval)
            self.listen_for_commands()

    def insult_player(self, player_id):
        """Insulta a un jugador moviéndose hacia él."""
        pos = self.mc.entity.getTilePos(player_id)
        self.move(pos.x, pos.y, pos.z)
        self.post_to_chat(self.insult())

    def stop_insulting(self):
        """Detiene la acción de insultar."""
        self.insulting = False
        self.post_to_chat("¡He dejado de insultar!")
        sys.exit()

    def listen_for_commands(self):
        """Escucha los comandos en el chat usando reflexión."""
        chat_posts = self.mc.events.pollChatPosts()
        commands = filter(lambda post: post.message.strip().lower() in self.commands, chat_posts)
        for post in commands:
            command = post.message.strip().lower()
            getattr(self, f"{command}_insulting")()  # Reflexión: ejecuta el método dinámicamente

    def interactive_chat(self):
        """Escucha mensajes y ejecuta comandos dinámicamente."""
        self.post_to_chat("Para empezar, escribe 'start'. Para parar, escribe 'stop'.")
        while True:
            chat_posts = self.mc.events.pollChatPosts()
            valid_posts = filter(lambda post: post.message.strip().lower() in self.commands, chat_posts)
            for post in valid_posts:
                command = post.message.strip().lower()
                self.commands[command]()  # Ejecuta el comando dinámicamente

if __name__ == "__main__":
    insult_bot = InsultBot()
    insult_bot.post_to_chat("¡Hola! Soy el bot de insultos. ¿Quieres que empiece a insultar?")
    insult_bot.interactive_chat()
