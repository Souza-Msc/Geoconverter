#!/usr/bin/env python3.10

#Last Updated: 20 Feb 2023
#Author: Pedro Mendes de Souza; pedromsouza0@gmail.com
#Usage: python Geoconverter.py
#Options: python Geoconverter.py --help

import argparse, re, os, sys
import pandas as pd
from argparse import RawTextHelpFormatter,SUPPRESS

# Guide Msg

def guide_msg():
    return "\n\nExemple of usage: pyhton Geoconverter.py -i data_RR.xlsx -lon Longitude -lat Latitude -o Locality_converted.xlsx"

# Author info

def author_info(param):

	valid = 0

	author = ('\n\n\t Any comments or questions? Please email Pedro Souza (author) at'\
	' pedromsouza0@gmail.com\n\n')

	if param.author == True:
		print (author)
		valid += 1
	
	return valid

## Parses and Check 

def get_parameters():

    parser = argparse.ArgumentParser(description=
	'\n\n\nThis script will convert GTM coordinates to decimal coordinates. The data to be converted must be in .csv, .txt or .xlsx format, split into two columns.\n'+guide_msg(), 
	usage=SUPPRESS,formatter_class=RawTextHelpFormatter)

    required_param_group = parser.add_argument_group('Required Options')

    required_param_group.add_argument('--input_file','-i', action='store',
	help="\n Table (.csv, .txt, .xlsx.) containing the soon to be converted coordinates\n\n")

    required_param_group.add_argument('--longitude','-lon', default = 'Longitude',
	help="\n User-defined column name for the longitude data (default = 'Longitude')\n\n")

    required_param_group.add_argument('--latitude','-lat', default = 'Latitude',
	help="\n User-defined column name for the latitude data (default = 'Latitude')\n\n")

    optional_arg_group = parser.add_argument_group('Options')

    optional_arg_group.add_argument('-author', action='store_true',
	help=' \n Print author contact information \n\n')

    optional_arg_group.add_argument('--out_file', '-o', action='store', default= "Geoconverter_out.csv", help='\n User-defined out file name and format\n')


    if len(sys.argv[1:]) == 0:
        print (parser.description)
        print ('\n')
        sys.exit()

    param = parser.parse_args()
	
    quit_eval = author_info(param)
    if quit_eval > 0:
        sys.exit()

    param = parser.parse_args()

    return param



# Converter


# This program accept coordinates in english and in portuguese so it needs two functions for understand and convert the data

# English one

def conversion_i(old):
    direction = {'N':1, 'S':-1, 'E': 1, 'W':-1}
    new = old.replace(u'°',' ').replace('\'',' ').replace('"',' ').replace('º',' ').replace('”', ' ').replace('′',' ').replace('″',' ').replace('’',' ')
    new = new.split()
    new_dir = new.pop()
    new.extend([0,0,0])
    return (int(float(new[0]))+int(float(new[1]))/60.0+int(float(new[2]))/3600.0) * direction[new_dir]

# Portuguese one

def conversion_p(old):
    direction = {'N':1, 'S':-1, 'L': 1, 'O':-1}
    new = old.replace(u'°',' ').replace('\'',' ').replace('"',' ').replace('º',' ').replace('”', ' ').replace('′',' ').replace('″',' ').replace('’',' ')
    new = new.split()
    new_dir = new.pop()
    new.extend([0,0,0])
    return (int(float(new[0]))+int(float(new[1]))/60.0+int(float(new[2]))/3600.0) * direction[new_dir]

# In case of the user have mix data, portuquese and english, on the same time the next function will try both converters with the data.

def conversor(param):
    
    df = param.input_file

    if df.lower().endswith('.xlsx'):
        data = pd.read_excel(df)
    elif df.lower().endswith('.csv'):
        data = pd.read_csv(df,sep=";", encoding= 'unicode_escape')
    elif df.lower().endswith('.txt'):
        data = pd.read_table(df)
    else:
        print("\n\nEnding session.")
        print("\n\nErro: Input file format not suported")

    x = param.latitude
    y = param.longitude

    long = []
    lat = []
    
    for i in data[f'{x}']:
        try:
            a = conversion_i(i)
            long.append(a)
        except:
            a = conversion_p(i) 
            long.append(a)
    
    for i in data[f'{y}']:
        try:
            b = conversion_i(i)
            lat.append(b)
        except:
            b = conversion_p(i)
            lat.append(b)
    
    data['Long_decimal'] = long
    data['Lat_decimal'] = lat

    out = param.out_file
    
    if out.lower().endswith('.xlsx'):
        data.to_excel(out)
    elif out.lower().endswith('.csv'):
        data.to_csv(out)
    elif out.lower().endswith('.txt'):
        data.to_csv(out, header=None, index=None, sep=' ', mode='a')
    else:
        print("\n\nEnding session.")
        print("\n\nErro: Out file format not suported")

    print("\nResults:\n")
    print(f"{len(data.Long_decimal)} coordinates converted from the inicial {len(data[f'{y}'])}.\n")
    return

def run():
    param = get_parameters()
    conversor(param)
    
run()
