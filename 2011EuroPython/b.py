import sys


def main():
    args = sys.argv[1:]
    if len(args) < 2:
        print 'Usage: b.py input output'
        sys.exit(1)
    inputFile = open(args[0],'rU')
    outputFile = open(args[1], 'w')
    noTestCases = int(inputFile.readline().strip())
    for t in xrange(noTestCases):
        #prepare output
        print 'Case #%d\n' % (t + 1)
        outputFile.write('Case #%d:\n' % (t+1));
        #start reading entries
        noEntries = int(inputFile.readline().strip())
        if noEntries < 2:
            outputFile.write('""\n')
            inputFile.readline()
            continue
        #more than one entry
        subsets = {}
        for n in xrange(noEntries):
            entry = inputFile.readline().strip().upper()
            entryLength = len(entry)
            for startIndex in xrange(entryLength):
                for subLength in xrange(entryLength-startIndex):
                    subString = entry[startIndex:startIndex+subLength+1]
                    if subString in subsets:
                        if subsets[subString] != n:
                            subsets[subString] = 1000
                    else:
                        subsets[subString] = n
        #extrct result
        result = {}
        for s in subsets:
            entryIndex = subsets[s]
            if entryIndex < 1000:
                if entryIndex not in result:
                    result[entryIndex] = []
                result[entryIndex].append(s)
        for i in xrange(noEntries):
            if i in result:
                vals = result[i]
                vals = sorted(vals,key=(lambda x: (len(x),x)))
                #print i, vals
                outputFile.write('"%s"\n'% (vals[0]))
            else:
                outputFile.write(':(\n')
    inputFile.close()
    outputFile.close()


if __name__ == '__main__':
    main()
