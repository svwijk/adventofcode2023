import argparse

allresults = {}
goodgames = []
powerlist = []

def getfilecontent(location):
    with open(location) as f: return f.read().splitlines()

#knwon bug: apperently all throws get added to the list twice. luckily it doesnt matter for the result
def addcontenttodict(string: str):
    gamenumber =  string.split(':')[0].split('Game ')[1]
    allgameresults = string.split(':')[1]
    reveallist = []
    for reveal in allgameresults.split(";"):
      d = {}
      for dice in reveal.split(','):
          kv = dice.split(' ')
          d[kv[2]]=int(kv[1])
          reveallist.append(d)
    allresults[gamenumber] = reveallist

def retrieveinvalidthrows(dict: dict):
    for key in dict:
        badresult = False
        for item in dict[key]:
            if 'red' in item.keys():
                if item['red'] > 12:
                  badresult = True
            if 'green' in item.keys():
                if item['green'] > 13:
                  badresult = True
            if 'blue' in item.keys():
                if item['blue'] > 14:
                  badresult = True
        if not badresult: 
            goodgames.append(key)

def sumlist(list: list):
    allresult = 0
    for item in list:
        allresult += int(item)
    return(allresult)

def getpowerofmaxdice(dict: dict):
    for keys in dict:
        bluemax = 1
        redmax = 1
        greenmax = 1
        for i in dict[keys]:
            for k,v in i.items():
                if k == 'blue':
                    if int(v) > bluemax:
                        bluemax = int(v)
                if k == 'red':
                    if int(v) > redmax:
                        redmax = int(v)
                if k == 'green':
                    if int(v) > greenmax:
                        greenmax = int(v)
        powerlist.append(bluemax * redmax * greenmax)

def main():
    parser = argparse.ArgumentParser(description='Get content of file and sum values of each first and last int in string')
    parser.add_argument('-f','--file', required=True, help='full path to input file')
    args = parser.parse_args()

    for line in getfilecontent(args.file):
        addcontenttodict(line)
    getpowerofmaxdice(allresults)
    print(sumlist(powerlist))


if __name__ == "__main__":
    main()
