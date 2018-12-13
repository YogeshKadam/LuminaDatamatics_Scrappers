#First line should contain number of tweets.
#Followed by N lines, each containing user name and tweet id separated by a space.

from collections import defaultdict
no_of_testcases = int(input())
list_of_all_cases = []

for no in range(no_of_testcases):
    no_of_tweets = int(input())
    dict1=defaultdict(int)
    for tweets in range(no_of_tweets):
        user_tweet = input()
        user_name,user_tweet_id = user_tweet.split(' ')[0],user_tweet.split(' ')[1]
        dict1[user_name]+=1
    list_of_all_cases.append(dict1)
	
for dicts in list_of_all_cases:
    max_tweets_no=max(dicts.values())
    list1=[k for k,v in dicts.items() if v==max_tweets_no]
    list1.sort()
    print ("***************OUTPUT***********************")
    for li in list1:
        print (li," ",max_tweets_no)
		
		
"""
OUTPUT
D:\YK Python\SteelEye>python3 avinash_bhosale_test.py
2
4
yk id_1
ky id_2
yk id_3
yk id_4
5
a id_5
b id_6
a id_7
b id_8
c id_9
***************OUTPUT***********************
yk   3
***************OUTPUT***********************
a   2
b   2
"""