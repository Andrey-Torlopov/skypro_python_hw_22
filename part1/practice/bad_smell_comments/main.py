# В данном коде все прокомментировано как надо,
# но слишком избыточно.
# Избавьтесь от комментариев, изменив имена переменных, 
# чтобы было понятно, за что эти переменные отвечают 
# и что происходит и без комментариев


class Unit:
    def __init__(self, is_flying: bool):
        self._is_flying = is_flying
        
    
    def move(self, field, coordinate_x, coordinate_y, direction, velocity = 1):
        """
        Функция реализует перемещение юнита по полю. в качестве параметров принимает текущие координаты юнита, 
        направление его движения, состояние не летит ли он, состояние не крадется ли он и базовый параметр скорости с 
        которым двигается юнит
        """
        
        if self._is_flying:
            velocity *= 1.2 
            if direction == 'UP':
                new_y = coordinate_y + velocity   
                new_x = coordinate_x 
            elif direction == 'DOWN':
                new_y = coordinate_y - velocity
                new_x = coordinate_x
            elif direction == 'LEFT':
                new_y = coordinate_y 
                new_x = coordinate_x - velocity 
            elif direction == 'RIGHT':
                new_y = coordinate_y
                new_x = coordinate_x + velocity
        else:
            velocity *= 0.5
            if direction == 'UP':
                new_y = coordinate_y + velocity
                new_x = coordinate_x 
            elif direction == 'DOWN':
                new_y = coordinate_y - velocity
                new_x = coordinate_x 
            elif direction == 'LEFT':
                new_y = coordinate_y 
                new_x = coordinate_x - velocity
            elif direction == 'RIGHT': 
                new_y = coordinate_y 
                new_x = coordinate_x + velocity
                
            field.set_unit(x=new_x, y=new_y, unit=self)
