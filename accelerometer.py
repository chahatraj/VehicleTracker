import adxl345
def accelerometer():
  accel = adxl345.ADXL345()
  axes = accel.getAxes(True)
  x = axes['x']
  y = axes['y']
  z = axes['z']
  print x
  print y
  print z
  return x,y,z
