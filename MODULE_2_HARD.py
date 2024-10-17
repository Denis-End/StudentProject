gr_ = []
for k in range(3, 21):
    stroka_ = ''
    for i in range(1, k):

        for j in range(i+1, k):

            if k % (i + j) == 0:
                stroka_ += str(i) + str(j)
                print(f'{k} - {stroka_}')







