from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
for i in range(20):
    x,y,z = mc.player.getPos()
    x+=i
    mc.setBlock(x,y-1,z,1)
mc.setBlocks(x+1,y-1,z-5,x+6,y+4,z+5,1)
mc.setBlocks(x+2,y,z-4,x+5,y+3,z+4,0)
mc.setBlocks(x+1,y,z,x+1,y+1,z,0)
time.sleep(3)
mc.spawnEntity(x+3,y,z,20)
mc.spawnEntity(x+3,y,z+3,20)
mc.spawnEntity(x+3,y,z-3,20)