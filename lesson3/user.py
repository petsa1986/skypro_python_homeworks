class User:
    def __init__(self, first_name, last_name):
        self.f_name = first_name
        self.l_name = last_name

    def print_first_name(self):
        print(self.f_name)

    def print_last_name(self):
        print(self.l_name)

    def print_full_name(self):
        print(f"{self.f_name} {self.l_name}")