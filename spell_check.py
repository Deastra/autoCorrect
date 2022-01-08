from deepdiff import DeepDiff


# Count letters of words to dictionary
def count_letters(word):
    d={}
    for j in set(word):
        d[j]=word.count(j)
    return d        
  
words={}

f=open("data.txt","r",encoding="utf8") # Read data

# Process data for database of words
sentence=" ".join(f.readlines())


# Building dictionary of words with count number of letters in it
for i in sentence.split():
    words[i]=count_letters(i)

# number of differences in values of words_differences
def new_old_value(d):
    sum_len=0
    for v in d.values():
        sum_len+=(abs(v["new_value"]-v["old_value"]))
    return sum_len

# Finding differences of two words
# Returning value of difference as an integer
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
        
# Correcting word with the less difference value
# (To the similar word, by its letters)
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


##################

# Using lower method (all the words in data are lowercase, so it depends on data of words and an example)
example = "corretc exmpaplE".lower()


print(example)

print("###########################\n\n\n\n")

# Checking each word and correcting them based on words dictionary
sent="" 
for i in example.split():
    
    sent+=spell_check(words,i)+" "

print("Corrected")
print(sent) # Corrected sentence

#####################
Y_true = 'Correct Example'


# Checking the accuracy
from thefuzz import fuzz
from thefuzz import process

print("######################################")
print("######################################")
print("######################################")

print("Standart Ratio")
print(fuzz.ratio(Y_true,sent))

print("######################################")


print("Sorted Token Ratio")
print(fuzz.token_sort_ratio(Y_true,sent))