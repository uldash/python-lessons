from xml.etree import ElementTree

tree = ElementTree

tree = ElementTree.parse("example00.xml")
root = tree.getroot()

tree.write("example00_copy.xml")