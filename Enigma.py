# -*- coding: utf-8 -*-

import random
import string
import fileinput
import sys


def txt_gen(lines, size=236, chars=string.ascii_uppercase +
                                      string.ascii_lowercase + string.digits +
                                      string.punctuation):
    for x in range(0, lines):
        return ''.join(random.choice(chars) for _ in range(size)) + "\n"


def savetxt(lines, typ='w+'):
    with open('sample.txt', typ, encoding='UTF-8') as sample:
        for x in range(lines):
            sample.write(txt_gen(lines))
    sample.close()


class Enigma:

    def __init__(self, qaz=0):
        self.qaz = qaz

    def oldtxt(self, line):
        with open('sample.txt', 'r') as f:
            for line in f.readlines()[line:line+1]:
                print(line)
                return line
        f.close()

    def newtxt(self, line, char, newchar):
        with open('sample.txt', 'r') as f:
            for line in f.readlines()[line:line + 1]:
                x = (list(line))
                x[char] = newchar
                print(''.join(x))
                return ''.join(x)
        f.close()


    def replace(self, file, searchExp, replaceExp):
        for line in fileinput.input(file, inplace=1):
            line = line.replace(searchExp, replaceExp)
            sys.stdout.write(line)


cY = Enigma()
old_txt = cY.oldtxt(2)
new_txt = cY.newtxt(2,0,"2")
cY.replace("sample.txt", old_txt, new_txt)
