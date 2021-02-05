from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
for i in range(30):
    x,y,z = mc.player.getTilePos()
    mc.setBlock(x+1,y-1,z,1)
    mc.player.setPos(x+1.5,y,z+0.5)
    time.sleep(0.1)