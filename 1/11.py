import argparse
import re

def getfilecontent(location):
    with open(location) as f: return f.readlines()
    

def getintfromstring(string):
    m = re.findall(r'\d', string)
    r =  m[0]+m[len(m)-1]
    return int(r)
    
    


def main():
    parser = argparse.ArgumentParser(description='Get content of file and sum values of each first and last int in string')
    parser.add_argument('-f','--file', required=True, help='full path to input file')
    args = parser.parse_args()
    


    result = 0
    for line in getfilecontent(args.file):
         #print(getintfromstring(line))
         result += getintfromstring(line)

    print(result)

if __name__ == "__main__":
    main()
