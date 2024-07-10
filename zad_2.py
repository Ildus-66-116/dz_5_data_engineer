"""Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла."""


def get_file_info(file_path: str) -> tuple:
    file_name = file_path.split("/")[-1]
    file_extension = file_name.split(".")[-1]
    path = file_path[:-len(file_name)]
    return (path, file_name[:-len(file_extension) - 1], "." + file_extension)


if __name__ == '__main__':
    file_path = 'file_in_current_directory.txt'
    print(get_file_info(file_path))

    file_path = "C:/Users/User/Documents/example.txt"
    print(get_file_info(file_path))
