import string
import os
from nltk.corpus import stopwords
eng_words = stopwords.words('english')


with open('stopwords.txt','r',encoding = 'UTF-8') as text_file:
    eng_words = [line.rstrip() for line in text_file]
print(eng_words)


def distill_tweet(tweet):
    words = tweet.translate(tweet.maketrans('\"\'', ' ' * 2, '.,!?"')).lower().split()
    result = words
    for word in result:
        if word in eng_words or word.startswith('http') or word.isnumeric():
            result.pop(result.index(word))
    return result

def tweet_lists(filename): #this code works, don't change it, but you need to use it
    result = []
    cur_name = ''
    with open(filename, 'r') as file:
        for line in file:
            line = line.split('\t')
            user = line[1]
            tweet = line[2]
            if user == cur_name:
                cur = open(user + '.txt', 'a')
            else:
                if cur_name != '':
                    cur.close()
                cur_name = user
                result += [user]
                cur = open(user + '.txt', 'w')
            cur.writelines(tweet + '\n')
            cur.close()
    return result
#print(tweet_lists('ALBUQUERQUEON.txt'))

def top_entries(tweets, num_cutoff = 1, hashes = False, mentions = False):
    
    dictHashtag = {}
    dictMentions = {}
    dictAscii = {}

    if hashes == True:
        if type(tweets) is list:
            newTweets = ' '.join(tweets)
            entryHash = distill_tweet(newTweets) 
            
        if type(tweets) is str:
            entryHash = distill_tweet(tweets)
            
        hashList = [word for word in entryHash if word.startswith('#')]
        
        for entry in hashList:
            if entry not in dictHashtag:
                dictHashtag[entry] = 1 #All values in dictHashtag have a starting value of 1. Only repeats will go to the else command chain

            else:
                dictHashtag[entry] += 1 #if there are repeats, add to counter by increments of 1

        for hashtag in dictHashtag.copy(): #condition for num_counter
            if dictHashtag[hashtag] < num_cutoff: #If the values corresponding to the keys are smaller than the indicated cutoff counter
                del dictHashtag[hashtag] #delete from the dictionary...error "dictionary changed size during iteration"...don't we want this? #FIXED, used dict.copy() method
                
        return dictHashtag

    if hashes == False and mentions == True:
        
        if type(tweets) is list:
            newTweets = ' '.join(tweets)
            entryMentions = distill_tweet(newTweets)

        if type(tweets) is str:
            entryMentions = distill_tweet(tweets)

        mentionList = [word for word in entryMentions if word.startswith('@')]

        for entry in mentionList:
            if entry not in dictMentions:
                dictMentions[entry] = 1
            else:
                dictMentions[entry] += 1

        for mention in dictMentions.copy():
            if dictMentions[mention] < num_cutoff:
                del dictMentions[mention]
                
        return dictMentions
    
    if hashes == False and mentions == False:
        
        if type(tweets) is list:
            newTweets = ' '.join(tweets)
            entryAscii = distill_tweet(newTweets)
            
        if type(tweets) is str:
            entryAscii = distill_tweet(tweets)

        asciiList = [word for word in entryAscii if word.isalpha()]

        for entry in asciiList:
            if entry not in dictAscii:
                dictAscii[entry] = 1
            else:
                dictAscii[entry] += 1
        
        for alphabet in dictAscii.copy():
            
            if dictAscii[alphabet] < num_cutoff:
                
                del dictAscii[alphabet]
                
        return dictAscii
    
def tweets_from_file(filename):

    with open(filename, 'r', encoding = 'UTF8') as text_file:
        tweetList = [word.rstrip() for word in text_file]
        return tweetList
    
print(tweets_from_file('SAMPLE.txt'))
print(top_entries(tweets_from_file('SAMPLE.txt'), hashes = False, mentions = False, num_cutoff = 2))


#Bibliography:
#https://www.w3schools.com/python/ref_string_join.asp
#https://www.w3schools.com/python/python_ref_dictionary.asp
#https://izziswift.com/how-to-avoid-runtimeerror-dictionary-changed-size-during-iteration-error/
#https://chercher.tech/python-programming/python-special-characters


