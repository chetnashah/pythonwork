

seq = 'ACTG'

len(seq)

seq1 = 'CCAA'
seq2 = 'GGTT'
print(seq1+seq2)

print(''.join(seq1))
print(','.join(seq2))

import random
rc = random.choice('ACGT')
print('random choice = '+rc)


seqrandom = ''

for _ in range(10):
    seqrandom += random.choice('ACGT')
print(seqrandom)

li = ['A','C','A','T','G','A','T','G','G']
# seperator.join(list)
print(','.join(li))
print(' '.join(li))
print(''.join(li))


# use split on string
longstr = 'A,G,C,T,A,G,G,G,C,A,T,A,G'
print(longstr.split(','))



