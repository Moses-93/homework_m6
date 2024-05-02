from collections import UserDict

# Оголошуємо клас Field, який представляє поле запису в адресній книзі
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

# Оголошуємо клас Name, який успадковує клас Field
class Name(Field):
    def __init__(self, value):
        # Ім'я є обов'язковим полем, тому перевіряємо, чи воно не порожнє
        if not value:
            raise ValueError("Ім'я не може бути порожнім")
        super().__init__(value)


# Оголошуємо клас Phone, який успадковує клас Field
class Phone(Field):
    # Конструктор класу Phone
    def __init__(self, value):
        # Перевіряємо правильність формату номера телефону (10 цифр)
        if len(value) != 10 or not value.isdigit():
            # Викидаємо ValueError, якщо формат номера телефону невірний
            raise ValueError("Невірний формат номера телефону")
        # Викликаємо конструктор класу Field з правильним значенням номера телефону
        super().__init__(value)

# Оголошуємо клас Record, який представляє запис в адресній книзі
class Record:
    # Конструктор класу Record
    def __init__(self, name):
        # Встановлюємо значення поля name
        self.name = Name(name)
        # Встановлюємо порожній список для зберігання номерів телефону
        self.phones = []

    # Метод для додавання номера телефону в запис
    def add_phone(self, phone):
        # Спробуємо додати номер телефону в список
        try:
            # Викликаємо конструктор класу Phone з правильним значенням номера телефону
            self.phones.append(Phone(phone))
        # Якщо формат номера телефону невірний, то спрацює виняток ValueError
        except ValueError as e:
            # Виводимо повідомлення про помилку
            print(e)

    # Метод для видалення номера телефону з запису
    def remove_phone(self, phone):
        # Фільтруємо список номерів телефону, залишаючи тільки ті, які не дорівнюють шуканому номеру
        self.phones = [p for p in self.phones if str(p) != phone]

    # Метод для редагування номера телефону в записі
    def edit_phone(self, old_phone, new_phone):
        # Знаходимо індекс старого номера телефону в списку номерів телефону
        try:
            index = self.phones.index(Phone(old_phone))
            # Замінюємо старий номер телефону на новий
            self.phones[index] = Phone(new_phone)
        # Якщо такого номера телефону немає в списку, то спрацює виняток ValueError
        except ValueError:
            # Виводимо повідомлення про помилку
            print("Такий номер телефону не знайдено")

    # Метод для пошуку номера телефону в записі
    def find_phone(self, phone):
        # Знаходимо індекс номера телефону в списку номерів телефону
        try:
            index = self.phones.index(Phone(phone))
            # Повертаємо рядок, який містить знайдений номер телефону
            return str(self.phones[index])
        # Якщо такого номера телефону немає в списку, то спрацює виняток ValueError
        except ValueError:
            # Повертаємо рядок, який містить повідомлення про те, що такого номера телефону не знайдено
            return "Такий номер телефону не знайдено"

    # Метод для отримання рядкового представлення запису
    def __str__(self):
        # Повертаємо рядок, який містить ім's користувача та його номери телефону
        return f"Контакт: {self.name}, Телефони: {', '.join(str(p) for p in self.phones)}"

# Оголошуємо клас AddressBook, який успадковує клас UserDict
class AddressBook(UserDict):
    # Метод для додавання запису в адресну книгу
    def add_record(self, record):
        # Додаємо запис в словник адресної книги
        self.data[record.name.value] = record

    # Метод для пошуку запису в адресній книзі
    def find(self, name):
        # Спробуємо знайти запис в словнику адресної книги
        try:
            # Повертаємо знайдений запис
            return self.data[name]
        # Якщо запис не знайдено, то спрацює виняток KeyError
        except KeyError:
            # Виводимо повідомлення про помилку
            print("Контакт не знайдено")

    # Метод для видалення запису з адресної книги
    def delete(self, name):
        # Спробуємо видалити запис з словника адресної книги
        try:
            # Видаляємо запис з словника адресної книги
            del self.data[name]
        # Якщо запис не знайдено, то спрацює виняток KeyError
        except KeyError:
            # Виводимо повідомлення про помилку
            print("Контакт не знайдено")


# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")
