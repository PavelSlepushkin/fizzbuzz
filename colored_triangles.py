#!/usr/bin/env python3
#codewars.com  - colored triangles
def triangle(row):
    # Your code here:
    if 1 == len(row):
        return row
    new_row=""
    rules={'BB':'B','BG':'R','BR':'G',
           'GG':'G','GB':'R','GR':'B',
           'RR':'R','RB':'G','RG':'B'}
    for i in range(len(row)-1):
        new_row = new_row + rules[row[i:i+2]]
    return triangle(new_row)
def main():
    print(triangle('GB'))
    print(triangle('RRR'))
    print(triangle('RGBG'))
    print(triangle('RBRGBRB'))
    print(triangle('RBRGBRBGGRRRBGBBBGG'))
    print(triangle('B'))

if __name__ == '__main__':
    main()  