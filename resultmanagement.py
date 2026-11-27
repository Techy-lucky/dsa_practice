class Node:
    def __init__(self,value):
        self.left = None
        self.data = value
        self.right = None

class examresultmanagement:
    def __init__(self):
        self.root = None

    def score_insert(self,new_node):
        if self.root is None:
            self.root = new_node
        else:
            temp = self.root
            while True:
                if new_node.data < temp.data:
                    if temp.left is None:
                        temp.left = new_node
                        return
                    temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = new_node
                        return
                    temp = temp.right

    def ascending_score(self,rt):
        if rt is None:
            return
        self.ascending_score(rt.left)
        print(rt.data,end=" ")
        self.ascending_score(rt.right)

    def highest_lowest_score(self,rt):
        if rt is None:
            return
        temp = rt
        while temp.left:
            temp = temp.left
        print("\nLowest : ",temp.data)
        temp = rt
        while temp.right:
            temp = temp.right
        print("Highest : ",temp.data)      

    def score_count(self,rt):
        if rt is None:
            return 0 
        count = 0
        if rt.data > 50:
            count = 1
        return (count + self.score_count(rt.left) + self.score_count(rt.right))

    def search_score(self,key):
        temp = self.root
        while temp:
            if temp.data == key:
                return True
            elif key < temp.data:
                temp = temp.left
            else:
                temp = temp.right
        return False 

    def averageofscore(self,rt):
            if rt is None:
                return 0
            return(rt.data +self.averageofscore(rt.left)+self.averageofscore(rt.right))
    def studentcount(self,rt):
            if rt is None:
                return 0
            return(1 + self.studentcount(rt.left)+ self.studentcount(rt.right))


result = examresultmanagement()
result.score_insert(Node(45))
result.score_insert(Node(78))
result.score_insert(Node(32))
result.score_insert(Node(89))
result.score_insert(Node(56))
result.score_insert(Node(92))
result.score_insert(Node(67))
result.score_insert(Node(34))
result.score_insert(Node(85))
result.score_insert(Node(73))
result.score_insert(Node(61))
result.score_insert(Node(98))

print("score in ascending order : ")
result.ascending_score(result.root)
print()
result.highest_lowest_score(result.root)

print("\nstudent score above 50 is",result.score_count(result.root))
print()
print("search result : ")
if result.search_score(374):
    print("Score was founded")
else:
    print("Score was not found")
print()

StudentScore = result.averageofscore(result.root)
StudentCount = result.studentcount(result.root)
Average = StudentScore/StudentCount
print("Average Score : ",Average)