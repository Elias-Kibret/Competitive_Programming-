class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand)%groupSize!=0:
            return False
        
        hand.sort()

        card_sets=[[] for _ in range(len(hand)//groupSize)]
     
     

        for card in hand:

            for card_set in card_sets:
                if len(card_set)<groupSize and card not in card_set:
                    card_set.append(card)
                    break

        print(card_sets)    
        for card  in card_sets:
            if len(card)!=groupSize:
                return False

            for  i in range(1,len(card)):
               
                if  card[i]-card[i-1]!=1:
                    return False
        return True
        
        

        