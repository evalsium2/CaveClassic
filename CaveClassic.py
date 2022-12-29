from ursina import *
from ursina.prefabs. \
    first_person_controller \
    import FirstPersonController
import pygame

app = Ursina()
Sky(texture="sky1")
player = FirstPersonController()

boxes = []
for n in range(50):
    for k in range(50):
        box = Button(color=color.white,
                     model="cube",
                     position=(k, 0, n),
                     texture='texture/grass',
                     parent=scene,
                     origin_y=0.5
                     )

        boxes.append(box)


def input(key):
    for box in boxes:
        if box.hovered:
            if key == "left mouse down":
                new = Button(color=color.white,
                             model="cube",
                             position=
                             box.position + mouse.normal,
                             texture='texture/stone',
                             parent=scene,
                             origin_y=0.5)
                boxes.append(new)
            if key == "right mouse down":
                boxes.remove(box)
                destroy(box)


app.run()
