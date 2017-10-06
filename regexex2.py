import re
regex = r"[a-zA-Z] + \d+"
matches = re.findall(regex, "June 24, August 9, Dec 12")

for match in matches:

    print "Full match: %s" % (match)



regex = r"([a-zA-Z]+) \d+"
matches = re.findall(regex, "June 24, August 9, Dec 12")
for match in matches:



    print "Match month: %s" % (match)




regex = r"([a-zA-Z]+) \d+"
matches = re.finditer(regex, "June 24, August 9, Dec 12")
for match in matches:


    print "Match at index: %s, %s" % (match.start(), match.end())
    


print re.sub(regex, r"\2 of \1", "June 24, August 9, Dec 12")
