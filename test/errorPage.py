print("-----------------try catch-------------------")
try:
    print("try")
    r = 10 / 0
    print("result:", r)
except ZeroDivisionError as e:
    print("exception : ", e)
finally:
    print("finally..")
print("END")

print("-----------------error py-------------------")


def foo(s):
    n = int(s)
    print(">>>n = %d " % n)
    return 10 / n


def main():
    foo("1")


main()


def foo(s):
    n = int(s)
    # 断言
    assert n != 0, 'n is zero!'
    return 10 / n


def main():
    foo("1")


main()


print("-----------------logging py-------------------")

import logging
logging.basicConfig(level=logging.INFO)

def foo(s):
    n = int(s)
    logging.info("n >>> %d" % n)
    return 10 / n


def main():
    foo("1")


main()

print("-----------------单元测试-------------------")

