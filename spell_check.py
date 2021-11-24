from deepdiff import DeepDiff


def count_letters(word):
    d={}
    for j in set(word):
        d[j]=word.count(j)
    return d        
  
sentence="azərbaycan respublikasının daşınmaz əmlakın dövlət reyestri xidməti hüquqların dövlət qeydiyyatı haqqında daşınmaz əmlakın dövlət reyestrindən çıxarış seriya mh no 0017485 hüquq sahibi (ləri) cəfərov fariz tahar oğlu hüququn növü mülkiyyət hüquq obyektinin adı torpaq sahəsi ünvan (olduğu yer) quba rayonu, zərdabi qəsəbəsi sahəsi (ölçüsü) 8.995724 ha təyinatı (kateqoriyası) kənd təsərrüfatı təyinatlı torpaqlar məqsədli istifadə növü çoxillik əkmələr daşınmaz əmlakın dövlət reyestrində 13 nömrəli reyestr kitabının 137 nömrəli vərəqində qeydiyyata alınmışdır. reyestr nömrəsi 303013003449 qeydiyyat nömrəsi 2808002842 qeydiyyat tarixi 14.04.2008 xaçmaz rayon ərazi idarəsinin rəisi c. abasov qeydiyyat icraçısı ə. əlistanov qeyd: laminasiya olunmasına yol verilmir"
words={}

  
for i in sentence.split():
    words[i]=count_letters(i)


def difference(diff):
    d=list(diff.values())
    if len(d)>=2:
        x=list(d[0])
        y=d[1]
        x.extend(y)
        return len(x)    
    elif len(d)==1:
        return len(d[0])
    else:
        return 0
        

def spell_check(words,example):
    
    d=count_letters(example)
    min_d=len(list(words.keys())[0])    
    
    for i in words.keys():    
        diff=DeepDiff(words[i],d)
        x=difference(diff)
        if x<min_d:
            word=i
            min_d=x

    return word



example="azerbcan"

print("INITIAL WORD::: ",example)
print("--------------------------------")
print("CORRECT WORD::: ",spell_check(words,example))




