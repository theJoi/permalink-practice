import re
import os
import json
import codecs
import csv

print "Starting script and reading in _data/menu3.csv ...."

with open("_data/menu3.csv", 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar="'")
    for row in spamreader:
        if row[0] == '2':
            print row[3]


## Grab sitemap data
#with codecs.open("_data/sitemap.json", "r", "utf-8") as data:
#    sitemap = json.load(data)
#
## Loop through all files in _post directory
#files = os.listdir("_posts")
#for file in files:
#    print "  Opening %s..." % file
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
#        print "    Permalink already set to: %s" % permalink
#      else :
#        title = re.findall("title:.+\n", content)[0]
#        title = title[len("title: "): -1]
#
#        # Check if url is in sitemap data
#        if title in sitemap:
#            url = "permalink: %s\n" % sitemap[title]
#            pos = content.find("---")
#            pos = content.find("---", pos+1)
#            content = content[0:pos] + url + content[pos:]
#
#            with open("_posts/" + file, "w") as f:
#                f.write(content)
#                print "    No permalink already present, set to: %s" % sitemap[title]
#        else:
#            print "    No permalink already present, nor in sitemap. Leaving as default."
print "END :)"
