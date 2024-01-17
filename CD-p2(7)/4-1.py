class Character :
    def __init__(self,name,weapon):
        self.name = name
        self.weapon = weapon

    def intro(self):
        print("Name: ", self.name)
        print("Weapon: ", self.weapon)

class Action(Character) :
    step = 0

    def move_forward(self,n):
        self.step += n
        print("Current location is %d." % self.step)
    def move_backward(self,n):
        self.step -= n
        print("Current location is %d." % self.step)

    def turn_right(self):
        print("Turn_Right")

    def turn_left(self):
        print("Turn_left")

lugo = Action("Lugo","gun")
lugo.intro()
lugo.move_forward(10)
lugo.move_backward(3)
lugo.turn_right()
lugo.turn_left()
