punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def strip_punctuation(word):
    for pc in punctuation_chars:
        if pc in word:
            word = word.replace(pc, "")
    return word

def get_neg(sentence):
    ng_cnt=0
    list_sentence = sentence.split(" ")
    for i in range(len(list_sentence)):
        list_sentence[i]=strip_punctuation(list_sentence[i]).lower()    
    for ls in list_sentence:
        if ls in negative_words:
            ng_cnt+=1
    return ng_cnt

def get_pos(sentence):
    ps_cnt=0
    list_sentence = sentence.split(" ")
    for i in range(len(list_sentence)):
        list_sentence[i]=strip_punctuation(list_sentence[i]).lower()    
    for ls in list_sentence:
        if ls in positive_words:
            ps_cnt+=1
    return ps_cnt

dataFile = open("project_twitter_data.csv", "r")
tweets = dataFile.readlines()
header = list(tweets[0].strip().split(","))
outPutFile = open("resulting_data.csv", "w")
outPutFile.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
outPutFile.write("\n")
for tw in tweets[1:]:
    list_tw = list(tw.strip().split(","))
    pc = get_pos(list_tw[0])
    nc = get_neg(list_tw[0])
    net = pc - nc
    row_string = "{}, {}, {}, {}, {}".format(list_tw[1], list_tw[2], pc, nc, net)
    outPutFile.write(row_string)
    outPutFile.write("\n")
outPutFile.close()
dataFile.close()