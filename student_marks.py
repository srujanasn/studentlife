"""Collect a student's subject marks and display their results."""


def read_mark(subject: str) -> float:
    """Read a mark from 0 to 100, repeating until the input is valid."""
    while True:
        try:
            mark = float(input(f"Enter marks for {subject} (0-100): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if 0 <= mark <= 100:
            return mark
        print("Marks must be between 0 and 100.")


def grade_for(average: float) -> str:
    if average >= 90:
        return "A"
    if average >= 80:
        return "B"
    if average >= 70:
        return "C"
    if average >= 60:
        return "D"
    return "F"


def main() -> None:
    student_name = input("Enter the student's name: ").strip()
    while not student_name:
        print("The student's name cannot be empty.")
        student_name = input("Enter the student's name: ").strip()

    while True:
        try:
            subject_count = int(input("Enter the number of subjects: "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        if subject_count > 0:
            break
        print("Enter at least one subject.")

    marks = []
    for number in range(1, subject_count + 1):
        subject = input(f"Enter the name of subject {number}: ").strip()
        while not subject:
            print("The subject name cannot be empty.")
            subject = input(f"Enter the name of subject {number}: ").strip()
        marks.append(read_mark(subject))

    total = sum(marks)
    average = total / subject_count

    print(f"\nResults for {student_name}")
    print(f"Total marks: {total:g} / {subject_count * 100}")
    print(f"Average: {average:.2f}%")
    print(f"Grade: {grade_for(average)}")


if __name__ == "__main__":
    main()