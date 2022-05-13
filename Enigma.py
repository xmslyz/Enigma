# -*- coding: utf-8 -*-

import random
import string
import fileinput
import sys

class txtGen:
    def __init__(self, z=0):
        self.z = z  # robię tak bo nie wiem jak zrobić aby nie krzyczało że puste!
    
    def txt_gen(lines, size=236, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation):
        for x in range(0, lines):
            return ''.join(random.choice(chars) for _ in range(size)) + "\n"

    def savetxt(lines, typ='w+'):
        with open('sample.txt', typ, encoding='UTF-8') as sample:
            for x in range(lines):
                sample.write(txt_gen(lines))
        sample.close()

        
class MagicBox:
    def __init__(self, q=0):
        self.q = q

    def oldtxt(self, line):
        with open('sample.txt', 'r') as f:
            for line in f.readlines()[line:line+1]:
                return line
        f.close()

    def newtxt(self, line, char, newchar):
        with open('sample.txt', 'r') as f:
            for line in f.readlines()[line:line + 1]:
                x = (list(line))
                x[char] = newchar
                return ''.join(x)
        f.close()

    def replace(self, file, old, new):
        for line in fileinput.input(file, inplace=1):
            line = line.replace(old, new)
            sys.stdout.write(line)

    def change(self, input, n, line, char, newchar):
        old_txt = oldtxt(line)
        new_txt = newtxt(line, char, newchar)
        for linia in fileinput.input("sample.txt", inplace=1):
            linia = linia.replace(old_txt, new_txt)
            sys.stdout.write(linia)

    def doIT(self, input, line=0, char=0, step=0):
    n = 0
    d = list(input)
    for t in range(1, len(input)+1):
        self.change(line, char, d[n])
        char += step
        n += 1

doIT("Big Brown Fox", 0, 5, 7)
