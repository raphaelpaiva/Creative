import os
import time
import numpy
import random

from PIL import Image, ImageDraw

WIDTH=500
HEIGHT=500
STEPS=100000

def walk():
  x = numpy.zeros((WIDTH), dtype=int)

  random.seed()

  start_pos = random.randint(0, WIDTH - 1)

  current_pos = start_pos
  for i in range(STEPS):
    x[current_pos] = x[current_pos] + 1
    
    direction = random.choice([1, -1])
    current_pos = current_pos + direction
    if current_pos > WIDTH - 1:
      current_pos = WIDTH - 1
    else:
      if current_pos < 0:
        current_pos = 0
  
  return x

def draw(walk):
  img = Image.new('RGB', (WIDTH, HEIGHT))
  draw = ImageDraw.Draw(img)

  for i in range( len(walk) ):
    draw.point((i, HEIGHT / 2 + walk[i]), (255, 255, 255))
  
  return img
  
def save(img):
  filename = os.path.basename(__file__)
  timestamp = int(round(time.time() * 1000))

  img.save(f"{filename}-{timestamp}.png")

def main():
  x = walk()
  
  img = draw(x)
  img.show()
  save(img)

if __name__ == "__main__":
  main()