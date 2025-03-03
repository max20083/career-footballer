import random

# Ввод имени футболиста
name_footballer = input('Введите имя своего футболиста: ')

# Генерация случайных значений для способностей
pace = random.randint(50, 60)
shoot = random.randint(50, 60)
pas = random.randint(50, 60)
dribble = random.randint(50, 60)  # Исправлено: drible на dribble
defend = random.randint(50, 60)
physics = random.randint(50, 60)

# Список способностей
sposobnosti = [pace, shoot, pas, dribble, defend, physics]

# Генерация случайного таланта
talent_count = random.randint(10, 20)
talent_sposobnosti = random.choice(sposobnosti)
index_talent_sposobnosti = sposobnosti.index(talent_sposobnosti)

# Увеличение случайной способности
if talent_sposobnosti == pace:
    pace += talent_count
elif talent_sposobnosti == shoot:
    shoot += talent_count
elif talent_sposobnosti == pas:
    pas += talent_count
elif talent_sposobnosti == dribble:
    dribble += talent_count
elif talent_sposobnosti == defend:
    defend += talent_count
elif talent_sposobnosti == physics:
    physics += talent_count

# Ввод клуба
club_footballer = input('Выбери в каком клубе России хочешь играть (зенит, спартак, химки): ').lower()

# Список клубов РПЛ
rpl_clubs = [
    "зенит",
    "цска",
    "спартак",
    "ростов",
    "ахмат",
    "краснодар",
    "динамо",
    "локомотив",
    "рубин",
    "крылья советов",
    "урал",
    "уфа",
    "торпедо",
    "амкар",
    "анжи",
    "тосно",
    "химки"
]

n = 15  # Количество матчей

while n > 0:
    if club_footballer == 'химки':
        if 'химки' in rpl_clubs:
            rpl_clubs.remove('химки')
        random_club = random.choice(rpl_clubs)
        random_himki_chance = random.randint(1, 4)

        if random_himki_chance == 1:
            rpl_clubs.remove(random_club)
            print("Химки победили! Поздравляю, вы заработали + 3 очка к рандомному навыку. Соперник: " + random_club)
            random_footballer_himki_sposobnosti = random.choice(sposobnosti)
            if random_footballer_himki_sposobnosti==pace :
                pace+=3
            elif random_footballer_himki_sposobnosti==shoot:
                shoot+=3
            elif random_footballer_himki_sposobnosti==dribble:
                dribble+=3
            elif random_footballer_himki_sposobnosti==pas:
                pas+=3
            elif random_footballer_himki_sposobnosti==defend:
                defend+=3
            elif random_footballer_himki_sposobnosti==physics:
                physics+=3
        else:
            rpl_clubs.remove(random_club)
            print('Химки проиграли. Вы теряете 1 очко рандомного навыка. Соперник: ' + random_club)
            random_footballer_himki_sposobnosti = random.choice(sposobnosti)
            if random_footballer_himki_sposobnosti==pace :
                pace-=1
            elif random_footballer_himki_sposobnosti==shoot:
                shoot-=1
            elif random_footballer_himki_sposobnosti==dribble:
                dribble-=1
            elif random_footballer_himki_sposobnosti==pas:
                pas-=3
            elif random_footballer_himki_sposobnosti==defend:
                defend-=1
            elif random_footballer_himki_sposobnosti==physics:
                physics-=1
        n -= 1
        print('Следующий матч')

    elif club_footballer == 'зенит':
        if 'зенит' in rpl_clubs:
            rpl_clubs.remove('зенит')
        random_club = random.choice(rpl_clubs)
        random_zenit_chance = random.randint(1, 2)

        if random_zenit_chance == 1:
            rpl_clubs.remove(random_club)
            print("Зенит победил! Поздравляю, вы заработали + 3 очка к рандомному навыку. Соперник: " + random_club)
            random_footballer_zenit_sposobnosti = random.choice(sposobnosti)
            if random_footballer_zenit_sposobnosti==pace :
                pace+=3
            elif random_footballer_zenit_sposobnosti==shoot:
                shoot+=3
            elif random_footballer_zenit_sposobnosti==dribble:
                dribble+=3
            elif random_footballer_zenit_sposobnosti==pas:
                pas+=3
            elif random_footballer_zenit_sposobnosti==defend:
                defend+=3
            elif random_footballer_zenit_sposobnosti==physics:
                physics+=3
        else:
            rpl_clubs.remove(random_club)
            print('Зенит проиграл. Вы теряете 1 очко рандомного навыка. Соперник: ' + random_club)
            random_footballer_zenit_sposobnosti = random.choice(sposobnosti)
            if random_footballer_zenit_sposobnosti==pace :
                pace-=1
            elif random_footballer_zenit_sposobnosti==shoot:
                shoot-=1
            elif random_footballer_zenit_sposobnosti==dribble:
                dribble-=1
            elif random_footballer_zenit_sposobnosti==pas:
                pas-=1
            elif random_footballer_zenit_sposobnosti==defend:
                defend-=1
            elif random_footballer_zenit_sposobnosti==physics:
                physics-=1

        n -= 1
        print('Следующий матч')

    elif club_footballer == 'спартак':
        if 'спартак' in rpl_clubs:
            rpl_clubs.remove('спартак')
        random_club = random.choice(rpl_clubs)
        random_spartak_chance = random.randint(1, 3)

        if random_spartak_chance == 1:
            rpl_clubs.remove(random_club)
            print("Спартак победил! Поздравляю, вы заработали + 3 очка к рандомному навыку. Соперник: " + random_club)
            random_footballer_spartak_sposobnosti = random.choice(sposobnosti)
            if random_footballer_spartak_sposobnosti==pace :
                pace+=3
            elif random_footballer_spartak_sposobnosti==shoot:
                shoot+=3
            elif random_footballer_spartak_sposobnosti==dribble:
                dribble+=3
            elif random_footballer_spartak_sposobnosti==pas:
                pas+=3
            elif random_footballer_spartak_sposobnosti==defend:
                defend+=3
            elif random_footballer_spartak_sposobnosti==physics:
                physics+=3
        else:
            rpl_clubs.remove(random_club)
            print('Спартак проиграл. Вы теряете 1 очко рандомного навыка. Соперник: ' + random_club)
            random_footballer_spartak_sposobnosti = random.choice(sposobnosti)
            if random_footballer_spartak_sposobnosti==pace :
                pace-=1
            elif random_footballer_spartak_sposobnosti==shoot:
                shoot-=1
            elif random_footballer_spartak_sposobnosti==dribble:
                dribble-=1
            elif random_footballer_spartak_sposobnosti==pas:
                pas-=1
            elif random_footballer_spartak_sposobnosti==defend:
                defend-=1
            elif random_footballer_spartak_sposobnosti==physics:
                physics-=1

        n -= 1
        print('Следующий матч')
if pace and shoot > pas and dribble and defend and physics  :
    if index_talent_sposobnosti == 0:
        print('''Статистика вашего игрока за сезон:
                       Имя: ''' + name_footballer +
              '\n' + str(pace) + ' скорость' +
              '\n' + str(shoot) + ' удар' +
              '\n' + str(pas) + ' пас' +
              '\n' + str(defend) + ' оборона' +
              '\n' + str(dribble) + ' дриблинг' +
              '\n' + str(physics) + ' физ.данные' +
              '\n' + 'талант : ' + 'скорость'
              '\n' + 'общий рейтинг : ' + str(int(pace + shoot + pas + defend + dribble + physics) // 6) +
              '\n' + 'позиция : ' + 'нападающий')
    elif index_talent_sposobnosti == 1:
        print('''Статистика вашего игрока за сезон:
                       Имя: ''' + name_footballer +
              '\n' + str(pace) + ' скорость' +
              '\n' + str(shoot) + ' удар' +
              '\n' + str(pas) + ' пас' +
              '\n' + str(defend) + ' оборона' +
              '\n' + str(dribble) + ' дриблинг' +
              '\n' + str(physics) + ' физ.данные' +
              '\n' + 'талант : ' + 'удар'
              '\n' + 'общий рейтинг : ' + str(int(pace + shoot + pas + defend + dribble + physics) // 6) +
              '\n' + 'позиция : ' + 'нападающий')

    elif index_talent_sposobnosti == 2:
        print('''Статистика вашего игрока за сезон:
                       Имя: ''' + name_footballer +
              '\n' + str(pace) + ' скорость' +
              '\n' + str(shoot) + ' удар' +
              '\n' + str(pas) + ' пас' +
              '\n' + str(defend) + ' оборона' +
              '\n' + str(dribble) + ' дриблинг' +
              '\n' + str(physics) + ' физ.данные' +
              '\n' + 'талант : ' + 'пас' +
              '\n' + 'общий рейтинг : ' + str(int(pace + shoot + pas + defend + dribble + physics) // 6) +
              '\n' + 'позиция : ' + 'нападающий')
    elif index_talent_sposobnosti == 3:
        print('''Статистика вашего игрока за сезон:
                       Имя: ''' + name_footballer +
              '\n' + str(pace) + ' скорость' +
              '\n' + str(shoot) + ' удар' +
              '\n' + str(pas) + ' пас' +
              '\n' + str(defend) + ' оборона' +
              '\n' + str(dribble) + ' дриблинг' +
              '\n' + str(physics) + ' физ.данные' +
              '\n' + 'талант : ' + 'дриблинг' +
              '\n' + 'общий рейтинг : ' + str(int(pace + shoot + pas + defend + dribble + physics) // 6) +
              '\n' + 'позиция : ' + 'нападающий')
    elif index_talent_sposobnosti == 4:
        print('''Статистика вашего игрока за сезон:
                       Имя: ''' + name_footballer +
              '\n' + str(pace) + ' скорость' +
              '\n' + str(shoot) + ' удар' +
              '\n' + str(pas) + ' пас' +
              '\n' + str(defend) + ' оборона' +
              '\n' + str(dribble) + ' дриблинг' +
              '\n' + str(physics) + ' физ.данные' +
              '\n' + 'талант : ' + 'оборона' +
              '\n' + 'общий рейтинг : ' + str(int(pace + shoot + pas + defend + dribble + physics) // 6) +
              '\n' + 'позиция : ' + 'нападающий')
    elif index_talent_sposobnosti == 5:
        print('''Статистика вашего игрока за сезон:
                       Имя: ''' + name_footballer +
              '\n' + str(pace) + ' скорость' +
              '\n' + str(shoot) + ' удар' +
              '\n' + str(pas) + ' пас' +
              '\n' + str(defend) + ' оборона' +
              '\n' + str(dribble) + ' дриблинг' +
              '\n' + str(physics) + ' физ.данные' +
              '\n' + 'талант : ' + 'физ.данные' +
              '\n' + 'общий рейтинг : ' + str(int(pace + shoot + pas + defend + dribble + physics) // 6) +
              '\n' + 'позиция : ' + 'нападающий')
elif pas and dribble > defend and pace and shoot and physics :
    if index_talent_sposobnosti == 0:
        print('''Статистика вашего игрока за сезон:
                       Имя: ''' + name_footballer +
              '\n' + str(pace) + ' скорость' +
              '\n' + str(shoot) + ' удар' +
              '\n' + str(pas) + ' пас' +
              '\n' + str(defend) + ' оборона' +
              '\n' + str(dribble) + ' дриблинг' +
              '\n' + str(physics) + ' физ.данные' +
              '\n' + 'талант : ' + 'скорость'
              '\n' + 'общий рейтинг : ' + str(int(pace + shoot + pas + defend + dribble + physics) // 6) +
              '\n' + 'позиция : ' + 'полузащитник')
    elif index_talent_sposobnosti == 1:
        print('''Статистика вашего игрока за сезон:
                       Имя: ''' + name_footballer +
              '\n' + str(pace) + ' скорость' +
              '\n' + str(shoot) + ' удар' +
              '\n' + str(pas) + ' пас' +
              '\n' + str(defend) + ' оборона' +
              '\n' + str(dribble) + ' дриблинг' +
              '\n' + str(physics) + ' физ.данные' +
              '\n' + 'талант : ' + 'удар'
              '\n' + 'общий рейтинг : ' + str(int(pace + shoot + pas + defend + dribble + physics) // 6) +
              '\n' + 'позиция : ' + 'полузащитник')

    elif index_talent_sposobnosti == 2:
        print('''Статистика вашего игрока за сезон:
                       Имя: ''' + name_footballer +
              '\n' + str(pace) + ' скорость' +
              '\n' + str(shoot) + ' удар' +
              '\n' + str(pas) + ' пас' +
              '\n' + str(defend) + ' оборона' +
              '\n' + str(dribble) + ' дриблинг' +
              '\n' + str(physics) + ' физ.данные' +
              '\n' + 'талант : ' + 'пас' +
              '\n' + 'общий рейтинг : ' + str(int(pace + shoot + pas + defend + dribble + physics) // 6) +
              '\n' + 'позиция : ' + 'полузащитник')
    elif index_talent_sposobnosti == 3:
        print('''Статистика вашего игрока за сезон:
                       Имя: ''' + name_footballer +
              '\n' + str(pace) + ' скорость' +
              '\n' + str(shoot) + ' удар' +
              '\n' + str(pas) + ' пас' +
              '\n' + str(defend) + ' оборона' +
              '\n' + str(dribble) + ' дриблинг' +
              '\n' + str(physics) + ' физ.данные' +
              '\n' + 'талант : ' + 'дриблинг' +
              '\n' + 'общий рейтинг : ' + str(int(pace + shoot + pas + defend + dribble + physics) // 6) +
              '\n' + 'позиция : ' + 'полузащитник')
    elif index_talent_sposobnosti == 4:
        print('''Статистика вашего игрока за сезон:
                       Имя: ''' + name_footballer +
              '\n' + str(pace) + ' скорость' +
              '\n' + str(shoot) + ' удар' +
              '\n' + str(pas) + ' пас' +
              '\n' + str(defend) + ' оборона' +
              '\n' + str(dribble) + ' дриблинг' +
              '\n' + str(physics) + ' физ.данные' +
              '\n' + 'талант : ' + 'оборона' +
              '\n' + 'общий рейтинг : ' + str(int(pace + shoot + pas + defend + dribble + physics) // 6) +
              '\n' + 'позиция : ' + 'полузащитник')
    elif index_talent_sposobnosti == 5:
        print('''Статистика вашего игрока за сезон:
                       Имя: ''' + name_footballer +
              '\n' + str(pace) + ' скорость' +
              '\n' + str(shoot) + ' удар' +
              '\n' + str(pas) + ' пас' +
              '\n' + str(defend) + ' оборона' +
              '\n' + str(dribble) + ' дриблинг' +
              '\n' + str(physics) + ' физ.данные' +
              '\n' + 'талант : ' + 'физ.данные' +
              '\n' + 'общий рейтинг : ' + str(int(pace + shoot + pas + defend + dribble + physics) // 6) +
              '\n' + 'позиция : ' + 'полузащитник')
elif defend and physics > dribble and shoot and pace and pas :
    if index_talent_sposobnosti == 0:
        print('''Статистика вашего игрока за сезон:
                       Имя: ''' + name_footballer +
              '\n' + str(pace) + ' скорость' +
              '\n' + str(shoot) + ' удар' +
              '\n' + str(pas) + ' пас' +
              '\n' + str(defend) + ' оборона' +
              '\n' + str(dribble) + ' дриблинг' +
              '\n' + str(physics) + ' физ.данные' +
              '\n' + 'талант : ' + 'скорость'
              '\n' + 'общий рейтинг : ' + str(int(pace + shoot + pas + defend + dribble + physics) // 6) +
              '\n' + 'позиция : ' + 'защитник')
    elif index_talent_sposobnosti == 1:
        print('''Статистика вашего игрока за сезон:
                       Имя: ''' + name_footballer +
              '\n' + str(pace) + ' скорость' +
              '\n' + str(shoot) + ' удар' +
              '\n' + str(pas) + ' пас' +
              '\n' + str(defend) + ' оборона' +
              '\n' + str(dribble) + ' дриблинг' +
              '\n' + str(physics) + ' физ.данные' +
              '\n' + 'талант : ' + 'удар'
              '\n' + 'общий рейтинг : ' + str(int(pace + shoot + pas + defend + dribble + physics) // 6) +
              '\n' + 'позиция : ' + 'защитник')

    elif index_talent_sposobnosti == 2:
        print('''Статистика вашего игрока за сезон:
                       Имя: ''' + name_footballer +
              '\n' + str(pace) + ' скорость' +
              '\n' + str(shoot) + ' удар' +
              '\n' + str(pas) + ' пас' +
              '\n' + str(defend) + ' оборона' +
              '\n' + str(dribble) + ' дриблинг' +
              '\n' + str(physics) + ' физ.данные' +
              '\n' + 'талант : ' + 'пас' +
              '\n' + 'общий рейтинг : ' + str(int(pace + shoot + pas + defend + dribble + physics) // 6) +
              '\n' + 'позиция : ' + 'защитник')
    elif index_talent_sposobnosti == 3:
        print('''Статистика вашего игрока за сезон:
                       Имя: ''' + name_footballer +
              '\n' + str(pace) + ' скорость' +
              '\n' + str(shoot) + ' удар' +
              '\n' + str(pas) + ' пас' +
              '\n' + str(defend) + ' оборона' +
              '\n' + str(dribble) + ' дриблинг' +
              '\n' + str(physics) + ' физ.данные' +
              '\n' + 'талант : ' + 'дриблинг' +
              '\n' + 'общий рейтинг : ' + str(int(pace + shoot + pas + defend + dribble + physics) // 6) +
              '\n' + 'позиция : ' + 'защитник')
    elif index_talent_sposobnosti == 4:
        print('''Статистика вашего игрока за сезон:
                       Имя: ''' + name_footballer +
              '\n' + str(pace) + ' скорость' +
              '\n' + str(shoot) + ' удар' +
              '\n' + str(pas) + ' пас' +
              '\n' + str(defend) + ' оборона' +
              '\n' + str(dribble) + ' дриблинг' +
              '\n' + str(physics) + ' физ.данные' +
              '\n' + 'талант : ' + 'оборона' +
              '\n' + 'общий рейтинг : ' + str(int(pace + shoot + pas + defend + dribble + physics) // 6) +
              '\n' + 'позиция : ' + 'защитник')
    elif index_talent_sposobnosti == 5:
        print('''Статистика вашего игрока за сезон:
                       Имя: ''' + name_footballer +
              '\n' + str(pace) + ' скорость' +
              '\n' + str(shoot) + ' удар' +
              '\n' + str(pas) + ' пас' +
              '\n' + str(defend) + ' оборона' +
              '\n' + str(dribble) + ' дриблинг' +
              '\n' + str(physics) + ' физ.данные' +
              '\n' + 'талант : ' + 'физ.данные' +
              '\n' + 'общий рейтинг : ' + str(int(pace + shoot + pas + defend + dribble + physics) // 6) +
              '\n' + 'позиция : ' + 'защитник')
else:
    if index_talent_sposobnosti == 0:
        print('''Статистика вашего игрока за сезон:
                       Имя: ''' + name_footballer +
              '\n' + str(pace) + ' скорость' +
              '\n' + str(shoot) + ' удар' +
              '\n' + str(pas) + ' пас' +
              '\n' + str(defend) + ' оборона' +
              '\n' + str(dribble) + ' дриблинг' +
              '\n' + str(physics) + ' физ.данные' +
              '\n' + 'талант : ' + 'скорость'
              '\n' + 'общий рейтинг : ' + str(int(pace + shoot + pas + defend + dribble + physics) // 6) +
              '\n' + 'позиция : ' + 'универсал')
    elif index_talent_sposobnosti == 1:
        print('''Статистика вашего игрока за сезон:
                       Имя: ''' + name_footballer +
              '\n' + str(pace) + ' скорость' +
              '\n' + str(shoot) + ' удар' +
              '\n' + str(pas) + ' пас' +
              '\n' + str(defend) + ' оборона' +
              '\n' + str(dribble) + ' дриблинг' +
              '\n' + str(physics) + ' физ.данные' +
              '\n' + 'талант : ' + 'удар'
              '\n' + 'общий рейтинг : ' + str(int(pace + shoot + pas + defend + dribble + physics) // 6) +
              '\n' + 'позиция : ' + 'универсал')

    elif index_talent_sposobnosti == 2:
        print('''Статистика вашего игрока за сезон:
                       Имя: ''' + name_footballer +
              '\n' + str(pace) + ' скорость' +
              '\n' + str(shoot) + ' удар' +
              '\n' + str(pas) + ' пас' +
              '\n' + str(defend) + ' оборона' +
              '\n' + str(dribble) + ' дриблинг' +
              '\n' + str(physics) + ' физ.данные' +
              '\n' + 'талант : ' + 'пас' +
              '\n' + 'общий рейтинг : ' + str(int(pace + shoot + pas + defend + dribble + physics) // 6) +
              '\n' + 'позиция : ' + 'универсал')
    elif index_talent_sposobnosti == 3:
        print('''Статистика вашего игрока за сезон:
                       Имя: ''' + name_footballer +
              '\n' + str(pace) + ' скорость' +
              '\n' + str(shoot) + ' удар' +
              '\n' + str(pas) + ' пас' +
              '\n' + str(defend) + ' оборона' +
              '\n' + str(dribble) + ' дриблинг' +
              '\n' + str(physics) + ' физ.данные' +
              '\n' + 'талант : ' + 'дриблинг' +
              '\n' + 'общий рейтинг : ' + str(int(pace + shoot + pas + defend + dribble + physics) // 6) +
              '\n' + 'позиция : ' + 'универсал')
    elif index_talent_sposobnosti == 4:
        print('''Статистика вашего игрока за сезон:
                       Имя: ''' + name_footballer +
              '\n' + str(pace) + ' скорость' +
              '\n' + str(shoot) + ' удар' +
              '\n' + str(pas) + ' пас' +
              '\n' + str(defend) + ' оборона' +
              '\n' + str(dribble) + ' дриблинг' +
              '\n' + str(physics) + ' физ.данные' +
              '\n' + 'талант : ' + 'оборона' +
              '\n' + 'общий рейтинг : ' + str(int(pace + shoot + pas + defend + dribble + physics) // 6) +
              '\n' + 'позиция : ' + 'универсал')
    elif index_talent_sposobnosti == 5:
        print('''Статистика вашего игрока за сезон:
                       Имя: ''' + name_footballer +
              '\n' + str(pace) + ' скорость' +
              '\n' + str(shoot) + ' удар' +
              '\n' + str(pas) + ' пас' +
              '\n' + str(defend) + ' оборона' +
              '\n' + str(dribble) + ' дриблинг' +
              '\n' + str(physics) + ' физ.данные' +
              '\n' + 'талант : ' + 'физ.данные' +
              '\n' + 'общий рейтинг : ' + str(int(pace + shoot + pas + defend + dribble + physics) // 6) +
              '\n' + 'позиция : ' + 'универсал')
input()





















