import xlrd
import os
import shutil 
  
# change dest and source to you own directory
# don't forget to put '/' at the end of dest
dest = ''

source=''

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
    #these two if statements are here to copy the renamed files (from source) to a new filder (dest)
    # so basically you have to run this twice :D
    if(sheet.cell_value(i,isbn_col_index).strip()!="" and os.path.exists(sheet.cell_value(i,isbn_col_index).strip()+'.jpg')):
        shutil.copyfile(sheet.cell_value(i,isbn_col_index).strip()+'.jpg', dest+"".join(i for i in (sheet.cell_value(i,isbn_col_index).strip()) if i.isdigit())+'.jpg')
    if(sheet.cell_value(i,isbn_col_index).strip()!="" and os.path.exists(sheet.cell_value(i,isbn_col_index).strip()+'.png')):
        shutil.copyfile(sheet.cell_value(i,isbn_col_index).strip()+'.jpg', dest+"".join(i for i in (sheet.cell_value(i,isbn_col_index).strip()) if i.isdigit())+'.png')
    if(os.path.exists(sheet.cell_value(i,image_col_index)+'.jpg' and sheet.cell_value(i,image_col_index).strip()!='') and not os.path.exists(sheet.cell_value(i,isbn_col_index).strip()+'.jpg')):
        os.rename(sheet.cell_value(i,image_col_index).strip()+'.jpg',sheet.cell_value(i,isbn_col_index).strip().replace('/','')+'.jpg')
    if(os.path.exists(sheet.cell_value(i,image_col_index)+'.png' and sheet.cell_value(i,image_col_index).strip()!='') and not os.path.exists(sheet.cell_value(i,isbn_col_index).strip()+'.png')):
        os.rename(sheet.cell_value(i,image_col_index).strip()+'.png',sheet.cell_value(i,isbn_col_index).strip().replace('/','')+'.png')



