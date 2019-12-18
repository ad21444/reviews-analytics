data = []
count = 0
length = 0
with open ('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print(count)
print('總共有',len(data),'筆資料')
for i in data:
	length +=len(i)

print(length / len(data))
print(data[12058])