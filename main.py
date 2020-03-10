

class Contact:

    def __init__(self, first_name, last_name, phone_number, selected_contact=False, *args, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.selected_contact = selected_contact
        self.args = args
        self.kwargs = kwargs

    def show_info_users(self):
        print(f'Имя: {self.first_name}')
        print(f'Фамилия: {self.last_name}')
        print(f'Телефон: {self.phone_number}')
        print(f'В избранных: {"Да" if self.selected_contact == True else "Нет"}')
        print(f'Дополнительная информация:')
        if len(self.args) > 0:
            for i in self.args:
                print(f'         {i}')
        if len(self.kwargs) > 0:
            for k, v in self.kwargs.items():
                print(f'         {k}: {v}')

    def __str__(self):

        self.show_info_users()
        return ' '


class PhoneBook:

    def __init__(self, phone_book_name):
        self.phone_book_name = phone_book_name

    def get_contacts(self):
        for contact in self.phone_book_name:
            print(contact)

    def add_new_contact(self, contact):
        self.phone_book_name.append(contact)

    def del_contact_by_phone_number(self, phone_number):
        for contact in self.phone_book_name:
            if phone_number == contact.phone_number:
                self.phone_book_name.remove(contact)

    def search_favorite_numbers(self):
        for contact in self.phone_book_name:
            if contact.selected_contact == True:
                print(contact.phone_number)

    def search_contact_by_first_and_last_name(self, first_name, last_name):
        for contact in self.phone_book_name:
            if contact.first_name == first_name and contact.last_name == last_name:
                print(contact)


if __name__ == '__main__':
    jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
    anastasia = Contact('Anastasia', 'Zharkova', '+79834758448', True, '+72947365247', telegram='@anastasia',
                        email='anastasia@gmail.com')
    jack = Contact('Jack', 'London', '+79564568125', telegram='@Jack', email='jack@gmail.com', mom_phone='+78265554466')
    jim = Contact('Jim', 'Carrey', '+79998877333', True, telegram='@Jim', email='Jim@gmail.com')
    brad = Contact('Brad', 'Pitt', '+72967564466', telegram='@Pitt', email='Pitt@gmail.com')

    phone_book_list = []

    phone_book = PhoneBook(phone_book_list)

    phone_book.add_new_contact(jhon)
    phone_book.add_new_contact(anastasia)
    phone_book.add_new_contact(jack)
    phone_book.add_new_contact(jim)
    phone_book.add_new_contact(brad)

    phone_book.get_contacts()

    phone_book.del_contact_by_phone_number('+79564568125')

    phone_book.search_favorite_numbers()
    print()
    phone_book.search_contact_by_first_and_last_name('Brad', 'Pitt')
