# Lab overview

This lab is about understanding the `lambda` function and making the code become **Object-Oriented**.


## Project Structure

This is the structure of this project

- **`oop_lab_1/`**: Contains every file for this program
	- **`README.md`**: # This file
	- **`Cities.csv`**: # The dataset
	- **`data_processing.py`**: # The analysis code


## Design Overview

This program is built to **load and analyze CSV data** using two main classes: `DataLoader` and `Table`.  
It supports data loading, filtering, and aggregation in a modular, object-oriented structure.

---

### **1. Class: `DataLoader`**

#### **Purpose**
Handles reading CSV files and converting them into Python data structures for analysis.

#### **Attributes**
- **`base_path`** *(Path)* – Base directory where CSV files are stored. Defaults to the current script location.

#### **Key Methods**
- **`__init__(self, base_path=None)`** – Initializes with an optional base path.  
- **`load_csv(self, filename)`** – Reads a CSV file and returns a list of dictionaries, one per row.

**Example:**
```python
loader = DataLoader()
data = loader.load_csv('Cities.csv')
```

---

### **2. Class: `Table`**

### **Overview**
The `Table` class represents a dataset loaded from a CSV file (or any list of dictionaries).  
It provides simple, reusable methods for **filtering** and **aggregating** data, allowing users to perform analysis without external libraries.

---

### **Attributes**

- **`table_name`** *(str)*  
	The name or label of the dataset (e.g., `"cities"`).  
	Useful for identifying tables when handling multiple datasets.

- **`table`** *(list)*  
	The main data structure — a list of dictionaries, where each dictionary represents a row.  
	Example:
	```python
	[
	    {"city": "Berlin", "country": "Germany", "temperature": "13.5"},
	    {"city": "Madrid", "country": "Spain", "temperature": "14.2"}
	]


# How to test and run your code

To run the program, execute `data_processing.py`:

```python
python data_processing.py
```
