def rotate(arr,num):
    new_arr = []
    for item in range(len(arr)):
    	print(item)
        if (item+num) >= len(arr):
        	a = (len(arr)-1) - item
        	b = num - a
        	new_arr[b] = arr[item]
        	print(new_arr)
        else:
        	new_arr[item+num] = arr[item]
        	print(arr)
        
    return new_arr

rotate([1,2,3,4], 2)
