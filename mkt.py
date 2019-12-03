import chardet

score = {}
with open('./material/valid_score.txt', 'rb') as f:
	line_cnt = 1
	for s_line in f:
		if line_cnt == 1:
			line_cnt += 1
			continue
		x = s_line.decode().split('\t')
		key = x[0]+','+x[1]
		score[key] = x[4].strip()
		line_cnt += 1

with open('./material/valid_set.tsv', 'rb') as f:
	line_cnt = 0
	for s_line in f: 
		if line_cnt == 0:
			line_cnt += 1
			continue
		json = chardet.detect(s_line)
		try:
			x = s_line.decode(json['encoding']).split("\t")
		except UnicodeDecodeError:
			continue
		with open('./dataset/test_essay'+x[1]+'.txt', 'a') as f:
			if x[1] != '2':
				s = score[x[3]+','+x[0]]
				try:
					f.write(x[2]+'\t'+s+'\n')
				except UnicodeEncodeError:
					continue
			else:
				s1 = score[x[3]+','+x[0]]
				s2 = score[x[4].strip()+','+x[0]]
				try:
					f.write(x[2]+'\t'+s1+'\t'+s2+'\n')
				except UnicodeEncodeError:
					continue
		line_cnt += 1
