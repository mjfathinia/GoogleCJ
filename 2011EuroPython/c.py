import sys

def checkSpell(entry):
    positions = []
    for i,l in enumerate(entry):
        if l in 'aoeiu':
            positions.append(i)
    for i in xrange(len(positions)-2):
        startIndex = positions[i]
        endIndex = positions[i+1]+1
        startWord = entry[startIndex:endIndex]
        searchIndex = positions[i+2]+1
        try:
            spell = entry.index(startWord,searchIndex)
            return 'Spell!'
        except ValueError:
            continue
    return 'Nothing.'

def main():
    args = sys.argv[1:]
    if len(args)<2:
        print 'Usage: python c.py input.in output.out'
        sys.exit(1)
    inputFile = open(args[0],'rU')
    outputFile = open(args[1],'w')
    T = int(inputFile.readline().strip())
    for t in xrange(T):
        entry = inputFile.readline().strip()
        outputFile.write('Case #%d: %s\n' % (t+1,checkSpell(entry)))
    inputFile.close()
    outputFile.close()

if __name__ == '__main__':
    main()
