#######################################
# csv-to-yaml.py
#
# CREATED BY: Joi Williams 01/03/2017
#
# DESCRIPTION: Takes a two-column csv file
# and generates YAML data so it can easily
# be access in Jekyll
#
# Usage:
# python module.py path/file-to-read.csv path/file-to-write.yml
#######################################
import re
import os
import json
import codecs
import csv
import sys

# Get filename
if len(sys.argv) > 2:
    print sys.argv[1]
    infile = sys.argv[1]
    outfile = sys.argv[2]
else:
    sys.exit("ERROR: Please provide both input and output filenames as arguments.")

print "Starting script and reading in %s ..." % infile

moduleMenuList = {}

# Open csv file with data and add to moduleMenu list keyed by unique first column
with open(infile, 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar="'")

    # Create, open and write to yaml file
    with open(outfile, "w") as f:

        for row in reader:
            cat1 = row[0]
            cat2 = row[1]

            f.write("%s:\n" % cat1)
            f.write("  - %s\n" % cat2)
        print "Creating and writing to %s ..." % outfile
print "DONE :)"
