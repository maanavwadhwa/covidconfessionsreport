from math import log2
import requests
import datetime
from helpers import getQuarterlyDates
import time

# Define the subreddit and API endpoint
subreddit = 'confessions'
api_url = 'https://api.pushshift.io/reddit/search/submission/'

# Define the date range
start_year = 2018
end_year = 2022

yearlyCounts = {2018: 35630, 2019:66178, 2020: 63246, 2021:56828, 2022: 84690}
iCounts = {}
linkages = {}
i = 'cheated'
j = 'boyfriend'

#Fetch the total number of posts per year with i as the query term. Used to calculate P(i), the linkage denominator
params = {
    'subreddit': subreddit,
    'size': 1000,
    'metadata': True,
    'after': int(datetime.datetime(2018,1,1,0,0,0).timestamp()),
    'before': int(datetime.datetime(2022,12,31,23,59,59).timestamp()),
    'q': i,
    'track_total_hits': True,
    'calendar_histogram': '1y' #buckets the data
}
response = requests.get(api_url, params=params)
buckets = response.json()['metadata']['es']['aggregations']['calendar_histogram']['buckets']
count = 0
for bucket in buckets:
    iCounts[start_year+count] = bucket['doc_count']
    count+=1

# Loop through each year, fetch all posts with query term of j and see how many have word i
postCounts = dict()
for year in range(start_year, end_year + 1):
    count = 0
    dates = getQuarterlyDates(year)
    postCounts[year]= 0
    for datePair in dates:
        #Pause in between requests to make sure requests finish
        time.sleep(1)
        params = {
            'subreddit': subreddit,
            'size': 1000,
            'metadata': True,
            'after': int(datePair[0].timestamp()),
            'before': int(datePair[1].timestamp()),
            'q': j,
            'track_total_hits': True
        }
        response = requests.get(api_url, params=params)
        metadata = response.json()['metadata']
        print(metadata['es']['hits']['total']['value'])
        if response.status_code == 200:
            data = response.json()['data']
            postCounts[year] += len(data)                
            for post in data:
                x= post['title'].lower()
                y= post['selftext'].lower()
                if i in x or i in y:
                    count+=1
    probIGivenJ = count / postCounts[year]
    probI = iCounts[year]/yearlyCounts[year]
    linkages[year] = log2(probIGivenJ/probI)

#Print linkages
print(linkages[year])