from sys import stdin
import random
from datetime import datetime
import argparse

def lt(a,b,i,typ):
	if typ == 'i' or typ == 'int':
		return int(a[i]) < int(b[i])
	elif typ == 'f' or typ == 'float':
		return float(a[i]) < float(b[i])		
	else:
		return a[i] < b[i]



def selection_sort(a,ii):
	n = len(a)
	for i in range(n):
		min_i = i
		for j in range(i+1,n):
			if lt(a[j],a[min_i],ii):
				min_i = j
		a[i],a[min_i] = a[min_i],a[i]
	return a

def insert_sort(a,ii):
	n = len(a)
	for i in range(n):
		j = i
		while j>0 and lt(a[i],a[j-1],ii):
			a[j],a[j-1] = a[j-1],a[j]
			j-=1
	return a

def shell_sort(a,ii):
	N = len(a)
	h = 1
	while h<N//3:
		h = h*3+1
	while h>=1:
		for t in range(h,N):
			j = t
			while j>=h and lt(a[j],a[j-h],ii):
				a[j],a[j-h] = a[j-h],a[j]
				j-=h
		h//=3

	return a


def merge(a,lo,mid,hi,aux,ii,typ):
	i = lo
	j = mid+1
	aux[lo:hi+1] = a[lo:hi+1]
	for k in range(lo,hi+1):
		if i>mid:
			a[k] = aux[j]
			j+=1
		elif j>hi:
			a[k] = aux[i]
			i+=1
		elif lt(aux[j],aux[i],ii,typ):
			a[k] = aux[j]
			j+=1
		else:
			a[k] = aux[i]
			i += 1


def m_sort(a,lo,hi,aux,ii,typ):
	if hi<=lo:return
	mid = lo + (hi-lo)//2
	m_sort(a,lo,mid,aux,ii,typ)
	m_sort(a,mid+1,hi,aux,ii,typ)
	merge(a,lo,mid,hi,aux,ii,typ)



def merge_sort(a,ii,typ):
	aux = [0]*len(a)
	m_sort(a,0,len(a)-1,aux,ii,typ)
	return a



#quick
def partition(a,lo,hi,ii):
	i = lo+1
	j = hi
	v = a[lo][4]
	while True:
		while i<=j and a[i][ii]<=v:
			i+=1
		while i<=j and a[j][ii]>=v:
			j-=1
		if i<=j:
			a[i],a[j] = a[j],a[i]
		else:break
	a[lo],a[j] = a[j],a[lo]
	return j

def q_sort(a,lo,hi,ii):
	if hi<=lo:return
	j = partition(a,lo,hi,ii)
	q_sort(a,lo,j-1,ii)
	q_sort(a,j+1,hi,ii)

def quick_sort(a,ii):
	random.shuffle(a)
	quick_sort_iter2(a,0,len(a)-1,ii)
	return a



def quick_sort_iter(a,lo,hi,ii):
	size = len(a)
	stack = [0]*size
	top = -1
	top+=1
	stack[top] = lo
	top+=1
	stack[top] = hi
	while top>=0:
		hi = stack[top]
		top-=1
		lo = stack[top]
		j = partition(a,lo,hi,ii)
		if j-1>lo:
			top+=1
			stack[top] = lo
			top+=1
			stack[top] = j-1
		if j+1 < hi:
			top+=1
			stack[top] = j+1
			top+=1
			stack[top] = hi



def quick_sort_iter2(a,lo,hi,ii):
	size = len(a)
	stack = []
	stack.append([lo,hi])
	while len(stack)>0:
		lo,hi = stack.pop()
		j = partition(a,lo,hi,ii)
		if j-1>lo:
			stack.append([lo,j-1])
		if j+1 < hi:
			stack.append([j+1,hi])



if __name__ == '__main__':
	
	parser = argparse.ArgumentParser(description='SMTH')
			
	parser.add_argument('m',type=int,help='m')
	parser.add_argument('i',type=int,help='i')
	parser.add_argument('--more','-m',action='count',default=0)
	parser.add_argument('--type','-type','-verbosity',type=str)
	args = parser.parse_args()
	a = []
	m = args.m
	i = args.i
	for line in stdin:
		a.append(line.split())
	a.pop(0)
	a = merge_sort(a,i,args.type)
	if args.more == 1:
		beg = len(a)-1
		goal = len(a)-m-1
		step = -1
	else:
		beg = 0
		goal = m
		step = 1
	for el in range(beg,goal,step):
		print(' '.join(a[el]))
