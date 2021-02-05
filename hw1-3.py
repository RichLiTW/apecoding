from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

while True:
    x,y,z = mc.player.getTilePos()
    mc.postToChat('haha you got hacked, located you at x:'+str(x)+' y:'+str(y)+' z:'+str(z))
    time.sleep(0.3)