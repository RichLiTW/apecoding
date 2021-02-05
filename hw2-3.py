from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random
import time
x,y,z = mc.player.getTilePos()
y-=1
while True:
    tex = random.randrange(0,16)
    mc.setBlocks(x-15,y,z-15,x+15,y,z+15,35,tex)
    time.sleep(0.3)