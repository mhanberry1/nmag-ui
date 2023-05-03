import tkinter as tk
import tksvg
from pprint import pprint

def on_click(event):
    x, y = event.x, event.y
    image = event.widget.image

    if image.transparency_get(x, y) == False:
        print('clicked')

def on_hover(event):
    x, y = event.x, event.y
    widget = event.widget
    image = event.widget.image
    width, height = image.width(), image.height()

    if not 0 <= x < width or not 0 <= y < height: return

    if image.transparency_get(x, y) == False and widget.hovering == False:
        widget.hovering = True
        print('hovered')

    elif image.transparency_get(x, y) == True and widget.hovering == True:
        widget.hovering = False
        print('hover ended')

window = tk.Tk()
svg_image = tksvg.SvgImage(file='orb.svg')
label = tk.Label(image=svg_image)
label.hovering = False
label.image = svg_image
label.bind('<Button-1>', on_click)
label.bind('<Motion>', on_hover)
label.pack()
window.mainloop()
