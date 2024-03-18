
# Car 클래스를 선언해서
# carCount 클래스 변수
# carNo 에는 carCount 숫자를 이용해서 carNo를 넣으시오.
# carNo, color="white", door=5, tire=4, speed
# up_speed 함수를 호출하면 10씩 증가
# down_speed 함수를 호출하면 -10씩 감소
# c1 - 1,white,5,4,0 -> speed 30이 되도록
# c2 - 2,red,5,4,0 -> speed 100
# c3 - 3, silver,5,4,0 -> speed 79
# car_list 추가하고

class Car:
    carCount = 0
    car_list =[]

    def __init__(self, color="white", door=5, tire=4, speed=0):
        Car.carCount += 1
        self.carNo = Car.carCount
        self.color = color
        self.door = door
        self.tire = tire
        self.speed = speed
        Car.car_list.append(self)

    def up_speed(self):
        self.speed += 10

    def down_speed(self):
        self.speed -= 10
   
   
c1 = Car()
c2 = Car("red",5,4,0)
c3 = Car("silver",5,4,-1)

c1.up_speed()
c1.up_speed()
c1.up_speed()

c2.up_speed()
c2.up_speed()
c2.up_speed()
c2.up_speed()
c2.up_speed()
c2.up_speed()
c2.up_speed()
c2.up_speed()
c2.up_speed()
c2.up_speed()

c3.up_speed()
c3.up_speed()
c3.up_speed()
c3.up_speed()
c3.up_speed()
c3.up_speed()
c3.up_speed()
c3.up_speed()

for car in Car.car_list:
    print(f"Car {car.carNo}: Color - {car.color}, Door - {car.door}, Tire - {car.tire}, Speed - {car.speed}")

    
