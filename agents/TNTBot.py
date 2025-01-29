import time
import random
from mcpi.minecraft import Minecraft
from mcpi import block

class TNTBot:
    def __init__(self):
        """Inicializa la conexión con Minecraft."""
        try:
            self.mc = Minecraft.create()
            print("Conexión establecida con el servidor de Minecraft.")
        except Exception as e:
            print("Error al conectar con Minecraft: {e}")

    def obtener_posicion_jugador(self):
        """Devuelve la posición del jugador."""
        return self.mc.player.getTilePos()

    def generar_posiciones_tnt(self, pos, rango=5, cantidad=5):
        """Genera posiciones aleatorias cerca del jugador."""
        return [
            (pos.x + random.randint(-rango, rango), pos.y, pos.z + random.randint(-rango, rango))
            for _ in range(cantidad)
        ]

    def es_posicion_valida(self, x, y, z):
        """Verifica que la posición es válida (no en el aire)."""
        return self.mc.getBlock(x, y - 1, z) != block.AIR.id

    def colocar_tnt(self, x, y, z):
        """Coloca y activa TNT en una posición válida."""
        try:
            tnt_block = getattr(block, "TNT")  # Reflexión: obtener el bloque TNT dinámicamente
            self.mc.setBlock(x, y, z, tnt_block.id)
            self.mc.setBlock(x, y, z, tnt_block.id, 1)  # Encender TNT
            print("TNT colocado en ({x}, {y}, {z}) y explotará pronto...")
        except Exception as e:
            print("Error al colocar TNT: {e}")

    def start_exploding(self, count=5, delay=3):
        """Coloca TNT en posiciones válidas y lo hace explotar."""
        pos = self.obtener_posicion_jugador()
        print("Posición del jugador: {pos.x}, {pos.y}, {pos.z}")

        # Generar y filtrar posiciones válidas
        posiciones = self.generar_posiciones_tnt(pos, cantidad=count)
        posiciones_validas = filter(lambda p: self.es_posicion_valida(*p), posiciones)

        # Colocar TNT en posiciones válidas
        for x, y, z in posiciones_validas:
            self.colocar_tnt(x, y, z)
            time.sleep(delay)  # Espera antes de la siguiente explosión

        print("¡Explosiones terminadas!")

if __name__ == "__main__":
    tnt_bot = TNTBot()
    try:
        tnt_bot.start_exploding(count=5)
    except KeyboardInterrupt:
        print("¡Explosiones detenidas por el usuario!")
