expr_input = input()
parshing_minus=list(expr_input.split('-'))
parshing_plus = []

for expr in parshing_minus:
    if '+' in expr:
        numbers = map(int, expr.split('+'))
        parshing_plus.append(sum(numbers))
    else:
        parshing_plus.append(int(expr))

result = 0
for expr in parshing_plus:
    result -= expr

result += parshing_plus[0] * 2

print(result)



