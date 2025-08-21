# Run Python Workflow Example

This repository demonstrates how to use **GitHub Actions runners** to execute a Python script.  
It’s a minimal example designed for data engineers who want to integrate data across platforms without needing to set up servers or heavy orchestration tools.

## What This Repo Does

- Uses a GitHub Actions workflow (`.github/workflows/run-script.yml`) to run a Python script (`test.py`).
- The script fetches the latest public events from the GitHub API and writes them into a CSV file using **pandas**.
- Every run generates a timestamped CSV file (e.g., `github_events_20250818_120301.csv`).

## Repository Structure

RunPythonWorkflow/
├── test.py # Example Python script
├── requirements.txt # Python dependencies
└── .github/
└── workflows/
└── run-script.yml # Workflow definition

## Running Locally

pip install -r requirements.txt
python test.py
