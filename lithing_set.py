bl_info = {
    "name": "LLightingset",
    "author": "headphones",
    "version": (0, 1, 0),
    "blender": (3, 10, 0),
    "location": "Editmode > F",
    "warning": "",
    "description": "Extends the 'Make Edge/Face' functionality",
    "doc_url": "{BLENDER_MANUAL_URL}/addons/mesh/f2.html",
    "category": "Mesh",
}

# ref: https://github.com/Cfyzzz/Other-scripts/blob/master/f2.py

import bmesh
import bpy
import itertools
import mathutils
import math
from mathutils import Vector
from bpy_extras import view3d_utils

# registration
classes = [] # classes = [MeshF2, F2AddonPreferences]
addon_keymaps = []


def register():
    # add operator
    for c in classes:
        bpy.utils.register_class(c)

    # add keymap entry
    kcfg = bpy.context.window_manager.keyconfigs.addon
    if kcfg:
        km = kcfg.keymaps.new(name='Mesh', space_type='EMPTY')
        kmi = km.keymap_items.new("mesh.f2", 'F', 'PRESS')
        addon_keymaps.append((km, kmi))


def unregister():
    # remove keymap entry
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

    # remove operator and preferences
    for c in reversed(classes):
        bpy.utils.unregister_class(c)


if __name__ == "__main__":
    register()