class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        myList1 = []
        for i in s:
            myList1.append(i)
        myList1.sort()
        myList2 = []
        for i in t:
            myList2.append(i)
        myList2.sort()

        if myList1 == myList2:
            return True
        else:
            return False

        