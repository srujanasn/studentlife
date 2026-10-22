"""Collect marks for five students and report their grades.

Run the boundary-value tests with: python studentf_marks.py --test
"""

import sys
import unittest


STUDENT_COUNT = 5


def grade_for(mark: float) -> str:
    """Return the grade for a mark from 0 to 100."""
    if mark >= 90:
        return "A"
    if mark >= 80:
        return "B"
    if mark >= 70:
        return "C"
    if mark >= 60:
        return "D"
    return "F"


def read_mark(student_number: int) -> float:
    """Prompt repeatedly until a valid mark between 0 and 100 is entered."""
    while True:
        try:
            mark = float(input(f"Enter marks for student {student_number} (0-100): "))
        except ValueError:
            print("Invalid input. Enter a number between 0 and 100.")
            continue

        if 0 <= mark <= 100:
            return mark
        print("Invalid mark. Marks must be between 0 and 100.")


def display_report(marks: list[float]) -> None:
    """Print a neatly aligned report with each student's grade."""
    print("\nStudent Marks Report")
    print("-" * 32)
    print(f"{'Student':<12}{'Mark':>8}{'Grade':>10}")
    print("-" * 32)

    for number, mark in enumerate(marks, start=1):
        print(f"{number:<12}{mark:>8.2f}{grade_for(mark):>10}")

    print("-" * 32)


def main() -> None:
    """Read five marks and display their report."""
    marks = [read_mark(number) for number in range(1, STUDENT_COUNT + 1)]
    display_report(marks)


class GradeBoundaryTests(unittest.TestCase):
    """Check the grade at and immediately below each threshold."""

    def test_grade_boundaries(self) -> None:
        # Each threshold receives its higher grade; just below receives the next.
        cases = [
            (100, "A"),
            (90, "A"),
            (89.99, "B"),
            (80, "B"),
            (79.99, "C"),
            (70, "C"),
            (69.99, "D"),
            (60, "D"),
            (59.99, "F"),
            (0, "F"),
        ]
        for mark, expected_grade in cases:
            with self.subTest(mark=mark):
                self.assertEqual(grade_for(mark), expected_grade)


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "--test":
        unittest.main(argv=[sys.argv[0]])
    else:
        main()