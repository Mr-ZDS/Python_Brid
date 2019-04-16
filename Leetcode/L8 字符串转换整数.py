class Solution:
    def myAtoi(self, str: str) -> int:
        visit = str.replace(' ', '')
        test = ''
        if len(visit) == 0:
            return 0
        if visit[0] == '-' or visit[0] == '+' or visit[0].isdigit():
            test += visit[0]
        else:
            return 0
        for i in range(1, len(visit)):
            if visit[i].isdigit():
                test += visit[i]
        if test == '+' or test == '-':
            return 0

        result = int(test)
        if result > (2 ** 31 - 1):
            return 2 ** 31 - 1
        elif result < (-2) ** 31:
            return (-2) ** 31
        else:
            return result
