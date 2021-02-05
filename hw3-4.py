from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random
x,y,z = mc.player.getPos()
def Tree(x,y,z):
    mc.setBlocks(x+1,y+2,z,x+3,y+5,z+2,35,COLOR)
    mc.setBlocks(x+2,y,z+1,x+2,y+4,z+1,17)

for i in range(50):
    for j in range(50):
        COLOR = random.randrange(0,16)
        Tree(x+i*j,y+i*i,z+j*i)