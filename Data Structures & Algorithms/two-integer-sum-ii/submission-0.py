class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = defaultdict(int) # instead of {} why?
        for i in range(0, len(numbers)):
            compliment = target - numbers[i]
            if hashmap[compliment]:
                return [hashmap[compliment], i + 1] # return the key value pair i want to store the index as the value since i probably could get it easier when returned we need to also return in a list
                # return [hashmap[compliment], i]
            # forgot how to add to hashmap but add here the compliment and the indicies 
            hashmap[numbers[i]] = i + 1
        
        return []