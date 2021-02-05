from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

x,y,z = mc.player.getPos()

time.sleep(15)
mc.player.setPos(x,y,z)