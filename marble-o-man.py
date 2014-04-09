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

ia = Image.new("RGB", (xdim, ydim));
ib = Image.new("RGB", (xdim, ydim));

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

checkerboard(ia);
ia.save("output.png");

