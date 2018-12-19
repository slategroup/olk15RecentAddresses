from parser import Parser
import argparse
import csv
import sys

parser = argparse.ArgumentParser(description="Convert olk15RecentAddresses to a list of email addresses.")
parser.add_argument('filename', type=str, help="Path to the olk15RecentAddresses file.")
args = parser.parse_args()
parser = Parser(args.filename)
data = parser.go()

writer = csv.writer(sys.stdout)
writer.writerow(['Email', 'First Name', 'Last Name'])
for email, first_name, last_name in data:
  writer.writerow([email, first_name, last_name])
