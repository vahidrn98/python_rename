import xlrd
import os

file_name = input("please enter file name!")

wb = xlrd.open_workbook(file_name)

image_col_name = input("please enter image column name")

isbn_col_name = input("please enter isbn column name")

image_col_index = 0

isbn_col_index = 0

sheet= wb.sheet_by_index(0)

for i in range(0,sheet.ncols):
    if(image_col_name==sheet.cell_value(0,i)):
        image_col_index = i
        break

for i in range(0,sheet.ncols):
    if(isbn_col_name==sheet.cell_value(0,i)):
        isbn_col_index = i
        break

for i in range(0,sheet.nrows):
    print(sheet.cell_value(i,image_col_index).strip()+'.jpg')
    if(os.path.exists(sheet.cell_value(i,image_col_index).strip()+'.jpg')):
        os.rename(sheet.cell_value(i,image_col_index).strip()+'.jpg',sheet.cell_value(i,isbn_col_index).strip()+'.jpg')
    if(os.path.exists(sheet.cell_value(i,image_col_index).strip()+'.png')):
        os.rename(sheet.cell_value(i,image_col_index).strip()+'.png',sheet.cell_value(i,isbn_col_index).strip()+'.png')

print(image_col_index);
print(isbn_col_index);

