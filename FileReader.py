# with open('/Users/Mohamad/Projects/PycharmProjects/FileReader/text.txt', 'r') as infile:
#     data = infile.read()
#     data = data.replace("</doc>","")
# with open('/Users/Mohamad/Projects/PycharmProjects/FileReader/ct.txt', 'w') as outfile:
#     outfile.write(data)
#

f = open("/Users/Mohamad/Projects/PycharmProjects/FileReader/ct.txt","r")
lines = f.readlines()

f2 = open("/Users/Mohamad/Projects/PycharmProjects/FileReader/ct2.txt","w")
for line in lines:
        if not line.__contains__("<doc"):
                f2.write(line)