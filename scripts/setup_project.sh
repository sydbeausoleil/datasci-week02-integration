#!/bin/bash
#This script is meant to scaffold a Python project by creating directories, initial files, and placeholders.

# TODO: Create directories: src, data, output

# TODO: Create .gitignore and include common Python ignores

# TODO: Create students.csv with data (name, age, grade, subject)

# TODO: Create Python template files with TODO comments
echo "Setting up project structure..."

mkdir src data output
echo "Created directories: src, data, output"

cat > output/.gitignore << 'EOF'
__pycache__/
*.pyc
.env
*.pyo
*.swp
.env
.venv
EOF
echo "Created output/.gitignore"

cat > output/requirements.txt << 'EOF'
pytest>=7.0.0
EOF
echo "Created output/requirements.txt"

cat > data/students.csv << 'EOF'
name,age,grade,subject
Alice,20,85,Math
Bob,19,92,Science
Charlie,21,78,English
Diana,20,88,Math
Eve,22,95,Science
Frank,19,82,History
Grace,21,91,Math
Henry,20,76,Science
EOF
echo "Created sample data file at data/students.csv"

cat > src/data_analysis.py << 'EOF'
#!/usr/bin/env python3
"""Basic Data Analysis Script"""
def load_students(filename):
    """Load student data from CSV."""
    # TODO: Open file, read lines, skip header
    # TODO: Split each line by comma
    # TODO: Return list of student data
    pass
def calculate_average_grade(students):
    """Calculate average grade."""
    # TODO: Sum all grades
    # TODO: Divide by number of students
    pass

def count_math_students(students):
    """Count students in Math."""
    # TODO: Count students where subject is Math
    pass

def generate_report(total, average, math_count):
    """Generate report string."""
    # TODO: Create formatted string with results
    # TODO: Use f-strings with .1f for decimals
    pass

def save_report(report, filename):
    """Save report to file."""
    # TODO: Create output directory if needed
    # TODO: Write report to file
    pass

def main():
    # TODO: Load data
    # TODO: Calculate statistics
    # TODO: Generate and save report
    pass

if __name__ == "__main__":
    main()
EOF
echo "Created src/data_analysis.py"

cat > src/data_analysis_functions.py << 'EOF'
#!/usr/bin/env python3
"""Basic Data Analysis Script"""

def load_students(filename):
    """Load student data from CSV."""
    # TODO: Open file, read lines, skip header
    # TODO: Split each line by comma
    # TODO: Return list of student data
    pass

def calculate_average_grade(students):
    """Calculate average grade."""
    # TODO: Sum all grades
    # TODO: Divide by number of students
    pass

def count_math_students(students):
    """Count students in Math."""
    # TODO: Count students where subject is Math
    pass

def generate_report(total, average, math_count):
    """Generate report string."""
    # TODO: Create formatted string with results
    # TODO: Use f-strings with .1f for decimals
    pass

def save_report(report, filename):
    """Save report to file."""
    # TODO: Create output directory if needed
    # TODO: Write report to file
    pass

def main():
    # TODO: Load data
    # TODO: Calculate statistics
    # TODO: Generate and save report
    pass

if __name__ == "__main__":
    main()
EOF
echo "Created src/data_analysis_functions.py"


chmod +x setup_project.sh

echo "Project setup complete."