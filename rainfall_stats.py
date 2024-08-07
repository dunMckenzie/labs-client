# Program:       rainfall_stats.py
# Programmer:    Lorenzo Openito
# Date:          07/08/2024
# Description:   Calculate average monthly rainfall and summary statistics

# declare and initialize list of months abbreviated starting with jan
months_short = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]

# declare and initialize list of months not abbreviated starting with January
months_long = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]

# declare and initialize list of inches of rainfall parallel to months of year
inches = [1.9, 2.37, 3.06, 3.20, 5.15, 3.23, 2.12, 2.03, 2.42, 4.11, 2.57, 2.57]

# use sum function to find the total rainfall and assign to total variable
total_rainfall = sum(inches)

# divide total rainfall by len function of list and assign to average variable
average_rainfall = total_rainfall / len(inches)

# find driest month name and inches
driest_month_index = inches.index(min(inches))
driest_month_name = months_long[driest_month_index]
driest_month_inches = inches[driest_month_index]

# find wettest month name and inches
wettest_month_index = inches.index(max(inches))
wettest_month_name = months_long[wettest_month_index]
wettest_month_inches = inches[wettest_month_index]

# print report header – Average Monthly Rainfall
print("Average Monthly Rainfall 2018 Dallas, TX\n")

# use for loop with the range function – pass len of month list
for i in range(len(months_short)):
    # print month and average rainfall by accessing temporary variable
    print(f"{months_short[i]:<10}{inches[i]:>20.2f}")

# print credit line showing source of data
print("\n Source: wwww.rssweather.com \n")

# display total and average rainfall for year
print(f"Total rainfall for the year:     {total_rainfall:.2f} inches")
print(f"Average monthly rainfall:         {average_rainfall:.2f} inches")

# display driest and wettest month statement
print(f"The driest month in Dallas Fort Worth  {driest_month_name.capitalize()} with {driest_month_inches:.2f} inches of precipitation, and with {wettest_month_inches:.2f} inches {wettest_month_name.capitalize()} is the wettest month ")

