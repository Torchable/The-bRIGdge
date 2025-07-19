 # The bRIGdge 
# by Colin Cheng 
# 
#  The bRIGdge is a window I created that saves time creating commonly used custom controls for your rig.
# To use, simply drag the .py file into your maya file and it will run.

#import bRIGdgeScript.thebRIGdge as bRIGdge
#import importlib
#importlib.reload(bRIGdge)

import maya.cmds as cmds
import maya.mel as mm


#offset group attribute 
def createoffset():
    offsetgroupnum = cmds.intField('offsetgroupnum', query=True, v = True)
    if cmds.checkBox('createoffset', query=True, v=True):
        if offsetgroupnum > 0:
            for i in range(0, offsetgroupnum):
                cmds.group() 
        else:
            cmds.group()

#gimbal lock fix attribute
def gimbalfix():
    if cmds.checkBox('gimbal', query=True, value=True):
        cmds.addAttr(ln='RotationOrder', k = True, attributeType= 'enum', en='xyz:yzx:zxy:xzy:yxz:zyx')
        cmds.connectAttr('.RotationOrder', '.rotateOrder')

#Creates an FK IK Switch with selected control
def switch(createoffset):
    createoffset = cmds.checkBox('createoffset', query=True, v=True)
    switchlist = ['.translateX','.translateY','.translateZ','.rotateX','.rotateY','.rotateZ','.scaleX','.scaleY','.scaleZ','.visibility']
    if cmds.checkBox('fkikswitch', query = True, v= True):
        if createoffset == False:
            cmds.warning('It is recommended that you have "Create offset Group" turned on when using this feature')
        cmds.addAttr(ln='FKIKSwitch', niceName='FK IK Switch', k = True, attributeType= 'float', min=0, max = 1, en='FK:IK')
        for x in range(len(switchlist)):
            cmds.setAttr(switchlist[x], lock= True, k=False)
            x += x + 1

#Runs checkbox statememts 
def queries():
    gimbalfix()
    switch(createoffset)
    createoffset()
    
#Creates Circle Control 
def CreateCircle():
    createcircle = cmds.circle(nr=(0,1,0))
    queries()

#Creates Cube Control
def CreateCube():
    cubecreate = mm.eval('curve -d 1 -p 0.5 0.5 -0.5 -p 0.5 0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 ;')
    queries()

#Creates Gear Control
def CreateGear():
    creategear = mm.eval('curve -d 1 -p -0.22961 0 0.92388 -p -0.206649 0 1.02388 -p -0.114805 0 1.12388 -p 0.114805 0 1.12388 -p 0.206649 0 1.02388 -p 0.22961 0 0.92388 -p 0.490923 0 0.81564 -p 0.577869 0 0.870115 -p 0.713523 0 0.875882 -p 0.875882 0 0.713523 -p 0.870115 0 0.577869 -p 0.81564 0 0.490923 -p 0.92388 0 0.22961 -p 1.02388 0 0.206649 -p 1.12388 0 0.114805 -p 1.12388 0 -0.114805 -p 1.02388 0 -0.206649 -p 0.92388 0 -0.22961 -p 0.81564 0 -0.490923 -p 0.870115 0 -0.577869 -p 0.875882 0 -0.713523 -p 0.713523 0 -0.875882 -p 0.577869 0 -0.870115 -p 0.490923 0 -0.81564 -p 0.22961 0 -0.92388 -p 0.206649 0 -1.02388 -p 0.114805 0 -1.123879 -p -0.114805 0 -1.123879 -p -0.206649 0 -1.023879 -p -0.22961 0 -0.923879 -p -0.490923 0 -0.81564 -p -0.577869 0 -0.870115 -p -0.713524 0 -0.875882 -p -0.875882 0 -0.713523 -p -0.870115 0 -0.577869 -p -0.81564 0 -0.490923 -p -0.92388 0 -0.22961 -p -1.02388 0 -0.206649 -p -1.123879 0 -0.114805 -p -1.123879 0 0.114805 -p -1.023879 0 0.206649 -p -0.923879 0 0.22961 -p -0.81564 0 0.490923 -p -0.870115 0 0.57787 -p -0.875882 0 0.713524 -p -0.713523 0 0.875883 -p -0.577869 0 0.870115 -p -0.490923 0 0.81564 -p -0.22961 0 0.92388 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33 -k 34 -k 35 -k 36 -k 37 -k 38 -k 39 -k 40 -k 41 -k 42 -k 43 -k 44 -k 45 -k 46 -k 47 -k 48 ;')
    queries()

#Creates Icosagon Control 
def CreateIco():
    createico = mm.eval('curve -d 1 -p -0.276393 0.850651 -0.447214 -p 0.276393 0.850651 0.447214 -p -0.723607 0.525731 0.447214 -p -0.276393 0.850651 -0.447214 -p -0.894427 -7.81933e-08 -0.447214 -p -0.723607 0.525731 0.447214 -p -0.723607 -0.525731 0.447214 -p -0.894427 -7.81933e-08 -0.447214 -p -0.276393 -0.850651 -0.447214 -p -0.723607 -0.525731 0.447214 -p -0.723607 0.525731 0.447214 -p 0 0 1 -p -0.723607 -0.525731 0.447214 -p 0.276393 -0.850651 0.447214 -p 0 0 1 -p 0.276393 0.850651 0.447214 -p -0.276393 0.850651 -0.447214 -p 0.723607 0.525731 -0.447214 -p 0.276393 0.850651 0.447214 -p 0.894427 0 0.447214 -p 0 0 1 -p 0.276393 -0.850651 0.447214 -p 0.723607 -0.525731 -0.447214 -p 0.894427 0 0.447214 -p 0.723607 0.525731 -0.447214 -p 0 0 -1 -p 0.723607 -0.525731 -0.447214 -p -0.276393 -0.850651 -0.447214 -p -0.894427 -7.81933e-08 -0.447214 -p 0 0 -1 -p -0.276393 0.850651 -0.447214 -p 0 0 -1 -p -0.276393 -0.850651 -0.447214 -p 0.723607 -0.525731 -0.447214 -p 0.276393 -0.850651 0.447214 -p 0.894427 0 0.447214 -p 0.276393 -0.850651 0.447214 -p -0.276393 -0.850651 -0.447214 -p 0.723607 -0.525731 -0.447214 -p 0.723607 0.525731 -0.447214 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33 -k 34 -k 35 -k 36 -k 37 -k 38 -k 39 ;')
    queries()

#Creates Arrow Control
def CreateArrow():
    createarrow = mm.eval('curve -d 1 -p 1 0 0 -p 1 0 -2 -p -1 0 -2 -p -1 0 0 -p -2 0 0 -p 0 0 2 -p 2 0 0 -p 1 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 ;')
    queries()
#Creates Square Control
def CreateSquare():
    createsquare = mm.eval('curve -d 1 -p 5 0 -5 -p -5 0 -5 -p -5 0 5 -p 5 0 5 -p 5 0 -5 -k 0 -k 1 -k 2 -k 3 -k 4 ;')
    queries()
#Creates Cone Control 
def CreateCone():
    createcone = mm.eval('curve -d 1 -p 0.0270729 0.174247 0.083322 -p 0 -0.000972612 0 -p 0.0708779 0.174247 0.0514958 -p 0.0270729 0.174247 0.083322 -p -0.027073 0.174247 0.083322 -p 0 -0.000972612 0' 
                                     '-p -0.027073 0.174247 0.083322 -p -0.0708779 0.174247 0.0514958 -p 0 -0.000972612 0 -p -0.0708779 0.174247 0.0514958 -p -0.0876099 0.174247 0 -p 0 -0.000972612 0' 
                                     '-p -0.0876099 0.174247 0 -p -0.0708779 0.174247 -0.0514958 -p 0 -0.000972612 0 -p -0.0708779 0.174247 -0.0514958 -p -0.0270729 0.174247 -0.083322 -p 0 -0.000972612 0' 
                                     '-p -0.0270729 0.174247 -0.083322 -p 0.027073 0.174247 -0.083322 -p 0 -0.000972612 0 -p 0.027073 0.174247 -0.083322 -p 0.0708779 0.174247 -0.0514958 -p 0 -0.000972612 0' 
                                     '-p 0.0708779 0.174247 -0.0514958 -p 0.0876099 0.174247 5.22196e-09 -p 0 -0.000972612 0 -p 0.0876099 0.174247 5.22196e-09 -p 0.0708779 0.174247 0.0514958' 
                                     '-k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 ;')
    queries()
    
#Creates joints by input #
def CreateJoints():
    jseq = int(input())
    jnum = 0
    for i in range(jseq):
        cmds.joint(p= (jnum, 0, 0))
        jnum = jnum + 1         
     
#---------------------------------------------------------------------
def brIGdgewindow():
    # Makes sure only one window is open 
    if cmds.window('thebRIGdgeUI', exists=True):
        cmds.deleteUI('thebRIGdgeUI')

    #window creation
    bwindow = cmds.window('thebRIGdgeUI', title='The bRIGdge', width = 500, height = 540)

    main_layout = cmds.columnLayout(width=500, height=540)

    #add frame layouts
    cmds.text(l= 'Welcome to the bRIGdge', al ='center', font='fixedWidthFont', rs = False, w=500, h =45 )
    
    joint_frame(main_layout)
    cmds.separator(style='none')
    control_data_frame(bwindow, main_layout)
    queries_arguements_frame(bwindow, main_layout)
    color_settings_frame(bwindow, main_layout)

    #Shows window
    cmds.showWindow(bwindow)


def joint_frame(main_layout):
    jointframe = cmds.frameLayout(label='Joint Sequence', width=500, height=50, collapsable=True, parent=main_layout, 
    collapseCommand= lambda: brigdge_collapse(window, frame_layout, height))
    
    jcl = cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[(1, 165)], rowSpacing=[(1, 2)], parent=jointframe)
    
    JointSequence = cmds.button( label='Create Joint Sequence', command= 'CreateJoints()', height= 25, width=495, parent=jcl)
    
def control_data_frame(window, main_layout):
    dataframe = cmds.frameLayout(label='Control Creation', width=500, height=230,
                                 collapsable=True, parent=main_layout)
    rcl = cmds.rowColumnLayout(numberOfColumns=3, columnWidth=[(1, 165), (2, 165), (3, 165)],
                               columnOffset=[(1, 'both', 3), (2, 'both', 3), (3, 'both', 3)], 
                               rowSpacing=[(1, 2), (2, 2), (3,2)], parent=dataframe)

    #Buttons 
    CircleControl = cmds.button( label='Create Circle Control', command= 'CreateCircle()', height= 30, width=10, parent=rcl)
    CubeControl = cmds.button( label='Create Cube Control', command = 'CreateCube()', height= 30, width=10, parent=rcl)
    GearControl = cmds.button( label='Create Gear Control', command = 'CreateGear()', height= 30, width=10, parent=rcl)

    IcosagonControl = cmds.button( l='Create Icosagon Control', command = 'CreateIco()', height= 30, width=10, parent=rcl)
    ArrowControl = cmds.button (l = 'Create Arrow Control', command = 'CreateArrow()', height= 30, width=10, parent=rcl)
    SquareControl = cmds.button (l = 'Create Square Control', command = 'CreateSquare()', height= 30, width=10, parent=rcl)  
    
    ConeControl = cmds.button (l = 'Create Cone Control', command = 'CreateCone()', height= 30, width=10, parent=rcl) 
    
def queries_arguements_frame(window, main_layout):
    argframe = cmds.frameLayout(label='Queries', width=500, height=130,
                                 collapsable=True, parent=main_layout)
    qrcl = cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[(1, 135)], 
                               rowSpacing=[(1, 2)], parent=argframe)                             
                                 
    CreateOffset = cmds.checkBox('createoffset', label='Create Offset Group', v = False)
    OffsetGroupName = cmds.text(l = 'Number of Groups', fn = 'smallBoldLabelFont', al = 'left')
    OffsetGroupnum = cmds.intField('offsetgroupnum', m = True, w = 5, h = 20, min = 0)
    GimbalFix = cmds.checkBox ('gimbal', label = 'Rotation Order', v = False)
    FKIKSwitch = cmds.checkBox('fkikswitch', label = 'FK IK Switch', v = False)


# Creates colors for controls
def color_settings_frame(window, main_layout):
    colorframe = cmds.frameLayout(label='Color Settings', width=500, height=90,
                                 collapsable=True, parent=main_layout)


def brigdge_collapse(window, frame_layout, height):
    window_height = cmds.window(window, query=True, height=True)
    frame_height = cmds.frameLayout(frame_layout, query=True, height=True)
    cmds.window(window, edit=True, height=window_height - height + 30)
    cmds.frameLayout(frame_layout, edit=True, height=frame_height - height + 30)

def brigdge_expand(window, frame_layout, height):
    window_height = cmds.window(window, query=True, height=True)
    frame_height = cmds.frameLayout(frame_layout, query=True, height=True)
    cmds.window(window, edit=True, height=window_height + height - 30)
    cmds.frameLayout(frame_layout, edit=True, height=frame_height + height - 30)