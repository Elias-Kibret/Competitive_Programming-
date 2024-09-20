# class Solution:
#     def shortestPalindrome(self, s: str) -> str:
#         countString=Counter(s)
#         value=""
#         length=0
        
        
#         for key , val in countString.items():
#             if val==1 and len(value)==0:
#                 value=str(val)
                
#             elif val%2!=0:
#                 countString[key]=val+1
                
            
#             length+=countString[key]
            
#         sorted_dict=dict(sorted(countString.items(), key=lambda item:item[1], reverse=True))
#         result=[0]*length
        
#         l,r=0,len(result)-1
#         print(sorted_dict)
#         for key,val in sorted_dict.items():
            
#             while val!=0 and l<=r:
#                 print(val)
              
#                 result[l],result[r]=key,key
#                 l+=1
#                 r-=1
#                 val-=2
            
#         print(result)


        
        
#         return "".join(result)
        

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        count = self.kmp(s[::-1], s)
        return s[count:][::-1] + s
    def kmp(self, txt: str, patt: str) -> int:
        new_string = patt + '#' + txt
        pi = [0] * len(new_string)
        i = 1
        k = 0
        while i < len(new_string):
            if new_string[i] == new_string[k]:
                k += 1
                pi[i] = k
                i += 1
            else:
                if k > 0:
                    k = pi[k - 1]
                else:
                    pi[i] = 0
                    i += 1
        return pi[-1]