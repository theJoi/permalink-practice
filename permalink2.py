########################################
# permalink.py
#
# CREATED BY: Joi Williams 12/16/16
#
# DESCRIPTION: Adds permalinks and
# menu ids to YAML Front Matter to
# posts, based on csv data.
#
# python permalink > log-permalink.txt
#######################################
import re
import os
import json
import codecs
import csv

print "Starting script and reading in _data/article-urls.csv ...."

articleURLs = {}

# Open csv file with permalink data and add to articleURLs dictionary keyed by article id
with open("_data/article-urls.csv", 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar="'")
    for row in reader:
        articleURLs[row[0]] = {
            'menuid':row[1],
            'path':row[4]
        }

# Loop through all files in _post directory
files = os.listdir("_posts")
for file in files:
    # Ignore directories
    if os.path.isdir(os.path.join("_posts/", file)):
         continue

    # Read in post file
    print "  Opening %s..." % file,
    with open("_posts/" + file, "r") as f:

        content = f.read()

        # Check if post already has permalink and/or menu id
        permalink_matches = re.findall("permalink:.+\n", content)
        menuid_matches = re.findall("menu_id:.+\n", content)

        # Do nothing if already has both permalink and menu id
        if permalink_matches and menuid_matches:
            permalink = permalink_matches[0]
            permalink = permalink[len("permalink: "): -1]
            print " Permalink already set to: %s" % permalink

        else:
            # Get joomla id of post
            matches = re.findall("joomla_id:.+\n", content)
            articleID = None
            if matches:
                articleID = matches[0]
                articleID = articleID[len("joomla_id: "): -1]

            # Check if article id is in sitemap data
            if articleID and articleID in articleURLs:
                url = ""
                menuId = ""
                # Add permalink and menu id to front matter
                if not permalink_matches:
                    url = "permalink: /%s\n" % articleURLs[articleID]['path']
                    print "\n   No permalink, setting to: /%s" % articleURLs[articleID]['path']
                if not menuid_matches:
                    menuId = "menu_id: %s\n" % articleURLs[articleID]['menuid']
                    print "\n   No menu id, setting to: %s" % articleURLs[articleID]['menuid']
                pos = content.find("---")
                pos = content.find("---", pos+1)
                content = content[0:pos] + url + menuId + content[pos:]
                with open("_posts/" + file, "w") as f:
                    f.write(content)

            # If not id is not in csv do nothing
            else:
                print " No permalink, leaving as default."
print "END :)"
