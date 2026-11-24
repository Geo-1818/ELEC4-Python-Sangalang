
# Name: IAN GEOFREY P. SANGALANG | Section: IV-BSIT B | Activity: P3 | Date: 2026-11-24

students = []
student_keys = set()


def add_student():
    name = input("Student name: ").strip()
    key = name.strip().casefold()

    if not name:
        print("Name cannot be blank.")
    elif key in student_keys:
        print("That student is already in the list.")
    else:
        students.append(name)
        student_keys.add(key)
        print(name, "added.")


def remove_student():
    name = input("Name to remove: ").strip()
    key = name.strip().casefold()

    for existing in students:
        if existing.strip().casefold() == key:
            students.remove(existing)
            student_keys.remove(key)
            print(existing, "removed.")
            return

    print("Student not found.")


def search_student():
    query = input("Search name: ").strip().casefold()

    matches = [
        name for name in students
        if query in name.strip().casefold()
    ]

    if matches:
        for name in sorted(matches, key=str.casefold):
            print("-", name)
    else:
        print("No matching student.")


def display_students():
    if not students:
        print("No students recorded.")
        return

    ordered = sorted(students, key=str.casefold)

    for number, name in enumerate(ordered, start=1):
        print(f"{number}. {name}")

    print("Total:", len(students))


def main():
    while True:
        print("\n1 Add 2 Remove 3 Search 4 Display 5 Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            search_student()
        elif choice == "4":
            display_students()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()



