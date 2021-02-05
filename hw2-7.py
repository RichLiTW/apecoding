from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random
import time

x,y,z = mc.player.getPos()
f = 0
while f < 10:
    tex = random.randrange(0,16)
    mc.setBlocks(x-10,y,z,x+10,y+5,z,35,tex)
    f+=1
    z-=2