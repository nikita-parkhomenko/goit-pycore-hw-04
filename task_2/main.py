from pathlib import Path

# Task 2
# get_cats_info(path) => [{ id, name, age }]


def get_cats_info(path: Path):
    if not path.is_file():
        print("The provided path is not a valid file.")
        return []

    with open(path, encoding="utf-8") as file:
        rows_list = [row.strip().split(",") for row in file.readlines()]
        cats_list = []
        for cat in rows_list:
            cats_list.append({"id": cat[0], "name": cat[1], "age": cat[2]})
        return cats_list


# print(get_cats_info(Path('cats.txt')))

# Task 3
path_to_dir = input("Please enter a path to the directory >>> ")
