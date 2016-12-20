#######################################
# module.py
#
# CREATED BY: Joi Williams 12/20/16
#
# DESCRIPTION: Generates a json dictionary
# based on module
#
#######################################
import re
import os
import json
import codecs
import csv

print "Starting script and reading in _data/module-list.csv ...."

moduleMenuList = [[]]

# Open csv file with permalink data and add to moduleMenu list keyed by menu id
with open("_data/module-list.csv", 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar="'")
    firstline = True
    for row in reader:
        if firstline:
            firstline = False
        else:
            moduleMenuList[int(row[1])].append(row[0])
            print moduleMenuList

print moduleMenuList
## Loop through all files in _post directory
#files = os.listdir("_posts")
#for file in files:
#    # ignore directories
#    if os.path.isdir(os.path.join("_posts/", file)):
#         continue
#    print "  Opening %s..." % file,
#    with open("_posts/" + file, "r") as f:
#
#      content = f.read()
#
#      # Check if post already has permalink
#      permalinks = re.findall("permalink:.+\n", content)
#
#      if permalinks:
#        permalink = permalinks[0]
#        permalink = permalink[len("permalink: "): -1]
#        print " Permalink already set to: %s" % permalink
#      else :
#        matches = re.findall("joomla_id:.+\n", content)
#        articleID = None
#        if matches:
#            articleID = re.findall("joomla_id:.+\n", content)[0]
#            articleID = articleID[len("joomla_id: "): -1]
#
#        # Check if article id is in sitemap data
#        if articleID and articleID in articleURLs:
#            #add permalink and menu id to front matter
#            url = "permalink: /%s\n" % articleURLs[articleID]['path']
#            menu = "menu_id: %s\n" % articleURLs[articleID]['menuid']
#            pos = content.find("---")
#            pos = content.find("---", pos+1)
#            content = content[0:pos] + url + menu + content[pos:]
#
#            with open("_posts/" + file, "w") as f:
#                f.write(content)
#                print "\n   No permalink, setting to: /%s" % articleURLs[articleID]['path']
#        else:
#            print " No permalink, leaving as default."
#print "END :)"
