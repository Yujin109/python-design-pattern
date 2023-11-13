from abc import ABCMeta, abstractmethod


class Button(metaclass=ABCMeta):
    @abstractmethod
    def press(self) -> None:
        pass


class Checkbox(metaclass=ABCMeta):
    @abstractmethod
    def switch(self) -> None:
        pass


class GUIFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


class WindowsButton(Button):
    def press(self) -> None:
        print("Windowsのボタンが押されました")


class WindowsCheckbox(Checkbox):
    def switch(self) -> None:
        print("Windowsのチェックボックスが切り替えられました")


class WindowsGUIFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()


class MacButton(Button):
    def press(self) -> None:
        print("Macのボタンが押されました")


class MacCheckbox(Checkbox):
    def switch(self) -> None:
        print("Macのチェックボックスが切り替えられました")


class MacGUIFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()


def run(factory: GUIFactory) -> None:
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    button.press()
    checkbox.switch()


if __name__ == "__main__":
    run(WindowsGUIFactory())
    run(MacGUIFactory())
