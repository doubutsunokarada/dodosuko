import random
import sys

FINISH: int = 1911

count: int = 0
ddsk_list: list = ['ドド', 'スコ']
exit_flg: bool = False
ddsk_sentences: list = []

while not exit_flg:
    index = random.randint(0, 1)
    print(ddsk_list[index], end='')
    ddsk_sentences.append(str(index))
    
    if 11 < count:
        ddsk_sentences.pop(0)
        ddsk_sentence = ''.join(ddsk_sentences)
        if int(ddsk_sentence, 2) == FINISH:
            print('ラブ注入♡')
            exit_flg = True
    count = count + 1

sys.exit()
