class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drunk=numBottles

        while numBottles>=numExchange:
            numBottles,emptyBottles=divmod(numBottles,numExchange)
            drunk+=numBottles
            numBottles+=emptyBottles
        return drunk
    