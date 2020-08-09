# Big-O

# 1. Constant----------------- O(1)
# 2. Logarithmic-------------- O(Log N)
    # log (base) N = exponent
    # log 8 = 3
# linear---------------------- 0(N)
animals = ['duck', 'cat', 'dog', 'bear']

def print_animals(animal_list):
    for i in range(len(animal_list)):
        print(animal_list[i])
        counter = 0
        for n in range(10000):
            counter += 1
print_animals(animals)
# O(100000*n) ----> O(N)

# linearithmic/log-linear----- O(N * Log N)
# polynomial ----------------- O(N^c)
# exponential ---------------- O(c^N)
#