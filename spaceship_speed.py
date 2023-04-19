def spaceship_speed(distance, time):
    speed = distance / time
    if speed > 300000:
        print("Космический корабль движется быстрее света!")
    else:
        return speed

print(spaceship_speed(1000000000, 10000)) # 100000.0
