from abc import ABCMeta, abstractmethod


class Vehicle(metaclass=ABCMeta):
    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color

    @abstractmethod
    def start(self) -> None:
        pass

    @abstractmethod
    def stop(self) -> None:
        pass

    @abstractmethod
    def fly(self) -> None:
        pass


class Airplane(Vehicle):
    def __init__(self, name: str, color: str):
        super().__init__(name, color)

    def start(self) -> None:
        print("start!")

    def stop(self) -> None:
        print("stop!")

    def fly(self) -> None:
        print("fly!")


class Car(Vehicle):
    def __init__(self, name: str, color: str):
        super().__init__(name, color)

    def start(self) -> None:
        print("start!")

    def stop(self) -> None:
        print("stop!")

    def fly(self) -> None:
        raise Exception("Car can't fly!")


if __name__ == "__main__":
    v1: Vehicle = Airplane("AirBus", "white")
    v2: Vehicle = Car("Prius", "black")

    v1.fly()
    v2.fly()
