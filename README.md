# Week 17: Simulated Device Monitoring and Alert System

## 1. Project Description
This Python program simulates a device temperature monitoring system. It stores temperature readings, accepts new readings, classifies temperatures, and displays a summary.

## 2. Objectives
- Practice using functions, loops, lists, and conditional statements.
- Validate user input.
- Classify temperature readings.
- Calculate summary statistics using manual loops.

## 3. Initial Data
The initial readings are `[28, 31, 35, 37, 29]`.

## 4. Classification Rules
- Below 30 °C: NORMAL
- 30 °C to 35 °C, inclusive: WARNING
- Above 35 °C: CRITICAL

Only whole numbers from 0 to 100 are accepted.

## 5. Main Menu
1. View Readings
2. Add Reading
3. Classify Readings
4. Generate Summary
5. Exit

## 6. Program Features
- View all recorded readings.
- Add a valid temperature reading.
- Classify readings into three categories.
- Generate a monitoring summary.
- Exit the program.

## 7. Input Validation
The program rejects empty input, non-numeric input, decimal numbers, negative values, and values greater than 100.

## 8. Summary Calculations
The program calculates the total, average, minimum, maximum, category counts, and category percentages. It uses loops to calculate the total, minimum, and maximum instead of the built-in `sum()`, `min()`, and `max()` functions.

## 9. Overall Status
- If at least one CRITICAL reading exists: ATTENTION REQUIRED
- Otherwise, if at least one WARNING reading exists: MONITOR
- Otherwise: NORMAL

## 10. Functions
The program uses functions for initial readings, input validation, classification, calculations, counting categories, displaying results, and controlling the main menu.

## 11. Expected Initial Summary
- Number of readings: 5
- Total: 160
- Average: 32.00 °C
- Minimum: 28 °C
- Maximum: 37 °C
- NORMAL: 2 (40.00%)
- WARNING: 2 (40.00%)
- CRITICAL: 1 (20.00%)
- Overall status: ATTENTION REQUIRED

## 12. How to Run
1. Install Python 3.
2. Save the program as `device_monitor.py`.
3. Open a terminal in the project folder.
4. Run `python device_monitor.py`.
5. Select a menu option and follow the prompts.

## Project Files
- `device_monitor.py` — Python program
- `README.md` — Project documentation
- `test_cases.md` — Test cases and results
