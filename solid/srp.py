# 単一責任の原則(SRP: Single Responsibility Principle)

class EmployeeData:
    def __init__(self, name: str, department: str):
        self.name = name
        self.department = department


class PayCalculator:
    def __get_regular_hours(self):
        print("給与計算用の労働時間計算ロジック")
    
    def calculate_pay(self, employee_data: EmployeeData):
        self.__get_regular_hours()
        print(f"{employee_data.name}の給与を計算しました")


class HourReporter:
    def __get_regular_hours(self):
        print("労働時間レポート用の労働時間計算ロジック")
    
    def report_hours(self, employee_data: EmployeeData):
        self.__get_regular_hours()
        print(f"{employee_data.name}の労働時間をレポートしました")


class EmployeeRepository:
    def save(self):
        pass


if __name__ == "__main__":
    employee_data = EmployeeData("鈴木", "開発部")
    pay_calculator = PayCalculator()
    hour_reporter = HourReporter()
    
    print("経理部門")
    pay_calculator.calculate_pay(employee_data)
    
    print("")
    print("人事部門")
    hour_reporter.report_hours(employee_data)
