from datetime import date
from address_book import AddressBook, Record, Birthday
from bot import add_contact, change_contact, show_phone, add_birthday, show_birthday, birthdays, show_all, parse_input

book = AddressBook()
assert add_contact(["Bob"], book) == "Enter the argument for the command."
assert add_contact(["Jime", "0501234356"], book) == "Contact added."
assert add_contact(["Jime", "0671234567"], book) == "Contact updated."
assert show_phone(["Jime"], book) == "0501234356; 0671234567"
assert show_phone(["Nobody"], book) == "Contact not found."
assert change_contact(["Jime", "0501234356", "0990000000"], book) == "Contact updated."
assert show_phone([], book) == "Enter the argument for the command."
assert add_birthday(["Jime", "25.10.1990"], book) == "Birthday added."
assert show_birthday(["Jime"], book) == "25.10.1990"
assert add_contact(["Bob", "1234567890"], book) == "Contact added."
assert add_birthday(["Bob", "2020-01-01"], book) == "Invalid date format. Use DD.MM.YYYY"
assert add_birthday(["Jime", "01.01.2000"], book) == "Birthday already set."
assert parse_input("  ADD-BIRTHDAY  Jime 1.1.2000 ") == ("add-birthday", ["Jime", "1.1.2000"])

# Дні народження: сьогодні 2026-10-24 (субота). 27.10.2026 — вівторок, 25.10 — неділя → понеділок 26.10
b2 = AddressBook()
r = Record("Ann"); r.add_birthday("25.10.1990"); b2.add_record(r)
r2 = Record("Ben"); r2.add_birthday("27.10.1985"); b2.add_record(r2)
r3 = Record("Old"); r3.add_birthday("01.01.1980"); b2.add_record(r3)
out = b2.get_upcoming_birthdays(today=date(2026, 10, 24))
assert out == [
    {"name": "Ann", "congratulation_date": "2026.10.26"},
    {"name": "Ben", "congratulation_date": "2026.10.27"},
], out

print("ALL HW7 TESTS PASSED")
