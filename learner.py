from battle_interface import *
from bot_creator import *
import numpy
import random
def weighted_choice(items):
    """
        Chooses a random element from items, where items is a list of tuples in
        the form (item, weight). weight determines the probability of choosing its
        respective item. Note: this function is borrowed from ActiveState Recipes.
        """
    weight_total = sum((item[1] for item in items))
    n = random.uniform(0, weight_total)
    for item, weight in items:
        if n < weight:
            return item
    n = n - weight
    return item
def get_random_list_with_size(size):
    import random
    return [random.randint(0,3) for i in range(size)]
print(numpy.array([get_random_list_with_size(18) for i in range(1000)]).shape)
import numpy
list_of_bots_files = bots()
def mate(matrix_a,matrix_b):
    a = []
    for i in range(1000):
        b = []
        for j in range(18):
            b+=[(matrix_a[i][j]+matrix_b[i][j])/2]
            if (matrix_a[i][j]+matrix_b[i][j])/2 > 3:
                print("bo")
        a+=[b]
    return numpy.array(a)
def mutate(matrix):
    import random
    a = random.randint(9990,10000)
    for i in range(a):
        matrix[random.randint(0,999)][random.randint(0,17)] = min(matrix[random.randint(0,999)][random.randint(0,17)],random.randint(0,3))

def score(matrix,g,index):
    bot_name = os.path.abspath(os.path.join('our_bots',str(g)+"_"+str(index)+'.py'))
    create_bot(bot_name,[matrix])
    
    score = 0
    for bot in list_of_bots_files:
        scores = run(bot_name,bot)[0]
        if scores[0]+scores[1]==0:
            score += 0
        else:
            score+=scores[0]/(scores[0]+scores[1])
    return score


g=0
current_generation = [numpy.array([get_random_list_with_size(18) for i in range(1000)]) for k in range(200)]
scores = [0 for i in range(200)]

for j in range(200):
    for k in range(200):
        scores[k] = score(current_generation[k],g,j)
        a = zip(current_generation,scores)
        new = []
    for i in range(200):
        matrix_to_add = mutate(mate(weighted_choice(a),weighted_choice(a)))
        mutate(matrix_to_add)
        new+=[matrix_to_add]
    current_generation = new
x = mylist.sort(key=lambda x: x[1])[-1]
np.set_printoptions(threshold=np.inf, linewidth=np.inf)  # turn off summarization, line-wrapping
with open(path, 'w') as f:
    f.write(np.array2string(x, separator=' '))
