import calendar
yy = int(input("Enter the year:"))
mm = int(input("Enter the month:"))

# For single month
print(calendar.month(yy,mm))

# For whole year 
print(calendar.calendar(yy))