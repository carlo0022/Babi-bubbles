
def get_initial_readings():
    return [28, 31, 35, 37, 29]


def classify_reading(reading, warning_limit, critical_limit):
    if reading < warning_limit:
        return "NORMAL"
    elif reading <= critical_limit:
        return "WARNING"
    else:
        return "CRITICAL"


def add_reading(readings):
    new_reading = input("Enter new reading: ")

    if new_reading == "":
        print("Invalid input. The reading cannot be empty.")
        return readings

    try:
        value = int(new_reading)
    except ValueError:
        print("Invalid input. Enter a whole number only.")
        return readings

    if value < 0 or value > 100:
        print("Invalid reading. Enter a value from 0 to 100.")
        return readings

    readings.append(value)
    print("Reading added successfully.")
    return readings


def compute_total(readings):
    total = 0
    for reading in readings:
        total += reading
    return total


def compute_average(readings):
    if len(readings) == 0:
        return 0

    total = compute_total(readings)
    return total / len(readings)


def find_minimum(readings):
    if len(readings) == 0:
        return 0

    smallest = readings[0]
    for reading in readings:
        if reading < smallest:
            smallest = reading
    return smallest


def find_maximum(readings):
    if len(readings) == 0:
        return 0

    largest = readings[0]
    for reading in readings:
        if reading > largest:
            largest = reading
    return largest


def count_category(readings, warning_limit, critical_limit, category):
    count = 0

    for reading in readings:
        result = classify_reading(
            reading, warning_limit, critical_limit
        )
        if result == category:
            count += 1

    return count


def determine_overall_status(warning_count, critical_count):
    if critical_count >= 1:
        return "ATTENTION REQUIRED"
    elif warning_count >= 1:
        return "MONITOR"
    else:
        return "NORMAL"


def display_readings(readings):
    print("\nCURRENT READINGS")
    print("----------------")

    for index in range(len(readings)):
        print(f"Reading {index + 1}: {readings[index]} °C")


def display_classifications(readings):
    print("\nREADING CLASSIFICATION")
    print("----------------------")

    for reading in readings:
        category = classify_reading(reading, 30, 35)
        print(f"{reading} °C -> {category}")


def display_summary(readings):
    total_count = len(readings)
    total = compute_total(readings)
    average = compute_average(readings)
    minimum = find_minimum(readings)
    maximum = find_maximum(readings)

    normal_count = count_category(readings, 30, 35, "NORMAL")
    warning_count = count_category(readings, 30, 35, "WARNING")
    critical_count = count_category(readings, 30, 35, "CRITICAL")

    if total_count > 0:
        normal_percent = normal_count / total_count * 100
        warning_percent = warning_count / total_count * 100
        critical_percent = critical_count / total_count * 100
    else:
        normal_percent = 0
        warning_percent = 0
        critical_percent = 0

    status = determine_overall_status(
        warning_count, critical_count
    )

    print("\nMONITORING SUMMARY")
    print("------------------")
    print(f"Number of readings   : {total_count}")
    print(f"Total of readings    : {total}")
    print(f"Average temperature : {average:.2f} °C")
    print(f"Minimum temperature : {minimum} °C")
    print(f"Maximum temperature : {maximum} °C")

    print(f"\nNORMAL   : {normal_count} ({normal_percent:.2f}%)")
    print(f"WARNING  : {warning_count} ({warning_percent:.2f}%)")
    print(f"CRITICAL : {critical_count} ({critical_percent:.2f}%)")

    print(f"\nOverall Status: {status}")


def display_menu():
    print("\nSIMULATED DEVICE MONITORING SYSTEM")
    print("---------------------------------")
    print("[1] View Readings")
    print("[2] Add Reading")
    print("[3] Classify Readings")
    print("[4] Generate Summary")
    print("[5] Exit")


def main():
    readings = get_initial_readings()

    while True:
        display_menu()
        choice = input("\nEnter choice: ")

        if choice == "1":
            display_readings(readings)

        elif choice == "2":
            readings = add_reading(readings)

        elif choice == "3":
            display_classifications(readings)

        elif choice == "4":
            display_summary(readings)

        elif choice == "5":
            print("\nThank you for using the Device Monitoring System.")
            break

        else:
            print("\nInvalid choice. Please enter a number from 1 to 5.")


main()
