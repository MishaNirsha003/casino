import random
bal = 1000
def blackjack():
    print("ваша ставка (минимум 100)")
    bj_bet1 = input()
    bj_bet = int(bj_bet1)
    global bal
    if bj_bet >= 100:
        if bj_bet > bal:
            print("вам не хватает денег")
        else:
            p_h = random.randint(2,11)
            d_h = random.randint(2,11)
            bj_i = "1"
            print("ваш счёт: ", p_h)
            while bj_i != "stand":
                bj_i = input()
                if bj_i == "hit":
                    p_h += random.randint(2,11)
                    print("ваш счёт: ", p_h)
                if p_h > 21:
                    print ("перебор")
                    bal -= bj_bet
                    return
                if p_h == 21:
                    print ("блекджек") 
                    bj_i = "stand"
            while d_h < 17:
                d_h += random.randint(2,11)
            print("счёт дилера:", d_h)
            if d_h > 21:
                print ("перебор")
                print("победа")
                bal += bj_bet
                return
            if d_h == 21:
                print ("блекджек")
                if p_h == d_h:
                    print ("ничья")
                    return
                elif d_h > p_h:
                    print("поражение")
                    bal -= bj_bet
                    return
            if d_h < 21:
                if d_h > p_h:
                    print("поражение")
                    bal -= bj_bet
                    return
                elif d_h < p_h:
                    print("победа")
                    bal += bj_bet
                    return
            if p_h == d_h:
                print ("ничья")
                return
    else:
        print("ставка некорректна")
    return

def roulette():
    print("ваша ставка (минимум 100)")
    rl_bet1 = input()
    rl_bet = int(rl_bet1)
    global bal
    if rl_bet >= 100:
        if rl_bet > bal:
            print("вам не хватает денег")
        else:
            print('выберите на что вы ставите, для этого пропишите "number" или "color"')
            rl_i = 1
            while rl_i == 1:
                rl_b = input()
                if rl_b == "number":
                    print("вы выбрали ставку на число, напишите число от 1 до 36 включительно")
                    rl_i = 0
                elif rl_b == "color":
                    print("вы выбрали ставку на цвет, выберите один из цветов: red/black")
                    rl_i = 0
            if rl_b == "number":
                rl_n_check = 1
                while rl_n_check == 1:
                    rl_n1 = input()
                    rl_n = int(rl_n1)
                    if rl_n < 37 & rl_n > 0:
                        rl_n_check = 0
                    else:
                        print("поставьте на существующий номер")
                rl_spin_n = random.randint(1,36)
                rl_spin_n2 = rl_spin_n % 2
                if rl_spin_c2 == 0:
                    print(rl_spin_n, " чёрный")
                elif rl_spin_c2 == 1:
                    print(rl_spin_n, "красный")
                if rl_n == rl_spin_n:
                    print("победа")
                    bal += (rl_bet * 10)
                    return
                else:
                    print("поражение")
                    bal -= rl_bet
                    return
            elif rl_b == "color":
                rl_c_check = 1
                while rl_c_check == 1:
                    rl_c = input()
                    if rl_c == "red":
                        rl_c_check = 0
                    elif rl_c == "black":
                        rl_c_check = 0
                    else:
                        print("поставьте на существующий цвет")
                rl_spin_c = random.randint(1,36)
                rl_spin_c2 = rl_spin_c % 2
                if rl_spin_c2 == 0:
                    print(rl_spin_c, " чёрный")
                elif rl_spin_c2 == 1:
                    print(rl_spin_c, "красный")
                if rl_c == "red":
                    if rl_spin_c2 == 0:
                        print("поражение")
                        bal -= rl_bet
                        return
                    elif rl_spin_c2 == 1:
                        print("победа")
                        bal += rl_bet
                        return
                elif rl_c == "black":
                    if rl_spin_c2 == 1:
                        print("поражение")
                        bal -= rl_bet
                        return
                    elif rl_spin_c2 == 0:
                        print("победа")
                        bal += rl_bet
                        return
    else:
        print("ставка некорректна")
    return

def slots():
    print("ваша ставка (минимум 100)")
    sl_bet1 = input()
    sl_bet = int(sl_bet1)
    global bal
    if sl_bet >= 100:
        if sl_bet > bal:
            print("вам не хватает денег")
        else:
            sl_w = 1
            print('чтобы крутить слоты введите "spin"')
            while sl_w == 1:
                sl_s = input()
                if sl_s == "spin":
                    sl_w = 0
            sl_sp1 = random.randint(0,9)
            sl_spin1 = str(sl_sp1)
            sl_sp2 = random.randint(0,9)
            sl_spin2 = str(sl_sp2)
            sl_sp3 = random.randint(0,9)
            sl_spin3 = str(sl_sp3)
            sl_spin = (sl_spin1, sl_spin2, sl_spin3)
            print(sl_spin)
            if sl_spin1 == sl_spin2 == sl_spin:
                bal += (sl_bet * 20)
                print("вы выйграли ", sl_bet*20)
                return
            elif sl_spin1 == sl_spin2:
                bal += sl_bet
                print("вы выйграли ", sl_bet)
                return
            elif sl_spin1 == sl_spin3:
                bal += sl_bet
                print("вы выйграли ", sl_bet)
                return
            elif sl_spin2 == sl_spin3:
                bal += sl_bet
                print("вы выйграли ", sl_bet)
                return
            else:
                bal -= sl_bet
                print("вы проиграли")
                return
    else:
        print("ставка некорректна")
    return

check = 1
while check == 1:
    print("чтобы посмотреть команды напишите help")
    command = input()
    if command == "help":
        print('команды:\n'
        'сыграть в блекждек - "blackjack"\n'
        'сыграть в рулетку - "roulette"\n'
        'сыграть в слоты - "slots"\n'
        'проверить баланс - "balance"\n'
        'заработать денег - "work"\n'
        )
    elif command == "blackjack":
        print('как играть:\n'
        '1) ставите деньги\n'
        '2) вам и дилеру выдаётся карта\n'
        '3) пишите "hit" чтобы взять ещё карту или "stand" чтобы остановиться\n'
        '4) если у вас счёт больше чем у дилера но меньше 21 - вы победили\n'
        '5) если у вас счёт 21 - это блекджек и вы побеждаете если конечно дилер не имеет такой же счёт\n'
        '6) если ваш счёт превышает 21 вы автоматически проигрываете даже если счёт дилера тоже превышает 21\n'
        '7) в случае ничьи ставки аннулируются\n'
        '8) в случае победы ваша ставка удваивается\n'
        )
        blackjack()
    elif command == "roulette":
        print('как играть:\n'
        '1) ставите деньги\n'
        '2) выбираете ставите вы на цвет или на число\n'
        '3) сыбираете само цвет (red/black) или число (от 1 до 36 включительно)\n'
        '4) если выпадает ваш цвет - ваша ставка удваивается\n'
        '5) если выпадает ваше число ваша ставка умножается на 10\n'
        )
        roulette()
    elif command == "slots":
        print('как играть:\n'
        '1) ставите деньги\n'
        '2) пишете "spin" чтобы крутить слоты\n'
        '3) если вам выпало 2 одинаковых числа - ваша ставка удваивается\n'
        '4) если вам выпало 3 одинаковых числа - ваша ставка умножается на 20\n'
         )
        slots()
    elif command == "balance":
        print("ваш баланс", bal)
    elif command == "work":
        num = random.randint(1,999999)
        print ("напишите в консоль (", num, ")")
        num2 = input()
        num3 = int(num2)
        if num3 == num:
            num4 = random.randint(1,10)
            print("вы заработали ", num4)
            bal += num4
        else:
            print("вы не прошли капчу")