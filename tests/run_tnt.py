import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))  # Apunta al directorio raíz

from agents.TNTBot import TNTBot

def run_tnt_bot():
    """Ejecutar el TNTBot"""
    print("Iniciando TNTBot...")
    tnt_bot = TNTBot()
    tnt_bot.start_exploding(count=5)

if __name__ == "__main__":
    run_tnt_bot()