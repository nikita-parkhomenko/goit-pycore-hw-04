# total_salary(path) => (total: int, averageSalary: float)
from pathlib import Path


# Task 1
def total_salary(path: Path):
    if path.is_file():
        with open(path, encoding="utf-8") as file:
            rows_list = [row.strip().split(",") for row in file.readlines()]
            salary_sum = 0
            employees_count = len(rows_list)
            for item in rows_list:
                salary_sum += int(item[1])

            return (salary_sum, salary_sum / employees_count)
    else:
        print("The provided path is not a valid file.")
        return None


# print(total_salary(Path('salary.txt')))
