from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random
import time
a = input('who r u?')
mc.postToChat('hi '+a+' and this house is for u')
x,y,z = mc.player.getPos()
mc.setBlocks(x,y,z,x+9,y+19,z+9,57)
mc.setBlocks(x+1,y+1,z+1,x+8,y+18,z+8,0)
mc.setBlocks(x+2,y+1,z,x+2,y+2,z,0)
mc.setBlocks(x,y+9,z,x+9,y+9,z+9,57)