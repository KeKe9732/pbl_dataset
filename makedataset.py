# Func
def tsv2txt(torv, s_line):
    s = s_line.split("\t")
    with open('./dataset/'+torv+s[1]+'.txt', 'a') as f:
        if s[1] != '2':
            f.write(s[2]+'\t'+s[6]+'\n')
        else:	
            f.write(s[2]+'\t'+s[6]+'\t'+s[9]+'\n')

# Main
with open('./material/training_set_rel3.tsv', encoding="utf8", errors='ignore') as f:
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

with open('./material/valid_set.tsv', encoding="utf8", errors='ignore') as f:
    line_cnt = 0
    for s_line in f:
        if line_cnt == 0:
            line_cnt += 1
            continue
        s = s_line.split("\t")
        with open('./dataset/test_essay'+s[1]+'.txt', 'a') as f:
            if x[1] != '2':
                sc = score[s[3]+','+s[0]]
                f.write(x[2]+'\t'+sc+'\n')
            else:
                s1 = score[x[3]+','+x[0]]
                s2 = score[x[4].strip()+','+x[0]]
                f.write(x[2]+'\t'+s1+'\t'+s2+'\n')
        line_cnt += 1
