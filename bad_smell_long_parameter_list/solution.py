class Unit:

    # ...
    def __init__(self):
        self.x = 0
        self.y = 0
        self.field = field
        self.state = None
        self.speed = 1

        self._get_speed()

    def move(self, direction):

        if direction == 'UP':
            self.field.set_unit(y=self.y + self.speed, x=self.x, unit=self)
        elif direction == 'DOWN':
            self.field.set_unit(y=self.y - self.speed, x=self.x, unit=self)
        elif direction == 'LEFT':
            self.field.set_unit(y=self.y, x=self.x - self.speed, unit=self)
        elif direction == 'RIGTH':
            self.field.set_unit(y=self.y, x=self.x + self.speed, unit=self)

    def _get_speed(self):
        if self.state == 'fly':
            self.speed *= 1.2
        elif self.state == 'crawl':
            self.speed *= 0.5
        else:
            raise ValueError('Эк тебя раскорячило')
