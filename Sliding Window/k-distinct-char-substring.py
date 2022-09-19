#lc medium
#sliding window
#Given a string, find the length of the longest substring in it with no more than K distinct characters.

def longest_substring_with_k_distinct(str, k):
  l = 0
  charSet = {}
  result = 0
  for j in range(len(str)):
    if str[j] in charSet.keys():
        charSet[str[j]] += 1
    else:
        charSet[str[j]] = 1
    while len(charSet) > k:
        if charSet[str[l]] == 1:
            del charSet[str[l]]
        else:
            charSet[str[l]] -= 1
        l += 1
    if len(charSet) == k: 
        result = max(result,sum(charSet.values()))
  return result


def main():
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))


main()
