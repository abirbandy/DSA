#brute force
#Given an array, find the average of all contiguous subarrays of size ‘K’ in it.
def find_averages_of_subarrays(K, arr):
  result = []
  for i in range(len(arr)-K+1):
    # find sum of next 'K' elements
    _sum = 0.0
    for j in range(i, i+K):
      _sum += arr[j]
    result.append(_sum/K)  # calculate average

  return result

#sliding window
def find_averages_of_subarrays_sw(K, arr):
  result = []
  start = 0
  curr_sum = 0.0
  for i in range(len(arr)):
    curr_sum += arr[i]
    if i >= K-1:
      result.append(curr_sum/K)
      curr_sum -= arr[start]
      start+=1
  return result

def main():
  result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
  print("Averages of subarrays of size K: " + str(result))


main()