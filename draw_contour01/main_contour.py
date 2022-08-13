import sys

sys.path+= [r"/Users/samuelhsue/寫程式/blenderScripts/draw_a_line"]

import mathutils as mu
import math
import init_grease_pencil as init
from draw_line import *
from draw_circle import *
from rotate_stroke import *
from draw_peeled_surface import *
from draw_contours import *

gp_name ='gpencil01'
glayer_name = 'layer01'
glayer = init.init_grease_pencil(gp_name, glayer_name)

gp_frame = glayer.frames.new(0)

#draw_line(gp_frame, (0,0,0), (1,1,2))

# draw_circle(gp_frame, (0,0,0),1.1, 40)
# rotate_stroke(gp_frame.strokes[0], mu.Vector((1,1,0)), math.radians(90))

draw_contours(gp_frame,n=10,r=1.02)