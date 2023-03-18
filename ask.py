# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал 
# для изменения и удаления данных

def operation():
    print("Выберите действие: \n 1 - Добавить новый номер \n 2 - Поиск сотрудника \n 3 - Удаление из справочника \n 4 - Изменение данных  \n 5 - Выход \n")
    q1 = int(input())
    return q1

def input_():
    print("Введите данные сотрудника:")
    name = input("Имя: ")
    surname = input("Фамилия: ")
    telephone = input("Телефон: ")
    worker = name + " " + surname + " " + " " + telephone + "\n"
    return worker
def find_person():
    data_str = input("Введите параметр для поиска: ")
    return data_str
def del_person():
    del_str = str(input("Введите параметр для удаления: "))
    return del_str
def change_person():
    change_str = input("Введите параметр для изменения: ")
    return change_str
