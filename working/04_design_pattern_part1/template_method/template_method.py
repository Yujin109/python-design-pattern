from abc import ABCMeta, abstractmethod


class TestTemplate(metaclass=ABCMeta):
    def test(self) -> None:
        self.setup()
        self.execute()
        self.teardown()

    @abstractmethod
    def setup(self) -> None:
        pass

    @abstractmethod
    def execute(self) -> None:
        pass

    def teardown(self) -> None:
        print("teardown")


class ItemServiceTest(TestTemplate):
    def setup(self) -> None:
        print("setup: ItemServiceTest")

    def execute(self) -> None:
        print("execute: ItemServiceTest")


class UserServiceTest(TestTemplate):
    def setup(self) -> None:
        print("setup: UserServiceTest")

    def execute(self) -> None:
        print("execute: UserServiceTest")


if __name__ == "__main__":
    itemServiceTest = ItemServiceTest()
    userServiceTest = UserServiceTest()

    itemServiceTest.test()
    print("")
    userServiceTest.test()
