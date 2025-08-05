class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        for i in fruits:
            for j in baskets:
                if j>=i:
                    baskets.remove(j)
                    break
        return len(baskets)