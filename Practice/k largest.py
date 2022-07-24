def hasArrayTwoCandidates(arr, n, x):
		# code her
    for item in arr:
        difference=x-item
        if(difference!=item):
            pos=arr.count(difference)
            if(pos>=1):
                return True
        if(difference==item):
            arr.pop(item)
            pos=arr.count(difference)
            if(pos>=1):
                return True
        return False

print(hasArrayTwoCandidates(arr=[1,2,5,6,7],n=5,x=4))