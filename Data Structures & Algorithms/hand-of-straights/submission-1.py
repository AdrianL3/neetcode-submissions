class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        frequencies = {}

        for num in hand:
            if num not in frequencies:
                frequencies[num] = 1
            else:
                frequencies[num] += 1

        hand.sort()

        for num in hand:
            if frequencies[num] != 0:

                for i in range(groupSize):
                    if frequencies.get(num + i, 0) == 0:
                        return False
                    frequencies[num + i] -= 1

        return True