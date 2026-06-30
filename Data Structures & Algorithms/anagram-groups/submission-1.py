class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # split the str into words 
        # how to check for ana 
            # compare their sorted components 
            # or the hash map for num seen or the array for lowercase case
        # how to add to groups idk
        
        groups = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            groups[key].append(word) # grouping by the key this is the same because its the sorted so the dict would be key: aet, value: ate, eat, tea thats how to group up into pairs
            # thats why you also append by the word

        return list(groups.values())
