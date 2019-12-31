import random
 
def get_secret_word(word_file="/usr/share/dict/words"):
    good_words = []
    with open(word_file) as f:
        for word in f:
            word = word.strip()
            if not word.isalpha():
                continue
            if len(word) < 5:
                continue
            if word[0].isupper():
                continue
            good_words.append(word)
 
    word = random.choice(good_words)
    return word.lower()

def mask_word(secret_word, guesses):
    if guesses == []:
        return "_" * len(secret_word)
    else:
        for i in secret_word:
            if i not in guesses:
                secret_word = secret_word.replace(i,"_")
        return secret_word
                
def status(sw,cg,wg,turns):
    m = mask_word(sw,cg+wg)
    g = " ".join(cg+wg)
    t = 7 - len(wg)
    status_msg ="""
{}
Guesses : {}
Turns left : {} 
""".format(m,g,t)
    return status_msg


def move(sw,cg,wg,ng,turns):
    game_over = False
    msg = ""
    if ng[0] not in cg+wg:
        if ng[0] in sw:
            cg = cg + ng
            guesses = cg + wg
            w = mask_word(sw,guesses)
            if "_" not in w:
                game_over = True
                msg = "You win"
            else:
                game_over = False
        else:
            wg = wg + ng
            turns = 7 - len(wg)
            if turns == 0:
                game_over = True
                msg = "You lose , The word is {}".format(sw)
    return cg,wg,game_over,turns,msg


    
