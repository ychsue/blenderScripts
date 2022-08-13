# Gotten from [this article](https://towardsdatascience.com/blender-2-8-grease-pencil-scripting-and-generative-art-cbbfd3967590)
import bpy

D = bpy.data
C = bpy.context

def get_grease_pencil(g_obj_name='GPencil')-> bpy.types.GreasePencil:
    """
    回傳給定名字的 grease-pencil 物件，若不存在，就造一個新的。
    :param g_obj_name: 油筆在scene裡的 name/key 值 
    """
    if g_obj_name not in C.scene.objects:
        bpy.ops.object.gpencil_add(align='WORLD', location=(0, 0, 0), scale=(1, 1, 1), type='EMPTY')
        #rename it
        C.scene.objects[-1].name = g_obj_name

    # Get grease pencil object
    gObj = C.scene.objects[g_obj_name]

    return gObj

def get_grease_pencil_layer(gpencil: bpy.types.GreasePencil, g_layer_name='GP_Layer', clear_layer=False)-> bpy.types.GPencilLayer:
    """
    回傳一個給定名字的layer，若無，就造一個。
    :param gpencil: 要取得的圖層所在的父級 grease pencil object
    :param g_layer_name: 該圖層的名字
    :param clear_layer: 是否清理之前圖層的資料
    """

    gpencil_layer: bpy.types.GPencilLayer
    if gpencil.data.layers and g_layer_name in gpencil.data.layers:
        gpencil_layer = gpencil.data.layers[g_layer_name]
    else:
        gpencil_layer = gpencil.data.layers.new(g_layer_name, set_active=True)

    if clear_layer:
        gpencil_layer.clear()

    return gpencil_layer

def init_grease_pencil(g_obj_name='GPencil01', g_layer_name='GP_Layer02', clear_layer=True)->bpy.types.GPencilLayer:
    """
    初始化 grease pencil，其中含有一個圖層
    """
    gpencil = get_grease_pencil(g_obj_name=g_obj_name)
    gpencil_layer = get_grease_pencil_layer(gpencil,g_layer_name,clear_layer)
    return gpencil_layer

