class Character :
    def __init__(self,name,weapon):
        self.name = name
        self.weapon = weapon

    def intro(self):
        print("Name: ", self.name)
        print("Weapon: ", self.weapon)
        
lugo = Character("Lugo","gun")
lugo.intro()
