from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random
import time
for i in range(10):
    tex = random.randrange(0,150)
    x,y,z = mc.player.getTilePos()
    mc.setBlocks(x,y-1,z,x+15,y-1,z+30,tex)
    time.sleep(0.5)