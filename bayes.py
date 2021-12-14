
import re
from collections import Counter
import pathlib

cwd = pathlib.Path.cwd()

filename = cwd / "data.txt"


def words(text):
    return re.findall(r"\w+", text.lower())


WORDS = Counter(words(open(filename).read()))


def P(word, N=sum(WORDS.values())):
    "Probability of `word`."
    return WORDS[word] / N


def correction(word):
    "Most probable spelling correction for word."
    return max(candidates(word), key=P)


def candidates(word):
    "Generate possible spelling corrections for word."
    return known([word]) or known(edits1(word)) or known(edits2(word)) or [word]


def known(words):
    "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in WORDS)


def edits1(word):
    "All edits that are one edit away from `word`."
    letters = "abcdefghijklmnopqrstuvxyzəüöğşçı"
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)


def edits2(word):
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))


text = "DAŞINMAZ ƏMLAKIN DÖVLƏT REYESTRİ XIDMƏTİ\nƏMLAK MƏSƏLƏLƏRİ DÖVLƏT KOMITƏSİ YANINDA\nHe h\nasi\naşınr\nmlak\nmaz\nmu\n387\narla)\nAZƏRBAYCAN RESPUBLIKASI\nDAŞINMAZ ƏMLAKIN DÖVLƏT REYESTRI XIDMƏTI\nÇIXARI Ş\nSeriya RX\nNo 1285271\nHüququ rəsmileşdirilen şəxs\nDaşınmaz əmlakın növü\nIsmayılov Tarverdi Güləli oğlu\nDaşınmaz əmlakın ünvanı (olduğu yer)\nTorpaq sahəsi\nDaşınmaz əmlakın mülkiyyət növü\nQuba rayonu, Mirzememmedkənd kəndi\nDaşınmaz əmlakın üzərində hüququn növü\nDaşınmaz əmlakın ümumi sahəsi (kvadratmetrlə)\nTorpaq sahesinin mülkiyyət növü\nTorpaq sahesi üzərində hüququn növü\nXüsusi\nTorpaq sahəsinin kateqoriyası (məqsədli təyinatı)\nMülkiyyət\nTorpaq sahəsinin (ölçüsü, hektarla)\nKand təsərrüfatı teyinatlı torpaqlar\n0.7614\nDaşınmaz emlakın reyestr nömrəsi\n303013081728\nSıra No\nHüquq sahibləri\nHüquq sahibinin adı\nPayı\nümumi birgə\nümumi birgə\nümumi birgə\nümumi birgə\nümumi birgə\nümumi birgə\nIsmayılov Tarverdi Güləli oğlu\nIsmayılov Pervin Tarverdi oğlu\n3\n1\nQeydiyyat nömrəsi Qeydiyyat tarixi\n2818010831\n05.06.2018\nİsmayılova Sevinc Əlibəy qızı\n[Ismayılov Perviz Tarverdi oğlu\nIsmayılova Günel Tarverdi qızı\nIsmayılova Ədilə Gülali qızı\n4\n6.\nDaşınmaz əmlakın dövlət reyestrində 201 nômrəli reyestr kitabının 35 nömrəli vərəqində qeydiyyata alınmışdır.\nRESPUBLIK\nASI\nHEYESTRI\nDOVLƏT\nORBAYCAS\nƏrazi İdarəsinin rəisi\nF.Bağırov\nQeydiyyat icraçısı\nA. Səfərov\nOMIAK Mas\n"


def correctionText(text):
    textSplitSpace = text.split()
    fixed_text = []
    for word in textSplitSpace:
        fixed_text.append(correction(word))
    return " ".join(fixed_text)


from thefuzz import fuzz
from thefuzz import process

print(text)

print("######################################")
print("Corrected")
print("######################################")
print(correctionText(text))

Y_true="DAŞINMAZ ƏMLAKIN DÖVLƏT REYESTRİ XİDMƏTİ Hüquqların Dövlət qeydiyyatı haqqında daşınmaz əmlakın Dövlət reyestrindən ÇIXARIŞ Seriya RX No 1285271 Hüququ rəsmiləşdirən şəxs İsmayılov Tarverdi Güləli oğlu Daşınmaz əmlakın növü Torpaq sahəsi Daşınmaz əmlakın ünvanı (olduğu yer) Quba rayonu Mirzəməmmədkənd kəndi Daşınmaz əmlakın mülkiyyət növü Daşınmaz əmlakın üzərində hüququn növü Daşınmaz əmlakın ümumi sahəsi (kvadratmetrlə) Torpaq sahəsinin mülkiyyət növü Xüsusi Torpaq sahəsinin üzərində hüququn növü Mülkiyyət Torpaq sahəsinin kateqoriyası (məqsədli təyinatı) Kənd təsərrüfatı təyinatlı torpaqlar Torpaq sahəsinin (ölçüsü, hektarla) 0.7614 Daşınmaz əmlakın reyestr nömrəsi 303013081728 Hüquq sahibləri Sıra No Hüquq sahibinin adı Payı Qeydiyyat nömrəsi Qeydiyyat tarixi 1 İsmayılov Tarverdi Güləli oğlu ümumi birgə 2818010831 05.06.2018 2 İsmayılov Pərvin Tarverdi oğlu ümumi birgə 3 İsmayılova Sevinc Əlibəy qızı ümumi birgə 4 İsmayılov Pərviz Tarverdi oğlu ümumi birgə 5 İsmayılova Günel Tarverdi qızı ümumi birgə 6 İsmayılova Ədilə Güləli qızı ümumi birgə Daşınmaz əmlakın dövlət reyestrində 201 nömrəli reyestr kitabının 35 nömrəli vərəqində qeydiyyata alınmışdır. Ərazi İdarəsinin rəisi F.Bağırov Qeydiyyat icraçısı A.Səfərov".casefold()

print("######################################")
print("######################################")
print("######################################")


result=correctionText(text).casefold()
print("Standart Ratio")

print(fuzz.ratio(Y_true,result))

print("######################################")


print("Sorted Token Ratio")
print(fuzz.token_sort_ratio(Y_true,result))


#%%

from thefuzz import fuzz
from thefuzz import process

print(fuzz.token_set_ratio("i a","a i c"))

