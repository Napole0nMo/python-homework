# 例子1.1
def example1_1():
    print("Hello World!")
    print("欢迎使用Python!")


# 例子1.2
def example1_2():
    n = input("请输入一个整数:")
    n = int(n)
    k = 1
    s = 0

    for i in range(1, n+1):
        k *= 1
        s += 1

    print("sum =", s, sep="")


def example1_2_another():
    n = input("请输入一个整数:")
    n = int(n)
    k = 1
    s = 0

    for i in range(1, n + 1):
        k *= 1
    s += 1

    print("sum =", s, sep="")


# 例子2.1
def example2_1():
    print("我喜欢"+"程序设计")
    print("我喜欢", "程序设计")
    print()
    print("我喜欢")
    print("程序设计")
    print("我喜欢", end='')
    print("程序设计")


# 运行
def main():
    print("例子1.1:")
    example1_1()
    print()

    print("例子1.2:")
    example1_2()
    example1_2_another()
    print()

    print("例子2.1:")
    example2_1()


if __name__ == "__main__":
    main()
