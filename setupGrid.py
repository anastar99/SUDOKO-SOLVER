class SudokoSetup:

    def __init__(self):
        pass

    def find_emtpies(self, nums):
        temp = []

        for i in nums:
            for j in i:
                try:
                    if str(j['aria-label']) == 'empty':
                        temp.append(0)
                    else:
                        temp.append(int(j['aria-label']))

            
                except Exception:
                    continue
        return temp

    def getAllValues():
        pass

    def buildGrid(self, temp):
        puzzle = []
        k = []
        for i in range(len(temp)):
            if (i + 1) % 9 == 0:
                k.append(temp[i])
                puzzle.append(k)
                k = []
            else:
                k.append(temp[i])
        return k