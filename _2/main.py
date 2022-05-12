class Verificator:
    def check_ua_letters(self, str, another_sym=''):
        self.str_set = set(str)


class Human:
    def __init__(self, f_n, s_n, ph='+38xxxxxxxxxx'):
        if f_n is None:
            self.input_value()
        else:
            self._first_name = f_n
            self._second_name = s_n
            self._phone = ph

    def __str__(self):
        return f"{self._first_name} {self._second_name}, mob.{self._phone}"

    def set_first_name(self, first_name):
        self._first_name = first_name

    def set_second_name(self, second_name):
        self._second_name = second_name

    def set_phone(self, phone):
        self._phone = phone

    def get_first_name(self):
        return self._first_name

    def get_second_name(self):
        return self._second_name

    def get_phone(self):
        return self._phone

    def input_value(self):
        print("Human")


class Student(Human):
    def __init__(self, f_n=None, s_n=None, age=None, ph='+38xxxxxxxxxx'):
        super().__init__(f_n, s_n, ph)
        if self._age is None:
            self._age = age

    def __str__(self):
        return f"{self._first_name} {self._second_name}, {self._age} years, mob.{self._phone}"

    def set_age(self, age):
        self._age = age

    def get_age(self):
        return self._age

    def input_value(self):
        print("Student")
        self.set_first_name(input("First name: "))
        self.set_second_name(input("Second name: "))
        self.set_age(input("Age: "))
        self.set_phone(input("Phone: "))


class Parent(Human):
    def __init__(self, f_n=None, s_n=None, t=None, ph='+38xxxxxxxxxx'):
        super().__init__(f_n, s_n, ph)
        if self._type is None:
            self._type = t

    def __str__(self):
        return f"{self._first_name} {self._second_name}, {self._type}, mob.{self._phone}"

    def set_type(self, t):
        self._type = t

    def get_type(self):
        return self._type

    def input_value(self):
        print("Parent")
        self.set_first_name(input("First name: "))
        self.set_second_name(input("Second name: "))
        self.set_type(input("Type: "))
        self.set_phone(input("Phone: "))


class Teacher(Human):
    def __init__(self, f_n=None, s_n=None, age=None, covid=None, ph='+38xxxxxxxxxx'):
        super().__init__(f_n, s_n, ph)
        if self._age is None:
            self._age = age
            self._covid = covid

    def __str__(self):
        return f"{self._first_name} {self._second_name}, {self._age} years, mob.{self._phone}, vacc: {self._covid}"

    def set_age(self, age):
        self._age = age

    def get_age(self):
        return self._age

    def set_covid(self, covid):
        self._covid = covid

    def get_covid(self):
        return self._covid

    def input_value(self):
        print("Teacher")
        self.set_first_name(input("First name: "))
        self.set_second_name(input("Second name: "))
        self.set_age(input("Age: "))
        self.set_phone(input("Phone: "))
        self.set_covid(input("Vaccine: "))


# s1 = Student("Dafydd", "Idontknowenko", 6)
# print(s1)
# p1 = Parent("Joe", "Baiden", "mother", "+03812345678")
# print(p1)
# t1 = Teacher("Nil", "Armstrong", 45, "red")
# print(t1)

s1 = Student()
p1 = Parent()
t1 = Teacher()
print(s1)
print(p1)
print(t1)
