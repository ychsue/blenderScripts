import bpy
import math

def draw_circle(gp_frame: bpy.types.GPencilFrame, center: tuple, radius: float, segments: int):
    """
    畫圓圈
    """
    gp_stroke = gp_frame.strokes.new()
    gp_stroke.display_mode = '3DSPACE' #You can choose others
    gp_stroke.use_cyclic = True

    d_angle = 2*math.pi/segments
    gp_stroke.points.add(segments,pressure=40)
    for i0 in range(segments):
        x = center[0]+radius*math.cos(d_angle*i0)
        y = center[1]+radius*math.sin(d_angle*i0)
        z = center[2]
        gp_stroke.points[i0].co = (x,y,z)

    return gp_stroke
