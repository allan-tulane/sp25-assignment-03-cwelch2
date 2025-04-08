import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    if S == "":
        return len(T)
    elif T == "":
        return len(S)
    elif S[0] == T[0]:
        return MED(S[1:], T[1:])
    else:
        insert = MED(S, T[1:])
        delete = MED(S[1:], T)
        substitute = MED(S[1:], T[1:])
        return 1 + min(insert, delete, substitute)


def fast_MED(S, T, MED={}):
    # Top-down memoization
    key = (S, T)
    if key in MED:
        return MED[key]
    if S == "":
        MED[key] = len(T)
    elif T == "":
        MED[key] = len(S)
    elif S[0] == T[0]:
        MED[key] = fast_MED(S[1:], T[1:], MED)
    else:
        insert = fast_MED(S, T[1:], MED)
        delete = fast_MED(S[1:], T, MED)
        substitute = fast_MED(S[1:], T[1:], MED)
        MED[key] = 1 + min(insert, delete, substitute)
    return MED[key]


def fast_align_MED(S, T, MED={}):
    key = (S, T)
    if key in MED:
        return MED[key]

    if S == "":
        MED[key] = (len(T), ("-" * len(T), T))
        return MED[key]
    if T == "":
        MED[key] = (len(S), (S, "-" * len(S)))
        return MED[key]
    if S[0] == T[0]:
        dist, (aS, aT) = fast_align_MED(S[1:], T[1:], MED)
        MED[key] = (dist, (S[0] + aS, T[0] + aT))
    else:
        # try insert, delete, substitute
        insert_dist, (insert_S, insert_T) = fast_align_MED(S, T[1:], MED)
        delete_dist, (delete_S, delete_T) = fast_align_MED(S[1:], T, MED)
        sub_dist, (sub_S, sub_T) = fast_align_MED(S[1:], T[1:], MED)

        # add edit and choose the best
        insert = (1 + insert_dist, ("-" + insert_S, T[0] + insert_T))
        delete = (1 + delete_dist, (S[0] + delete_S, "-" + delete_T))
        substitute = (1 + sub_dist, (S[0] + sub_S, T[0] + sub_T))

        MED[key] = min(insert, delete, substitute, key=lambda x: x[0])

    return MED[key]

