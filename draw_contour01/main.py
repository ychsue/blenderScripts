import sys

sys.path += [r"C:\\Users\\hsuy1\\OneDrive\\Documents\\blenderScripts\\draw_contour01"]

import mathutils as mu
import math
import init_grease_pencil as init
from draw_line import *
from draw_circle import *
from rotate_stroke import *
from draw_peeled_surface import *


gp_name = 'gpencil01'
glayer_name = 'layer01'
glayer = init.init_grease_pencil(gp_name, glayer_name)

gp_frame = glayer.frames.new(0)

# draw_line(gp_frame, (0,0,0), (1,1,2))

# draw_circle(gp_frame, (0,0,0),1.1, 40)
# rotate_stroke(gp_frame.strokes[0], mu.Vector((1,1,0)), math.radians(90))

draw_peeled_surface(gp_frame, r=4, n=5)
