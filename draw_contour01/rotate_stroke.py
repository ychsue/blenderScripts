import bpy
import mathutils as mu
import math
import numpy as np

def rotate_stroke(stroke: bpy.types.GPencilStroke, norm: mu.Vector, angle=0.0):
    """
    這是zyz旋轉方式,2pi為一個圓的角度
    """

    transform_matrix = np.array(mu.Matrix.Rotation(angle,4,norm).to_3x3())
    for i,p in enumerate(stroke.points):
        p.co = transform_matrix @ np.array(p.co).reshape(3,1)