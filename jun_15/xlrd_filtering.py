#! /usr/bin/env python

'''
This is a program that takes an xl workbook, reads it and uses its
first sheet to perform filtering as specified by the user.

-Remember that you cannot write	too many rows to an excel sheet,
there is a limitation!

'''

import sys
import os
import pdb
import xlrd
import xlwt


#Functions

def filter_sheet(xl_sheet, name):
    '''A functions that takes an xl-sheet
    as input and filters it according to the users specifications
    on Func.refGene, ExonicFunc.refGene, 1000g2014oct_eur, 1000g2014oct_all
    Input: xl_sheet, name
    Output: None
    '''
    
    #Create an excel workbook and a sheet to write to
    workbook_w = xlwt.Workbook()
    sheet_w = workbook_w.add_sheet('Sheet_1')
    

    row_idx = 0 #Row to transfer from
    row_n = 0 #To keep track of which row to write to
    write_to_sheet(row_idx, sheet_w, xl_sheet, row_n)
    
    for row_idx in range(0, xl_sheet.nrows):
        #print xl_sheet.row(row_idx)
        
        if xl_sheet.cell(row_idx, 4).value.encode('ascii','ignore') == 'exonic':
            #print  xl_sheet.cell(row_idx, 4).value
            row_n += 1
            write_to_sheet(row_idx, sheet_w, xl_sheet, row_n)

    workbook_w.save('filtered_'+name)

    return None

def write_to_sheet(row_idx, sheet_w, xl_sheet, row_n):
    '''A function that writes data into a sheet in the excel workbook.
    Input: row_idx, sheet_w, xl_sheet
    Output: None
    '''

    #Iterate over all columns
    for col_idx in range(0, xl_sheet.ncols):
        cell = str(xl_sheet.cell(row_idx, col_idx).value)
        cell = cell.encode('ascii','ignore')
        sheet_w.write(row_n, col_idx, cell)

    pdb.set_trace()
    return None
                
#Main program

try:
    workbook_r = xlrd.open_workbook(sys.argv[1])
    
    #Checks if file is empty
    if os.stat(sys.argv[1]).st_size == 0:
       print "Empty file."       
except IOError:
    print 'Cannot open', sys.argv[1]
else:
    try:
        xl_sheet=workbook_r.sheet_by_index(0)
    except IOError:
        print 'Could not read the first sheet', sys.argv[1]

try:
    name = str(sys.argv[1])
    filter_sheet(xl_sheet, name)
except IOError:
    print 'Could not filter sheet'

        
