from typing import List


class Solution:

    left = right = 0

    def moveRight(self, arr) -> bool:
        self.right += 1
        return self.checkIndex(arr)

    def checkIndex(self, arr) -> bool:
        return False if self.right == len(arr) else True

    def isDuplicated(self, arr) -> bool:
        return True if arr[self.left] == arr[self.right] else False

    def changeNumber(self, arr):
        self.left += 1
        arr[self.left] = arr[self.right]

    def removeDuplicates(self, arr: List[int]) -> int:
        while self.moveRight(arr):
            if self.isDuplicated(arr):
                continue
            self.changeNumber(arr)

        return self.left + 1
