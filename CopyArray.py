def Copy(Array):
	NewArray = []
	for X in range(0, len(Array)):
		NewArray.append(Array[X])

	return NewArray

Array = [1, 5, 3, 7, 2, 6, 2, 7, 7 , 2, 3, 1, 6, 2, 6]
CopyArray = Copy(Array)

print(Array)
print(CopyArray)
	
