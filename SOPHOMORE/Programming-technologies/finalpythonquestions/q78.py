lines = []
# input the number of lines
N = int(input())
#input the lines
for i in range(N):
    lines.append(input())
# find the length of longest line 
max_len = 0
for line in lines:
    max_len = max(max_len, len(line)) 
print("Number of characters in longest line is", max_len)