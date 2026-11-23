
# Name: IAN GEOFREY P. SANGALANG | Section: IV-BSIT B | Activity: P2 | Date: 2026-11-23

def average(grades):
    return sum(grades) / len(grades) if grades else 0


def passed(grades, passing_mark=75):
    return average(grades) >= passing_mark


def highest(grades):
    return max(grades)


def lowest(grades):
    return min(grades)
