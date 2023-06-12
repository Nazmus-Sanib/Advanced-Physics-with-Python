# Calculate velocity if the energy and mass is known
def return_velocity(energy, mass):
  v_ = ((energy*2)/mass)**0.5
  return [[i, i*(-1)] for i in v_]
