import calendar

print(calendar.calendar(2026))

cal = calendar.HTMLCalendar(calendar.SUNDAY)
print(cal.formatmonth(2026, 9))