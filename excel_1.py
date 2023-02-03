# import the required library 

import xlsxwriter

book = xlsxwriter.Workbook("MyWorkBook.xlsx")

sheet = book.add_worksheet()

# rows and columns are zero indexed 

row,column =0,0

content = ["Java","Python","JavaScript"]

# iterating through the content list 

for item in content:
    # write operation perform
    sheet.write(row,column,item)

    # incrementing the value of row by one with each iterations
    row+=1

book.close() # close the book

print("Content successfully written in excel file")
