class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        res=len(students)
        cnt=Counter(students)
        for val in sandwiches:
            if cnt[val]>0:
                res-=1
                cnt[val]-=1
            else:
                return res
        return res
     

