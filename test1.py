def Barray(n):
	n=len(arr)
	mid=n//2
	new_arr=[]
	suml=0
	for i in range(0,mid):
		suml=suml+arr[i]
	new_arr.append(suml)
	sumr=0
	for j in range(mid,n):
		sumr=sumr+arr[j]
	new_arr.append(sumr)
	t1=max(new_arr)
	t2=min(new_arr)
	print(new_arr)
	if t1==t2:
		print(" the array is balanced ")
	else:
		print("the minimum required value for balance arr = ",t1-t2)
arr=[]
sizeofarr=int(input("enter the size of array = "))
for z in range(sizeofarr):
	val=int(input("enter the value = "))
	arr.append(val)
Barray(arr)

