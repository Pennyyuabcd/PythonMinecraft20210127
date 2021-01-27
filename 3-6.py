from mcpi.minecraft import Minecraft
PY=Minecraft.create()
x,y,z=PY.player.getTilePos()
for i in range(0,20):
    PY.setBlock(x+i,y-1,z+i,56)
    PY.setBlock(x+i+1,y-1,z+i,56)
    PY.setBlock(x+i+2,y-1,z+i,56)

