# OOP Lab 1 — CSV Data Processing

## Lab Overview
This lab demonstrates loading, processing, and aggregating CSV data using a small object-oriented design. The goal is to encapsulate CSV I/O and table-style data operations into reusable classes so that data analysis tasks are easier to test and extend.

## Project Structure
- **`oop_lab_1/`**: Contains every file for this program
    - **`README.md`**: # This file
    - **`Cities.csv`**: # Cities dataset
	- **`Countries.csv`**: # Countries dataset
    - **`data_processing.py`**: # The data formating code
    - **`result.txt`**: # Where the results are written to

## Design Overview
This project centers on two primary classes defined in [oop_lab_1/data_processing.py](data_processing.py):

- [`DataLoader`](data_processing.py)
  - Purpose: Read CSV files and convert them into a list-of-dictionaries representation.
  - Key attributes:
    - `base_path` (Path) — optional base directory for dataset files.
  - Key methods:
    - [`DataLoader.__init__`](data_processing.py) — Initialize loader with optional base path.
    - [`DataLoader.load_csv`](data_processing.py) — Read a CSV file and return `List[Dict[str, str]]`. Handles header parsing and basic trimming.
    - (Optional) utility methods for safe type conversion or filtering while loading.

- [`Table`](data_processing.py)
  - Purpose: Provide table-like operations (filtering, projection, aggregation) on the loaded data.
  - Key attributes:
    - `rows` (List[Dict[str, Any]]) — current table rows.
    - `columns` (List[str]) — detected column names (from CSV header).
  - Key methods:
    - [`Table.filter`](data_processing.py) — Return a new `Table` with rows matching a predicate or simple condition (e.g., column == value).
    - [`Table.select`](data_processing.py) — Project a subset of columns.
    - [`Table.aggregate`](data_processing.py) — Compute aggregations (sum, mean, count) grouped by column(s).
    - [`Table.to_text`](data_processing.py) — Serialize results to a human-readable string (used to write to [oop_lab_1/result.txt](result.txt)).

Note: See [oop_lab_1/data_processing.py](data_processing.py) for the exact method signatures and any additional helper classes or functions.

## How to run and test
1. Ensure you are in the lab folder:
   ```sh
   cd d:\KU_SKE\Y1S1\com_prog1\oop_lab_1
