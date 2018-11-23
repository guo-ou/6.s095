#Programming for the Puzzled -- Srini Devadas
#You Will All Conform
#Input is a vector of F's and B's, in terms of forwards and backwards caps
#Output is a set of commands (printed out) to get either all F's or all B's
#Fewest commands are the goal

caps = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'B', 'F', 'B']
cap2 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'F', 'F',
        'F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'F', 'F']
cap3 = ['F', 'F', 'B', 'H', 'B', 'F', 'B', 'B', 'B', 'F', 'H', 'F', 'F']

def pleaseConformOpt(caps):
    #Initialization
    start = 0
    forward = 0
    backward = 0
    intervals = []

    caps = caps + ['END']

    #Determine intervals where caps are on in the same direction
    for i in range(1, len(caps)):
        if caps[start] != caps[i]:
            # each interval is a tuple with 3 elements (start, end, type)
            intervals.append((start, i - 1, caps[start]))
            
            if caps[start] == 'F':
                forward += 1
            else:
                backward += 1
            start = i

    if forward < backward:
        flip = 'F'
    else:
        flip = 'B'
    for t in intervals:
        if t[2] == flip:
            #Exercise: if t[0] == t[1] change the printing!
            if t[0] == t[1]:
                print ('Person at position', t[0], 'flip your cap!')
            else:
                print ('People in positions', t[0], 'through', t[1], 'flip your caps!')


def pleaseConformOnepass(caps):
    if len(caps) == 0:
        return
    caps = caps + [caps[0]]
    count = 0
    m = 0
    msg = ''
    for i in range(1, len(caps)):
        count += 1
        if caps[i] != caps[i-1]:
            if m == 0:
                m = count
#            print('\n', m, count,'\n')
            if count-m == 1:
                print('Person at position', i-1, 'flip your cap!')
                count = 0
                m = 0
                continue
            if caps[i] != caps[0]:
                msg = 'People in positions {:d}'.format(i)
            else:
                print(msg,'through', i-1, 'flip your caps!')
                count = 0
                m = 0

                           
#pleaseConformOpt(caps)
pleaseConformOnepass(caps)
