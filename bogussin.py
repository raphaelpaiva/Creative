import os
import math
import time
import random
import inspect

from PIL import Image, ImageDraw

WIDTH =  1000
HEIGHT = 1000

random.seed()

def choose_func():
  return random.choice([
    lambda p,x,y: math.sin(p * math.pi * x ),
    lambda p,x,y: math.sin(p * math.pi * y ),
    lambda p,x,y: math.sin(p * math.pi * x * y ),
    lambda p,x,y: math.cos(p * math.pi * x ),
    lambda p,x,y: math.cos(p * math.pi * y ),
    lambda p,x,y: math.cos(p * math.pi * x * y ),
  ])

def generate_image():
  PI_FACTOR = random.random() * 10
  
  rfunc = choose_func()
  gfunc = choose_func()
  bfunc = choose_func()

  print(
    inspect.getsource(rfunc).strip(),
    inspect.getsource(gfunc).strip(),
    inspect.getsource(bfunc).strip(),
    sep='\n'
  )

  print(PI_FACTOR)

  return draw(PI_FACTOR, rfunc, gfunc, bfunc)

def draw(pi_factor, rfunc, gfunc, bfunc):
  img = Image.new('RGB', (WIDTH, HEIGHT))
  draw = ImageDraw.Draw(img)
  
  for x in range(0, WIDTH):
    for y in range(0, HEIGHT):
      r = int (127 + 127 * rfunc(pi_factor, x, y) )
      g = int (127 + 127 * gfunc(pi_factor, x, y) )
      b = int (127 + 127 * bfunc(pi_factor, x, y) )

      draw.point((x, y), (r, g, b))
  
  return img

def save(img):
  filename = os.path.basename(__file__)
  timestamp = int(round(time.time() * 1000))
  
  img.save(f"{filename}-{timestamp}.png")

if __name__ == "__main__":
    for i in range(2):
      img = generate_image()
      save(img)