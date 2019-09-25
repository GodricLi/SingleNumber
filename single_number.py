"""找出列表中的单个数字，只出现一次的数字"""


def find_single(arr: list):
    """
    :param arr:列表
    :return:单个数字
    """
    result = 0
    for i in arr:
        result ^= i  # 异或运算符：相应位，值相同为0，不相同为1
    if result == 0:
        print("No single numbers")
    else:
        return result


def single(arr):
    se = set()
    li = []
    for i in arr:
        if i not in se:
            se.add(i)
        else:
            li.append(i)
    single_num = []
    for i in arr:
        if i not in li:
            single_num.append(i)
    return single_num


if __name__ == '__main__':
    print(find_single([1, 2, 3, 4, 5, 6, 2, 3, 4, 5, 6, 0]))
    print(single([1, 2, 3, 4, 5, 6, 2, 3, 4, 5, 6, 0]))
