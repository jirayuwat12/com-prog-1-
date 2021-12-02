class Tweet:
    def __init__(self,tweet):
        self.id = tweet['id']
        self.words = tweet['words']
        self.time = tweet['time']
        self.user = tweet['user']
        
    def __lt__(self,rhs):
        l = self.time.split(' ')
        l[0] = l[0].split('-')
        l[1] = l[1].split(':')
        r = rhs.time.split(' ')
        r[0] = r[0].split('-')
        r[1] = r[1].split(':')
        if int(l[0][0]) > int(r[0][0]): # year
            return False
        elif int(l[0][0]) == int(r[0][0]):
            if int(l[0][1]) > int(r[0][1]): #month
                return False
            elif int(l[0][1]) == int(r[0][1]):
                if int(l[0][2]) > int(r[0][2]): #day
                    return False
                elif int(l[0][2]) == int(r[0][2]):
                    if int(l[1][0]) > int(r[1][0]): #hours
                        return False
                    elif int(l[1][0]) == int(r[1][0]):
                        if int(l[1][1]) > int(r[1][1]):
                            return False
                        elif int(l[1][1]) == int(r[1][1]):
                            return len(self.words) < len(rhs.words)
        return True
    def __str__(self):
        return self.time+': ['+self.user+'] '+' '.join(self.words)+' ('+str(self.id)+')'

    def similarity(self,other):
        u = set()
        i = list()
        for x in self.words:
            if x in other.words:
                i.append(x)
            u.add(x)
        for x in other.words:
            u.add(x)
        return len(i) / len(list(u))

def find_similarity(tweets):
    ret = []
    for i in range(len(tweets)):
        for j in range(i+1,len(tweets)):
            ret.append((tweets[i].similarity(tweets[j]),(min(tweets[i].id,tweets[j].id),max(tweets[i].id,tweets[j].id))))
    return sorted(ret)

def show_tweets(tweets):
    tweets = sorted(tweets)
    for z in tweets:
        print(z)



tw1=Tweet({'id':1,'user':'abc','words':['this','is','a','blockchain','made','from','scratch','in','~50','lines','of','python','code'],'time':'2021-11-18 16:38'})
tw2=Tweet({'id':2,'user':'cdg','words':['javascript', 'java', 'python', 'php', 'and', 'their', 'learning', 'curves'],'time':'2021-11-06 14:28'})
tw3=Tweet({'id':3,'user':'def123','words':['python', 'and', 'javascript'],'time':'2021-11-01 07:56'})
tw4=Tweet({'id':4,'user':'def123','words':['only','python'],'time':'2021-11-01 07:56'})
tweets=[tw1,tw2,tw3,tw4]

