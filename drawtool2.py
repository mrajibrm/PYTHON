from drawtool import DrawTool
import numpy as np
dt = DrawTool()
dt.set_XY_range(0,10, 0,10)
dt.set_aspect('equal')
pixels = dt.read_imagefile('CHEGG.png')
num_rows = pixels.shape[0]
num_cols = pixels.shape[1]

for i in range(num_rows):
    for j in range(num_cols):
        if((pixels[i,j,1] > pixels[i,j,0]) and (pixels[i,j,2] < 0.5 *pixels[i,j,1])):
            pixels[i,j,0] = 0
            pixels[i,j,1] = 0
            pixels[i,j,2] = 255

dt.set_axes_off()
dt.draw_image(pixels)
dt.display()