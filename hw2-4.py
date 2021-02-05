from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random
import time

x,y,z = mc.player.getTilePos()
mc.setBlocks(x,y,z,x+4,y,z+4,57)
mc.setBlocks(x,y,z,x+4,y+4,z,57)
mc.setBlocks(x,y,z,x,y+4,z+4,57)
mc.setBlocks(x+4,y,z,x+4,y+4,z+4,57)
mc.setBlocks(x,y,z+4,x+4,y+4,z+4,57)
mc.setBlocks(x,y+4,z,x+4,y+4,z+4,57)