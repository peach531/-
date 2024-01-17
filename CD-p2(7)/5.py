class TV:
    def __init__(self,ch,vol):
        self.channel = ch
        self.volume = vol
        self.power = True
    def on_off(self):
        if(self.power == True):
            self.power = False
            print("Turn off")
        else:
            self.power = True
            print("Trun on")
    def info(self):
        print("Power: ",self.power)
        print("Channel: ",self.channel)
        print("Volume: ",self.volume)
    def set_channel(self,n):
        if(self.power == True):
            self_channel = ch
        else :
            print("Power off")
            
    def set_volume(self,n):
        if(self.power == True):
            self_volume = vol
        else :
            print("Power off")

tv = TV("1","16")
tv.info()
tv.on_off()
tv.on_off()
