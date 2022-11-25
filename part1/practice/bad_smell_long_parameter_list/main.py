# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)

from dataclasses import dataclass
 
@dataclass(slots=False)
class UnitDestination:
    field: dict
    x: float
    y: float
    direction: str
    # fly is not crawl
    is_fly: bool
    speed: float = 1

class Unit:
    
    def move(self, destination: UnitDestination):
        new_speed = destination.speed * 1.2 if destination.is_fly else destination.speed * 0.5
        destination.speed = new_speed
        direction_sign = 1 if destination.direction in ['UP', 'RIGHT'] else -1
        
        if destination.direction in ['UP', 'DOWN']:
            new_x = destination.x
            new_y = destination.y + direction_sign * destination.speed
        elif destination.direction in ['LEFT', 'RIGHT']:
            new_y = destination.y
            new_y = destination.y + direction_sign * destination.speed
 
        destination.field.set_unit(x=new_x, y=new_y, unit=self)