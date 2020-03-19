import csv
import re
from tkinter import filedialog as fd
from tkinter import Button, StringVar, Tk, Label, Entry, Text, NORMAL, DISABLED, END

root = Tk()
root.title('Поиск сотрудников')

first_name = StringVar()
first_name_label = Label(text='Введите Имя')
first_name_label.grid(row=0, column=0, sticky="w")
first_name_entry = Entry(textvariable=first_name)
first_name_entry.grid(row=0, column=1, padx=5, pady=5)

second_name = StringVar()
second_name_label = Label(text='Введите Фамилию')
second_name_label.grid(row=1, column=0, sticky="w")
second_name_entry = Entry(textvariable=second_name)
second_name_entry.grid(row=1, column=1, padx=5, pady=5)

file_name = StringVar()
file_name.set("Файл не выбран")
filename_label = Label(root, textvariable=file_name)
filename_label.grid(row=3, column=1, pady=5, sticky="w")

results_widget = Text(root, width=55, height=15)

global result_data
result_data = {}


def get_file_path():
    file_path = fd.askopenfilename()
    return file_path


def import_from_csv(file_path):
    result_data.clear()
    results_widget.delete('1.0', END)
    results_widget.grid_forget()
    results_widget.update()
    if re.match(r'.*\.csv', file_path):
        with open(file_path) as csv_file:
            next(csv_file, None)
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                full_name = str(row[0])+' '+str(row[1])
                if full_name in result_data:
                    result_data[full_name].append([row[2], row[3]])
                else:
                    result_data.update({full_name: [[row[2], row[3]]]})

        file_name.set('Выбран файл  ' + (file_path.split('/'))[-1])
        find_button.config(state=NORMAL)
        return result_data
    elif file_path == '' :
        print('not choosen')
        return('not choosen')
    else:
        find_button.config(state=DISABLED)
        file_name.set("Выберите файл в формате csv !!!")
        print('Wrong file type')
        return ('Wrong file type')


def show_info(data_csv, first_name, second_name):
    results_widget.delete('1.0', END)
    results_widget.grid(row=4, column=1, padx=5, pady=5)
    results_widget.update()
    first_name = (first_name.replace(" ", "")).capitalize()
    second_name = (second_name.replace(" ", "")).capitalize()
    full_name = first_name + " " + second_name
    data_list = []
    if second_name == "":
        dict_of_found_data = dict(
            filter(lambda item: first_name in (item[0].split())[0], data_csv.items()))
        for keys, values_list in dict_of_found_data.items():
            for value_pair_list in values_list:
                print(keys + " - " +
                      value_pair_list[0]+' - ' + value_pair_list[1])
                results_widget.insert(
                    END, keys + ' - ' + value_pair_list[0]+' - ' + value_pair_list[1] + '\n')
                data_list.append(
                    keys + " - " + value_pair_list[0]+' - ' + value_pair_list[1])
    elif first_name == "":
        dict_of_found_data = dict(
            filter(lambda item: second_name in (item[0].split())[1], data_csv.items()))
        for keys, values_list in dict_of_found_data.items():
            for value_pair_list in values_list:
                print(keys + " - " +
                      value_pair_list[0]+' - ' + value_pair_list[1])
                results_widget.insert(
                    END, keys + ' - ' + value_pair_list[0]+' - ' + value_pair_list[1] + '\n')
                data_list.append(
                    keys + " - " + value_pair_list[0]+' - ' + value_pair_list[1])
    else:
        dict_of_found_data = dict(
            filter(lambda item: full_name in item[0], data_csv.items()))
        for keys, values_list in dict_of_found_data.items():
            for value_pair_list in values_list:
                print(keys + " - " +
                      value_pair_list[0]+' - ' + value_pair_list[1])
                results_widget.insert(
                    END, keys + ' - ' + value_pair_list[0]+' - ' + value_pair_list[1] + '\n')
                data_list.append(
                    keys + " - " + value_pair_list[0]+' - ' + value_pair_list[1])
    return data_list


find_button = Button(text='Найти сотрудника', command=lambda: show_info(
    result_data, first_name.get(), second_name.get()))
find_button.grid(row=2, column=1, padx=5, pady=5, sticky="e")
find_button.config(state=DISABLED)

import_button = Button(text='Импортировать csv файл',
                       command=lambda: import_from_csv(get_file_path()))
import_button.grid(row=2, column=2, padx=5, pady=5, sticky="e")

if __name__ == "__main__":
    root.mainloop()
