USER_SCHEME = ("id", "first_name", "second_name", "email", "password")
RECORD_SCHEME = ("id", "date", "content", "user", "title")
DATABASE = []

def parse_record(entity_scheme, record_str):
    record_dict = {}
    for field in record_str.split(','):
        key, value = field.split('=')
        key = key.strip()
        value = value.strip()
        if key in entity_scheme:
            record_dict[key] = value
    return record_dict

def create_record(entity, record_str, entity_scheme):
    global DATABASE
    try:
        record_dict = parse_record(entity_scheme, record_str)
        DATABASE.append((entity, record_dict))
        print(f"{entity} створено успішно")
    except Exception as err:
        print(f"Помилка при створенні {entity}: {err}")

def search_entity_by_id(entity_name, entity_id):
    global DATABASE
    for entity, data in DATABASE:
        if data.get('id') == entity_id:
            print(f"Знайдено {entity_name}: {data}")
            return
    print(f"{entity_name} з id {entity_id} не знайдено")

def search_entity_by_field(entity_name, field_name, field_value):
    global DATABASE
    found = False
    for entity, data in DATABASE:
        if data.get(field_name) == field_value:
            print(f"Знайдено {entity_name}: {data}")
            found = True
    if not found:
        print(f"{entity_name} з {field_name} '{field_value}' не знайдено")

def main():
    global DATABASE
    while True:
        print("\nМеню:")
        print("1. Створити запис")
        print("2. Створити користувача")
        print("3. Пошук користувача за id")
        print("4. Пошук користувача за електронною адресою")
        print("5. Пошук запису за id")
        print("6. Пошук запису за назвою")
        choice = input("Виберіть дію: ")
        if choice == "1":
            entity = "Record"
            record_str = input("Введіть дані для нового запису: ")
            create_record(entity, record_str, RECORD_SCHEME)
        elif choice == "2":
            entity = "User"
            record_str = input("Введіть дані для нового користувача: ")
            create_record(entity, record_str, USER_SCHEME)
        elif choice == "3":
            entity_id = input("Введіть id користувача: ")
            search_entity_by_id("Користувач", entity_id)
        elif choice == "4":
            email = input("Введіть електронну адресу користувача: ")
            search_entity_by_field("Користувач", "email", email)
        elif choice == "5":
            entity_id = input("Введіть id запису: ")
            search_entity_by_id("Запис", entity_id)
        elif choice == "6":
            title = input("Введіть назву запису: ")
            search_entity_by_field("Запис", "title", title)
        else:
            print("Невідома цифра")

if __name__ == "__main__":
    main()
