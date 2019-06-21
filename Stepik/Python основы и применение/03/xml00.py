from xml.etree import ElementTree

tree = ElementTree.parse('example00.xml')
root = tree.getroot()
print(root)
print(root.tag, root.attrib)
for child in root:
    print(child.tag, child.attrib)

print(root[0][0].text)  # Greg

for element in root.iter("scores"):
    print(element)
    for child in element:
        print(child.text)
