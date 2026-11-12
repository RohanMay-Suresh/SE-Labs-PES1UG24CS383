import re

RATES = {"bike": 10, "car": 30, "truck": 60}

# HH:MM-HH:MM, ASCII digits only (int() would also accept other Unicode digits)
TIMES_PATTERN = re.compile(r"([0-9]{1,2}):([0-9]{2})-([0-9]{1,2}):([0-9]{2})")
# Indian plate, e.g. KA01AB1234: state, district, series, number
PLATE_PATTERN = re.compile(r"([A-Za-z]{2})([0-9]{2})([A-Za-z]{2})([0-9]{4})")

def minutes_parked(times):
    if not isinstance(times, str):
        return None
    match = TIMES_PATTERN.fullmatch(times.strip())
    if not match:
        return None
    h1, m1, h2, m2 = (int(g) for g in match.groups())
    if h1 > 23 or h2 > 23 or m1 > 59 or m2 > 59:
        return None
    duration = (h2 * 60 + m2) - (h1 * 60 + m1)
    if duration < 0:
        return None
    return duration

def hourly_rate(vehicle):
    if not isinstance(vehicle, str):
        return None
    return RATES.get(vehicle.strip().lower())

def format_plate(plate):
    if not isinstance(plate, str):
        return None
    match = PLATE_PATTERN.fullmatch(plate.strip())
    if not match:
        return None
    return " ".join(match.groups()).upper()

def main():
    print("==== Running minutes_parked ====")
    user_input = input("Enter entry and exit time (e.g. 09:30-11:45): ")
    result = minutes_parked(user_input)
    print("Minutes Parked:", result if result is not None else "Invalid time range")

    print("\n==== Running hourly_rate ====")
    user_input = input("Enter vehicle type (bike/car/truck): ")
    result = hourly_rate(user_input)
    print("Hourly Rate:", result if result is not None else "Unknown vehicle type")

    print("\n==== Running format_plate ====")
    user_input = input("Enter a number plate (e.g. ka01ab1234): ")
    result = format_plate(user_input)
    print("Formatted Plate:", result if result is not None else "Invalid number plate")

if __name__ == "__main__":
    main()
