import sys

def pushButtons(buttonSequence):
    robotPosition = {'O':1, 'B':1}
    robotTimer = {'O': 0, 'B': 0}
    time = 0
    N = int(buttonSequence[0])
    for i in range(N):
        robot = buttonSequence[2*i+1]
        position = int(buttonSequence[2*i+2])
        travelDistance = abs(position - robotPosition[robot])
        travelDistance -= time -  robotTimer[robot]
        time += max(0,travelDistance) + 1
        robotPosition[robot] = position
        robotTimer[robot] = time
    return time

def main():
    args = sys.argv[1:]
    if len(args) < 2:
        print 'Usage: a.py input output'
        sys.exit(1)
    inputFile = open(args[0],'rU')
    result = []
    T = int(inputFile.readline().strip())
    for t in range(T):
        buttonSequence = inputFile.readline().split()
        result.append('Case #%d: %d\n' % (t+1, pushButtons(buttonSequence)))
    inputFile.close()
    outputFile = open(args[1], 'w')
    outputFile.writelines(result)
    outputFile.close()

if __name__ == '__main__':
    main()


