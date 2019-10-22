import maya.cmds as mc

obj = mc.ls(sl=True)
parent = mc.listRelatives(obj[0], p=True)
children = mc.listRelatives(parent, c=True)
mc.select(children)
