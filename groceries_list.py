import openpyxl #to be able to work with Excel
import csv #to be able to work with .csv

#Accessed the cells in meal plan
document = openpyxl.load_workbook("/Users/danyaramirez/Dropbox/Shared_Kyle_Danya/Food/Program/meal_plan.xlsx")
sheet =  document.get_sheet_by_name("current week")
many_cells = sheet["B1":"H47"]

#Create a list with all the foods in meal plan, even repeated ones.
all_foods = []
for row in many_cells:
    for cell in row:
        all_foods.append(cell.value)
#Eliminate the empty cells from the list of foods
rr = [x for x in all_foods if x is not None]

#Accessing the dictionary for amounts.
reader = csv.reader(open("/Users/danyaramirez/Dropbox/Shared_Kyle_Danya/Food/Program/meal_amounts.csv","r"))
d = {}#creating the dictionary
for row in reader:#telling python that in the file above the elements in a and b are a row,and that b is th evalue of the key a.
    a,b = row
    d[a] = float(b)

#Creating a dictionary 1: Count the instances of each item on the list (key) and add that number as a value.
instances_of_food = {}
for item in rr:
    count = rr.count(item)
    instances_of_food[item] = float(count)

#Creating a dictionary 2: The value is the total of number of incidences times the amounts.
total_per_food = {}
for item in instances_of_food:
    if item in d:
        total = instances_of_food[item] * d[item]
    else:
        total = instances_of_food[item] * 0
    total_per_food[item] = float(total)

#Accessing the dictionary for foods and units.
reader = csv.reader(open("/Users/danyaramirez/Dropbox/Shared_Kyle_Danya/Food/Program/meal_units.csv","r"))
units = {}#creating the dictionary
for row in reader:#telling python that in the file above the elements in a and b are a row,and that b is th evalue of the key a.
    a,b = row
    units[a] = b

#Creating a final list of foods
final_list = set(rr)
final_ordered = sorted(final_list)
# print final_ordered

#Printing one by one [foods, amounts and units] and export to .txt
file = open("/Users/danyaramirez/Dropbox/Shared_Kyle_Danya/Food/Program/shopping_list.txt","w")
for item in final_ordered:
    if item in units:
        print>>file, item + " - " + str(total_per_food[item])+ units[item]
    else:
        print>>file,str(item) + " is not in the data base"
