import fraction as fr


sum = fr.create(0,1)
for i in range(int(input())):
    k = fr.inp()
    sum = fr.add(sum, k)
fraction1 = fr.div(1,sum)
fr.prt(fraction1)
