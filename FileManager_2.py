import argparse
import os
import shutil

def get_working_directory():
    try:
        with open('config.txt', 'r') as file:
            return file.readline().strip()
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
        files = os.listdir()
        for file in files:
            print(file)
    except:
        print("Ошибка при просмотре содержимого папки")

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

if __name__ == "__main__":
    working_directory = get_working_directory()
    if working_directory:
        os.chdir(working_directory)
        print(f"Рабочая папка установлена в: {working_directory}")
    else:
        print("Программа не может продолжить работу без указания рабочей папки.")
        exit()

    parser = argparse.ArgumentParser(description='Управление файловой системой.')
    parser.add_argument('command', choices=['rcd', 'rmkdir', 'rmdir', 'rls', 'rtouch', 'rwrite', 'rread', 'rrm', 'rcp', 'rmv', 'rrename'],
                        help='Команда для выполнения')
    parser.add_argument('args', nargs='*', help='Аргументы команды')

    args = parser.parse_args()

    command = args.command

    if command == "rcd":
        if args.args:
            ChangeDir(args.args[0])
        else:
            print("Необходимо указать имя папки для перехода.")
    elif command == "rrmkdir":
        if args.args:
            CreateDir(args.args[0])
        else:
            print("Необходимо указать имя папки для создания.")
    elif command == "rmdir":
        if args.args:
            RemDir(args.args[0])
        else:
            print("Необходимо указать имя папки для удаления.")
    elif command == "rls":
        ListFiles()
    elif command == "rtouch":
        if args.args:
            CreateFile(args.args[0])
        else:
            print("Необходимо указать имя файла для создания.")
    elif command == "rwrite":
        if len(args.args) >= 2:
            file_name = args.args[0]
            text = ' '.join(args.args[1:])
            WriteToFile(file_name, text)
        else:
            print("Необходимо указать имя файла и текст для записи.")
    elif command == "rread":
        if args.args:
            ReadFile(args.args[0])
        else:
            print("Необходимо указать имя файла для чтения.")
    elif command == "rrm":
        if args.args:
            RemFile(args.args[0])
        else:
            print("Необходимо указать имя файла для удаления.")
    elif command == "rcp":
        if len(args.args) >= 2:
            source_path = args.args[0]
            destination_path = args.args[1]
            CopyFile(source_path, destination_path)
        else:
            print("Необходимо указать исходный и целевой пути для копирования файла.")
    elif command == "rmv":
        if len(args.args) >= 2:
            source_path = args.args[0]
            destination_path = args.args[1]
            MoveFile(source_path, destination_path)
        else:
            print("Необходимо указать исходный и целевой пути для перемещения файла.")
    elif command == "rrename":
        if len(args.args) >= 2:
            old_name = args.args[0]
            new_name = args.args[1]
            RenameFile(old_name, new_name)
        else:
            print("Необходимо указать текущее и новое имя файла для переименования.")
