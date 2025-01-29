from mcpi.minecraft import Minecraft
from mcpi import block
import time

class MinecraftAgent:
    def __init__(self):
        """Inicializa el agente de Minecraft."""
        self.mc = Minecraft.create()
        self.mc.postToChat("¡Hola! Agente conectado al servidor.")

    def post_to_chat(self, message):
        """Publica un mensaje en el chat."""
        self.mc.postToChat(message)

    def move(self, x, y, z):
        """Mueve al agente a una posición específica."""
        self.mc.player.setTilePos(x, y, z)

    def get_player_position(self):
        """Obtiene la posición actual del jugador."""
        return self.mc.player.getTilePos()

    def wait(self, seconds):
        """Espera una cantidad específica de tiempo."""
        time.sleep(seconds)

    def place_block(self, x, y, z, block_type):
        """Coloca un bloque en una posición específica."""
        self.mc.setBlock(x, y, z, block_type)

    def place_blocks(self, x1, y1, z1, x2, y2, z2, block_type):
        """Coloca un área rectangular de bloques."""
        self.mc.setBlocks(x1, y1, z1, x2, y2, z2, block_type)

    def get_random_position(self, x_range=(-50, 50), y_range=(1, 63), z_range=(-50, 50)):
        """Genera una posición aleatoria dentro de los rangos especificados."""
        import random
        x = random.randint(*x_range)
        y = random.randint(*y_range)
        z = random.randint(*z_range)
        return x, y, z

    def poll_chat_posts(self):
        """Obtiene los mensajes recientes del chat."""
        return self.mc.events.pollChatPosts()

    def detect_block(self, x, y, z):
        """Detecta qué bloque está en una posición específica."""
        return self.mc.getBlock(x, y, z)

    def replace_block(self, x, y, z, old_block, new_block):
        """Reemplaza un bloque si coincide con el tipo especificado."""
        if self.detect_block(x, y, z) == old_block:
            self.place_block(x, y, z, new_block)

    def follow_player(self, player_id):
        """Sigue a un jugador en el mundo."""
        pos = self.mc.entity.getTilePos(player_id)
        self.move(pos.x, pos.y, pos.z)

    def build_structure(self, x, y, z, structure):
        """Construye una estructura basada en una matriz de bloques."""
        for dz, layer in enumerate(structure):
            for dy, row in enumerate(layer):
                for dx, block_type in enumerate(row):
                    self.place_block(x + dx, y + dy, z + dz, block_type)
