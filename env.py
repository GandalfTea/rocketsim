
import math
# Create a simulating environment for the rocket

# Physics:
# * gravity - constant
# * air density variable to height - gradient

# G =6e-11

class Environment:
  def __init__( self, launch_theta, launch_phi ):
    self.ACC_GRAVITY = 9.80665   # m s-2
    self.PLANET_MASS = 5.972e24  # kg
    self.PLANET_RADIUS = 6371000 # m
    self.G = 6.67430e-11         # N m^2 kg-2
    self.LAUNCH = [self.PLANET_RADIUS*math.sin(launch_theta)*math.cos(launch_phi),
                   self.PLANET_RADIUS*math.sin(launch_theta)*math.sin(launch_phi),
                   self.PLANET_RADIUS*math.cos(launch_theta)] # [x,y,z] m

    # air density equation
    self.molar_mass_air = 0.0289644    # kg mol-1
    self.gas_constant = 8.31432        # N m mol-1 k-1
    self.std_temp_lapse_rate = -0.0065 # K m-1
    self.temp_sea_level = 288.15       # K
    self.sea_level_pressure=101325     # Pa
    self.pressure_expo=-self.ACC_GRAVITY*self.molar_mass_air / (self.gas_constant*self.std_temp_lapse_rate)

  # https://www.mide.com/air-pressure-at-altitude-calculator
  def get_air_density( self, height ):
    pressure = self.sea_level_pressure*(1+(self.std_temp_lapse_rate/self.temp_sea_level)*height)**(self.pressure_expo)
    temp = self.get_temp(height)
    if isinstance(pressure, complex): pressure = 0
    if temp < 0 : temp = 0
    return 0 if temp == 0 else pressure / (self.gas_constant*temp) # returning density

  def get_temp( self, height ):
    return self.std_temp_lapse_rate * height + self.temp_sea_level

  def get_force_grav(self, height, rocket_mass):
    return self.G * ( self.PLANET_MASS * rocket_mass) / (self.PLANET_RADIUS+height)**2
    
#def air_resistance( rotation, position, velocity ):

env = Environment()
for i in range(250000000, 300000000, 100000):
  print( env.get_force_grav( 10))
	
# Rocket
# * air resistance - crossectionial area perpendicular to trajectory + velocity -> decceleration due to airRes


