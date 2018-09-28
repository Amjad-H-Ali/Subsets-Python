print("Subsets!")

# Recursive function
# Function takes in three parameters:
# data: the array containing a given set
# subset: an array that will contain the subsets of data
# i: the current index.
# No return value, only prints all subsets
def helper(data, subset, i):

	# When i equals data array length,
	# It means we have found a subset.
	# Print the subset
	if (i == len(data)):
		print(subset)

	else:
		# For the subsets containing nothing
		subset[i] = None

		helper(data, subset, i + 1)	

		# When we add values to the subset
		subset[i] = data[i]

		helper(data, subset, i + 1)

# Wrapper function that we will call
# Takes in one parameter
# data: the array containing a given set
# It will call helper function
def subsets(data):
	# Empty array same length as data array
	subset = [None] * len(data)

	# i will start at 0 because that is the first index in array
	helper(data, subset, 0)


subsets([1, 2])

print("-------------------")

subsets(["monkey", "banana"])

print("-------------------")

subsets(['a', 'b', 'c', 'd'])