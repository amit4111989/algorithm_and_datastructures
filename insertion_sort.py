import sys


#Insertion Sort

def insertion_sort(X):

	for i in range(1,len(X)):

		key = X[i]
		j = i-1

		while j>=0 and X[j]>key:

			X[j+1] = X[j] #A[i+1] = A[i]
			j = j -1

		X[j+1] = key

	return X


if __name__=="__main__":

	arr = sys.argv[1]
	arr = map(int, arr)
	print insertion_sort(arr)
