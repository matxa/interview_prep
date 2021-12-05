#!/usr/bin/env python3
"""
implemente a função splitConsecutives que divide uma dada
lista não vazia xs de inteiros numa lista de sub-listas. Cada sub-lista
é composta por números consecutivos (seja crescente, decrescente ou ambas) da lista dada,
respeitando a ordem inicial.

print(splitConsecutives([2,4,1,2,7,6,5,1]))
output:
[[2], [4], [1, 2], [7, 6, 5], [1]]

def splitConsecutives(xs):
"""

def splitConsecutivesHelper(xs, index, output, sub_list):
    if index >= len(xs):
        return
    if abs(sub_list[-1] - xs[index]) == 1:
        sub_list.append(xs[index])
    else:
        sub_list = [xs[index]]
        output.append(sub_list)
    return splitConsecutivesHelper(xs, index+1, output, sub_list)


def splitConsecutives(xs):
    if len(xs) <= 1:
        return []

    output = []
    sub_list = [xs[0]]

    splitConsecutivesHelper(xs, 0, output, sub_list)
    return output

xs = [2,4,1,2,7,6,5,1]
print(splitConsecutives(xs))
