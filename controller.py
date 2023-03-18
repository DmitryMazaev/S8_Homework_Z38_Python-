# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал 
# для изменения и удаления данных

import ask
import database

def main():
    while True:
        op = ask.operation()
        if op == 1:
            data_worker = ask.input_()
            database.add_data(data_worker)
        if op == 2:
            find_str = ask.find_person()
            database.find_person(find_str)
        if op == 3:
            del_str = ask.del_person()
            database.del_person(del_str)
        if op == 4:
            change_str = ask.change_person()
            database.change_person(change_str)     
        if op == 5:
            break

if __name__ == "__main__":
    main()