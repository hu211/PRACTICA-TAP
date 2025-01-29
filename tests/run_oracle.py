import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))  # Apunta al directorio raíz

from agents.OracleBot import OracleBot

def run_oracle_bot():
    """Ejecutar el OracleBot"""
    print("Iniciando OracleBot...")
    oracle_bot = OracleBot()
    oracle_bot.command_iniciar_oraculo()

if __name__ == "__main__":
    run_oracle_bot()