class Solution:
    """
    693. 交替位二进制数
    """
    def hasAlternatingBits(self, n: int) -> bool:
        a = (n >> 1) ^ n
        return a & (a + 1) == 0
