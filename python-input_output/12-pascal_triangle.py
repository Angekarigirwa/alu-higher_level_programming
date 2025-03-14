#!/usr/bin/python3
"""define function pascal_triangle(n)"""


def pascal_triangle(n):
    """represents pascal's triangle"""
    if n <= 0:
        return []
    answer = []
    for k in range(n):
        if k == 0:
            answer.append([1])
        else:
            ans = []
            list = answer[k - 1][:]
            list.insert(0, 0)
            list.append(0)
            i = 0
            while i < len(list) - 1:
                ans.append(list[i] + list[i + 1])
                i = i + 1
            answer.append(ans)
    return answer
