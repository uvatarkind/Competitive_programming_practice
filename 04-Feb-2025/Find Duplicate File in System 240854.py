# Problem: Find Duplicate File in System - https://leetcode.com/problems/find-duplicate-file-in-system/

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        output=defaultdict(list)
        for path in paths:
            directory,*files = path.split()
            for f in files:
                start= f.find("(")+1
                end= f.find(")")
                key=f[start:end]
                f_type=f[:start-1]
                f_path= directory+"/"+f_type
                output[key].append(f_path)
        res=[]
        for item,value in output.items():
            if len(value)>1:
                res.append(value)
        return res


