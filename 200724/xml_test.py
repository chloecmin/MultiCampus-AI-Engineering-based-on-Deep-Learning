#Import required library
import xml.etree.ElementTree as xml

#def createXML(filename):
#     # Start with the root element
#     root = xml.Element("users")
#     children1 = xml.Element("user")
#     root.append(children1)
#     tree = xml.ElementTree(root)
#     with open(filename, "wb") as fh:
#         tree.write(fh)
#
# if __name__ == "__main__":
#     createXML("testXML.xml")

root = xml.Element("employees")

child = xml.Element("employee")
nm = xml.SubElement(child, "name")
age = xml.SubElement(child, 'age')
sal = xml.SubElement(child, "salary")
nm.text = 'John'
age.text = '20'
sal.text = '3000'

child2 = xml.Element("employee")
nm = xml.SubElement(child2, "name")
age = xml.SubElement(child2, 'age')
sal = xml.SubElement(child2, "salary")
nm.text = 'susan'
age.text = '30'
sal.text = '6000'


root.append(child)
root.append(child2)

tree = xml.ElementTree(root)

f = open('C:\\test2\\employees2.xml', 'wb')
tree.write(f)