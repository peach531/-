class Car :
    def __init__(self,model, color):
        self.model = model
        self.color = color

    def info(self):
        print("Model :" ,self.model, ",color : ", self.color)

bmw = Car("BMW", "white")
benz = Car("Benz", "black")
bmw.info()
benz.info()
