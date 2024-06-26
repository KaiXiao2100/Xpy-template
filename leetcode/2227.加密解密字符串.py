#
# @lc app=leetcode.cn id=2227 lang=python3
#
# [2227] 加密解密字符串
#

# @lc code=start
class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.map = dict(zip(keys, values))
        self.cnt = Counter(self.encrypt(s) for s in dictionary)

    def encrypt(self, word1: str) -> str:
        res = ""
        for ch in word1:
            if ch not in self.map:
                return ""
            res += self.map[ch]
        return res

    def decrypt(self, word2: str) -> int:
        return self.cnt[word2]



# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)
# @lc code=end

