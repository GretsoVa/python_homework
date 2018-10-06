############################################################
def func_01(a, x, b, y, z=50):
    pr = "Нельзя"
    x1 = 0
    y1 = 0
    while z>a and y1<=y:
        if z % a == 0 and z // a <= x:
            x1 = z // a
            if y1 <= y:
                pr = str(x1) + " монет A, " + str(y1) + " монет В"
                break
        elif z % b == 0 and z // b <= y:
            y1 += z // b
            if y1 <= y:
                pr = str(x1) + " монет A, " + str(y1) + " монет В"
                break
        z -= b
        y1 += 1
    print(pr)

def func_02(x):
    r=0
    while x > 0:
        x = x // 10
        r += 1
    print(r)

def func_03(s):
    l = len(s) - 1
    polindrom = " полиндром "
    for i in range(l//2):
        if s[i] != s[l-i]:
           polindrom = " не полиндром "
           break
    print(polindrom)

def func_04(s_,s_1,s_2):
    l=len(s_1)
    in_s=True
    i=0
    while i <= len(s_) - l:
        print(s_[i:i + l], s_[i:l] == s_1)
        if s_[i:l + i] == s_1:
            s_ = s_[:i] + s_2 + s_[i + l:]
        i += 1
    return s_


