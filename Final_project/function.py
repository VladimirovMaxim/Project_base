
import var_input_output


def sum_a_note():
    sum_string = input(var_input_output.input_name) + " " + input(var_input_output.input_surname) \
            + " " + input(var_input_output.input_lastname) + " " + \
            input(var_input_output.input_telephone_number) + " " + \
            input(var_input_output.input_telephone_number) + "\n"
    print(sum_string)
    return sum_string


def add_a_note(data):  # добавить запись в базу данных взяв их с консоли через лист
    with open('data_base.csv', 'a+') as file:
        file.write(data + '\n')
    print(var_input_output.result_to_add)


def print_list():  # вывести весь список в консоль
    print(var_input_output.result_to_view)
    with open('data_base.csv', 'r') as base:
        print(base.read())


def exit_program():
    print(var_input_output.result_to_exit)


def export_format_2():
    name = input("Введите название для файла ")
    base_file = open("data_base.csv", "r")
    data = base_file.readlines()
    base_file.close()
    new_data = []
    for i in data:
        new_data.append(i.replace("\n", ""))
    user_file_data = ", ".join(new_data)
    export_file_type_2 = open(name+".csv", "w")
    export_file_type_2.write(user_file_data)
    export_file_type_2.close()
    print(var_input_output.result_to_export_format2)


def export_format_1():
    name = input("Введите название для файла ")
    base_file = open("data_base.csv", "r")
    data = base_file.readlines()
    base_file.close()
    user_file_data = "".join(data)
    export_file_type_1 = open(name + ".csv", "w")
    export_file_type_1.write(user_file_data)
    export_file_type_1.close()
    print(var_input_output.result_to_export_format1)


def back_to_menu():
    input("\n\nВведите любой символ для возврата в меню ")


def search_surname():  # поиск по фамилии (encoding="utf-8")
    import io
    surname = input(var_input_output.input_surname)
    with io.open('data_base.csv', 'r') as file:
        search = False
        for lin in file:
            if surname in lin:
                print(lin, end='\n')
                search = True
        if not search:
            print('Такого контакта не найденно')


def delete_entry():  # удалить запись с бд взяв с консоли
    import re
    with open('data_base.csv', 'r') as fi:
        lines = fi.readlines()
    delete = input('Введите фамилию: ')
    pattern = re.compile(re.escape(delete))
    with open('data_base.csv', 'w') as f:
        for lin in lines:
            result = pattern.search(lin)
            if result is None:
                f.write(lin)
    print()
    print(var_input_output.result_to_delete)


def import_format_1():
    f = open('file_1.csv', 'r')
    data = f.read()
    f.close()
    with open('data_base.csv', 'a') as f:
        f.write(data)
    print(var_input_output.result_to_import_format1)


def import_format_2():
    f = open('file_2.csv', 'r')
    data = f.read()
    f.close()
    data = "\n" + data
    new_data = data.replace(", ", "\n")
    with open('data_base.csv', 'a') as f:
        f.write(new_data)
    print(var_input_output.result_to_import_format2)
