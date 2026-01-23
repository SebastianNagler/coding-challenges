class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        heapq.heapify(hand)
        counter = Counter(hand)
        for _ in range(int(len(hand) / groupSize)):
            min_counter = heapq.heappop(hand)
            while min_counter not in counter:
                min_counter = heapq.heappop(hand)
            for card_num in range(min_counter, min_counter + groupSize):
                if card_num in counter:
                    if counter[card_num] == 1:
                        del counter[card_num]
                    else:
                        counter[card_num] -= 1
                else: 
                    return False
        return True