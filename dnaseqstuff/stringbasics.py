

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

