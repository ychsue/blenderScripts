import bpy
import math

def draw_1_segment(gp_frame:bpy.types.GPencilFrame,r=4.0, n=5, m=0, segments=40):
    d_theta = math.pi/(2*n-1)
    sin_m = math.sin(m*d_theta)
    cos_m_p_half = math.cos((m+.5)*d_theta)
    d_l = 2*r*math.sin(d_theta/2)

    R = r*sin_m/cos_m_p_half
    Theta_half = math.pi*cos_m_p_half

    cx = -R+d_l*m

    #get storke
    gp_stroke = gp_frame.strokes.new()

    if m == n-1:
        gp_stroke.points.add(4, pressure=20)
        gp_stroke.points[0].co = (d_l*m, -math.pi*r*sin_m,0)
        gp_stroke.points[1].co = (d_l*m, math.pi*r*sin_m,0)
        gp_stroke.points[2].co = (d_l*(m+1), math.pi*r*sin_m,0)
        gp_stroke.points[3].co = (d_l*(m+1), -math.pi*r*sin_m,0)

    else:
        gp_stroke.points.add(segments*2, pressure=20)
        #draw first curve from -Theta -> Theta
        d_phi = 2*Theta_half/(segments-1)
        phi = -Theta_half
        for i0 in range(segments):
            x = R*math.cos(phi)+cx
            y = R*math.sin(phi)
            z = 0
            gp_stroke.points[i0].co = (x,y,z)
            phi = phi+d_phi 

        #draw the 2nd curve from Theta -> - Theta
        phi = Theta_half
        for i0 in range(segments):
            x = (R+d_l)*math.cos(phi)+cx
            y = (R+d_l)*math.sin(phi)
            z = 0
            gp_stroke.points[i0+segments].co = (x,y,z)
            phi = phi-d_phi 
    
    gp_stroke.use_cyclic = True

def draw_peeled_surface(gp_frame:bpy.types.GPencilFrame, r=4, n=5, segments=40):
    for i0 in range(n):
        draw_1_segment(gp_frame,r=r, n=n,m=i0,segments=segments) 