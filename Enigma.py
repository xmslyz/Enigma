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
