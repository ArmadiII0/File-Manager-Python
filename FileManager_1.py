import os
import shutil
import zipfile

def get_working_directory():
    try:
        with open('config.txt', 'r') as file:
            return file.readline().strip()  # чтение строки и удаление лишних пробелов и символов новой строки
    except FileNotFoundError:
        print("Файл конфигурации не найден.")
        return None

def CreateDir(dir_name):
    try:
        os.mkdir(dir_name)
        print(f'Папка {dir_name} успешно создана')
    except FileExistsError:
        print(f'Папка с именем {dir_name} уже существует')

def RemDir(dir_name):
    try:
        os.rmdir(dir_name)
        print(f'Папка {dir_name} успешно удалена')
    except FileNotFoundError:
        print(f'Папки с именем {dir_name} не существует')

def ChangeDir(dir_name):
    try:
        os.chdir(dir_name)
        print(f'Перемещение в папку {dir_name} успешно произведено')
    except FileNotFoundError:
        print(f'Папки с именем {dir_name} не существует')

def ListFiles():
    try:
        directory = input("Введите путь к папке (нажмите Enter для текущей): ")
        if directory:
            os.chdir(directory)
        files = os.listdir()
        for file in files:
            print(file)
    except:
        print(f"Директории {directory} не существует")

def CreateFile(file_name):
    try:
        with open(file_name, 'x'):
            pass
        print(f"Файл '{file_name}' успешно создан.")
    except FileExistsError:
        print(f"Файл с именем '{file_name}' уже существует.")

def WriteToFile(file_name, text):
    try:
        with open(file_name, 'w') as file:
            file.write(text)
        print(f"Текст успешно записан в файл '{file_name}'.")
    except FileNotFoundError:
        print(f"Файл с именем '{file_name}' не найден.")

def ReadFile(file_name):
    try:
        with open(file_name, 'r') as file:
            print(f"Содержимое файла '{file_name}':")
            print(file.read())
    except FileNotFoundError:
        print(f"Файл с именем '{file_name}' не найден.")

def RemFile(file_name):
    try:
        os.remove(file_name)
        print(f"Файл '{file_name}' успешно удален.")
    except FileNotFoundError:
        print(f"Файл с именем '{file_name}' не найден.")

def CopyFile(source_path, destination_path):
    try:
        shutil.copy(source_path, destination_path)
        print(f"Файл успешно скопирован из '{source_path}' в '{destination_path}'.")
    except FileNotFoundError:
        print(f"Файл '{source_path}' не найден.")

def MoveFile(source_path, destination_path):
    try:
        shutil.move(source_path, destination_path)
        print(f"Файл успешно перемещен из '{source_path}' в '{destination_path}'.")
    except FileNotFoundError:
        print(f"Файл '{source_path}' не найден.")

def RenameFile(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print(f"Файл успешно переименован из '{old_name}' в '{new_name}'.")
    except FileNotFoundError:
        print(f"Файл с именем '{old_name}' не найден.")

def ArchiveFiles(file_list, archive_name):
    try:
        os.makedirs(archive_name)  # создаем временную папку для архива
        for file in file_list:
            shutil.move(file, os.path.join(archive_name, os.path.basename(file)))  # перемещаем файлы во временную папку
        shutil.make_archive(archive_name, 'zip', archive_name)  # создаем архив
        shutil.rmtree(archive_name)  # удаляем временную папку
        print(f"Файлы успешно архивированы в '{archive_name}.zip'.")
    except FileNotFoundError:
        print("Не удалось создать архив.")

def UnarchiveFile(archive_name, destination):
    try:
        with zipfile.ZipFile(archive_name, 'r') as zipf:
            zipf.extractall(destination)
        print(f"Файлы успешно разархивированы в '{destination}'.")
    except FileNotFoundError:
        print(f"Файл архива '{archive_name}' не найден.")

def DiskSpaceInfo():
    total, used, free = shutil.disk_usage(".")
    print(f"Общий объем диска: {total / (2**30):.2f} GB")
    print(f"Использовано: {used / (2**30):.2f} GB")
    print(f"Свободно: {free / (2**30):.2f} GB")

def ShowCurrentDirectory():
    try:
        current_directory = os.getcwd()
        print(f"Текущий рабочий каталог: {current_directory}")
    except OSError:
        print("Ошибка при получении текущего рабочего каталога.")

if __name__ == "__main__":
    working_directory = get_working_directory()
    if working_directory:
        os.chdir(working_directory)
        print(f"Рабочая папка установлена в: {working_directory}")
    else:
        print("Программа не может продолжить работу без указания рабочей папки.")
        exit()
    
    while True:
        print("\nДоступные команды:")
        print("1. Создать папку")
        print("2. Удалить папку")
        print("3. Перейти в папку")
        print("4. Создать файл")
        print("5. Записать текст в файл")
        print("6. Просмотреть содержимое файла")
        print("7. Удалить файл")
        print("8. Скопировать файл")
        print("9. Переместить файл")
        print("10. Переименовать файл")
        print("11. Просмотреть содержимое папки")
        print("12. Архивировать файлы")
        print("13. Разархивировать файл")
        print("14. Информация о дисковом пространстве")
        print("15. Текущий рабочий каталог")
        print("16. Выйти из программы")

        choice = input("\nВведите номер команды: ")
        
        if choice == "1":
            directory_name = input("Введите имя папки: ")
            CreateDir(directory_name)
        elif choice == "2":
            directory_name = input("Введите имя папки: ")
            RemDir(directory_name)
        elif choice == "3":
            directory_name = input("Введите имя папки: ")
            ChangeDir(directory_name)
        elif choice == "4":
            file_name = input("Введите имя файла: ")
            CreateFile(file_name)
        elif choice == "5":
            file_name = input("Введите имя файла: ")
            text = input("Введите текст для записи в файл: ")
            WriteToFile(file_name, text)
        elif choice == "6":
            file_name = input("Введите имя файла: ")
            ReadFile(file_name)
        elif choice == "7":
            file_name = input("Введите имя файла: ")
            RemFile(file_name)
        elif choice == "8":
            source_path = input("Введите путь к исходному файлу: ")
            destination_path = input("Введите путь к папке, куда нужно скопировать файл: ")
            CopyFile(source_path, destination_path)
        elif choice == "9":
            source_path = input("Введите путь к исходному файлу: ")
            destination_path = input("Введите путь к папке, куда нужно переместить файл: ")
            MoveFile(source_path, destination_path)
        elif choice == "10":
            old_name = input("Введите текущее имя файла: ")
            new_name = input("Введите новое имя файла: ")
            RenameFile(old_name, new_name)
        elif choice == "11":
            ListFiles()
        elif choice == "12":
            file_list = input("Введите через пробел имена файлов/папок для архивации: ").split()
            archive_name = input("Введите имя для архива: ")
            ArchiveFiles(file_list, archive_name)
        elif choice == "13":
            archive_name = input("Введите имя архива: ")
            destination = input("Введите путь к папке для разархивации: ")
            UnarchiveFile(archive_name, destination)
        elif choice == "14":
            DiskSpaceInfo()
        elif choice == "15":
            ShowCurrentDirectory()
        elif choice == "16":
            print("Завершение программы.")
            break
        else:
            print("Неверная команда. Пожалуйста, выберите существующую команду.")
