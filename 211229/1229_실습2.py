def list_avg(numlist):
    sum = 0
    for x in numlist:
        sum += x
    return sum / len(numlist)

input_score = input()
scores = input_score.split()
score = []
for x in scores :
    score.append(int(x))

print("평균 = %.2f" %list_avg(score))
