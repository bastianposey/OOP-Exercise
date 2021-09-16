class car:
# init car class
    def __init__(self, mod, make):
        self.__year_model = mod
        self.__year_make = make
        self.__speed = 0

# method that increases speed by 5
    def accelerate(self):
        self.__speed += 5

# method that decreases speed by 5
    def brake(self):
        if self.__speed >=0:
            self.__speed -=5
            
# method that outputs seed
    def get_speed(self):
        return self.__speed