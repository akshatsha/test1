color = ['red','orange','blue','white','red','orange']

def col_count(var):

	j = 0
	for i in var:
			j = j+ 1

	return j

def count_field(var):

        counts = {}
        for i in var:
		if i in counts:
			counts[i] = counts[i] + 1
		else:
			counts[i] = 1

        return counts



count = col_count(color)
print count	

count1 = count_field(color)
print count1

