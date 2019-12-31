import hangman
 
def test_secret_word_no_punctuation():
    with open("/tmp/words.txt","w") as f:
        for i in ["word'one", "word_two", "wordthree"]:
            f.write(i+"\n")
    selected_word = hangman.get_secret_word('/tmp/words.txt')
    assert selected_word == "wordthree"
 
def test_secret_word_atleast_five():
    with open("/tmp/words.txt","w") as f:
        for i in ["wo", "wor", "word", "bigword"]:
            f.write(i+"\n")
    selected_word = hangman.get_secret_word('/tmp/words.txt')
    assert selected_word == "bigword"
 
def test_secret_word_lowercase():
    with open("/tmp/words.txt","w") as f:
        for i in ["Wording", "wOrding", "WORDING", "wording"]:
            f.write(i+"\n")
    selected_word = hangman.get_secret_word('/tmp/words.txt')
    assert selected_word == "wording"
 
def test_secret_word_no_repeat():
    with open("/tmp/words.txt","w") as f:
        for i in ["disaster","recall","advise","national","infrastructure","shots","fired", "federation", "duress"]:
            f.write(i+"\n")
    l = []
    for i in range(3):
        l.append(hangman.get_secret_word('/tmp/words.txt'))
    assert len(set(l)) == 3
     
 
 
 
def test_mask_word_no_guesses():
    assert hangman.mask_word("elephant", []) == "________"
    assert hangman.mask_word("animal",[]) == "______"
    
def test_mask_word_guess_double_letter():
    assert hangman.mask_word("elephant",["e"]) == "e_e_____"

def test_mask_word_guess_single_letter():
    assert hangman.mask_word("elephant",["p"]) == "___p____"

def test_mask_word_second_guess_right():
    assert hangman.mask_word("elephant",["e","x","l"]) == "ele_____" 


def test_status():
    a = hangman.status(sw = "elephant",cg = ["e","l"],wg = ["x"],turns=6)
    e = """
ele_____
Guesses : e l x
Turns left : 6 
"""
    assert a == e

def test_move_correct_guess_win():
    cg,wg,game_over,turns,msg = hangman.move(sw="cat",cg=["c","t"],wg=["x"],ng=["a"],turns=6)

    assert cg == ["c","t","a"]
    assert wg == ["x"]
    assert game_over == True
    assert turns == 6
    assert msg == "You win"

def test_move_correct_guess_normal():
    cg,wg,game_over,turns,msg = hangman.move(sw="cat",cg=["c"],wg=["x"],ng=["t"],turns=6)

    assert cg == ["c","t"]
    assert wg == ["x"]
    assert game_over == False
    assert turns == 6

def test_move_wrong_guess_normal():
    cg,wg,game_over,turns,msg = hangman.move(sw="cat",cg=["c"],wg=["x"],ng=["l"],turns=6)

    assert cg == ["c"]
    assert wg == ["x","l"]
    assert game_over == False
    assert turns == 5

def test_move_wrong_guess_lose():
    cg,wg,game_over,turns,msg = hangman.move(sw="cat",cg=["c"],wg=["x","m","n","o","r","y"],ng=["l"],turns=1)

    assert cg == ["c"]
    assert wg == ["x","m","n","o","r","y","l"]
    assert game_over == True
    assert turns == 0
    
def test_move_repeat_correct_normal():
    cg,wg,game_over,turns,msg = hangman.move(sw="cat",cg=["c"],wg=["x"],ng=["c"],turns=6)

    assert cg == ["c"]
    assert wg == ["x"]
    assert game_over == False
    assert turns == 6
    
def test_move_repeat_wrong_normal():
    cg,wg,game_over,turns,msg = hangman.move(sw="cat",cg=["c"],wg=["x"],ng=["x"],turns=6)

    assert cg == ["c"]
    assert wg == ["x"]
    assert game_over == False
    assert turns == 6

