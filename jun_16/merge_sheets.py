#! /usr/bin/env python

'''
This is a program that merges two excel workbooks based on chromosomal
positions. Three arguments: python code, filtered excel sheet, vcf-query sheet

Note! Remember that one cannot write too many rows to an excel sheet (there
is a limit). 
'''

import sys
import os
import pdb
import xlrd
import xlwt


#Functions

def merge_sheets(sheet_1, sheet_2, name):
    '''A functions that takes two xl-sheets
    as input and merges them based on chromosomal
    positions.
    Input: sheet_1 (the filtered sheet), sheet_2 (the vcf-query sheet), name
    Output: None
    '''
    
    #Create an excel workbook and a sheet to write to
    workbook_w = xlwt.Workbook()
    sheet_w = workbook_w.add_sheet('Sheet_1')
    

    row_1 = 0 #Row to match in sheet_1
    row_2 = 0 #Row to match in sheet_2
    row_n = 0 #To keep track of which row to write to
    write_to_sheet(row_1, row_2, sheet_w, sheet_1, sheet_2, row_n)
    
    for row_1 in range(1, sheet_1.nrows):
        #Convert cell in sheet 1 to string in order to encode it to ascii
        sheet_1_cell = str(sheet_1.cell(row_1, 1).value)
        sheet_1_cell = sheet_1_cell.encode('ascii','ignore')

        for row_2 in range(1, sheet_2.nrows):
            #Convert cell in sheet 2 to string in order to encode it to ascii
            sheet_2_cell = str(sheet_2.cell(row_2, 1).value)
            sheet_2_cell = sheet_2_cell.encode('ascii','ignore')
            
            if float(sheet_1_cell) == float(sheet_2_cell):
                row_n += 1
                write_to_sheet(row_1, row_2, sheet_w, sheet_1, sheet_2, row_n)              

    workbook_w.save('merged_'+name)

    return None

def write_to_sheet(row_1, row_2, sheet_w, sheet_1, sheet_2, row_n):
    '''A function that writes data into a sheet in the excel workbook.
    Input: row_1, row_2, sheet_w, sheet_1, sheet_2, row_n 
    Output: None
    '''
    
    col_n = 0 #To keep track of which column to write to
    
    #Iterate over all columns
    for col_idx in range(0, sheet_1.ncols):
        sheet_1_cell = str(sheet_1.cell(row_1, col_idx).value)
        sheet_1_cell = sheet_1_cell.encode('ascii','ignore')
        sheet_w.write(row_n, col_idx, sheet_1_cell)
        col_n += 1
        
    for col_idx in range(2, sheet_2.ncols):
        sheet_2_cell = str(sheet_2.cell(row_2, col_idx).value)
        sheet_2_cell = sheet_2_cell.encode('ascii','ignore')
        sheet_w.write(row_n, col_n, sheet_2_cell)
        col_n += 1

    return None
                
#Main program

try:
    workbook_1_r = xlrd.open_workbook(sys.argv[1])
    workbook_2_r = xlrd.open_workbook(sys.argv[2])
    
    #Checks if file is empty
    if os.stat(sys.argv[1]).st_size == 0:
        print 'The file', sys.argv[1], 'is empty.' 
    elif os.stat(sys.argv[2]).st_size == 0:
        print 'The file', sys.argv[1], 'is empty.'
        
except IOError:
    print 'Cannot open', sys.argv[1], 'or', sys.argv[2]

else:
    try:
        sheet_1=workbook_1_r.sheet_by_index(0)
        sheet_2=workbook_2_r.sheet_by_index(0)
    except IOError:
        print 'Could not read the first sheet', sys.argv[1], 'or the second', sys.argv[2]

try:
    name = str(sys.argv[1])
    merge_sheets(sheet_1, sheet_2, name)
except IOError:
    print 'Could not merge sheets'



    
