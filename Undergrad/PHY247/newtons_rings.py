radii = [2.51, 2.53, 2.55, 2.565, 2.577, 2.585]
diff_sq = []
for i in range(1, len(radii)):
	diff_sq.append(radii[i]**2 - radii[i-1]**2)
	
print(diff_sq)

lens = 0.5 # 50 cm
lamb = []
for i in range(1, len(diff_sq)):
	lamb.append((radii[i]**2 - radii[0]**2)/(i*lens))
print(lamb)
