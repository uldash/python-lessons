'''
Вам дано описание пирамиды из кубиков в формате XML.
Кубики могут быть трех цветов: красный (red), зеленый (green) и синий (blue﻿).
Для каждого кубика известны его цвет, и известны кубики, расположенные прямо под ним.

Пример:

<cube color="blue">
  <cube color="red">
    <cube color="green">
    </cube>
  </cube>
  <cube color="red">
  </cube>
</cube>
 
Введем понятие ценности для кубиков. Самый верхний кубик, соответствующий корню XML документа имеет ценность 1. Кубики, расположенные прямо под ним, имеют ценность 2. Кубики, расположенные прямо под нижележащими кубиками, имеют ценность 3. И т. д.

Ценность цвета равна сумме ценностей всех кубиков этого цвета.

Выведите через пробел три числа: ценности красного, зеленого и синего цветов.
Sample Input:

<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>
Sample Output:

4 3 1
'''
import xml.etree.ElementTree as ET

XML_FILE = 'example03.xml'

stack = [1]
kubiks = {'red': 0, 'green': 0, 'blue': 0}


def dd(root, kubiks, stack):
    stack.insert(0, stack[0] + 1)
    for child in root:
        kubiks.update({
            child.attrib['color']:
            kubiks[child.attrib['color']] + stack[0]
        })
        dd(child, kubiks, stack)
    stack.pop(0)


#tree = ET.parse(XML_FILE)
tree = ET.ElementTree(ET.fromstring(input()))
root = tree.getroot()
#print(root.attrib['color'])
kubiks.update({root.attrib['color']: kubiks[root.attrib['color']] + stack[0]})
#print(kubiks[root.attrib['color']])
dd(root, kubiks, stack)

print(' '.join(str(kubiks[i]) for i in kubiks))