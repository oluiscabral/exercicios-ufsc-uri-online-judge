N = int(input())

seq = [1, 1]

for i in range(1, N-1):
    seq.append(seq[i - 1] + seq[i])

seq.reverse()
output = ""
for i in range(N):
    output += str(seq[i]) + ' '

output = output[:-1]

print(output)
