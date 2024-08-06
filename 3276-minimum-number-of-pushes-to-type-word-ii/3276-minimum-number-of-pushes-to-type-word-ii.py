class Solution:
    def minimumPushes(self, word: str) -> int:
        vs=sorted(Counter(word).values(), reverse=True)
        total=0
        for index,val in enumerate(vs):
            total+=val*(index//8+1)
        return total





        # x=Counter(word).most_common()
        # y=Counter(word)
        # print(x)

        # count=2
        # d=defaultdict(list)
        
        # for val,c in x:
        #     print(val)
        #     if count not in d:
        #         d[count]=[val]
        #     else:
        #         d[count].append(val)
        #     count+=1
        #     if count==10:
        #         count=2
        # print(d)
        # res=0
        # for key in d.keys():
        #     for index,val in enumerate(d[key]):
                
        #         res+=(index+1)*y[val]
        # return res

            
        
        
        

        

        
       

        
                
                    
                
            
      
      

      
        
            
    
    



    
        
        