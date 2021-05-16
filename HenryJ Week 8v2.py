class Vehicle: 
    #Vehicle is the parent
  def __init__(self,make,model,color,fueltype,options):
    self.make = make
    self.model = model
    self.color = color
    self.fueltype = fueltype
    self.options = options

  def getmake(self):
    return self.make

  def getmodel(self):
    return self.model

  def getcolor(self):
    return self.color

  def getfueltype(self):
    return self.fueltype

  def getoptions(self):
    return self.options

class Car(Vehicle): 
      #First child class
  def __init__(self, enginesize, numdoors, make, model, color, fueltype, options):

    super().__init__(make, model, color, fueltype, options)
    self.enginesize = enginesize
    self.numdoors = numdoors

  def getenginesize():
    return self.enginesize

  def getnumdoors():
    return self.numdoors

class Pickup(Vehicle): 
      #Second child class
  def __init__(self, cabstyle, bedlength, make, model, color, fueltype, options):

    super().__init__(make, model, color, fueltype, options)
    self.cabstyle = cabstyle
    self.bedlength = bedlength

  def getcabstyle(self):
    return self.cabstyle

  def getbedlength(self):
    return self.bedlength

c=Car("5.0 L 8-cylinder",4,"Ford","Mustang GT Premium","red","gas",['power mirrors', 'power locks', 'remote start','backup camera','bluetooth','cruise control'])
#car options

p=Pickup("Regular cab",4,"Dodge","x","black","diesel",['cd player','heated seats', 'leather seats', 'invisible mirror'])
#pickup options

i=1
#tutor support - need to use to provide the user with options and solve the problem
while i==1:
  #i==1 supports options 1-3
    print("Select from the following options for your virtual garage:")
    print("1.Add Car\n2.Add Pickup\n3.Retrieve Specifications\n4.Exit")
    choice = int(input("Enter your choice:"))
    if choice == 1:
      enginesize = input("engine size:")
      numdoors = int(input("number of doors:"))
      make = input("make:")
      model=input("model:")
      color = input("color:")
      fueltype = input("fuel type:")
      option= input("Enter options:")
    
    elif choice==2:
      cabstyle = input("cab style:")
      bedlength = int(input("bed length:"))
      make = input("make:")
      model = input("model:")
      color = input("color:")
      fueltype = input("fuel type:")
      option= input("Enter options:")
      
    elif choice == 3:
      input("Are you satisfied with your options?")
      input("Should I return the vehicle to the virtual garage?")

    elif choice == 4:
        i=0
        #ends loop(?)

    else:
      print("Please enter a valid selection.\n")