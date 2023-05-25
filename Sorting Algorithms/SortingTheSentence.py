class Solution(object):
    def sortSentence(self, s):
        y = s.split()
        srt = [None] * len(y)

        for i in range(len(y)):
            srt[int(y[i][-1]) - 1] = y[i][:-1]

        return " ".join(srt) 