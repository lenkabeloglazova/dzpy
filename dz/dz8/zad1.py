from os import path

fail_base = "base.txt"
all_date = []
last_id = 0
exist_contact = []
data_collection = []
if not path.exists(fail_base):
    with open(fail_base, "w", encoding="utf-8") as _:
        pass


def read_records():
    global all_date, last_id
    with open(fail_base, encoding="utf-8") as f:
     all_date = [i.strip() for i in f]
     if all_date:
         last_id = int(all_date[-1].split()[0])
    return all_date
    return []


def show_all():
    if all_date:
         print(*all_date, sep="\n")
     else:
      print("Empty base!\n")


def add():
    # Добавление
    global last_id
    array = ["name", "surname", "patronymic", "phone"]
    answers = []
    for i in array:
       answers.append(data_collection(i))
    if not path.exists(0, "".join(answers)):

        if not exist_contact(0, " ".join(answers)):
         last_id += 1
        answers.insert(0, str(last_id))

        with open(file_base, 'a', encoding="utf-8") as f:
            f.write(f'{" ".join(answers)}\n')
        print("Data added successfully!\n")
    else:
        print("The data already exists!")


def Delete():
    # Удаление
    global all_data

    symbol = "\n"
    show_all()
    del_record = input("Enter the record id: ")

    if exist_contact(del_record, ""):
        all_data = [k for k in all_data if k.split()[0] != del_record]

        with open(file_base, 'w', encoding="utf-8") as f:
            f.write(f'{symbol.join(all_data)}\n')
        print("Deleted!\n")
    else:
        print("The data is not correct!")

        def change(data_tuple):
        #Изменения

            global all_data
            symbol = "\n"

            record_id, num_data, data = data_tuple

            for i, v in enumerate(all_data):
                if v.split()[0] == record_id:
                    v = v.split()
                    v[int(num_data)] = data
                    if exist_contact(0, " ".join(v[1:])):
                        print("The data already exists!")
                        return
                    all_data[i] = " ".join(v)
                    break

            with open(file_base, 'w', encoding="utf-8") as f:
                f.write(f'{symbol.join(all_data)}\n')
            print("Changed!\n")


def search():
       search_data = exist_contact(0, input("Enter the search data: "))
       if search_data:
         print(*search_data, sep="\n")
       else:
            print("The data is not correct!")


def exist_contact(rec_id, data):

    : type data: """Проверка записи"""
    : type rec_id:"""Проверка id"""

    if rec_id:
        candidates = [i for i in all_data if rec_id in i.split()[0]]
    else:
        candidates = [i for i in all_data if data in i]
    return candidates


def data_collection(num):
    # Проверка данных

    answer = input(f"Enter a {num}: ")
    while True:
        if num in "surname name patronymic":
            if answer.isalpha():
                break
        if num == "phone number":
            if answer.isdigit() and len(answer) == 11:
                break
        answer = input(f"Data is incorrect!\n"
                       f"Use only use only the letters"
                       f" of the alphabet, the length"
                       f" of the number is 11 digits\n"
                       f"Enter a {num}: ")
    return answer


def main_menu():
    work = True
    while work:
        read_records()
        answer = input("Phone book: \n"
                       "1.Show all \n"
                       "2.Add \n"
                       "3.Search \n"
                       "4.Change \n"
                       "5.Delete \n"
                       "6.Export\Import \n"
                       "7.Exit \n")

    match answer:
        case "1":
            show_all()
        case "2":
            add()
        case "3":
            search()
        case "4":
          work = edit_menu()
          if work:
               change(work)
        case "5":
            Delete()
        case "6":
            exp_imp_menu()
        case "7":
           work = False
        case _:
            print("Try again!\n")


main_menu()
