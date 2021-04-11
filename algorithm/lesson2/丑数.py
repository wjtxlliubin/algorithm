class Solution:
    def nthUglyNumber(self, n: int) -> int:
        import heapq
        primes = [2, 3, 5]
        seen = {1}
        heap = [1]
        for _ in range(1, n):
            cur = heapq.heappop(heap)
            for prime in primes:
                nxt = cur * prime
                if nxt not in seen:
                    seen.add(nxt)
                    heapq.heappush(heap, nxt)
        return heapq.heappop(heap)

if __name__ == '__main__':
    result = Solution().nthUglyNumber(15)
    print(result)
