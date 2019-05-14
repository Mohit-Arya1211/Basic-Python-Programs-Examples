def sum_arr(arr, size):
   if (size == 0):
     return 0

   else:
     return arr[size-1] + sum_arr(arr, size-1)

n = int(input())
      a = []
        for i in range(0, n):
            x = int(input())
            a.append(x)
b = sum_arr(a, n)
print(b)
