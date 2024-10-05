class solution:
    def cookieschild(self,g:list[int],c:list[int])->int:
        g.sort()
        c.sort()

        i=0
        j=066666666666666666666666666666666666666666666666666

        while i<len(g) and j<len(c):
            if c(j)>=g(i):
                i+=1
                j+=1
        return i
