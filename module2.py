#######################################
# module.py
#
# CREATED BY: Joi Williams 12/20/16
#
# DESCRIPTION: Generates a YAML file
# with module ids used for each menu id
#
#######################################
import re
import os
import json
import codecs
import csv

print "Starting script and reading in _data/module-list.csv ..."

moduleMenuList = {}

# Open csv file with permalink data and add to moduleMenu list keyed by menu id
with open("_data/module-list.csv", 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar="'")
    firstline = True
    for row in reader:
        if firstline:
            firstline = False
        else:
            moduleid = row[0]
            menuid = row[1]
            # See if menu id is already on list
            if menuid in moduleMenuList:
                moduleMenuList[menuid].append(moduleid)
            else:
                moduleMenuList[menuid] = []
                moduleMenuList[menuid].append(moduleid)

# Create, open and write to module_list.yml
with open("_data/module_list2.yml", "w") as f:
    for menuid in moduleMenuList:
        f.write("%s:\n" % menuid)
        for moduleid in moduleMenuList[menuid]:
             f.write("  - %s\n" % moduleid)
    print "Creating _data/module_list2.yml ..."
print "DONE :)"
