from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random
x,y,z = mc.player.getPos()
COL = random.randrange(0,16)
mc.setBlock(x,y,z,35,COL)
for i in range(150):
    f = random.choice(range(1,7))
    COL = random.randrange(0,16)
    if f == 1:
        mc.setBlocks(x+1,y,z,x+2,y,z,35,COL)
        x+=2
    if f == 2:
        mc.setBlocks(x-1,y,z,x-2,y,z,35,COL)
        x-=2
    if f == 3:
        mc.setBlocks(x,y,z+1,x,y,z+2,35,COL)
        z+=2
    if f == 4:
        mc.setBlocks(x,y,z-1,x,y,z-2,35,COL)
        z-=2
    if f == 5:
        mc.setBlocks(x,y+1,z,x,y+2,z,35,COL)
        y+=2
    if f == 6:
        mc.setBlocks(x,y-1,z,x,y-2,z,35,COL)
        y-=2