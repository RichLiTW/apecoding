from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random
import time

while True:
    tex = random.randrange(0,9)
    x,y,z = mc.player.getPos()
    mc.setBlock(x,y,z,38,tex)
    time.sleep(0.2)