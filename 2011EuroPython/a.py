import sys

def findRuler(country):
    lastChar = country.lower()[-1]
    if lastChar == 'y':
        return 'nobody'
    elif lastChar in 'aieou':
        return 'a queen'
    else:
        return 'a king'

def main():
    args = sys.argv[1:]
    if len(args) < 2:
        print 'Usage: a.py input output'
        sys.exit(1)
    inputFile = open(args[0],'rU')
    result = []
    T = int(inputFile.readline().strip())
    for t in range(T):
        country = inputFile.readline().strip()
        result.append('Case #%d: %s is ruled by %s.\n' % (t+1,country,findRuler(country)))
    inputFile.close()
    outputFile = open(args[1], 'w')
    outputFile.writelines(result)
    outputFile.close()

if __name__ == '__main__':
    main()


