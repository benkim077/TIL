N, M = map(int, input().split())
set1 = set()
for _ in range(N):
    set1.add(input())

set2 = set()
for _ in range(M):
    set2.add(input())

union_set = set1 & set2
print(len(union_set))
union_lst = sorted(list(union_set))
for ele in union_lst:
    print(ele)