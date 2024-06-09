#
# @lc app=leetcode.cn id=2296 lang=python3
#
# [2296] 设计一个文本编辑器
#

# @lc code=start
class Node:
    __slots__ = 'prev', 'next', 'ch'

    def __init__(self, ch=''):
        self.prev = None
        self.next = None
        self.ch = ch

    # 在 self 后插入 node，并返回该 node
    def insert(self, node: 'Node') -> 'Node':
        node.prev = self
        node.next = self.next
        node.prev.next = node
        node.next.prev = node
        return node

    # 从链表中移除 self
    def remove(self) -> None:
        self.prev.next = self.next
        self.next.prev = self.prev
class TextEditor:

    def __init__(self):
        self.root = self.cur = Node()  # 哨兵节点
        self.root.prev = self.root
        self.root.next = self.root

    def addText(self, text: str) -> None:
        for ch in text:
            self.cur = self.cur.insert(Node(ch))

    def deleteText(self, k: int) -> int:
        k0 = k
        while k and self.cur != self.root:
            self.cur = self.cur.prev
            self.cur.next.remove()
            k -= 1
        return k0 - k
    
    def text(self) -> str:
        s = []
        k, cur = 10, self.cur
        while k and cur != self.root:
            s.append(cur.ch)
            cur = cur.prev
            k -= 1
        return ''.join(reversed(s))

    def cursorLeft(self, k: int) -> str:
        while k and self.cur != self.root:
            self.cur = self.cur.prev
            k -= 1
        return self.text()

    def cursorRight(self, k: int) -> str:
        while k and self.cur.next != self.root:
            self.cur = self.cur.next
            k -= 1
        return self.text()


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)
# @lc code=end

