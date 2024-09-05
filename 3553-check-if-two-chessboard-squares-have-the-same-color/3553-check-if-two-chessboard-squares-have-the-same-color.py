class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:

        # odd odd --white
        # even even --white
        # odd even black
        # even odd black

        def getColor(s:str)->str:
            print(ord(s[0]))
            
            if (ord(s[0])-97)%2==0 and int(s[1])%2==0 or (ord(s[0])-97)%2!=0 and int(s[1])%2!=0:
                print('white')
                return "white"
            print('black')

            return "black"
        
        return getColor(coordinate1)==getColor(coordinate2)

        