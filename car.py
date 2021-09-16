import CarClass as cc
#initalizes the object
racecar = cc.car("2020","Honda")

#accelerates and outputs the current speed
for x in range(5):
    racecar.accelerate()
    print(racecar.get_speed())
    
#brakes and outputs the current speed
for x in range(5):
    racecar.brake()
    print(racecar.get_speed())
