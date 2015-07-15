import os

__author__ = 'MiRo'

def main():
    outputFile = open('results','w')
    for file in os.listdir('/Users/MiRo/Documents/Programming/CarsAutoRuBackup/'):
        if file[0]=='_':
            carsFile = open(file,'r')
            for sLine in carsFile.readlines():
                outputFile.write(file[1:]+';'+sLine)
            carsFile.close()
    outputFile.close()


if __name__ == '__main__':
    main()
