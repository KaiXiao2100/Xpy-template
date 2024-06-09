#
# @lc app=leetcode.cn id=2069 lang=python3
#
# [2069] 模拟行走机器人 II
#

# @lc code=start
class Robot:

    def __init__(self, width: int, height: int):
        self.w, self.h, self.s = width, height, 0

    def step(self, num: int) -> None:
        self.s = (self.s + num - 1) % ((self.w + self.h - 2) * 2) + 1

    def get(self):
        s, w, h = self.s, self.w, self.h
        if s < w: return s, 0, "East"
        if s < w + h - 1: return w - 1, s - w + 1, "North"
        if s < w * 2 + h - 2: return w * 2 + h - 3 - s, h - 1, "West"
        return 0, (w + h - 2) * 2 - s, "South"

    def getPos(self) -> List[int]:
        x, y, _ = self.get()
        return [x, y]

    def getDir(self) -> str:
        return self.get()[2]



# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
# @lc code=end

