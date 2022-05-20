"""
Rocket stats:
 * Mass -- update function
 * rotation
 * location
 * thrusty thrust
 * rotational thrust
"""

class Quaternion:
  def __init__(self, s, v1, v2, v3):
    self.s , self.v1, self.v2 ,self.v3 = s, v1, v2, v3
    self.m = ( self.s**2 + self.v1**2 + self.v2**2 + self.v3**2 )**0.5

  def to_rot_mat(self):
    pass

  def to_euler(self):
    pass

class Engine:
  def __init__(self, max_thrust):
    self.thrust = get_thrust(0)

    # internals
		self.pt=
		self.Tt=
		self.po=
		self.gamma=
		self.R=
		self.At=
		self.pe=
		self.ve=
		self.Te=
		self.Ae=
		self.mdot=
    
    # externals
    self.max_thrust = max_thrust
    self.direction = Quanternion(0, 0, 0, 0)

  def get_thrust(fuel):
    pass

  def get_mass_flow_rate():
    

class FirstStage:
  def __init__(self):
    self.eng = [24 * Engine( )]
    self.stage_mass = 1
class Rocket:
  def __init__(self):
    self.eng = [24 * Engine()]
    