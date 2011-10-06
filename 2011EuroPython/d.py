import sys


def main():
    args = sys.argv[1:]
    if len(args)<2:
        print 'Usage: python d.py input.in output.out'
        sys.exit(1)
    inputFile = open(args[0],'rU')
    outputFile = open(args[1],'w')
    T = int(inputFile.readline().strip())
    for t in xrange(T):
        N = int(inputFile.readline().strip())
        fks = inputFile.readline().split()
        monks = {}
        for n in xrange(N):
            fk = int(fks[n]) - 1
            if fk not in monks:
                monks[fk] = []
            monks[fk].append(n)
        outputFile.write('Case #%d:\n' % (t+1))
        for d in xrange(N):
            stack = []
            visited = []
            visited.append(d)
            if d in monks:
                stack = monks[d][:]
                while len(stack)>0:
                    m = stack.pop(0)  #it doesn't matter from where we are removing items
                    if m not in visited:
                        if m in monks:
                            stack += monks[m][:]
                        visited.append(m)
            outputFile.write('%d\n' % (len(visited)))
    outputFile.close()
    inputFile.close()

if __name__ == '__main__':
    main()
