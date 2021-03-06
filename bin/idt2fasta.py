# Copyright 2014 Uri Laserson
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys

import seqtools

if len(sys.argv) == 3:
    inhandle = open(sys.argv[1],'r')
    outhandle = open(sys.argv[2],'w')
elif len(sys.argv) == 2:
    inhandle = open(sys.argv[1],'r')
    outhandle = sys.stdout
elif len(sys.argv) == 1:
    inhandle = sys.stdin
    outhandle = sys.stdout

for line in inhandle:
    if line.strip() == '':
        print >>outhandle, ''
        continue
    descr = line.split()[0]
    seq = line.split()[1]
    print >>outhandle, ">%s\n%s" % (descr,seq)
