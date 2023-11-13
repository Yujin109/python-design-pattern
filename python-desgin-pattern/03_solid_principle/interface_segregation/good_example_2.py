from abc import ABCMeta, abstractmethod


class Vehicle(metaclass=ABCMeta):
    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color


class Movable(metaclass=ABCMeta):
    @abstractmethod
    def start(self) -> None:
        pass

    @abstractmethod
    def stop(self) -> None:
        pass


class Flyable(metaclass=ABCMeta):
    @abstractmethod
    def fly(self) -> None:
        pass


class Airplane(Vehicle, Movable, Flyable):
    def __init__(self, name: str, color: str):
        super().__init__(name, color)

    def start(self) -> None:
        print("start!")

    def stop(self) -> None:
        print("stop!")

    def fly(self) -> None:
        print("fly!")


class Car(Vehicle, Movable):
    def __init__(self, name: str, color: str):
        super().__init__(name, color)

    def start(self) -> None:
        print("start!")

    def stop(self) -> None:
        print("stop!")


if __name__ == "__main__":
    v1 = Airplane("AirBus", "white")
    v2 = Car("Prius", "black")

    v1.fly()
    v2.start()
