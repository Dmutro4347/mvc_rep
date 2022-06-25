from colorama import Fore


class View:

    def main_menu(self):
        # preview_text = Figlet(font='slant')
        # print(colored(preview_text.renderText('MAIN MENU'), 'green'))
        print(Fore.CYAN + '1 - Робота з БД\n2 - Адміністрування\n3 - Вихід')
        return input(Fore.GREEN + 'що будем робити?: ')

    def db_menu(self, file_name):
        print(Fore.CYAN + '1 - Вивід з БД\n2 - Вставка в БД\n3 - Замінити інформацію\n4 - Видалити\n5 - новий учень')
        if file_name:
            print('6 - Вставка з файлу')
        return input(Fore.GREEN + 'що будем робити?: ')

    def new_menu(self):
        print(Fore.CYAN + '1 - Нова людина\n2 - Нова група\n3 - Новий курс\n 4 -новий учень')
        return input(Fore.GREEN + 'що будем робити?: ')

    def new_human(self):
        print(Fore.CYAN + 'Нова людина')
        return (
            input(Fore.GREEN + "Ім'я: "),
            input(Fore.GREEN + 'Прізвище: '),
            input(Fore.GREEN + 'Номер телефону: '),
            input(Fore.GREEN + 'Дата народження (DD.MM.YYYY): ')
        )

    def new_student(self):
        print(Fore.CYAN + 'Новий студент')
        print(Fore.RED + 'Коми тільки для розділення!!!!!!!!!')
        return (
            input(Fore.GREEN + "Ім'я, Прізвище, Дата народження (DD.MM.YYYY), Номер телефону: "),
            input(Fore.GREEN + "Ім'я по-батькові, Прізвище, Номер телефону, Дата народження (DD.MM.YYYY): "),
            input(Fore.GREEN + 'номер групи: ')
        )

    def insert_menu(self):
        print(Fore.CYAN + 'Вставка в БД')
        return (
            input(Fore.GREEN + "Ім'я таблиці: "),
            input(Fore.GREEN + 'Значення: '),
            input(Fore.GREEN + 'Порядок стовпців в таблиці або пусте значення: ')
        )

    def select_menu(self):
        print(Fore.CYAN + 'Вивід з БД')
        return input(Fore.GREEN + 'Імя таблиці: ')

    def update_menu(self):
        print(Fore.CYAN + 'Замінити інформацію')
        return (
            input(Fore.GREEN + 'Імя таблиці: '),
            input(Fore.GREEN + 'Колонка: '),
            input(Fore.GREEN + 'Значення: '),
            input(Fore.GREEN + 'id: ')
        )

    def delete_menu(self):
        print(Fore.CYAN + 'Видалити')
        return (
            input(Fore.GREEN + 'Імя таблиці: '),
            input(Fore.GREEN + 'id: ')
        )

    def insert_from_file_menu(self):
        print(Fore.CYAN + 'Вставка з файлу')
        return input(Fore.GREEN + 'Імя таблиці: ')

    def admin_menu(self):
        print('')
