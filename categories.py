import requests
import time

from helpers import getBiWeeklyDates
from cleanedCategories import newCategories

# Define the subreddit and API endpoint
subreddit = 'confessions'
api_url = 'https://api.pushshift.io/reddit/search/submission/'

# Define the date range
start_year = 2018
end_year = 2022

# Initialize counters for each year
yearly_counts = {year: 0 for year in range(start_year, end_year + 1)}
bucket = {b:0 for b in ['1-10','10-20','20-40', '40-60', '60-80', '80-100', '>100']}

# Loop through each year
postCounts = dict()
numComments = dict()
averageCommentsPerPost = dict()
commentCounts = dict()
wordCount = dict()
for year in range(start_year, end_year + 1):
    totalWords=0
    totalWordsInPosts = 0
    postCount = 0
    dates = getBiWeeklyDates(year)
    postCounts[year] = dict()
    numComments[year]= dict()
    averageCommentsPerPost[year]= dict()
    commentCounts[year]= dict()
    for category in newCategories:
        postCounts[year][category]= 0
        numComments[year][category]= 0
        averageCommentsPerPost[year][category] = 0
        commentCounts[year][category] = dict()
    for datePair in dates:
        print(datePair)
        time.sleep(2)
        params = {
            'subreddit': subreddit,
            'size': 1000,
            'metadata': True,
            'after': int(datePair[0].timestamp()),
            'before': int(datePair[1].timestamp()),
        }
        response = requests.get(api_url, params=params)
        if response.status_code == 200:
            data = response.json()['data']
            for post in data:
                x= post['title'].lower().split(' ')
                y= post['selftext'].lower().split(' ')
                totalWordsInPosts += len(x) + len(y)
                postCount += 1
                totalWords+=len(set(x+y))
                for category in newCategories:
                    for word in newCategories[category]:
                        if word in x or word in y:
                            wordCount[word]=wordCount.get(word,0)+1
                            numCommentsOnPost = post['num_comments']
                            postCounts[year][category]+=1
                            numComments[year][category]+=numCommentsOnPost
                            break
    for category in newCategories:
        averageCommentsPerPost[year][category] = numComments[year][category]/postCounts[year][category]

print(postCounts)
print(averageCommentsPerPost)
print(commentCounts)
print(sorted(wordCount.items(), key = lambda x:x[1], reverse = True))
print(totalWords)
print(postCount)
print(totalWordsInPosts/postCount)

