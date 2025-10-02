#!/usr/bin/env python3

import csv
import os

def load_data(filename):
    """Generic loader that checks file extension and calls CSV loader."""
    if filename.endswith(".csv"):
        return load_csv(filename)
    else:
        raise ValueError("Unsupported file format. Only CSV is supported.")

def load_csv(filename):
    """Load CSV data and return list of dictionaries."""
    students = []
    with open(filename, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            students.append(row)
    return students

def analyze_data(students):
    """Return dictionary with statistics: totals, averages, subject counts, distribution."""
    grades = [float(student["Grade"]) for student in students]

    total_students = len(students)
    average_grade = sum(grades) / total_students if total_students > 0 else 0
    highest_grade = max(grades) if grades else None
    lowest_grade = min(grades) if grades else None

    # Count students per subject
    subject_counts = {}
    for student in students:
        subject = student["Subject"]
        subject_counts[subject] = subject_counts.get(subject, 0) + 1

    # Grade distribution
    grade_distribution = analyze_grade_distribution(grades)

    return {
        "total_students": total_students,
        "average_grade": average_grade,
        "highest_grade": highest_grade,
        "lowest_grade": lowest_grade,
        "subject_counts": subject_counts,
        "grade_distribution": grade_distribution,
    }

def analyze_grade_distribution(grades):
    """Return dictionary of grade ranges with counts and percentages."""
    distribution = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for g in grades:
        if g >= 90:
            distribution["A"] += 1
        elif g >= 80:
            distribution["B"] += 1
        elif g >= 70:
            distribution["C"] += 1
        elif g >= 60:
            distribution["D"] += 1
        else:
            distribution["F"] += 1

    total = len(grades)
    if total > 0:
        for letter in distribution:
            distribution[letter] = {
                "count": distribution[letter],
                "percent": distribution[letter] / total * 100
            }
    return distribution

def save_results(results, filename):
    """Save detailed report to text file."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write("Analysis Report\n")
        f.write("====================\n")
        f.write(f"Total students: {results['total_students']}\n")
        f.write(f"Average grade: {results['average_grade']:.1f}\n")
        f.write(f"Highest grade: {results['highest_grade']}\n")
        f.write(f"Lowest grade: {results['lowest_grade']}\n\n")

        f.write("Subject Counts:\n")
        for subject, count in results["subject_counts"].items():
            f.write(f"  {subject}: {count}\n")
        f.write("\n")

        f.write("Grade Distribution:\n")
        for grade, data in results["grade_distribution"].items():
            f.write(f"  {grade}: {data['count']} ({data['percent']:.1f}%)\n")

def main():
    input_file = "data/students.csv"    # Adjust path if needed
    output_file = "output/analysis_report.txt"

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    students = load_data(input_file)
    results = analyze_data(students)
    save_results(results, output_file)
    print(f"Analysis complete. Report saved to {output_file}")

if __name__ == "__main__":
    main()