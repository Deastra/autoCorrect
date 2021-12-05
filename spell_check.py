from deepdiff import DeepDiff
import re

def count_letters(word):
    d={}
    for j in set(word):
        d[j]=word.count(j)
    return d        
  


words={}

f=open("data.txt","r",encoding="utf8")

sentence=" ".join(f.readlines())
sentence+=" "+sentence.upper()


for i in sentence.split():
    words[i]=count_letters(i)


def new_old_value(d):
    sum_len=0
    for v in d.values():
        sum_len+=(abs(v["new_value"]-v["old_value"]))
    return sum_len

def difference(diff):
    d=list(diff.values())

    if len(d)==2:
        x=list(d[0])
        y=d[1]
        x.extend(y)
        return len(x)    
    elif len(d)==1:
        try:
            return new_old_value(d[0])
        except:   
            return len(d[0])
    elif len(d)==3:
        x=list(d[0])
        y=d[1]
        x.extend(y)
        d1=d[2]
        return len(x)+new_old_value(d[2])
    else:
        return 0
        

def spell_check(words,example):
    d=count_letters(example)
    min_d=len(list(words.keys())[0])    
    word=""
    for i in words.keys():    
        diff=DeepDiff(words[i],d)
        x=difference(diff)
        if x<min_d:
            word=i
            min_d=x

    return word

example = "DAŞINMAZ ƏMLAKIN DÖVLƏT REYESTRİ XIDMƏTİ\nƏMLAK MƏSƏLƏLƏRİ DÖVLƏT KOMITƏSİ YANINDA\nHe h\nasi\naşınr\nmlak\nmaz\nmu\n387\narla)\nAZƏRBAYCAN RESPUBLIKASI\nDAŞINMAZ ƏMLAKIN DÖVLƏT REYESTRI XIDMƏTI\nÇIXARI Ş\nSeriya RX\nNo 1285271\nHüququ rəsmileşdirilen şəxs\nDaşınmaz əmlakın növü\nIsmayılov Tarverdi Güləli oğlu\nDaşınmaz əmlakın ünvanı (olduğu yer)\nTorpaq sahəsi\nDaşınmaz əmlakın mülkiyyət növü\nQuba rayonu, Mirzememmedkənd kəndi\nDaşınmaz əmlakın üzərində hüququn növü\nDaşınmaz əmlakın ümumi sahəsi (kvadratmetrlə)\nTorpaq sahesinin mülkiyyət növü\nTorpaq sahesi üzərində hüququn növü\nXüsusi\nTorpaq sahəsinin kateqoriyası (məqsədli təyinatı)\nMülkiyyət\nTorpaq sahəsinin (ölçüsü, hektarla)\nKand təsərrüfatı teyinatlı torpaqlar\n0.7614\nDaşınmaz emlakın reyestr nömrəsi\n303013081728\nSıra No\nHüquq sahibləri\nHüquq sahibinin adı\nPayı\nümumi birgə\nümumi birgə\nümumi birgə\nümumi birgə\nümumi birgə\nümumi birgə\nIsmayılov Tarverdi Güləli oğlu\nIsmayılov Pervin Tarverdi oğlu\n3\n1\nQeydiyyat nömrəsi Qeydiyyat tarixi\n2818010831\n05.06.2018\nİsmayılova Sevinc Əlibəy qızı\n[Ismayılov Perviz Tarverdi oğlu\nIsmayılova Günel Tarverdi qızı\nIsmayılova Ədilə Gülali qızı\n4\n6.\nDaşınmaz əmlakın dövlət reyestrində 201 nômrəli reyestr kitabının 35 nömrəli vərəqində qeydiyyata alınmışdır.\nRESPUBLIK\nASI\nHEYESTRI\nDOVLƏT\nORBAYCAS\nƏrazi İdarəsinin rəisi\nF.Bağırov\nQeydiyyat icraçısı\nA. Səfərov\nOMIAK Mas\n"

# example="danmaz emlakin REyiSTİ XIDMƏTİ\nƏMLAK MƏseLƏRİ DÖVLƏT KOMITƏSİ YANINDA\nHe h\nasi\naşınr\nmlak\nmaz\nmu\n387\narla)\nAZƏRBAYCAN RESPUBLIKASI\nDAŞINMAZ ƏMLAKIN DÖVLƏT REYESTRI XIDMƏTI\nÇIXARI Ş\nSeriya RX\nNo 1285271\nHüququ rəsmileşdirilen şəxs\nDaşınmaz əmlakın növü\nIsmayılov Tarverdi Güləli oğlu\nDaşınmaz əmlakın ünvanı (olduğu yer)\nTorpaq sahəsi\nDaşınmaz əmlakın mülkiyyət növü\nQuba rayonu, Mirzememmedkənd kəndi\nDaşınmaz əmlakın üzərində hüququn növü\nDaşınmaz əmlakın ümumi sahəsi (kvadratmetrlə)\nTorpaq sahesinin mülkiyyət növü\nTorpaq sahesi üzərində hüququn növü\nXüsusi\nTorpaq sahəsinin kateqoriyası (məqsədli təyinatı)\nMülkiyyət\nTorpaq sahəsinin (ölçüsü, hektarla)\nKand təsərrüfatı teyinatlı torpaqlar\n0.7614\nDaşınmaz emlakın reyestr nömrəsi\n303013081728\nSıra No\nHüquq sahibləri\nHüquq sahibinin adı\nPayı\nümumi birgə\nümumi birgə\nümumi birgə\nümumi birgə\nümumi birgə\nümumi birgə\nIsmayılov Tarverdi Güləli oğlu\nIsmayılov Pervin Tarverdi oğlu\n3\n1\nQeydiyyat nömrəsi Qeydiyyat tarixi\n2818010831\n05.06.2018\nİsmayılova Sevinc Əlibəy qızı\n[Ismayılov Perviz Tarverdi oğlu\nIsmayılova Günel Tarverdi qızı\nIsmayılova Ədilə Gülali qızı\n4\n6.\nDaşınmaz əmlakın dövlət reyestrində 201 nômrəli reyestr kitabının 35 nömrəli vərəqində qeydiyyata alınmışdır.\nRESPUBLIK\nASI\nHEYESTRI\nDOVLƏT\nORBAYCAS\nƏrazi İdarəsinin rəisi\nF.Bağırov\nQeydiyyat icraçısı\nA. Səfərov\nOMIAK Mas\n".casefold()
example=example.replace("\n"," ")
 
print(example)

print("###########################\n\n\n\n")

# example1 = "AZERBAYCAN AzErBAYCAN azrbaycan azerbaycan azerbaycn azerbaycn azbaycn azerbn Azbaycan aaazerbaycan azzzerbaycan azzerrbaycan"
# example1="ÇIXARI"

sent=""
for i in example.split():
    
    # print("INITIAL WORD::: ",i)
    # print("CORRECT WORD::: ",spell_check(words,i))
    # print("--------------------------------")
    sent+=spell_check(words,i)+" "

print(sent)


Y_true="DAŞINMAZ ƏMLAKIN DÖVLƏT REYESTRİ XİDMƏTİ Hüquqların Dövlət qeydiyyatı haqqında daşınmaz əmlakın Dövlət reyestrindən ÇIXARIŞ Seriya RX No 1285271 Hüququ rəsmiləşdirən şəxs İsmayılov Tarverdi Güləli oğlu Daşınmaz əmlakın növü Torpaq sahəsi Daşınmaz əmlakın ünvanı (olduğu yer) Quba rayonu Mirzəməmmədkənd kəndi Daşınmaz əmlakın mülkiyyət növü Daşınmaz əmlakın üzərində hüququn növü Daşınmaz əmlakın ümumi sahəsi (kvadratmetrlə) Torpaq sahəsinin mülkiyyət növü Xüsusi Torpaq sahəsinin üzərində hüququn növü Mülkiyyət Torpaq sahəsinin kateqoriyası (məqsədli təyinatı) Kənd təsərrüfatı təyinatlı torpaqlar Torpaq sahəsinin (ölçüsü, hektarla) 0.7614 Daşınmaz əmlakın reyestr nömrəsi 303013081728 Hüquq sahibləri Sıra No Hüquq sahibinin adı Payı Qeydiyyat nömrəsi Qeydiyyat tarixi 1 İsmayılov Tarverdi Güləli oğlu ümumi birgə 2818010831 05.06.2018 2 İsmayılov Pərvin Tarverdi oğlu ümumi birgə 3 İsmayılova Sevinc Əlibəy qızı ümumi birgə 4 İsmayılov Pərviz Tarverdi oğlu ümumi birgə 5 İsmayılova Günel Tarverdi qızı ümumi birgə 6 İsmayılova Ədilə Güləli qızı ümumi birgə Daşınmaz əmlakın dövlət reyestrində 201 nömrəli reyestr kitabının 35 nömrəli vərəqində qeydiyyata alınmışdır. Ərazi İdarəsinin rəisi F.Bağırov Qeydiyyat icraçısı A.Səfərov".casefold()

from thefuzz import fuzz
from thefuzz import process

print(fuzz.ratio("this is a test", "this is a test!"))