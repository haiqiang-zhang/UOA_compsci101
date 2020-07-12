number_of_minutes = 65601
minutes_per_hour = 60
hours_per_day = 24
day = number_of_minutes // (minutes_per_hour * hours_per_day)
hour = (number_of_minutes % (minutes_per_hour * hours_per_day)) // minutes_per_hour
minute = ((number_of_minutes % (minutes_per_hour * hours_per_day)) % minutes_per_hour)
print(number_of_minutes,"minutes =",day,"days,",hour,"hours and",minute,"minutes")
