class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        counter = Counter(hand)
        for _ in range(int(len(hand) / groupSize)):
            max_counter = max(counter)
            for card_num in range(max_counter, max_counter - groupSize, -1):
                if card_num in counter:
                    if counter[card_num] == 1:
                        del counter[card_num]
                    else:
                        counter[card_num] -= 1
                else: 
                    return False
        return True