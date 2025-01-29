from agents.minecraft_agent import MinecraftAgent
import random
import time
import sys

class InsultBot(MinecraftAgent):
    def __init__(self):
        super().__init__()  # Llamamos al constructor de MinecraftAgent
        self.insulting = False  # Variable para controlar el estado de la acción

    def insult(self):
        """Genera un insulto aleatorio y lo envía al chat"""
        insults = ["loser", "jerk", "noob", "dork", "dummy", "nerd"]
        insult = random.choice(insults)
        self.post_to_chat(insult)

    def start_insulting(self, interval=5):
        """Inicia la acción de insultar a los jugadores en el chat"""
        self.insulting = True
        self.post_to_chat("¡Empezando a insultar!")
        while self.insulting:
            players = self.mc.getPlayerEntityIds()
            for player in players:
                self.move_to_player(player)
                self.insult()
                self.wait(interval)
            # Escucha el chat cada vez que el bot insulta
            self.listen_for_stop()

    def stop_insulting(self):
        """Detiene la acción de insultar"""
        self.insulting = False
        self.post_to_chat("¡He dejado de insultar!")
        sys.exit()  # Salir del programa

    def listen_for_stop(self):
        """Escuchar si alguien escribe 'stop' para parar el bot"""
        chat_posts = self.mc.events.pollChatPosts()
        for post in chat_posts:
            message = post.message.strip().lower()

            if message == "stop":
                self.stop_insulting()  # Detener la acción de insultar
                return  # Salir del bucle de escucha

    def interactive_chat(self):
        """Escuchar los mensajes del chat para los comandos 'start' y 'stop'"""
        self.post_to_chat("Para empezar a insultar, escribe 'start'. Para parar, escribe 'stop'.")

        while True:
            chat_posts = self.mc.events.pollChatPosts()
            for post in chat_posts:
                message = post.message.strip().lower()

                if message == "start" and not self.insulting:
                    self.start_insulting()  # Comienza a insultar
                elif message == "stop" and self.insulting:
                    self.stop_insulting()  # Detiene el insulto
                else:
                    self.post_to_chat("No entiendo lo que quieres decir. Usa 'start' para comenzar y 'stop' para parar.")
                    self.wait(5)

    def move_to_player(self, player_id):
        """Mover el agente hacia un jugador"""
        pos = self.mc.entity.getTilePos(player_id)
        self.move(pos.x, pos.y, pos.z)

if __name__ == "__main__":
    insult_bot = InsultBot()
    insult_bot.post_to_chat("¡Hola! Soy el bot de insultos. ¿Quieres que empiece a insultar?")
    insult_bot.interactive_chat()