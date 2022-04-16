f1_maximas = [0.54, 1.62, 2.713, 3.79, 4.85, 5.94]
f1 = 1e6
# distance was in mm, convert into metres
lambda_vals = [(2e-3)*(f1_maximas[i] - f1_maximas[i-1]) for i in range(1, len(f1_maximas))]
v1_vals = [(f1* val) for val in lambda_vals]
print(lambda_vals)
print(v1_vals)
