

a = {'1':{'20': {'31':{'90':0,
                        '91':0},
                '32':{'92':0},},
        '21':{ '33':{'92':0},},
        '24':0,
        }}


import pprint
pp = pprint.PrettyPrinter(depth=6)
pp.pprint(a)


result=dict()
rowspan= dict()






def collapsedict(d):
        collapse = dict()
        update = False
        for i in d:
                if isinstance(d[i], dict):
                        for j in d[i].keys():
                                grp = "%s.%s" % (i, j)
                                collapse[ grp ] = d[i][j]
                                dotgrp = grp.split('.')
                                for h in range(1, len(dotgrp)+1):
                                        subdotgrp = '.'.join(dotgrp[:h])
                                        if subdotgrp in rowspan:
                                                rowspan[ subdotgrp ] += 1
                                        else:
                                                rowspan[ subdotgrp ] = 1
                                update = True
                else:
                        collapse[i] = d[i]
                        #rowspan[ i ] = 1
        return (update, collapse)




(update, ret) = collapsedict(a)
print ret
print rowspan
(update, ret2) = collapsedict(ret)
print ret2
print rowspan


exit()
def recurse(a, result):
        (update, ret) = collapsedict(a)
        if update:
                recurse(ret, result)
        else:
                result.update(ret)




#recurse(a, result)




lines = result.keys()
lines.sort()
for i in lines:
        print i
print rowspan
rowspan = dict()

for i in lines:
    dotgrp = i.split('.')
    for h in range(1, len(dotgrp)+1):

        subdotgrp = '.'.join(dotgrp[:h]) + '.'
        for k in lines:
            if k.startswith(subdotgroup):

                if subdotgrp in rowspan:
                    rowspan[ subdotgrp ] += 1




print rowspan











