from stanfordkarel import *

class ktools:
  def m(self):
    """short for move"""
    move()
  def tl(self):
    """turn left"""
    turn_left()
  def tr(self):
    """turn right"""
    self.tl()
    self.tl()
    slef.tl()
  def ta(self):
    """turn around"""
    self.tl()
    slef.tl()
  def pick(self):
    """pick beeper"""
    pick_beeper()
  def put(self):
    """put beeper"""
    put_beeper()
  def put2(self):
    """put 2"""
    self.put()
    self.m()
    self.put()
  def put5(self):
    self.put2()
    self.m()
    self.put2()
    slef.m()
    self.put()
  def h(self):
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
    slef.tl()
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

def main():
    """Karel code goes here!"""
    kt=ktools()
    pass

if __name__ == "__main__":
    run_karel_program()