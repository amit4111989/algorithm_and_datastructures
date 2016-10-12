import sys


#Insertion Sort

def merge_sort(X,p,r):
	if p<r:
		q = (p+r)/2
		merge_sort(X,p,q)
		merge_sort(X,q+1,r)
		X = merge(X,p,q,r)
		print X

def merge(X,p,q,r):
	n1 = q-p+1
	n2 = r-q
	#L[1..n1+1],R[1..n2+1]
	a = []
	b = []
	print p,q,r
	for i in range(n1):
		a.append(X[p+i])
	for j in range(n2):
		b.append(X[q+j+1])
	i=0
	j=0
	print a,b
	for k in range(p,r):
		print 'i=',i,'j=',j
		if a[i]<=b[j]:
			X[k] = a[i]
			i = i+1
		else:
			X[k] = b[j]
			j = j+1

	return X



if __name__=="__main__":

	arr = sys.argv[1]
	arr = map(int, arr)
	merge_sort(arr,0,len(arr)-1)
	print arr
