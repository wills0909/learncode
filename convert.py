# *_*coding:utf-8 *_*
def convert(s: str, numRows: int) -> str:
    if numRows < 2:
        return s
    str_list = ["" for _ in range(numRows)]
    i = 0
    flag = 1
    for c in s:
        str_list[i] += c
        i += flag
        if i == 0 or i == numRows - 1:
            flag = -flag
    return "".join(str_list)

print(convert('AB',1))