# pbl_dataset
cat ./asap-aes/training_set_rel3.tsv | iconv -f ISO-8859-1 -t UTF-8 | sed -e 's/\t/????/g' | ./mosesdecoder/scripts/tokenizer/remove-non-printing-char.perl | sed -e 's/????/\t/g' > tmp.tsv
cat ./asap-aes/valid_set.tsv | iconv -f ISO-8859-1 -t UTF-8 | sed -e 's/\t/????/g' | ./mosesdecoder/scripts/tokenizer/remove-non-printing-char.perl | sed -e 's/????/\t/g' > tmp_valid.tsv
