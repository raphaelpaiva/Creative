import math
import operator
import random

def isprimitive(obj):
  return type(obj) in (int, float)

class Expression(object):
  def __init__(self, lhs, operand, rhs):
    self.lhs = lhs
    self.operand = operand
    self.rhs = rhs
    self.name = self.operand.__name__

  def eval(self):
    lhs = self.lhs  if isprimitive(self.lhs) else self.lhs.eval()
    rhs = self.rhs if isprimitive(self.rhs) else self.rhs.eval()
    
    return self.operand(lhs, rhs)
  
  def __str__(self):
    return f"({self.lhs} {self.name} {self.rhs})"

class Multiply(Expression):
  def __init__(self, a, b):
    super(Multiply, self).__init__(
      a, operator.mul, b
    )

    self.name = '*'

class Add(Expression):
  def __init__(self, a, b):
    super(Add, self).__init__(
      a, operator.add, b
    )

    self.name = '+'

class Sub(Expression):
  def __init__(self, a, b):
    super(Sub, self).__init__(
      a, operator.sub, b
    )

    self.name = '-'

class Div(Expression):
  def __init__(self, a, b):
    super(Div, self).__init__(
      a, operator.add, b
    )

    self.name = '/'

class Const(object):
  def __init__(self, val):
    self.val = val
  
  def eval(self):
    return self.val
  
  def __str__(self):
    return str(self.val)

class Var(object):
  def __init__(self, name, init_val=None):
    self.val = init_val
    self.name = name
  
  def __str__(self):
    return self.name
  
  def eval(self):
    return self.val
  
  def update(self, new_val):
    self.val = new_val


class Function(object):
  def __init__(self, func, arg):
    self.func = func
    self.arg = arg
    self.name = self.func.__name__
  
  def eval(self):
    arg_val = self.arg if isprimitive(self.arg) else self.arg.eval()
    return self.func(arg_val)
  
  def __str__(self):
    return f"{self.name}( {self.arg} )"
 
class Sin(Function):
  def __init__(self, arg):
    super(Sin, self).__init__(math.sin, arg)

class Cos(Function):
  def __init__(self, arg):
    super(Cos, self).__init__(math.cos, arg)

def random_expr(vars):
  ops = [
    Multiply,
    Div,
    Sin,
    Cos,
    Const
  ]

  op = random.choice(ops + vars)

  if isinstance(op, Var):
    return op
  
  if op is Const:
    return op(random.random() * random.randint(1, 100))

  if issubclass(op, Function):
    pi_factor = random.random() * 2 * math.pi
    arg = Multiply(pi_factor, random_expr(vars))

    return op(arg)
  
  if issubclass (op, Expression):
    return op(random_expr(vars), random_expr(vars))


if __name__ == "__main__":
  random.seed()

  var_x = Var('x', 2)
  var_y = Var('y', 1.45253)
  vars = [var_x, var_y]

  func = random_expr(vars)
  result = func.eval()

  print(f"{func} = {result}")
