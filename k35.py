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
    self.tl()
  def ta(self):
    """turn around"""
    self.tl()
    self.tl()
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
    self.m()
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
    self.tl()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.m()
    self.m()
    self.m()
  def e(self):
    self.tl()
    self.put5()
    self.tr()
    self.m()
    self.put2()
    self.ta()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.put2()
    self.ta()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.put2()
    self.m()
    self.m()
    
    pass
  def l(self):
    self.tl()
    self.put5()
    self.ta()
    self.m()
    self.m()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.put2()
    self.m()
    self.m()
    pass
  def o(self):
    self.tl()
    self.put5()
    self.tr()
    self.m()
    self.put2()
    self.m()
    self.tr()
    self.put5()
    self.tr()
    self.m()
    self.put2()
    self.ta()
    self.m()
    self.m()
    self.m()
    self.m()
    pass

def main():
    """Karel code goes here!"""
    kt=ktools()
    kt.h()
    kt.e()
    kt.l()
    kt.l()
    kt.o()
    pass

if __name__ == "__main__":
    run_karel_program()