import time
import random
from mcpi.minecraft import Minecraft
from mcpi import block

class TNTBot:
    def __init__(self):
        try:
            # Conectar al servidor de Minecraft
            self.mc = Minecraft.create()
            print("Conexión establecida correctamente con el servidor de Minecraft.")
        except Exception as e:
            print(f"Error al conectar con Minecraft: {e}")

    def start_exploding(self, count=5, delay=3):
        """ Coloca TNT en el mundo y lo hace explotar. """
        # Posición del jugador
        pos = self.mc.player.getTilePos()
        print(f"Posición del jugador: {pos.x}, {pos.y}, {pos.z}")

        for _ in range(count):
            # Generar una posición aleatoria cercana al jugador
            x = pos.x + random.randint(-5, 5)
            y = pos.y  # Mantener la misma altura, pero podría ajustarse para estar en un bloque sólido
            z = pos.z + random.randint(-5, 5)

            # Asegurarse de que la posición seleccionada esté sobre un bloque sólido
            if self.mc.getBlock(x, y-1, z) != block.AIR.id:  # Comprobamos que hay algo debajo
                try:
                    # Coloca el TNT en la posición
                    self.mc.setBlock(x, y, z, block.TNT.id)
                    # Enciende el TNT (el valor 1 enciende el TNT)
                    self.mc.setBlock(x, y, z, block.TNT.id, 1)
                    print(f"TNT colocado en ({x}, {y}, {z}) y explotará en {delay} segundos...")
                except Exception as e:
                    print(f"Error al colocar TNT: {e}")
            else:
                print(f"Posición {x}, {y}, {z} no es válida. Intentando otra posición.")
                continue  # Si no hay un bloque debajo, intenta otra posición.

            # Espera antes de hacer explotar el TNT
            time.sleep(delay)
            # El TNT explotará después de unos segundos
            time.sleep(2)  # Asegúrate de darle tiempo suficiente para explotar antes de la siguiente iteración.

if __name__ == "__main__":
    tnt_bot = TNTBot()
    try:
        tnt_bot.start_exploding(count=5)  # Ejecuta el bot con 5 explosiones.
    except KeyboardInterrupt:
        print("¡Explotando detenida por el usuario!")
