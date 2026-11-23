
# Name: IAN GEOFREY P. SANGALANG | Section: IV-BSIT B | Activity: P2 | Date: 2026-11-23

import student_utils
from student_utils import average
from datetime import datetime


def main():
    grades = []

    print("Enter grades from 0 to 100. Type done to finish.")

    while True:
        value = input("Grade: ").strip()

        if value.lower() == "done":
            break

        try:
            grade = float(value)

            if 0 <= grade <= 100:
                grades.append(grade)
            else:
                print("Grade must be from 0 to 100.")

        except ValueError:
            print("Enter a valid number.")

    if not grades:
        print("No grades entered.")
        return

    print("\nSTUDENT REPORT")
    print("Generated:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print(f"Average: {average(grades):.2f}")
    print("Highest:", student_utils.highest(grades))
    print("Lowest:", student_utils.lowest(grades))
    print("Status:", "PASSED" if student_utils.passed(grades) else "FAILED")


if __name__ == "__main__":
    main()
