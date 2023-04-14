from abc import abstractmethod


class Unit:
    def move(self):
        pass


class MovieMixin:
    @abstractmethod
    def move(self):
        pass


class Warrior(Unit, MovieMixin):
    def attack(self):
        pass

    def defense(self):
        pass

    def move(self):
        pass


class Healer(MovieMixin):
    def defense(self):
        pass

    def move(self):
        pass

    def heal(self):
        pass


class Tree:
    def defense(self):
        pass

    def on_fire(self):
        pass


class Trap:
    def attack(self):
        pass


if __name__ == '__main__':
    unit = Warrior()
    healer = Healer()
    trap = Trap()