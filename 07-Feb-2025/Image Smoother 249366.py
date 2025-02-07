# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row=len(img)
        col=len(img[0])
        def bound(l,r):
            return  0<=l<row and 0<=r<col

        direction=[[-1,0],[1,0],[0,1],[0,-1],[-1,1],[1,1],[-1,-1],[1,-1]]

        matrix=[[0]*col for i in range(row)]

        # for i in range(row):
        #     temp=[0]*col
        #     matrix.append(temp)

        for i in range(row):
            for j in range(col):
                summ= img[i][j]
                count=1
                for left,right in direction :
                    tempi=i+left
                    tempj=j+right
                    if bound(tempi,tempj):
                        summ+=img[tempi][tempj]
                        count+=1
                div=summ//count
                matrix[i][j]=div
        return matrix
            


