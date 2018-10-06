def from_alf_to_val(val):
    if val == '0':
        return int(0)
    if val == '1':
        return int(1)
    if val == '2':
        return int(2)
    if val == '3':
        return int(3)
    if val == '4':
        return int(4)
    if val== '5':
        return int(5)
    if val == '6':
        return int(6)
    if val == '7':
        return int(7)
    if val == '8':
        return int(8)
    if val == '9':
        return int(9)
    if val == 'А' or val == 'a':
        return int(10)
    if val == 'B' or val == 'b':
        return int(11)
    if val == 'C' or val == 'c':
        return int(12)
    if val == 'D' or val == 'd':
        return int(13)
    if val == 'E' or val == 'e':
        return int(14)
    if val== 'F' or val == 'f':
        return int(15)
    print("Некорректный ввод числа")

def from_val_to_alf(val):
    if val == 0:
        return '0'
    if val == 1:
        return '1'
    if val == 2:
        return '2'
    if val == 3:
        return '3'
    if val == 4:
        return '4'
    if val== 5:
        return '5'
    if val == 6:
        return '6'
    if val == 7:
        return '7'
    if val == 8:
        return '8'
    if val == 9:
        return '9'
    if val == 10:
        return 'A'
    if val == 11:
        return 'B'
    if val == 12:
        return 'C'
    if val == 13:
        return 'D'
    if val == 14:
        return 'E'
    if val== 15:
        return 'F'


def to_ten(val_ss, ss):
    if ss > 16:
        print('Не умею')
    else:
        val=0
        for i in val_ss:
            val=val*ss+int(from_alf_to_val(i))
        return(val)

def from_ten(val,ss):
   if ss > 16:
       print('Не умею')
   else:
       val_ss=''
       while val>0:
           ost=val % ss
           val=val // ss
           val_ss=from_val_to_alf(ost)+val_ss
   return val_ss







def s1_s2(value_i,s_i,s_j):
    step=0
    value_j=0
    while value_i>0:
        ost = value_i % s_j
        value_i=value_i // s_j
        value_j+=ost*(s_i**step)
        step+=1
        #print(value_j)

    return value_j

set=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','A','B','C','D','E','F']
v_good=False
while v_good==False:
    v_good = True
    print("Введите число")
    v_i = str(input())
    for el in v_i:
        if not el in set:
            v_good=False
            print(el+' не допустимо')
            continue




print("Из какой системы счисления")
i=int(input())
print("В какую счисления")
j=int(input())
print(from_ten(to_ten(str(v_i),i),j))
print(to_ten(str(v_i),i))


#############################################################
# def money(a,x,b,y,z=50):
#     pr = "Нельзя"
#     x1 = 0
#     y1 = 0
#     while z>a and y1<=y:
#         if z % a == 0 and z // a <= x:
#             x1 = z // a
#             if y1 <= y:
#                 pr = str(x1) + " монет A, " + str(y1) + " монет В"
#                 break
#         elif z % b == 0 and z // b <= y:
#             y1 += z // b
#             if y1 <= y:
#                 pr = str(x1) + " монет A, " + str(y1) + " монет В"
#                 break
#         z -= b
#         y1 += 1
#     print(pr)
# print("Введите A");
# a=int(input())
# print("Введите x");
# x=int(input())
# print("Введите B");
# b=int(input())
# print("Введите Y");
# y=int(input())
# print("Введите Z");
# z=int(input())
#
# money(a,x,b,y,z)
#
