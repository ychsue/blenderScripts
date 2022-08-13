# import sys
# sys.path+= [r"/Users/samuelhsue/寫程式/blenderScripts/draw_a_line"]

import bpy

def draw_line(gp_frame:bpy.types.GPencilFrame, p0:tuple, p1:tuple):
    """
    用兩點畫線
    """
    gp_stroke = gp_frame.strokes.new()
    gp_stroke.display_mode = '3DSPACE' #還有其他選擇

    gp_stroke.points.add(count=2,pressure=80.0)
    gp_stroke.points[0].co = p0
    gp_stroke.points[1].co = p1

    return gp_stroke