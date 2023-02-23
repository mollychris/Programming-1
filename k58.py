from stanfordkarel import *


class ktools:
  def m(self):
    """Shorthand for move"""
    move()
  
  def tl(self):
    """Turn Left"""
    turn_left()

  def tr(self):
    """Turn Right"""
    self.tl()
    self.tl()
    self.tl()

  def ta(self):
    """Turn Around"""
    self.tl()
    self.tl()
    
  def pick(self):
    """Pick Beeper"""
    pick_beeper()

  def put(self):
    """Put Beeper"""
    put_beeper()

  def put2(self):
    """Put 2 beepers in a line"""
    self.put()
    self.m()
    self.put()

  def put5(self):
    """Put 5 beepers in a line"""
    self.put2()
    self.m()
    self.put2()
    self.m()
    self.put()

  def h(self):
    """Print H using beepers"""
    self.tl()
    self.put5()
    self.tr()
    self.m()
    self.m()
    self.m()
    self.tr()
    self.put5()
    self.ta()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.put2()
    self.tl()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.m()
    self.m()
    self.m()

  def e(self):
    pass

  def l(self):
    pass

  def o(self):
    pass

  def fic(self) -> bool:
    """Front is Clear"""
    return front_is_clear()

  def fib(self):
    """Front is Blocked"""
    return not self.fic()
  
  def ric(self):
    """Right is Clear"""
    self.tr()
    if self.fic():
      self.tl()
      return True  # Immediately exit the function
    self.tl()
    return False

  def rib(self):
    """Right is Blocked"""
    return not self.ric()

  def mazemove(self):
    """Maze Move"""
    if self.fib():
      self.tl()
    else:  # Otherwise...
      self.m()
      if self.ric():
        self.tr()
        self.m()
        if self.ric():
          self.tr()
          self.m()
    pass

def main():
    """Karel code goes here!"""
    kt = ktools()
    kt.m()
    kt.m()
    kt.m()
    kt.tl()
    kt.m()
    kt.m()
    kt.put2()
    kt.m()
    kt.put()
    kt.tl()
    kt.m()
    kt.tr()
    kt.m()
    kt.tr()
    kt.m()
    kt.tl()
    kt.put2()
    kt.m()
    kt.put()
    kt.m()
    kt.tr()
    kt.m()
    kt.tr()
    kt.m()
    kt.put2()
    kt.m()
    kt.tl()
    kt.put5()
    kt.m()
    kt.tr()
    kt.m()
    kt.tr()
    kt.m()
    kt.put5()
    kt.tl()
    kt.m()
    kt.put2()
    
    
    
    
    pass
def mm(self, num):
  """Move Multiple"""
  for number in range(num):
    self.m()
def pickm(self, num):
  """Pick multiple"""
  for number in range(num-1):
    self.pick()
    self.m()
  self.pick()
def putm(self, num):
  """put multiple"""
  for _ in range(num-1):
    self.put()
    self.m()
  self.put()
def sob(self):
  return beepers_present()

  
def jump(self):
  while self.fic():
    self.m()
  self.tl()
  while self.rib():
    self.m()
  self.tr()
  self.m()
  self.tr()

  def find(self):
    while not facing_north():
      self.tl()
    self.m()
    if not self.sob():
      self.tl()
      self.m()
      self.tl()
      self.m()
    for _ in range(2):
      if not self.sob():
        self.m()
        self.tl()
        self.m()
      pass
    
  
if __name__ == "__main__":
    run_karel_program()