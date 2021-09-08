from queue import PriorityQueue
class Calculate:
    ''' this class contains method for comparing input text to the generated triagrams corpus'''
    rank = PriorityQueue()
    def __init__(self,corpus,input):
        ''' this method finds the most similar documents to our input text and returns the similarity percentage in a similarity queue'''
        for name in corpus:
            o = corpus[name]
            q = 0
            for t in input:
                if t in o:
                    q+=1
            self.rank.put((q/len(input)*100,name))
