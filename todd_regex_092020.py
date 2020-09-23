import re

fh = open("regex_sum_974075.txt")

linesum = 0

for line in fh:
    ln = line.rstrip()    
    ss = re.findall('[0-9]+', ln)
    if len(ss) >= 1:             
      for nums in ss:
         linesum += int(nums)

print(linesum)