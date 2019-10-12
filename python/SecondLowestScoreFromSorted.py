if __name__ == '__main__':
    listofstudents = []
    scorelist = []
    for n in range(0,int(input())):
        name = input()
        score = float(input())
        listofstudents+= [(name,score)]
        scorelist+=[score]
    b = sorted(list(set(scorelist)))[1]
    for name1,score1 in sorted(listofstudents):
        if(score1==b):
            print(name1)
