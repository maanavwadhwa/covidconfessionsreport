import datetime

def getYearlyDates(year):
    return [[datetime.datetime(year, 1, 1), datetime.datetime(year,12, 31, 23,59,59)]]

def getMonthlyDates(year):
    d = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30, 10:31,11:30,12:31}
    return [[datetime.datetime(year, a, 1), datetime.datetime(year, a, d[a], 23,59,59)] for a in range(1,13)]

def getWeeklyDates(year):
    d = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30, 10:31,11:30,12:31}
    dates = []
    for a in range(1,13):
        dates.append([datetime.datetime(year, a, 1), datetime.datetime(year, a, 7,23,59,59)])
        dates.append([datetime.datetime(year, a, 8), datetime.datetime(year, a, 14,23,59,59)])
        dates.append([datetime.datetime(year, a, 15), datetime.datetime(year, a, 21,23,59,59)])
        dates.append([datetime.datetime(year, a, 22), datetime.datetime(year, a, d[a],23,59,59)])
    return dates
        
def getBiWeeklyDates(year):
    d = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30, 10:31,11:30,12:31}
    dates = []
    for a in range(1,13):
        dates.append([datetime.datetime(year, a, 1), datetime.datetime(year, a, 14,23,59,59)])
        dates.append([datetime.datetime(year, a, 15), datetime.datetime(year, a, d[a],23,59,59)])
    return dates

def getQuarterlyDates(year):
    dates = []
    dates.append([datetime.datetime(year, 1, 1), datetime.datetime(year, 3, 31,23,59,59)])
    dates.append([datetime.datetime(year, 4, 1), datetime.datetime(year, 6, 30,23,59,59)])
    dates.append([datetime.datetime(year, 7, 1), datetime.datetime(year, 9, 30,23,59,59)])
    dates.append([datetime.datetime(year, 10, 1), datetime.datetime(year, 12, 31,23,59,59)])
    return dates

notGood = ["i", "im", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]