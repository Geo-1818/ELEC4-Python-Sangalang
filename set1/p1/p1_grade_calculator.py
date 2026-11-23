
# Name: IAN GEOFREY P. SANGALANG | Section: IV-BSIT B | Activity: P1 | Date: 2026-11-23

def enter_grades():
    grades = []

    while True:
        raw = input("Enter a grade (0-100), or 'done': ").strip()

        if raw.lower() == "done":
            if grades:
                return grades
            print("Enter at least one grade.")
            continue

        try:
            grade = float(raw)

            if 0 <= grade <= 100:
                grades.append(grade)
            else:
                print("Grade must be from 0 to 100.")

        except ValueError:
            print("Please enter a number or 'done'.")


def calculate_average(grades):
    return sum(grades) / len(grades)


def get_highest(grades):
    return max(grades)


def get_lowest(grades):
    return min(grades)


def get_status(grades, passing_mark=75):
    return "PASSED" if calculate_average(grades) >= passing_mark else "FAILED"


def main():
    grades = []

    while True:
        print("\n1. Enter grades")
        print("2. View results")
        print("3. Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            grades = enter_grades()

        elif choice == "2":
            if not grades:
                print("No grades yet. Choose option 1 first.")
            else:
                print(f"Average: {calculate_average(grades):.2f}")
                print(f"Highest: {get_highest(grades):.2f}")
                print(f"Lowest: {get_lowest(grades):.2f}")
                print(f"Status: {get_status(grades)}")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid menu choice.")


if __name__ == "__main__":
    main()


# Local variables exist inside the function where they are created.
# For example, grades inside enter_grades is local to that function.
# A global variable is defined outside functions and can be accessed
# throughout the module. This program avoids needing a global grades
# variable by passing the list to functions as an argument.
