__author__ = 'roeyz'
import random

def modify(bots2fitness_mapping):
    """
    this function modifies the given set of bots to the next generation by keeping
    the best results within the set and breeding them. afterward, the bred ones shall be mutated.
    :param bots2fitness_mapping: a mapping between the current generation bots and their fitness due to
    the last tournament between them.
    :return: an new set of 100 bots that includes some of the best bots given (the best 22 will continue,
    and the best 13 will mate (22+Choose(13,2)=100)/
    """
    lst_survivors = sorted(bots2fitness_mapping, key=bots2fitness_mapping.get, reverse=True)[:22]
    result = set()
    for i in range(12):
        better_parent = lst_survivors[i]
        for j in range(i + 1, 12):
            worse_parent = lst_survivors[j]
            result.add(mate((better_parent, bots2fitness_mapping[better_parent]),
                            (worse_parent, bots2fitness_mapping[worse_parent])))
    return result | set(lst_survivors)


def mate(mat1_details, mat2_details):
    """
    mating two given matrices of bots by weighted summing their persentage for each sequence of actions with their
    fitness as their ranking and divides by their sum.
    :param better_parent_det:
    :param worse_parent_det:
    :return:
    """
    result = {}
    mat1 = mat1_details[0]
    mat2 = mat2_details[0]
    for x in set(mat1.keys()) | set(mat2.keys()):
        if x not in mat1:
            result[x] = {y: mat2_details[0] * mat2[y] for y in mat2}
        elif x not in mat2:
            result[x] = {y: mat1_details[0] * mat1[y] for y in mat1}
        else:
            result[x] = dict()
            for y in mat2[x]:
                if y in mat1[x]:
                    result[x][y] = (mat1_details[0] * mat1[x][y] + mat2_details[0] * mat2[x][y])
                else:
                    result[x][y] = mat2[x][y]
    return mutate(result)


def mutate(bot):
    for x in bot:
        for statement in x:
            c=random.random()
            if c<0.01:
                x[statement]+=1
            elif 0.99<c and x[statement]!=0:
                x[statement]-=1
    return bot


