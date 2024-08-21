class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start_city=set()
        for citys in paths:
            if citys[0] not in start_city:
                start_city.add(citys[0])
        for citys in paths:
            if citys[1] not in start_city:
                return citys[1]
        return ""
        