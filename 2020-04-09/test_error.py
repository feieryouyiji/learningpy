try:
    10 / 0
except ZeroDivisionError as e:
    print("错误了", e)
else:
    print("No problem")
finally:
    print("finally")
