import bpy
import math
from draw_circle import draw_circle

def draw_contours(gp_frame: bpy.types.GPencilFrame, n=5, r=1.05, segments=40):
    d_theta = math.pi/(2*n-1)

    # 1. draw a verticle arc
    gp_stroke = gp_frame.strokes.new()
    gp_stroke.display_mode = '3DSPACE'
    gp_stroke.points.add(segments,pressure =40)
    dd = d_theta*n/segments
    for i in range(segments):
        theta = i*dd
        x=r*math.sin(theta)
        y=0
        z=r*math.cos(theta)
        gp_stroke.points[i].co = (x,y,z)

    # 2. draw circles
    for i in range(n):
        theta =d_theta*(i+1)
        draw_circle(gp_frame,(0,0,r*math.cos(theta)),r*math.sin(theta),segments)
    