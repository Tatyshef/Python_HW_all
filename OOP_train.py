# Объектно-ориентированное программирование
#пропишем параметры и что умеет делать
class car:
    color = 'red'
    form = 'sedan'
    engine = '3'
    speed = 100
#self по умолчанию - это ссылка на объект car
    def moove(self,speed):
        self.speed = speed

    def changecolor(self,color):
        self.color = color
#создадим  объекты, экземпляры
obj1 = car()
obj2 = car()
print('1color =', obj1.color)
print('form =', obj1.form)
print('engine =', obj1.engine)
print('speed =', obj1.speed)

print('----------------')
print('2color =', obj2.color)
print('form =', obj2.form)
print('engine =', obj2.engine)
print('speed =', obj2.speed)

#поизменяем их параметры
obj1.moove(50)
obj1.changecolor('pink')
print('obj1_change_speed=', obj1.speed)
print('obj1_change_color=', obj1.color)

obj2.moove(70)
print('obj2_change_speed=', obj2.speed)