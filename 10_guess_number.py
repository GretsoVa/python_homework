def func_01(true_value):
    print("Введите Ваше число")
    your_value=int(input())
    while(your_value!=true_value):
        if your_value>true_value:
            print("Ваше число больше моего")
        else:
            print("Ваше число меньше моего")
        your_value=int(input())
    print("Вы угадали!")



def func_02(true_value, step, lim):
    print("Ход",step)
    print("Ведите Ваше число")
    your_value = int(input())
    while(your_value!=true_value and step<=lim):
        if your_value>true_value:
            print("Ваше число больше моего")
        else:
            print("Ваше число меньше моего")
        print("попробуйте снова")
        step+=1
        print("Ход",step)
        your_value=int(input())
    if your_value==true_value:
        print("Вы угадали!")
        step += 1
        return step
    if step>lim:
        print("Вы исчерпали свои попытки")
        step+=1
        return step

def func_03(lim):
    step=1
    games=1
    again='да'
    while again=='да' and step<=lim:
        print("Партия",games,"\n Игрок 1 вводит число")
        true_value = int(input())
        step=func_02(true_value,step,lim)
        if (step<lim):
            games+=1
            print("Хотите сыграть снова?")
            again=str(input())
        else:
            print('Ходы исчерпаны')
    #print('Было сыграно '+str(games)+' игр')

func_03(10)