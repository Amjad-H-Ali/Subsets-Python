print("Subsets!")

# Function takes in three parameters:
# data: the array containing a given set
# subset: an array that will contain the subsets of data
# i: the current index.
# No return value, only prints all subsets
def helper(data, subset, i):

	# When i equals data array length,
	# It means we have found a subset.
	# Print the subset
	if (i == data.length):
		print(subset)