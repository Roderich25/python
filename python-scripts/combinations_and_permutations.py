import itertools

my_list = [1, 2, 3, 4, 5, 6]

combinations = itertools.combinations(my_list, 3)
permutations = itertools.permutations(my_list, 3)

#for c in combinations:
#    print(c)

#for p in permutations:
#    print(p)

print([result for result in combinations if sum(result) == 10])

#print([result for result in permutations if sum(result) == 10])

word = 'sample'
my_letters = 'plames'

permutations = itertools.permutations(my_letters, 6)

for p in permutations:
    if "".join(p) == word:
        print('Match!')
        break
else:
    print('No match!')