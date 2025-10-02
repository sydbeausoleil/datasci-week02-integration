# DataSci Week 02 Integration Project

## Project Overview

This project implements a basic and advanced data analysis workflow in Python as part of **Part 3: Python Data Processing** of the assignment.  
The goal is to process student grade data stored in CSV format and generate formatted reports with key statistics.

The repository demonstrates:
- Git workflow and branching
- CLI automation with `setup_project.sh`
- Python programming for data analysis

## Repository Structure
datasci-week02-integration/ ├── README.md ├── .gitignore ├── requirements.txt ├── setup_project.sh ├── src/ │ ├── data_analysis.py │ └── data_analysis_functions.py ├── data/ │ ├── students.csv │ └── courses.json └── output/ └── analysis_report.txt

## Features
- **Project Scaffold**: Automated project setup with `setup_project.sh`
- **Data Processing**: Python scripts for student grade analysis
- **Git Workflow**: Feature branch development and merging

## Usage
1. Run `./setup_project.sh` to create project structure.  
2. Execute `python src/data_analysis.py` for basic analysis 
3. Run `python src/data_analysis_functions.py` for advanced analysis (highest/lowest grades, subject counts, grade distribution).  

## Git Workflow
| Branch | Purpose | Status |
|--------|---------|--------|
| main | Production code | Active |
| feature/project-scaffold | CLI automation | Merged |
| feature/data-processing | Python analysis | Merged |