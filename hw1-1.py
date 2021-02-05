from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

x = 7845.5
y = 145.5
z = 777.5
mc.player.setPos(x,y,z)
time.sleep(3)
mc.player.setPos(x+156,y-4,z)
time.sleep(3)
mc.player.setPos(x,y,z-100)