
# Name: IAN GEOFREY P. SANGALANG | Section: IV-BSIT B | Activity: P4 | Date: 2026-11-23

def divide_numbers():
    try:
        first = float(input("First number: "))
        second = float(input("Second number: "))

        result = first / second

    except ValueError:
        print("Error: enter numeric values only.")

    except ZeroDivisionError:
        print("Error: cannot divide by zero.")

    else:
        print("Result:", result)

    finally:
        print("Division operation finished.")


def read_file():
    filename = input("File name to open: ").strip()

    try:
        with open(filename, "r", encoding="utf-8") as file:
            contents = file.read()

    except FileNotFoundError:
        print("Error: that file does not exist.")

    except OSError as error:
        print("File error:", error)

    else:
        print("--- File contents ---")
        print(contents)

    finally:
        print("File operation finished.")


def main():
    while True:
        print("\n1. Divide numbers")
        print("2. Open a text file")
        print("3. Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            divide_numbers()

        elif choice == "2":
            read_file()

        elif choice == "3":
            print("Goodbye.")
            break

        else:
            print("Invalid menu choice. Select 1, 2, or 3.")


if __name__ == "__main__":
    main()
