num = 0
total = 0.0
while True:
    sval = input('Enter a number: ')
    if sval == 'done' or sval = '':
        break
    try:
        fval = float(sval)
    except:
        print('invalid input')
        continue
    print(fval)
    num += 1
    total += fval

print('all done')
print(total, num, (total/num))

