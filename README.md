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
This repository defines three main classes in `data_processing.py`. Descriptions below match the current code (no other methods such as `select` or `to_text` are implemented).

- DataLoader
  - Purpose: Read CSV files into memory.
  - Attributes:
    - `base_path` (Path) — directory used to resolve filenames (defaults to the script directory).
  - Methods:
    - `__init__(base_path=None)` — set the base path.
    - `load_csv(filename)` — return a `list[dict]` by reading the named CSV file with `csv.DictReader`.

- DB
  - Purpose: Simple in-memory container for named Table objects.
  - Attributes:
    - `database` (dict) — mapping from `table.table_name` to `Table` instances.
  - Methods:
    - `__init__()` — initialize empty database.
    - `insert(table)` — store a `Table` using its `table_name` as key.
    - `search(table_name)` — retrieve a `Table` by name (returns `None` if not found).

- Table
  - Purpose: Hold rows (list of dicts) and provide basic operations.
  - Attributes:
    - `table_name` (str) — optional name for the table.
    - `table` (list[dict]) — the rows of the table.
  - Methods:
    - `__init__(table_name='', table=[])` — create a Table with given name and rows.
    - `__str__()` — string representation: "name:rows".
    - `filter(condition)` — returns a new `Table` containing rows for which `condition(row)` is truthy.
    - `aggregate(aggregation_function, aggregation_key)` — builds a list of values for `aggregation_key` (attempting float conversion; falls back to raw value on ValueError) and applies `aggregation_function` to that list, returning the result.
    - `join(other_table, key)` — for each row in this table, finds the first matching row in `other_table` where `row[key] == other_row[key]`, merges `other_row` into `row` (using `dict.update`) and returns a new `Table` with the merged rows.
  - Notes:
    - `join` mutates the matched rows by calling `update` on them before returning the new Table's rows.
    - There is no `select` or `to_text` method in the current implementation.

## How to run and test
```bash
python data_processing.ppy
