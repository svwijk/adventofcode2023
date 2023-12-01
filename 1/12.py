import argparse
import re
from word2number import w2n

numberstrings = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def getfilecontent(location):
    with open(location) as f: return f.readlines()

def getintfromstring(string):
    m = re.finditer(r'(?=(\d|one|two|three|four|five|six|size|seven|eight|nine))', string)
    result = []
    for a in m:
        result.append(a.group(1))
    if result[0] in numberstrings:
        first = str(w2n.word_to_num(result[0]))
    else: first = result[0]
    if result[len(result)-1] in numberstrings:
        last = str(w2n.word_to_num(result[len(result)-1]))
    else: last = result[len(result)-1]

    return int(first + last)

def main():
    parser = argparse.ArgumentParser(description='Get content of file and sum values of each first and last int in string')
    parser.add_argument('-f','--file', required=True, help='full path to input file')
    args = parser.parse_args()
    
    result = 0
    for line in getfilecontent(args.file):
        result += getintfromstring(line)
  
    print(result)
if __name__ == "__main__":
    main()
