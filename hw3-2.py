from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time,random

while True:
    ENT = random.randrange(0,105)
    POS = mc.player.getPos()
    x,y,z = POS.x + random.uniform(-10,10),POS.y + 5,POS.z + random.uniform(-10,10)
    mc.spawnEntity(x,y,z,19)
    time.sleep(0.001)