lst  = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
]
def oddnumb(n):
    for num in lst:
        if num == n:
            print('Number ',n,'found')
            break
        if num % 2 == 0:
            print(num)
        
oddnumb(248)
