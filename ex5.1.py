num, total = 0, 0.0
while True:
    sval = input('Enter a number: ')
    if sval == 'done' or sval == '':
        break
    try:
        fval = float(sval)
    except:
        print('invalid input')
    print(fval)
    num += 1
    total += fval
print(f"all done!\ntotal:{total}, num:{num}, total/num:{(total/num)}")
