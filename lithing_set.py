bl_info = {
    "name": "LLightingset",
    "author": "headphones",
    "version": (0, 1, 0),
    "blender": (3, 10, 0),
    "location": "View3D > Add",
    "warning": "",
    "description": "選択中のオブジェクトに対し、X軸正方向を正面としたライト設置アドオン",
    "doc_url": "",
    "category": "Object",
}

# ref: https://github.com/Cfyzzz/Other-scripts/blob/master/f2.py

import bpy
from bpy.props import FloatVectorProperty, EnumProperty
from mathutils import Vector

class Noperation(bpy.types.Operator):

    bl_idname = "object._noperation"
    bl_label = "Nop"
    bl_description = "No operation"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        return {'FINISHED'}

class TWO_lightsetting(bpy.types.Operator):

    bl_idname = "object.plactice_plus_duplicate"
    bl_label = "Plus Duplicate"
    bl_description = "Duplication by plus vectol"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        active_obj = context.active_object
        #first light add
        bpy.ops.object.light_add(type='Area',rotation=(60.0, 0.0, 45.0))
        active_light = context.active_object
        active_light.location = active_obj.location + Vector((7.0, -7.0, 5.0))
        #second light add
        bpy.ops.object.light_add(type='Area',rotation=(120.0, 0.0, 120.0))
        active_light = context.active_object
        active_light.location = active_obj.location + Vector((7.0, 5.5, -1.0))
        
        self.report({'INFO'},
                    "Add two lights")
        print("Operator '{}' is executed".format(self.bl_idname))
        return {'FINISHED'}

class THREE_lightsetting(bpy.types.Operator):

    bl_idname = "object.plactice_minus_duplicate"
    bl_label = "Minus Duplicate"
    bl_description = "Duplication by minus vectol"
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

class DuplicatingMenu(bpy.types.Menu):

    bl_idname = "PLACTICE_MT_CupMenu"
    bl_label = "Dup Menu"
    bl_description = "Menu for Duplication"

    # 引数
    #   self: メニュークラスのインスタンス [メニュークラス]
    #   context: drawメソッドが呼ばれたときのコンテキスト
    #            [bpy.types.Context]
    def draw(self, context):
        layout = self.layout
        # メニュー項目の追加
        layout.operator(TWO_lightsetting.bl_idname, text=("Two Lamp Lighting"))
        layout.operator(Noperation.bl_idname, text=("Three Lamp Lighting"))

# メニューを構築する関数
def menu_fn(self, context):
    self.layout.separator()
    self.layout.menu(DuplicatingMenu.bl_idname)


# Blenderに登録するクラス
classes = [
    Noperation,
    TWO_lightsetting,
    THREE_lightsetting,
    DuplicatingMenu,
]


# アドオン有効化時の処理
def register():
    for c in classes:
        bpy.utils.register_class(c)
    bpy.types.VIEW3D_MT_object.append(menu_fn)

# アドオン無効化時の処理
def unregister():
    bpy.types.VIEW3D_MT_object.remove(menu_fn)
    for c in classes:
        bpy.utils.unregister_class(c)

if __name__ == "__main__":
    register()