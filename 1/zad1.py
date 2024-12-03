from collections import Counter

with open("input.txt") as f:
    L, R = map(list, zip(*(line.split() for line in f)))
    L.sort()
    R.sort()
    S = [abs(int(L[i]) - int(R[i])) for i in range(len(L))]
    print(sum(S))

with open("input.txt", "r") as f:
    L_count, R_count = Counter(L), Counter(R)
    S2 = [int(k) * R_count[k] for k, v in L_count.items() if k in R_count]
    print(sum(S2))