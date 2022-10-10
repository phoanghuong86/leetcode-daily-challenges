class Solution:
    def breakPalindrome(self, p: str) -> str:
        if len(p) == 1:
            return ""

        answer = []

        if p == p[::-1]:
            p = list(p)
            k = [i for i in p]

            for i in range(0, len(p)):
                if p[i] != 'a':
                    p[i] = 'a'
                    answer.append(''.join(p))
                    break

            k[-1] = 'b'
            answer.append(''.join(k))
            print(answer)

            t = list(set(answer[0]))

            if len(t) == 1 and t[0] == 'a':
                return answer[1]

            print(min(answer))
            return (min(answer))

        else:
            return p
