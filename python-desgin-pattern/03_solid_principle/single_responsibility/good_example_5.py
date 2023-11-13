class EmployeeData:
    def __init__(self, name: str, department: str) -> None:
        self.name = name
        self.department = department


class PayCalculator:
    def __get_regular_hours(self) -> None:
        print("給与計算専用の労働時間計算ロジック")

    def calculate_pay(self, employee_data: EmployeeData) -> None:
        self.__get_regular_hours()
        print(f"{employee_data.name}の給与を計算しました")


class HourReporter:
    def __get_regular_hours(self) -> None:
        print("労働時間レポート専用の労働時間計算ロジック_V2")

    def report_hours(self, empolyee_data: EmployeeData) -> None:
        self.__get_regular_hours()
        print(f"{empolyee_data.name}の労働時間をレポートしました")


class EmployeeRepositry:
    def save(self) -> None:
        pass


if __name__ == "__main__":
    empolyee_data = EmployeeData("Suzuki", "develop")
    payCalculator = PayCalculator()
    hourReporter = HourReporter()

    print("経理部門")
    payCalculator.calculate_pay(empolyee_data)

    print("")
    print("人事部門")
    hourReporter.report_hours(empolyee_data)
