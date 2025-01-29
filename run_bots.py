# run_bots.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))  # Apunta al directorio raíz

from agents.insultBot import InsultBot
from agents.TNTBot import TNTBot
from agents.OracleBot import OracleBot

def run_insult_bot():
    """Ejecutar el InsultBot"""
    print("Iniciando InsultBot...")
    insult_bot = InsultBot()
    insult_bot.post_to_chat("¡Hola! Soy el bot de insultos. ¿Quieres que empiece a insultar?")
    insult_bot.interactive_chat()

def run_tnt_bot():
    """Ejecutar el TNTBot"""
    print("Iniciando TNTBot...")
    tnt_bot = TNTBot()
    tnt_bot.start_exploding(count=5)

def run_oracle_bot():
    """Ejecutar el OracleBot"""
    print("Iniciando OracleBot...")
    oracle_bot = OracleBot()
    oracle_bot.command_iniciar_oraculo()

if __name__ == "__main__":
    print("Elige un bot para ejecutar:")
    print("1. InsultBot")
    print("2. TNTBot")
    print("3. OracleBot")
    
    choice = input("Ingresa el número de tu elección (1/2/3): ")
    
    if choice == "1":
        run_insult_bot()
    elif choice == "2":
        run_tnt_bot()
    elif choice == "3":
        run_oracle_bot()
    else:
        print("Opción no válida. Intenta de nuevo.")
