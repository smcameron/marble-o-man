#       Copyright (C) 2014 Stephen M. Cameron
#       Author: Stephen M. Cameron
#
#       This file is part of marble-o-man.
#
#       marble-o-man is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#
#       marble-o-man is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with marble-o-man; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#

# This program is based on the ideas of Aubrey Jaffer
# found here: http://people.csail.mit.edu/jaffer/Marbling/Mathematics
#

from PIL import Image, ImageDraw
import math

xdim = 800
ydim = 400
z = 60.0
u = 0.95

# Create a new blank image
ia = Image.new("RGB", (xdim, ydim))

draw = ImageDraw.Draw(ia)

def clear_image(im):
    for x in range(0, xdim):
        for y in range(0, ydim):
            im.putpixel((x, y), (255, 255, 255))

def paintpixel(im, coord, color):
    x, y = coord
    r, g, b = color
    if 0 <= x < xdim and 0 <= y < ydim:
        im.putpixel((x, y), (r, g, b))

def checkerboard(im):
    for x in range(0, xdim):
        for y in range(0, ydim):
            if ((x // 10 + y // 10) % 2) == 0:
                im.putpixel((x, y), (255, 255, 255))
            else:
                im.putpixel((x, y), (0, 0, 0))

def vertical_stroke(x, y, xl):
    return (int(x), int(y + z * math.pow(u, abs(x - xl))))

def horizontal_stroke(x, y, yl):
    return (int(x + z * math.pow(u, abs(y - yl))), int(y))

def clamped_getpixel(i, coord):
    x, y = coord
    x = max(0, min(x, xdim - 1))
    y = max(0, min(y, ydim - 1))
    return i.getpixel((x, y))

def marble(im, f, xl):
    i = Image.new("RGB", (xdim, ydim))
    for x in range(0, xdim):
        for y in range(0, ydim):
            paintpixel(i, (x, y), clamped_getpixel(im, f(x, y, xl)))
    return i

# Create the checkerboard pattern
checkerboard(ia)

# Apply marble effect
ib = marble(ia, vertical_stroke, xdim // 2)
ic = marble(ib, vertical_stroke, xdim // 4)
ib = marble(ic, vertical_stroke, 3 * xdim // 4)
ic = marble(ib, horizontal_stroke, ydim // 4)
ib = marble(ic, horizontal_stroke, ydim // 2)
ic = marble(ib, horizontal_stroke, 3 * ydim // 4)

# Save the resulting image
ic.save("output.png")
