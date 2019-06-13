s = int(input())
b = [int(x) for x in input().split()]
b.sort()
print(b[int(len(b)/2)])
