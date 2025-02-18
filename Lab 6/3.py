from datetime import date

date1 = (12, 5, 2025)  
date2 = (18, 2, 2025)  

date1_obj = date(date1[2], date1[1], date1[0])
date2_obj = date(date2[2], date2[1], date2[0])

day_difference = (date1_obj - date2_obj).days

print("Number of days between the two dates:", day_difference, "days")
