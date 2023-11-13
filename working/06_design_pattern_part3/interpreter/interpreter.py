import datetime
import re
from abc import ABCMeta, abstractmethod
from typing import Union


class Context:
    def __init__(self, expression: str, date: datetime.date):
        self.validate(expression)
        self.expression = expression
        self.date = date

    def validate(self, expression: str) -> None:
        is_mathch_re = bool(re.match("(?=.*YYYY)(?=.*MM)(?=.*DD)", expression))
        if len(expression) != 10 or not is_mathch_re:
            raise Exception("expressionが不正です")


class AbstractExpression(metaclass=ABCMeta):
    @abstractmethod
    def interpret(self, context: Context) -> Context:
        pass


class YearExpression(AbstractExpression):
    def __init__(self) -> None:
        self.__child: Union[None, AbstractExpression] = None

    def set_child(self, child: AbstractExpression) -> None:
        self.__child = child

    def interpret(self, context: Context) -> Context:
        expression = context.expression
        year = context.date.year
        context.expression = expression.replace("YYYY", str(year))

        if self.__child:
            self.__child.interpret(context)

        return context


class MonthExpression(AbstractExpression):
    def __init__(self) -> None:
        self.__child: Union[None, AbstractExpression] = None

    def set_child(self, child: AbstractExpression) -> None:
        self.__child = child

    def interpret(self, context: Context) -> Context:
        expression = context.expression
        month = context.date.month
        context.expression = expression.replace("MM", str(month).zfill(2))

        if self.__child:
            self.__child.interpret(context)

        return context


class DayExpression(AbstractExpression):
    def __init__(self) -> None:
        self.__child: Union[None, AbstractExpression] = None

    def set_child(self, child: AbstractExpression) -> None:
        self.__child = child

    def interpret(self, context: Context) -> Context:
        expression = context.expression
        day = context.date.day
        context.expression = expression.replace("DD", str(day).zfill(2))

        if self.__child:
            self.__child.interpret(context)

        return context


if __name__ == "__main__":
    now_date = datetime.datetime.now().date()
    expression = "MM/DD/YYYY"

    context = Context(expression, now_date)

    year_expression = YearExpression()
    month_expression = MonthExpression()
    day_expression = DayExpression()
    month_expression.set_child(day_expression)
    year_expression.set_child(month_expression)

    result = year_expression.interpret(context)

    print(now_date.strftime("%m/%d/%Y"))
    print(result.expression)
