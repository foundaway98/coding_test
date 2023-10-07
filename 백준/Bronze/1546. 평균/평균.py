import statistics

n = int(input())
scores = list(map(int,input().split(" ")))
scoreMax = max(scores)
newScores = []
for score in scores:
  newScores.append(score/scoreMax*100)
print(statistics.mean(newScores))