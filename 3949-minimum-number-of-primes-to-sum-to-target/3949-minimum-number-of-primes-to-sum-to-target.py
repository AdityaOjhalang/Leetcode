class Solution:
    def minNumberOfPrimes(self, n: int, m: int) -> int:
        # Helper function to generate the first m primes
        def first_m_primes(m):
            primes = []
            num = 2
            while len(primes) < m:
                for p in primes:
                    if num % p == 0:
                        break
                else:
                    primes.append(num)
                num += 1
            return primes

        primes = first_m_primes(m)
        
        # DP for coin change (unbounded)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for p in primes:
                if i - p >= 0:
                    dp[i] = min(dp[i], dp[i - p] + 1)
        
        return dp[n] if dp[n] != float('inf') else -1