class solution(object):
 def isnumber(self,s):
     s=s.strip()
     try:
         s=float(s)
         return True
        
     except:
        return False
ob=solution()
print(ob.isnumber("0"))
print(ob.isnumber("e"))
print(ob.isnumber(""))
print(ob.isnumber("."))
print(ob.isnumber("%"))
