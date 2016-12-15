import re
import os

print "Starting script.."
#with open("_data/sitemap.")

files = os.listdir("_posts")
for file in files:
    print "Opening ",file
    with open("_posts/" + file, "r") as f:
      content = f.read()
      # Check if post already has permalink
      #print content
      permalinks = re.findall("permalink:.+\n", content)
      print permalinks
      if permalinks:
        permalink = permalinks[0]
        permalink = permalink[len("permalink:"): -1]
        print "Permalink already set to: ", permalink
      else :
        print "No permalink present"
        title = re.findall("title:.+\n", content)[0]
        title = title[len("title:"): -1]

        # For now, just gonna make the permalink to the title for testing purposed
        url = "permalink: ",title, "\n"
        pos = content.find("---")
        pos = content.find("---", pos+1)
        content = content[0:pos] + url + content[pos:]

#    url = LOOKUP_IN_DATA(title)
#
#
#
#     # Transform url to whatever the permalink declaration is in Jekyll
#
#  content = content[0:pos] + url + content[pos:]
#
# with open(MARKDOWN_FILENAME, "w") as f:
# f.write(content)
# close post file
#close data file
print "END :)"
