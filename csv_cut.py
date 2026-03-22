import argparse
import csv

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--field', type=int)
    parser.add_argument('csv_file', type=str)
    return parser.parse_args()

args = parse_args()
args.field -= 1
with open(args.csv_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for line in csv_reader:
        print(line[args.field])