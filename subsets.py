# creates all subsets from defined input set

def getAllSubsets(inputSet):

	result = []

	# If input set is empty -> stop recursion and return empty tuple
	if len(inputSet) == 0:
		return [[]]

	firstItem = inputSet[0]

	for item in getAllSubsets(inputSet[1:]):
		result.append(item + [firstItem]) # append subset with selected item
		result.append(item) # append subset without selected item

	return result


print(getAllSubsets([1,2,3,4]))