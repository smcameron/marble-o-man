#!/usr/bin/python
#
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

import sys
import Image
import ImageDraw
import math
import random

xdim = 800;
ydim = 400;
z = 60.0;
u = 0.95;

ia = Image.new("RGB", (xdim, ydim));

draw = ImageDraw.Draw(ia);

def clear_image(im):
   for x in range(0, int(xdim)):
      for y in range(0, int(ydim)):
         im.putpixel((x, y), (255, 255, 255));

def paintpixel(im, (x, y), (r, g, b)):
   if (x >= 0 and x < xdim and y >= 0 and y < ydim):
      im.putpixel((x, y), (r, g, b));

def checkerboard(im):
   for x in range(0, int(xdim)):
      for y in range(0, int(ydim)):
         if (((int(x / 10) + int(y / 10)) % 2) == 0):
	    im.putpixel((x, y), (255, 255, 255));
         else:
	    im.putpixel((x, y), (0, 0, 0));

def vertical_stroke(x, y, xl):
    return (int(x), int(y + z * math.pow(u, math.fabs(x - xl))));

def horizontal_stroke(x, y, yl):
    return (int(x + z * math.pow(u, math.fabs(y - yl))), int(y));

def clamped_getpixel(i, coord):
   x = coord[0];
   y = coord[1];
   if (x < 0):
      x = 0;
   if (x >= xdim):
      x = xdim - 1;
   if (y < 0):
      y = 0;
   if (y >= ydim):
      y = ydim - 1;
   return i.getpixel((x, y));

def marble(im, f, xl):
   i = Image.new("RGB", (xdim, ydim));
   for x in range(0, xdim):
      for y in range(0, ydim):
         paintpixel(i, (x, y), clamped_getpixel(im, f(x, y, xl))); 
   return i;

checkerboard(ia);
ib = marble(ia, vertical_stroke, xdim / 2);
ic = marble(ib, vertical_stroke, xdim / 4);
ib = marble(ic, vertical_stroke, 3 * xdim / 4);
ic = marble(ib, horizontal_stroke, ydim / 4);
ib = marble(ic, horizontal_stroke, ydim / 2);
ic = marble(ib, horizontal_stroke, 3 * ydim / 4);
ic.save("output.png");

