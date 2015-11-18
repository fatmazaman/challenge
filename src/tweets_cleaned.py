# example of program that calculates the number of tweets cleaned

#open the file 
tweets = open("tweets.txt", 'r').readlines()
#print tweets
s = str(tweets).strip('[]')
print(s.decode('unicode_escape').encode('ascii','ignore'))




'''#tokenize the file

tokenized_tweets = tweets.split(" ")
#print tokenized_tweets

# store the value of file in list
mod_data = []
for row in tokenized_tweets:
    split_row  = row.split('\n')
    mod_data.append(split_row)
#print mod_data 

#function to remove punctuation
no_punctuation_tokens = []
def remove_punctuation(token):
  
    token = token.replace(".", "")
    token = token.replace(",", "")
    token = token.replace("'", "")
    token = token.replace("'", "")
    token = token.replace(";", "") 
    token = token.replace("\n","")
    token = token.replace("/","")
    return token.lower()


#    
for token in mod_data:
    token = remove_punctuation(token)
    no_punctuation_tokens.append(token) 
    
print no_punctuation_tokens

#unique value(unicode)
def uniq_val(l):
    return list(set(l))
print uniq_val(no_punctuation_tokens)'''


