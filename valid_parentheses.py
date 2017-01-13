class Solution(object):
    # 从左到右读string，是不是左括号？ 是，就存到stack里面
    # 如果是右括号 （重点：第一个右括号一定stack里面最后一个左括号相匹配）： 如果pop() 是匹配的左括号 && stack is not empty, then, that's valid

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in range(len(s)):
            if s[i] == "{" or s[i] == "(" or s[i] == "[":
                stack.append(s[i])
            elif s[i] == "}":
                if stack == [] or stack.pop() != "{":
                    return False
            elif s[i] == ")":
                if stack == [] or stack.pop() != "(":
                    return False
            elif s[i] == "]":
                if stack == [] or stack.pop() != "[":
                    return False
        if stack:
            return False
        else:
            return True

if __name__ == "__main__":
    print(Solution().isValid("{(25})"))
    print(Solution().isValid("{(25)}"))
