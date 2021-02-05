from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

x,y,z = mc.player.getTilePos()
mc.setBlock(x+2,y,z,1)
mc.setBlock(x-2,y,z,1)
mc.setBlock(x,y,z+2,1)
mc.setBlock(x,y,z-2,1)
mc.setBlock(x+1,y,z+1,1)
mc.setBlock(x+1,y,z-1,1)
mc.setBlock(x-1,y,z-1,1)
mc.setBlock(x-1,y,z+1,1)