import calendar

def birthday_calendar():
    month = int(input("Enter your birthday month (1-12): "))
    year = int(input("Enter your birthday year (e.g., 1995): "))
    
    if month < 1 or month > 12:
        print("Invalid month! Please enter a number between 1 and 12.")
        return
    
    print(f"\nHere is the calendar for {calendar.month_name[month]} {year}:\n")
    print(calendar.month(year, month))

birthday_calendar()