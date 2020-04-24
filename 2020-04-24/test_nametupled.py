from collections import namedtuple, Counter
# from collections import Counter
c = Counter()
Point = namedtuple('Point', ['x', 'y',])
p = Point(1, 2)

# print(p.x)
# print(p.y)
# for ch in 'programming':
#     print("c=", c)
#     c[ch] = c[ch] + 1
#     print("c=", c)

# print(c)
# colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
# c = Counter(colors)
import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5)
print(md5.hexdigest())
