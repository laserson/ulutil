# BLAT tools
# based on Sri's code

import subprocess
import os

hg_idx = '~/genome/hg19.2bit'

def start_gfServer(file2idx,tileSize=7,stepSize=2,minMatch=1,maxGap=4):
    params = (tileSize,stepSize,minMatch,maxGap,file2idx)
    cmd = "gfServer -tileSize=%i -stepSize=%i -minMatch=%i -maxGap=%i start localhost 17779 %s" % params
    p = subprocess.Popen(cmd,shell=True)
    return p

def stop_gfServer(p):
    cmd = "gfServer stop localhost 17779"
    q = subprocess.Popen(cmd,shell=True)
    return q

def poll_sequence(seq,file2idx,minScore=10,minIdentity=70):
    nibdir = os.path.dirname(file2idx)
    params = (minScore,minIdentity,nibdir)
    cmd = "gfClient -minScore=%i -minIdentity=%i -nohead localhost 17779 %s /dev/stdin /dev/stdout" % params
    import sys
    print "About to initiate command"
    sys.stdout.flush()
    p = subprocess.Popen(cmd,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
    print "Initiated command.  Will now communicate with process."
    sys.stdout.flush()
    import cStringIO
    p.stdin.write(cStringIO.StringIO(">query\n%s" % seq).read())
    # p.communicate(">query\n%s" % seq)
    print "Finished communicating.  Waiting now..."
    sys.stdout.flush()
    
    print p.stdout.read()
    
    num = 0
    for line in p.stdout:
        print "Reading output..."
        sys.stdout.flush()
        num += 1
    
    print "Finished with output.  Returning"
    sys.stdout.flush()
    
    return num