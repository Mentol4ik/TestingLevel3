import os
from main import *

def test_deleting_file():
    # Создаем временный файл
    file_path = "test_file.txt"
    with open(file_path, "w") as file:
        file.write("test")

    # Вызываем функцию deleting()
    deleting(file_path)

    # Проверяем, что файл удален
    assert not os.path.exists(file_path), "Файл не был удален"
#tgt5g

def test_deleting_folder():
    # Создаем временную папку
    folder_path = "test_folder"
    os.mkdir(folder_path)

    # Вызываем функцию deleting()
    deleting(folder_path)

    # Проверяем, что папка удалена
    assert not os.path.exists(folder_path), "Папка не была удалена"