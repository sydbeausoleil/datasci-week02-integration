#!/usr/bin/env python3
"""Basic analysis script for student grades."""

from pathlib import Path

def load_students(filename="data/students.csv"):
    """Read CSV and return list of student data as tuples (name, subject, grade)."""
    students = []
    with open(filename, "r") as f:
        lines = f.readlines()[1:]  # skip header
        for line in lines:
            parts = line.strip().split(",")
            if len(parts) < 3:
                continue
            try:
                grade = int(parts[2].strip())
            except ValueError:
                continue
            name = parts[0].strip()
            subject = parts[1].strip()
            students.append((name, subject, grade))
    return students

"""Enact Required Functions for Analysis"""
def calculate_average_grade(students):
    grades = [g for _, _, g in students]
    return sum(grades) / len(grades) if grades else 0

def count_math_students(students):
    return sum(1 for _, subject, _ in students if subject.lower() == "math")

def generate_report(students):
    total = len(students)
    average = calculate_average_grade(students)
    math_count = count_math_students(students)
    return (
        f"Total students: {total}\n"
        f"Average grade: {average:.1f}\n"
        f"Math students: {math_count}\n"
    )

def save_report(report, filename="output/analysis_report.txt"):
    out_path = Path(filename)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(report, encoding="utf-8")

def main():
    students = load_students("data/students.csv")
    report = generate_report(students)
    save_report(report, "output/analysis_report.txt")
    print(report)

if __name__ == "__main__":
    main()
