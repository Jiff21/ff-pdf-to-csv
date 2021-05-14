#!/usr/bin/python3
import sys, getopt
import tabula
import argparse

# Currently this will run in python3 but not via CL
# python3 convert.py -i /Users/jeff/Documents/footbal/514PPR300.pdf  -o 514PPR300.csv

def main(argv):
    print('Input file is "', argv.input)
    print('Output file is "', argv.output)
    tabula.convert_into(argv.input, argv.output, output_format="csv", pages='all')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='convert pdfs to csvs.')
    parser.add_argument('-o', '--output', help='path to output file', required=True)
    parser.add_argument('-i', '--input', help='path to output file', required=True)
    args = parser.parse_args()
    main(args)
