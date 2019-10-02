import os
import math
import time
import random
import inspect

from PIL import Image, ImageDraw
from Function import Multiply, Sin, Cos, random_expr, Var

WIDTH =  1000
HEIGHT = 1000

random.seed()

def generate_image(vars=[]):
  
  rfunc = random_expr(vars, 0.5)
  gfunc = random_expr(vars, 0.5)
  bfunc = random_expr(vars, 0.5)

  print(
    rfunc,
    gfunc,
    bfunc,
    sep='\n'
  )

  return draw(rfunc, gfunc, bfunc, vars)

def draw(rfunc, gfunc, bfunc, vars):
  img = Image.new('RGB', (WIDTH, HEIGHT))
  draw = ImageDraw.Draw(img)

  var_x, var_y = vars
  
  for x in range(0, WIDTH):
    var_x.update(x)
    print(".", end='')
    for y in range(0, HEIGHT):
      var_y.update(y)
      
      r = int (127 + 127 * rfunc.eval() )
      g = int (127 + 127 * gfunc.eval() )
      b = int (127 + 127 * bfunc.eval() )

      draw.point((x, y), (r, g, b))
  
  return img

def save(img):
  filename = os.path.basename(__file__)
  timestamp = int(round(time.time() * 1000))
  
  img.save(f"{filename}-{timestamp}.png")

if __name__ == "__main__":
  vars = [Var('x', 0), Var('y', 0)]
  for i in range(30):
    img = generate_image(vars)
    save(img)