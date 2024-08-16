class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique=set()

        for email in emails:
            [local,domain]=email.split("@")
            
            buildLocal=""

            for char in local:
                if char=='+':
                    break
                if char!=".":
                    buildLocal+=char
            unique.add(tuple((buildLocal,domain)))
        return len(unique)

            



    

                   
            
                





    


        
        