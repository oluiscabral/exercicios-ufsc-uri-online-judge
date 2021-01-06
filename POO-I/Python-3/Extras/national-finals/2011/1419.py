class Streak:
    def __init__(self, peak):
        self.__peak = peak
        self.__value = None
        self.__count = 0

    def compare(self, value):
        if self.__value is None or self.__value != value:
            self.__value = value
            self.__count = 1
            self.__reached_peak = False
        else:
            self.__count += 1

        if self.__count == self.__peak:
            self.__count = 1
            return True
        return False

    def get(self):
        return self.__count


while True:
    R = int(input())
    if R == 0:
        break

    M = [int(w) for w in input().split()]
    L = [int(w) for w in input().split()]

    mark_power = 0
    leti_power = 0

    got_extra = False
    mark_streak = Streak(3)
    leti_streak = Streak(3)

    for i in range(R):
        mark_power += M[i]
        leti_power += L[i]
        if not got_extra:
            mark_streak_peak = mark_streak.compare(M[i])
            leti_streak_peak = leti_streak.compare(L[i])
            if mark_streak_peak or leti_streak_peak:
                got_extra = True
                if not mark_streak_peak or not leti_streak_peak:
                    if mark_streak_peak:
                        mark_power += 30
                    else:
                        leti_power += 30

    if mark_power != leti_power:
        if mark_power > leti_power:
            print('M')
        else:
            print('L')
    else:
        print('T')
