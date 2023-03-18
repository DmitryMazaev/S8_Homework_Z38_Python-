# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал 
# для изменения и удаления данных
import ask

def add_data(worker):
    with open('phone_book.txt', 'a', encoding = 'utf-8') as f:
        f.write(worker)

def find_person(data_str):
    with open('phone_book.txt', 'r', encoding = 'utf-8') as f:
        lst_str = f.readlines()
        i = 0
        for worker in lst_str:
            i+=1
            if data_str in worker:
                print(i, worker)
        if data_str not in worker:
            print("Указанный параметр не найден")

def del_person(del_str):
    with open('phone_book.txt', 'r', encoding = 'utf-8') as f:
        del_lst_str = f.readlines()
        i = 0
        c = 0
        for worker in del_lst_str:
            i+=1
            if del_str in worker:
                print(i, worker)
            else:
                c += 1
        if c != len(del_lst_str):
            a = int(input("Введите номер удаляемой позиции: "))
            with open('phone_book.txt', 'w', encoding = 'utf-8') as f:
                j = 0
                for worker in del_lst_str:
                    j+=1
                    if j != a:
                        f.write(worker)
        else:
            print("Указанный параметр не найден")

def change_person(change_str):
    with open('phone_book.txt', 'r', encoding = 'utf-8') as f:
        change_lst_str = f.readlines()
        i = 0
        c = 0
        for worker in change_lst_str:
            i+=1
            if change_str in worker:
                print(i, worker)
            else:
                c +=1
        if c == len(change_lst_str):
            print("Указанный параметр не найден")
        else:
            b = int(input("Введите номер изменяемой позиции: "))
            with open('phone_book.txt', 'w', encoding = 'utf-8') as f:
                j = 0
                for worker in change_lst_str:
                    j+=1
                    if j != b:
                        f.write(worker)
                    else:
                        new_name = ask.input_()
                        f.write(new_name)
