# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
    print("x-=>", x)
a = (x + 2 for x in range(1))
print("type--?", type(it))
print("a--?", a)
