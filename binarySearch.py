#an easy example of how to implement binary search with recursion metod

def BinarySearch(MyList,Myitem):

    if len(MyList) == 0:
	return False , "not found"
    else:
	midpoint = len(MyList)//2
	if MyList[midpoint] == Myitem:
	    found = True
	    return True, midpoint
        else:	    
            if Myitem > MyList[midpoint]:
		return BinarySearch(MyList[midpoint+1:],Myitem)
	    else:
		return BinarySearch(MyList[:midpoint],Myitem)

listToS = [17,20,30,35,42,53,78,]
datatoSearch = 35

print (BinarySearch(listToS,datatoSearch))

