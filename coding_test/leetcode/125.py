class Solution:
    def isPalindrome(self, s: str) -> bool:
        # [1] 슬라이싱을 이용한 방법
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]

        # [2] Deque를 이용한 방법
        # strs: Deque = collections.deque()
        #
        # for char in s:
        #     if char.isalnum():
        #         strs.append(char.lower())
        #
        # while len(strs) > 1:
        #     if strs.popleft() != strs.pop():
        #         return False
        #
        # return True

        # [1] list를 이용한 방법
        # strs = []
        #
        # for char in s:
        #     if char.isalnum():
        #         strs.append(char.lower())
        #
        # while len(strs) > 1:
        #     if strs.pop(0) != strs.pop():
        #         return False
        #
        # return True