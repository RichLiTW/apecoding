from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

x,y,z = mc.player.getPos()
SC = 1
time.sleep(3)
for i in range(8):
    for i in range(SC):
        mc.spawnEntity(x,y,z,30)
    SC*=2