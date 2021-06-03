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

# input = "mean cow saw carefully green alice with book".split()
input = "mean green".split()
input_idx = 0

nt = "mean"
# ct = input[input_idx]
output = ""


def lexical():
    global input_idx
    global nt
    input_idx += 1
    if(input_idx < len(input)):
        nt = input[input_idx]

# def peek():


def parseSentence():
    s = parseSub()
    v = parseVp()
    o = parseObj()

    print(output)


def parseSub():
    pass


def parseVp():
    pass


def parseObj():
    pass

# def nounPhrase():
#     if nt


def adjPhrase():
    global nt
    if (nt in adj):
        parseAdj()
        adjPhrase()
    else:
        return

    # check nt
    # if adj


def parseAdj():
    global output
    global nt
    if (nt in adj):
        output += '("' + nt + '")'
        lexical()

    return


adjPhrase()
