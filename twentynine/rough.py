for t in range(int(input())):
	n, m = [int(x) for x in input().split()]
	colors = [[] for i in range(n+1)]
	pos = 0
	a = [int(x) for x in input().split()]
	b = [int(x) for x in input().split()]
	for i in range(n):
		if a[i] == b[i]:
			colors[b[i]].append(i)
	for i in range(n):
		if a[i] != b[i]:
			colors[b[i]].append(i)
	print(colors)
	mm = list(map(int, input().split()))
	if len(colors[mm[-1]]) == 0:
		print('NO')
		continue
	lastpos = colors[mm[-1]][-1]
	ans = [0] * m
	for i in range(m - 1, -1, -1):
		c = mm[i]
		#print(c, colors)
		if len(colors[c]) == 0:
			ans[i] = lastpos
		elif len(colors[c]) == 1:
			ans[i] = colors[c][0]
		else:
			ans[i] = colors[c].pop()
	#print(ans)
	for i in range(m):
		a[ans[i]] = mm[i]
	if a == b:
		print('YES\n'+' '.join([str(i+1) for i in ans]))
	else:
		print('NO')


# 6
# 1 1
# 1
# 1
# 1
# 5 2
# 1 2 2 1 1
# 1 2 2 1 1
# 1 2
# 3 3
# 2 2 2
# 2 2 2
# 2 3 2
# 10 5
# 7 3 2 1 7 9 4 2 7 9
# 9 9 2 1 4 9 4 2 3 9
# 9 9 7 4 3
# 5 2
# 1 2 2 1 1
# 1 2 2 1 1
# 3 3
# 6 4
# 3 4 2 4 1 2
# 2 3 1 3 1 1
# 2 2 3 4
