def calculator(sqrt,floor):
    ''' function calculator takes 2 parameters
        and returns sqrt and floor and takes into account
        certain parameter limitations'''
    if sqrt or floor >0:
      import math
      try:
          solution=(round(math.sqrt(sqrt),2),math.floor(floor))
          return "The squared root of {} returns {} and floor of {}  returns {}".format(sqrt,solution[0],floor,solution[1])
      except:
           return "Must be a positive real number"
    else:
          return "Gotta be greater than 0"

print(calculator(900,9.2)
