
def listsum(list):
    '''
     Normal Sum
    '''
    total = 0
    for x in list:
        total = total + x
        
    return total

print (listsum((2,3,3,4,5)))

def listsumR(list):
    '''
    * Recursion sum
    '''   
    if len(list)==1:
        return list[0]
    else:
        return list[0] + listsumR(list[1:])
        

print (listsumR((2,3,3,4,5)))

x = raw_input('presiona enter')