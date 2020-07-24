import xml.etree.ElementTree as xml

tree = xml.ElementTree(file="C:\\test2\\employees2.xml")

root = tree.getroot() #employees
# children = root.getchildren()
children = list(root)
student = []

for child in children: #employee
    dic = {}
    for i in child:
        # print(i.tag,":", i.text)
        dic[i.tag] = i.text
    student.append(dic)

print(student)
