f = open("high.score")

scores = []
while True:
    line = f.readline().strip()
    if line == "":
        break
    parts = line.split()
    if len(parts) == 2:
        initials, score = parts[0], int(parts[1])
        scores.append((initials, score))

scores.sort(key=lambda x: x[1], reverse=True)

high_score = scores[0]
print(f"HIGHSCORE:\n{high_score[0]}: {high_score[1]}\n")

print("SCOREBOARD:")
for initials, score in scores:
    print(f"{initials}: {score}")

f.close()