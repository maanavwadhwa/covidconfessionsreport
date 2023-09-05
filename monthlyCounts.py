import string
import time
import requests
from helpers import notGood, getMonthlyDates

# Define the subreddit and API endpoint
subreddit = 'confessions'
api_url = 'https://api.pushshift.io/reddit/search/submission/'

# Define the date range
start_year = 2020
end_year = 2020

# Loop through each year
month = 0
cleanedNotGood = [word.translate(str.maketrans('', '', string.punctuation)).lower() for word in notGood]
for year in range(start_year, end_year + 1):
    dates = getMonthlyDates(year)
    for datePair in dates:
        month+=1
        d = dict()
        onlyTitleWords = dict()
        totalWords = 0
        totalWordsTitle = 0
        allTitleWords = set()
        allBothWords = set()
        time.sleep(2)
        print(datePair)
        params = {
            'subreddit': subreddit,
            'size': 1000,
            'metadata': True,
            'after': int(datePair[0].timestamp()),
            'before': int(datePair[1].timestamp()),
            'track_total_hits':True
        }
        response = requests.get(api_url, params=params)
        if response.status_code == 200:
            data = response.json()['data']
            # print(data[0])
            for post in data:
                x= post['title'].lower().split(' ')
                y= post['selftext'].lower().split(' ')
                allBothWords.update(set(y))
                allTitleWords.update(set(x))
                for word in set(x+y):
                    if word not in cleanedNotGood: #and word in wordsIn2018:
                        cleanWord = word.translate(str.maketrans('', '', string.punctuation))
                        if cleanWord!='':
                            d[cleanWord] = d.get(cleanWord,0)+1
                for word in set(x):
                    if word not in cleanedNotGood: #and word in wordsIn2018:
                        cleanWord = word.translate(str.maketrans('', '', string.punctuation))
                        if cleanWord!='':
                            onlyTitleWords[cleanWord] = onlyTitleWords.get(cleanWord,0)+1

            print(f"{month}-{year}, total words both:", len(allBothWords))
            print(f"{month}-{year}, total words title:", len(allTitleWords))

            sorted_dict_both = dict(sorted(d.items(), key = lambda x:x[1], reverse = True))
            sorted_dict_title = dict(sorted(onlyTitleWords.items(), key = lambda x:x[1], reverse = True))

            with open(f"{month}-{year}_both.csv", 'w') as f:
                for key in sorted_dict_both.keys():
                    f.write("%s,%s\n"%(key,sorted_dict_both[key]))
                f.close()
            with open(f"{month}-{year}_title.csv", 'w') as f:
                for key in sorted_dict_title.keys():
                    f.write("%s,%s\n"%(key,sorted_dict_title[key]))
                f.close()