from __future__ import annotations

from abc import ABCMeta, abstractmethod


class LightState(metaclass=ABCMeta):
    @abstractmethod
    def switch(self) -> LightState:
        pass


class OffState(LightState):
    def switch(self) -> LightState:
        print("ライトを点灯します")
        return OnState()


class OnState(LightState):
    def switch(self) -> LightState:
        print("ライトを消灯します")
        return OffState()


class LightSwitch:
    def __init__(self) -> None:
        self.__state: LightState = OffState()

    def switch(self) -> None:
        self.__state = self.__state.switch()


if __name__ == "__main__":
    light_switch = LightSwitch()
    light_switch.switch()
    light_switch.switch()
    light_switch.switch()
