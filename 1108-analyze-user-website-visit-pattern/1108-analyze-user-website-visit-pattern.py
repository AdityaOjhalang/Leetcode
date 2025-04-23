class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        data = list(sorted(zip(timestamp,username,website)))
        user_sites = defaultdict(list)

        for time,user,site in data:
            user_sites[user].append(site)
        
        patterns = defaultdict(set)
        for user,site in user_sites.items():
            if len(site) < 3:
                continue
            sequences = set(combinations(site,3))
            for seq in sequences:
                patterns[seq].add(user)
        
        maxcount = 0 
        result = tuple()
        for pattern,users in patterns.items():
            count = len(users)
            if count > maxcount or (count == maxcount and pattern < result):
                maxcount = count 
                result = pattern
        return result 