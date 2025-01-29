import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))  # Apunta al directorio raíz

from agents.insultBot import InsultBot

def run_insult_bot():
    """Ejecutar el InsultBot"""
    print("Iniciando InsultBot...")
    insult_bot = InsultBot()
    insult_bot.post_to_chat("¡Hola! Soy el bot de insultos. ¿Quieres que empiece a insultar?")
    insult_bot.interactive_chat()

if __name__ == "__main__":
    run_insult_bot()