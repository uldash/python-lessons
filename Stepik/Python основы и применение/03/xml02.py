from xml.etree import ElementTree

tree = ElementTree.parse("example00.xml")
root = tree.getroot()

greg = root[0]
module1 = next(greg.iter("module1"))
print(module1, module1.text)

module1.text = str(float(module1.text) + 10)
tree.write("example00_modified.xml")