import os
import platform

resultOS = platform.uname().system
if resultOS == 'Linux' or resultOS == 'Windows':
    pass
else:
    exit('\033[31;5;208m' + resultOS + ' не поддерживается.\033[0;0m')


DIRECTORY = input("Введите адрес: ")
if not os.path.isdir(DIRECTORY):
    exit('\033[31;5;208m' + DIRECTORY + ' не является директорией или её не существует.\033[0;0m')

SRC = input("Введите расширение SRC: ")  # webp
DST = input("Введите расширение DST: ")  # jpg
SRC = '.' + SRC
DST = '.' + DST


if resultOS == 'Linux':
    if '/' != DIRECTORY[-1]:
        DIRECTORY = DIRECTORY + '/'
elif resultOS == 'Windows':
    if '\\' != DIRECTORY[-1]:
        DIRECTORY = DIRECTORY + '\\'


with os.scandir(DIRECTORY) as entries:
    i = 0
    for entry in entries:
        if os.path.splitext(DIRECTORY+entry.name)[1] == SRC:
            i = i + 1
    if i < 1:
        exit('\033[31;5;208mФайлов с расширением ' + SRC + ' не найдено.\033[0;0m')


with os.scandir(DIRECTORY) as files:
    for file in files:
        fn = os.path.splitext(DIRECTORY + file.name)
        if not file.name.startswith('.') and file.is_file() and SRC == fn[1]:
            if os.path.isfile(DIRECTORY + file.name):
                lists = fn[0] + fn[1]
                os.rename(DIRECTORY + file.name, fn[0] + DST)
                lists_old = fn[0] + DST
                print(f'\033[32;5;208m{lists} >> {lists_old} \033[0;0m')
            elif os.path.isdir(DIRECTORY + file.name):
                print('\033[2;31;40m Папка ' + DIRECTORY + file + ' была пропущена.')
