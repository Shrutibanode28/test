class Solution:
    def countAndSay(self, n):
        if (n==1):
            return"1"
        res="1"
        for i in range(2,n+1):
            res=self.countandsay(res)
        return res
    def countandsay(self,res):
        count=1
        temp=" "
        for i in range(1,len(res)):
            if(res[i]==res[i-1]):
                count+=1
            else:
                temp+=str(count)+res[i-1]
                count=1
        temp+=str(count)+res[len(res)-1]
        return temp
