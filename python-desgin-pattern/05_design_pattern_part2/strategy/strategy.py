from abc import ABCMeta, abstractmethod


class PaymentStrategy(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, amount: int) -> None:
        pass


class CreditCardPaymentStrategy(PaymentStrategy):
    def pay(self, amount: int) -> None:
        print(f"クレジットカードで{amount}円の支払い")


class CashPaymentStrategy(PaymentStrategy):
    def pay(self, amount: int) -> None:
        print(f"現金で{amount}円の支払い")


class ShoppingCart:
    def __init__(self) -> None:
        self.__total = 0
        self.__items: list[tuple[str, int]] = []

    def add_item(self, item: str, price: int) -> None:
        self.__total += price
        self.__items.append((item, price))

    def pay(self, payment_strategy: PaymentStrategy) -> None:
        payment_strategy.pay(self.__total)


if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("item1", 500)
    cart.add_item("item2", 1000)

    payment_strategy1 = CreditCardPaymentStrategy()
    cart.pay(payment_strategy1)

    payment_strategy2 = CashPaymentStrategy()
    cart.pay(payment_strategy2)
