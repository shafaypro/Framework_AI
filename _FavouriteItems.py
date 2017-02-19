from collections import Counter
Videos = []
def Most_Common(lst):
    data = Counter(lst)
    return data.most_common(1)[0][0]

def getFavouriteVideo():
    with open('Data/Searched_Songs.txt', 'r') as getSongs:
        Lines = getSongs.readlines()
        for i in Lines:
            i = i.replace('\n', '')
            Videos.append(i)
        return (Most_Common(Videos))
