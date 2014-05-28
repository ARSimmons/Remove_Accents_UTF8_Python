
## !python3
## coding: utf8

## This script is a quickie regex to strip accents
## from python unicode strings. letters only

import csv
import string
import unicodedata

## Input csv location, open in read

csvfile = open(r'I:\It_24\115125_India_Placenames_ALL\csv\in_cities_india_subset.csv', 'r',  encoding="utf8")

## create an object using DictReader function of the csv list

csvheader = csv.DictReader(csvfile)

for (i, col) in enumerate(csvheader.fieldnames):
    print (str(i) + ": " + str(col))

## create a file to write to

new_csvfile = open(r'I:\It_24\115125_India_Placenames_ALL\results\csv\in_cities_india_subset_edited_v2.csv', 'w', encoding="utf8")

## Ask the user to input which column # to use in the csv

csv_col_index = int(input('Which Column in csv contains the data you would like to run pattern match on? >'))

## Iterate over csv file

print ("\n...Iterating over csv file, based on your column choice..!") 

reader = csv.reader(csvfile)

def remove_accents(myString):    
    return ''.join(x for x in unicodedata.normalize('NFD', myString)
                   if unicodedata.category(x) != 'Mn')

# set the output to what you want, note that row[1] is hardpathed at the moment

new_csvfile.write(','.join(x for x in csvheader.fieldnames) + "\n")

for row in reader:
    row[csv_col_index] = remove_accents(row[csv_col_index])
    new_csvfile.write(','.join(x for x in row)+ "\n")

