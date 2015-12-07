filename = '/mnt/testing/mergesort_input.txt'

outputfilename = '/mnt/testing/mergesort_output.txt'

issorted = True
with open(outputfilename) as f:
    lineold = int(f.readline().strip())
    linenew = int(f.readline().strip())
    while(linenew):
        if linenew < lineold:
            issorted = False
            break
        lineold = linenew
        
        linenew = f.readline().strip()
        try:
            linenew = int(linenew)
        except ValueError:
            print(linenew)
    if issorted:
        print('success')
    else:
        print('failure')