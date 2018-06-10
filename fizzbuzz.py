#!/usr/bin/env python3
# Standard boilerplate to call the main() function to begin
# the program.
def main():
    for i in range(1,101):
        if 0 == i%15 :
            print ('FizzBuzz')
        elif 0 == i%5 :
            print ('Buzz')
        elif 0 == i%3 :
            print ('Fizz')
        else:
            print(i)
if __name__ == '__main__':
    main()  