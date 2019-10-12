if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
a = max(arr)
while max(arr)==a:
   arr.remove(a)
print(max(arr))
