import openpyxl #to be able to work with Excel
import csv #to be able to work with .csv
import os #to be able to find the files in the current folder

#Location of THIS file is dir_path
dir_path = os.path.dirname(os.path.realpath(__file__))

#Accessed the cells in meal plan
document = openpyxl.load_workbook(dir_path + "/meal_plan.xlsx")
sheet =  document.get_sheet_by_name("current week")
many_cells = sheet["B1":"H47"]

#Create a list with all the foods in meal plan, even repeated ones.
all_foods = []
for row in many_cells:
    for cell in row:
        all_foods.append(cell.value)
#Eliminate the empty cells from the list of foods
rr = [x for x in all_foods if x is not None]

#Creating a final list of foods
final_list = set(rr)
final_ordered = sorted(final_list)

# Creating a dictionary 1: Count the instances of each item on the list (key) and add that number as a value.
instances_of_food = {}
for item in final_ordered:
    count = final_ordered.count(item)
    instances_of_food[item] = float(count)

# Accessing the file for amounts.
reader = csv.reader(open(dir_path + "/dictionary.csv","Ur"))
for row in reader:
    d = dict((rows[0],float(rows[2])) for rows in reader)

# Creating a dictionary 2: The value is the total of number of incidences times the amounts.
total_per_food = {}
for item in instances_of_food:
    if item in d:
        total = instances_of_food[item] * d[item]
    else:
        total = instances_of_food[item] * 0
    total_per_food[item] = float(total)


# Accessing the dictionary for foods and units.
reader = csv.reader(open(dir_path + "/dictionary.csv","Ur"))
units = {}
for row in reader:
     units = dict((rows[0],rows[1]) for rows in reader)

#Accessing the dictionary for shopping rules.
reader = csv.reader(open(dir_path + "/dictionary.csv","Ur"))
rules = {}
for row in reader:
    rules = dict((rows[0],rows[3]) for rows in reader)

# Printing one by one [food, amount, unit and rule] and export to .txt
file = open(dir_path + "/shopping_list.txt","w")
for item in final_ordered:
    if item in units:
        print>>file, str(item) + " - " + str(total_per_food[item])+ " " + units[item] + "\n" + rules[item] + "\n"
    else:
        print>>file,str(item) + " is not in the database" + "\n"
