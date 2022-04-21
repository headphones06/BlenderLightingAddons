import bpy
from bpy.props import FloatVectorProperty, EnumProperty
from mathutils import Vector
import math

bl_info = {
    "name": "Lightingset",
    "author": "headphones",
    "version": (0, 1, 0),
    "blender": (3, 10, 0),
    "location": "View3D > Add",
    "warning": "",
    "support": 'TESTING',
    "description": "選択中のオブジェクトに対し、X軸正方向を正面としたライト設置アドオン",
    "doc_url": "",
    "category": "Object",
}

class Noperation(bpy.types.Operator):

    bl_idname = "object._noperation"
    bl_label = "Nop"
    bl_description = "No operation"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        return {'FINISHED'}

class TWO_lightsetting(bpy.types.Operator):

    bl_idname = "object.two_lights"
    bl_label = "Two Lamps Lighting"
    bl_description = "Add two lamps"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        active_obj = context.active_object
        #first light add
        bpy.ops.object.light_add(type='AREA')
        active_light = context.active_object
        active_light.location = active_obj.location + Vector((7.0, -7.0, 6.0))
        active_light.rotation_euler.x = math.pi*1/3
        active_light.rotation_euler.y = 0
        active_light.rotation_euler.z = math.pi*1/4
        #second light add
        bpy.ops.object.light_add(type='AREA')
        active_light = context.active_object
        active_light.location = active_obj.location + Vector((3.8, 2, -1))
        active_light.rotation_euler.x = math.pi*105/180
        active_light.rotation_euler.y = 0
        active_light.rotation_euler.z = math.pi*2/3
        
        self.report({'INFO'},
                    "Add two lights")
        print("Operator '{}' is executed".format(self.bl_idname))
        return {'FINISHED'}

class THREE_lightsetting(bpy.types.Operator):

    bl_idname = "object.three_lights"
    bl_label = "Three Lamps Lighting"
    bl_description = "Add three lamps"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        moving = (-5.0, 0.0, 0.0)
        bpy.ops.object.duplicate()
        active_obj = context.active_object
        active_obj.location = active_obj.location + Vector(moving)
        self.report({'INFO'},
                    "Duplicated object(minus)")
        print("Operator '{}' is executed".format(self.bl_idname))
        return {'FINISHED'}

class LighttingSetMenu(bpy.types.Menu):

    bl_idname = "PLACTICE_MT_CupMenu"
    bl_label = "Lots Lighting"
    bl_description = "Menu for Lightings"

    def draw(self, context):
        layout = self.layout
        # メニュー項目の追加
        layout.operator(TWO_lightsetting.bl_idname, text=("Two Lamps Lighting"))
        layout.operator(Noperation.bl_idname, text=("Three Lamps Lighting"))

# メニューを構築する関数
def menu_fn(self, context):
    self.layout.separator()
    self.layout.menu(LighttingSetMenu.bl_idname)


# Blenderに登録するクラス
classes = [
    Noperation,
    TWO_lightsetting,
    THREE_lightsetting,
    LighttingSetMenu,
]


# アドオン有効化時の処理
def register():
    for c in classes:
        bpy.utils.register_class(c)
    bpy.types.VIEW3D_MT_add.append(menu_fn)

# アドオン無効化時の処理
def unregister():
    bpy.types.VIEW3D_MT_add.remove(menu_fn)
    for c in classes:
        bpy.utils.unregister_class(c)

if __name__ == "__main__":
    register()