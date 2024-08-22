class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # direction=set()

        # for val in path:
        #     if val in direction:
        #         return True
        #     else:
        #         direction.add(val)
        # return False
        

        direction={
            "N":[0,1],
            "E":[1,0],
            "W":[-1,0],
            "S":[0,-1]
        }

        # if len(path)<1:
        #     return True
        # result=direction[path[0]]
        # print(result)

        # for i in range(1,len(path)):
        #     result[0]=result[0]+direction[path[i]][0]
        #     result[1]=result[1]+direction[path[i]][1]
        #     if result[0]==0 and result[1]==0:
        #         return True
        # return False

        # visit=set()
        # x,y=0,0

        # for d in path:
        #     visit.add((x,y))

        #     dx,dy=direction[d]

        #     x,y=x+dx,y+dy

        #     if (x,y) in visit:
        #         return True
        # return False


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        curr = [0, 0]
        visit = {tuple(curr)}
        
        for p in path:
            if p == "N":
                curr[0] += 1
            elif p == "S":
                curr[0] -= 1
            elif p == "E":
                curr[1] += 1
            else:
                curr[1] -= 1
            if tuple(curr) not in visit:
                visit.add(tuple(curr))
            else:
                return True
        
        return False