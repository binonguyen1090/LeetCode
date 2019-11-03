# https://leetcode.com/problems/top-k-frequent-elements/submissions/


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dic = {}
        for num in nums:
          if num not in dic:
            dic[num] = 1
          else:
            dic[num] += 1

        value_sort = sa = sorted(dic.values())
     
    
        max_value = []
        while len(max_value) < k:
            v = value_sort.pop()
            max_value.append(v)

        result = []
        for i in max_value:
          for k in dic:
            if dic[k] == i and k not in result:
              result.append(k)
        print(result)
        return(result)
    