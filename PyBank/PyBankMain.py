import os
import csv

pybank_path = os.path.join(".", "budget_data_1.csv")

#creating a list for months and revenue from the csv
month_data = []
revenue_data = []
revenue_change = []

#importing the csv to a csvreader in order to add the information to the blank lists
with open(pybank_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #print(csvreader)
    for row in csvreader:
        if str(row[0]) != "Date":
            month_data.append(row[0])
            #print(month_data)

        if str(row[1]) != "Revenue":
            revenue_data.append(int(row[1]))
            #print(revenue_data)

print("Financial Analysis")
print("-------------------------------------------------")
print(" ")

# identify total number of months by counting the total number of rows
number_of_months = len(month_data)
print("Total Months: " + str(number_of_months))

# sum of all revenues
revenue_sum = sum(revenue_data)
print("Total Revenue: " + str(revenue_sum))

# average change in revenue between months
index = 0
for i in range(len(revenue_data)-1):
    revenue_change.append(revenue_data[index+1] - revenue_data[index])
    index = index + 1
average_change = round((sum(revenue_change) / number_of_months),2)

print("Average Revenue Change: $" + str(average_change))

#greatest increase of revenue change
greatest_increase = max(revenue_change)

#identify the position in the average_change list where the greatest increase of revenue change occurred
#print(revenue_change.index(greatest_increase))

#once you have the position it occurred, you can apply it's position to the month_data list to acquire the date it occurred
greatest_increase_date = month_data[revenue_change.index(greatest_increase)]
print("Greatest Increase in Revenue: " + str(greatest_increase_date) + " (" + str(greatest_increase) + ")")


#greatest decrease of revenue change
#can use same method as the greatest increase of revenue
greatest_decrease = min(revenue_change)
#print(revenue_change.index(greatest_decrease))
greatest_decrease_date = month_data[revenue_change.index(greatest_decrease)]
print("Greatest Decrease in Revenue: " + str(greatest_decrease_date) + " (" + str(greatest_decrease) + ")")

### I had difficulty trying to export the PyBank information onto a text file
"""file = open("PyBank_Main_Text.txt", "w")

file.write("Financial Analysis")
file.write("--------------------------------------")
file.write(" ")
file.write("Total Months: " + str(number_of_months)
file.write("Total Revenue: " + str(revenue_sum))
file.write("Average Revenue Change: $" + str(average_change))
file.write("Greatest Increase in Revenue: " + str(greatest_increase_date) + " (" + str(greatest_increase) + ")")
file.write("Greatest Decrease in Revenue: " + str(greatest_decrease_date) + " (" + str(greatest_decrease) + ")")
file.close()"""