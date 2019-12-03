import chardet

# Func
def tsv2txt(torv, s_line):
	json = chardet.detect(s_line)
	try:
		x = s_line.decode(json['encoding']).split("\t")
	except UnicodeDecodeError:
		return
	with open('./dataset/'+torv+x[1]+'.txt', 'a') as f:
		if x[1] != '2':
			try:
				f.write(x[2]+'\t'+x[6]+'\n')
			except UnicodeEncodeError:
				return
		else:	
			try:
				f.write(x[2]+'\t'+x[6]+'\t'+x[9]+'\n')
			except UnicodeEncodeError:
				return

# Main
with open('./material/training_set_rel3.tsv', 'rb') as f:
	line_cnt = 0
	for s_line in f:
		if line_cnt == 0:
			line_cnt += 1
			continue
		if line_cnt % 10 == 0:
			tsv2txt('valid_essay', s_line)
		else:
			tsv2txt('train_essay', s_line)
		line_cnt += 1

