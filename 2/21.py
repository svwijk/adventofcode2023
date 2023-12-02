import argparse

allresults = {}
goodgames = []

def getfilecontent(location):
    with open(location) as f: return f.read().splitlines()

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

def suminvalidthrowsgames(list: list):
    allresult = 0
    for item in list:
        allresult += int(item)
    return(allresult)

def main():
    parser = argparse.ArgumentParser(description='Get content of file and sum values of each first and last int in string')
    parser.add_argument('-f','--file', required=True, help='full path to input file')
    args = parser.parse_args()

    for line in getfilecontent(args.file):
        addcontenttodict(line)
    retrieveinvalidthrows(allresults)
    #print(goodgames)
    print(suminvalidthrowsgames(goodgames))

if __name__ == "__main__":
    main()
