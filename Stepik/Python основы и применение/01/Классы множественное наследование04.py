# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 20:03:04 2018

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 16:01:28 2018

@author: user
"""
'''
Вам дано описание наследования классов в следующем формате. 
<имя класса 1> : <имя класса 2> <имя класса 3> ... <имя класса k>
Это означает, что класс 1 отнаследован от класса 2, класса 3, и т. д.

Или эквивалентно записи:

class Class1(Class2, Class3 ... ClassK):
    pass
Класс A является прямым предком класса B, если B отнаследован от A:


class B(A):
    pass


Класс A является предком класса B, если 
A = B;
A - прямой предок B
существует такой класс C, что C - прямой предок B и A - предок C

Например:
class B(A):
    pass

class C(B):
    pass

# A -- предок С


Вам необходимо отвечать на запросы, является ли один класс предком
 другого класса

Важное примечание:
Создавать классы не требуется.
Мы просим вас промоделировать этот процесс, и понять существует ли путь от 
одного класса до другого.
Формат входных данных
В первой строке входных данных содержится целое число n - число классов.

В следующих n строках содержится описание наследования классов. 
В i-й строке указано от каких классов наследуется i-й класс. 
Обратите внимание, что класс может ни от кого не наследоваться. 
Гарантируется, что класс не наследуется сам от себя (прямо или косвенно), 
что класс не наследуется явно от одного класса более одного раза.

В следующей строке содержится число q - количество запросов.

В следующих q строках содержится описание запросов в формате 
<имя класса 1> <имя класса 2>.
Имя класса – строка, состоящая из символов латинского алфавита, длины не более 50.

Формат выходных данных
Для каждого запроса выведите в отдельной строке слово "Yes", если класс 1
 является предком класса 2, и "No", если не является. 

Sample Input:

4
A
B : A
C : A
D : B C
4
A B
B D
C D
D A
Sample Output:

Yes
Yes
Yes
No
'''


# Отыщем путь в заданном графе
def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.__contains__(start):
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath
    return None


f = open('input.txt', 'r')
# n=int(input())
n = int(f.readline())
cl = dict()
lst = list()
for i in range(n):
    # lst=input().split()
    lst = f.readline().strip().split()
    cl.update({lst[0]: list()})
    cl[lst[0]].extend(lst[2:])
print(cl)

# n=int(input())
n = int(f.readline())
for i in range(n):
    # end,start=input().split()
    end, start = f.readline().split()
    # print(find_path(cl,start,end))
    if find_path(cl, start, end):
        print('Yes')
    else:
        print('No')
f.close()
