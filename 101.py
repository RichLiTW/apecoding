from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getPos()
i = 0
l = 0
o = 0
for j in range(10):
    mc.setBlocks(x-j,y-l,z-j,x+j+6,y-l,z+j+6,168,1)
    mc.setBlocks(x-j,y-1-l,z-j,x+j+6,y-1-l,z+j+6,168,1)
    mc.setBlocks(x-j,y-2-l,z-j,x+j+6,y-2-l,z+j+6,168,1)
    l+=3
for k in range(6):
    for j in range(3):
        mc.setBlocks(x-j,y+i,z-j,x+6+j,y+i,z+6+j,168,1)
        mc.setBlocks(x-j,y+1+i,z-j,x+6+j,y+1+i,z+6+j,168,1)
        mc.setBlocks(x-j,y+2+i,z-j,x+6+j,y+2+i,z+6+j,168,1)
        i+=3
for j in range(5):
    mc.setBlocks(x+2+j,y+54+j,z+2+j,x+4-j,y+54+j,z+4-j,168,1)
for j in range(2):
    mc.setBlocks(x+2+j,y+59+j,z+2+j,x+4-j,y+59+j,z+4-j,168,1)
mc.setBlocks(x+3,y+61,z+3,x+3,y+67,z+3,168,1)