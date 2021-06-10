prep = ["of", "at", "with"]
adj = ["mean", "lean", "green"]
noun = ["cow", "alice", "book"]
verb = ["lifted", "saw", "found"]
adv = ["quickly", "carefully", "brilliantly"]

'''
<sentence>    -->  <subject> <verb_phrase> <object>
    <subject>     -->  <noun_phrase>
    <verb_phrase> -->  <verb> | <verb> <adv>
    <object>      -->  <noun_phrase>
    <verb>        -->  lifted | saw | found
    <adv>         -->  quickly | carefully | brilliantly
    <noun_phrase> -->  [<adj_phrase>] <noun> [<prep_phrase>]
    <noun>        -->  cow | alice | book
    <adj_phrase>  -->  <adj> | <adj> <adj_phrase>
    <adj>         -->  green | lean | mean
    <prep_phrase> -->  <prep> <noun_phrase>
    <prep>        -->  of | at | with
'''

input = "mean cow saw carefully green alice with book".split()
# input = "alice found mean green book".split()
# input = "alice book found".split()
input_idx = 0
nt = input[0]
output = ""
invalid_token = False
invalid_s = False
nt_none = False


def lexical():
    global input_idx
    global nt
    global invalid_token
    input_idx += 1
    if(input_idx < len(input)):
        if ((nt not in adj) and (nt not in verb) and (nt not in noun) and (nt not in adv) and (nt not in prep)):
            print(nt)
            invalid_token = True
        nt = input[input_idx]
    else:
        nt = None


def isToken(t):

    if ((t not in adj) and (t not in verb) and (t not in noun) and (t not in adv) and (t not in prep)):
        return False
    return True
# def peek():


def parseSentence():
    global nt
    global output
    output += "(("
    nounPhrase()
    output += ")"

    verbPhrase()

    output += "("
    nounPhrase()
    output += "))"

    if (invalid_token):
        print("invalid token")
    else:
        print(output)


def verbPhrase():
    global nt
    global output
    output += "("
    if nt in verb:
        output += '"' + nt + '"'
        lexical()
    if nt in adv:
        output += '"' + nt + '"'
        lexical()
    output += ")"


def adjPhrase():
    global nt
    global output
    global invalid_token
    global invalid_s
    if (nt in adj):
        output += "("
        parse()
        adjPhrase()
        output += ")"
    elif isToken(nt):
        invalid_token = True
        return
    elif nt in noun:
        return
    else:
        invalid_s = True


def parse():
    global output
    global nt
    # if (nt in adj):
    output += '"' + nt + '"'
    lexical()


def parseAdj():
    global output
    global nt
    # if (nt in adj):
    output += '"' + nt + '"'
    lexical()
    # else:
    #     print("invalid sentence")


def prepPhrase():
    global nt
    global output
    if (nt in prep):
        output += "("
        parse()
        nounPhrase()
        output += ")"


def parsePrep():
    global output
    global nt
    # if (nt in prep):
    output += '"' + nt + '"'
    lexical()
    # else:
    #     print("invalid sentence")


def nounPhrase():
    global nt
    global output
    # if nt:
    output += "("
    if(nt in adj):
        adjPhrase()
    if(nt in noun):
        parse()
    if(nt in prep):
        prepPhrase()
    output += ")"


parseSentence()
# adjPhrase()
# print(f"{output}")
