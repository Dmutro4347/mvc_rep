from colorama import Fore


class View:

    def main_menu(self):
        # preview_text = Figlet(font='slant')
        # print(colored(preview_text.renderText('MAIN MENU'), 'green'))
        print(Fore.CYAN + '1 - Робота з БД\n2 - Адміністрування\n3 - Вихід')
        return input(Fore.GREEN + 'що будем робити?: ')

    def db_menu(self, file_name):
        print(Fore.CYAN + '1 - Вставка в БД\n2 - Вивід з БД\n3 - Замінити інформацію\n4 - Видалити')
        if file_name:
            print('5 - Вставка з файлу')
        return input(Fore.GREEN + 'що будем робити?: ')

    def insert_menu(self):
        print(Fore.CYAN + 'Вставка в таблицю')
        return (
            input(Fore.GREEN + 'Імя таблиці: '),
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
            input(Fore.GREEN + 'Колонка: '), input(Fore.GREEN + 'Значення: '),
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
