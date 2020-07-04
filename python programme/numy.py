def num_p(group,int):
     for value in group:
         if int == value:
             return True
     return False    




print(num_p([1,2,3,4,5],3))
print(num_p([1,4,6,9,5],2))        