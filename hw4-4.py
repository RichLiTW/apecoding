from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random
x,y,z = mc.player.getPos()
for i in range(10):
    for j in range(10):
        COL = random.randrange(0,16)
        mc.setBlock(x+j,y-1,z+i,35,COL)
ANS = random.randrange(0,16)
ID = mc.getPlayerEntityId("RiceTW_YT")
while True:
    hits = mc.events.pollBlockHits()
    if len(hits) > 0:
        hit = hits[0]
        block = mc.getBlockWithData(hit.pos)
        data = block.data
        if data > ANS:
            mc.postToChat('haha u wrong')
        elif data < ANS:
            mc.postToChat('cmon man')
        else:
            mc.postToTitle(ID,'Wow wow wow')
            mc.setBlock(hit.pos,57)
            break