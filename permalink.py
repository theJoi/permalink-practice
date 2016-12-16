import re
import os

print "Starting script.."
#with open("_data/sitemap.")

files = os.listdir("_posts")
for file in files:
    print "Opening %s..." % file
    with open("_posts/" + file, "r") as f:

      content = f.read()

      # Check if post already has permalink
      permalinks = re.findall("permalink:.+\n", content)

      if permalinks:
        permalink = permalinks[0]
        permalink = permalink[len("permalink: "): -1]
        print "  Permalink already set to: %s" % permalink
      else :
        title = re.findall("title:.+\n", content)[0]
        title = title[len("title: "): -1]

        # For now, just gonna make the permalink to the title for testing purposes
        url = "permalink: /%s/" % title
        pos = content.find("---")
        pos = content.find("---", pos+1)
        content = content[0:pos] + url + content[pos:]

        with open("_posts/" + file, "w") as f:
          f.write(content)
          print "  No permalink already present, set to: ", url

#    url = LOOKUP_IN_DATA(title)
#


print "END :)"
