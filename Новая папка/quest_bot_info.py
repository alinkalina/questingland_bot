import shelve


def names_list():
    names = []
    for game in games:
        names.append(game['name'])
    return names


def descriptions_list():
    descriptions = []
    for game in games:
        descriptions.append(game['description'])
    return descriptions


def get_dict(game):
    for i in games:
        if i['name'] == game:
            return i


got_balloon = {
    'photo': 'images/Vinnie/green_balloon.jpg',
    'text': 'Пятачок был рад тебя видеть и с радостью одолжил тебе воздушный шарик зелёного цвета. 🟢 Ты приносишь '
            'его ослику, но тот говорит, что шарик должен лежать в горшочке мёда. Куда же идти теперь?',
    'variants': {
        'К Сове 🦉': {
            'photo': 'images/Vinnie/closed_door.jpg',
            'text': 'Сова даже не открыла дверь, сколько ты не стучал_а 🚪',
            'variants': {},
            'win': False
        },
        'К Зайцу 🐰': {
            'photo': 'images/Vinnie/much_honey.jpg',
            'text': 'Заяц очень хозяйственный, и у него дома оказалось несколько горшочков с мёдом. 🍯 Как только ослик '
                    'получил горшочек, у него тут же поднялось настроение, и он рассказал, что грустит, потому что '
                    'где-то потерял свой хвост. Что делать?',
            'variants': {
                'Идти к Винни Пуху 🐻': {
                    'photo': 'images/Vinnie/dark_trail.jpg',
                    'text': 'Пух рассказал тебе, что видел похожий хвост в лесу. Ты направляешься туда, но... Начинает '
                            'темнеть, а где же тропинка? Похоже, ты потерялся/потерялась 🔦',
                    'variants': {},
                    'win': False
                },
                'Искать в лесу 🌳': {
                    'photo': 'images/Vinnie/in_dark_forest.jpg',
                    'text': 'Ты ходил_а по лесу, смотрел_а во все глаза, но вот ты уже не знаешь, куда идти дальше...'
                            'Кажется, ты заплутал_а и теперь не сможешь выбраться 🌲',
                    'variants': {},
                    'win': False
                },
                'Идти к Сове 🦉': {
                    'photo': 'images/Vinnie/bell.jpg',
                    'text': 'И вот дом Совы. Над дверью висит шнурочек со звонком. 🔔 Позвонить '
                            'или постучать в дверь?',
                    'variants': {
                        'Позвонить 🔔': {
                            'photo': 'images/Vinnie/win.jpg',
                            'text': 'Как только ты дёрнул_а за шнурок, он оборвался! Пока Сова ругала тебя за такую '
                                    'неосторожность, ты рассмотрел_а шнурок и... это же и есть хвост Иа! Ты приносишь '
                                    'его хозяину, и ослик теперь очень счастлив! 🎉',
                            'variants': {},
                            'win': True
                        },
                        'Постучать 💥': {
                            'photo': 'images/Vinnie/teapot.jpg',
                            'text': 'Сова вышла к тебе, пригласила в дом, предложила чаю 🫖, но о хвосте '
                                    'ослика Иа она ничего не знает',
                            'variants': {},
                            'win': False
                        }
                    }
                }
            }
        },
        'К Винни Пуху 🐻': {
            'photo': 'images/Vinnie/vinnies_house.jpg',
            'text': 'Винни Пуха не оказалось дома 🏡',
            'variants': {},
            'win': False
        }
    }
}


def house(cabinet):
    next_loc = {
        'photo': 'images/Holmes/corridor.png',
        'text': 'Ну что ж, пора отправиться дальше. Итак, ты оказываешься в коридоре. Где же искать секретные '
                'документы 🚪?',
        'variants': {
            'На кухне 🍴': {
                'photo': 'images/Holmes/refrigerator.png',
                'text': 'ААААААА – только и успела произнести жена Силвертона перед тем, как упасть в обморок. На крик '
                        'сразу же прибежал хозяин дома... Видимо не вышло из тебя грабителя 🤷‍♀',
                'variants': {},
                'win': False
            },
            'В спальне 🛏': {
                'photo': 'images/Holmes/bedroom.png',
                'text': 'Ну зачем же ты сюда зашёл/зашла? Силвертон не спал и, бодро вскочив с кровати, схватил тебя. '
                        'Теперь он вызовет полицию... 👮‍♂',
                'variants': {},
                'win': False
            },
            'В кабинете 📎': cabinet
        }
    }
    return next_loc


cabinet_lose = {
    'photo': 'images/Holmes/angry_cat.png',
    'text': 'Войдя в кабинет, ты встретил_а... кошку! 🐈 Правда, МЯУ! похоже она ШШШШШ! не настроена РРР!!!... Как бы '
            'пригодился сейчас тот пакетик корма!',
    'variants': {},
    'win': False
}

on_table = {
    'photo': 'images/Holmes/electricity.png',
    'text': 'Стол оказался под напряжением. ⚡ Так что очнулся/очнулась ты уже связанный/связанная верёвками...',
    'variants': {},
    'win': False
}

cabinet_part = {
    'photo': 'images/Holmes/angry_cat.png',
    'text': 'Войдя в кабинет, ты встретил_а... кошку! 🐈 Правда, МЯУ! похоже она ШШШШШ! не настроена РРР!!!... Но самое '
            'главное в таких ситуациях – не теряться. Где там пакетик кошачьего корма? Итак, кошка довольна, и теперь '
            'можно свободно начинать поиски. Где посмотреть?',
    'variants': {
        'На столе 🔝': on_table,
        'В сейфе 🗄': {
            'photo': 'images/Holmes/closed_vault.png',
            'text': 'Посмотреть в сейфе – разумная идея, но вот только отмычки-то ты с собой не взял_а 🔒',
            'variants': {},
            'win': False
        }
    }
}

cabinet_win = {
    'photo': 'images/Holmes/angry_cat.png',
    'text': 'Войдя в кабинет, ты встретил_а... кошку! 🐈 Правда, МЯУ! похоже она ШШШШШ! не настроена РРР!!!... Но самое '
            'главное в таких ситуациях – не теряться. Где там пакетик кошачьего корма? Итак, кошка довольна, и теперь '
            'можно свободно начинать поиски. Где посмотреть?',
    'variants': {
        'На столе 🔝': on_table,
        'В сейфе 🗄': {
            'photo': 'images/Holmes/opened_vault.png',
            'text': 'Как хорошо, что ты взял_а отмычки с собой! 🔓 Именно в сейфе тебе удалось найти секретные '
                    'документы. Теперь дело за малым – выбраться из дома. Каким образом?',
            'variants': {
                'Через окно кабинета 🖼': {
                    'photo': 'images/Holmes/documents.png',
                    'text': 'Да-да, ведь назад уже не вернуться – кошка наелась. Итак, воздушный прыжок, пружинистое '
                            'приземление, забор и... 📄 Задание выполнено!',
                    'variants': {},
                    'win': True
                },
                'Через чердак 🏠': {
                    'photo': 'images/Holmes/fire_cat.png',
                    'text': 'Хорошая идея, но как же кошка на выходе из кабинета? 🐱 Пакетиков с кормом больше нет... '
                            'МЯУ! ШШШШ!..',
                    'variants': {},
                    'win': False
                },
                'Через переднюю дверь 🚪': {
                    'photo': 'images/Holmes/fire_cat.png',
                    'text': 'А как же кошка на выходе из кабинета? 🐱 Пакетиков с кормом больше нет... МЯУ! ШШШШ!..',
                    'variants': {},
                    'win': False
                }
            }
        }
    }
}

things = {
    'Отмычки 🗝': house(cabinet_part),
    'Фонарик 🔦': house(cabinet_win),
    'Кошачий корм 🍴': house(cabinet_lose)
}

games = [
    {'name': 'В стране Винни Пуха 🍯',
     'description-photo': 'images/Vinnie/description.jpg',
     'description': 'Ты окажешься в мире, в котором живут медвежонок Винни Пух, ослик Иа, поросëнок Пятачок и другие '
                    'добрые герои книг Алана Милна и попробуешь помочь одному из них отыскать очень дорогую ему вещь 🔎'
                    '\n\nАвтор: @alulamalula.\nВсе права защищены.',
     'game': {
         'photo': 'images/Vinnie/start.jpg',
         'text': 'Ты оказываешься на лесной дорожке и встречаешь ослика Иа. 🫏 С ним бы поговорить, но он грустит и '
                 'молчит. Чтобы его развеселить, советуем подарить ему воздушный шарик. Куда пойдёшь?',
         'variants': {
             'К Пятачку 🐽': got_balloon,
             'К Винни Пуху 🐻': {
                 'photo': 'images/Vinnie/honey.jpg',
                 'text': 'У Винни Пуха шариков не оказалось, но он предложил тебе поесть с ним мёда. 🥄🍯 Согласишься?',
                 'variants': {
                     'Да ✔': {
                         'photo': 'images/Vinnie/dark_forest.jpg',
                         'text': 'Мёд был очень вкусный, ты так увлёкся/увлеклась, что наступила ночь 🌙, и теперь '
                                 'ты уже не успеешь найти шарик для ослика Иа',
                         'variants': {},
                         'win': False
                     },
                     'Нет ❌': {
                         'photo': 'images/Vinnie/trail_to_piglet.jpg',
                         'text': 'Винни не очень обиделся, поэтому предложил тебе пойти в гости к Пятачку, может у '
                                 'него есть шарики? 🏞 Пойдёшь?',
                         'variants': {
                             'Да ✔': got_balloon,
                             'Нет ❌': {
                                 'photo': 'images/Vinnie/stupidly.jpg',
                                 'text': 'А на самом деле у Пятачка были шарики... 🤷‍♀',
                                 'variants': {},
                                 'win': False
                             }
                         }
                     }
                 }
             },
             'К Зайцу 🐰': {
                 'photo': 'images/Vinnie/yellow_balloons.jpg',
                 'text': 'В норке у Зайца нашлись воздушные шарики, все они были жёлтого цвета . 🟡 Ты попробовал_а '
                         'подарить их Иа, но ему нравятся только зелёные, и он расстроился ещё сильнее :(',
                 'variants': {},
                 'win': False
             }
         }
     },
     'win': 'Ура! 🎆 Ты помог_ла ослику Иа найти свой хвост! Игра выиграна!',
     'lose': 'Игра проиграна. 🙁 Можешь попробовать помочь ослику снова /again'},

    {'name': 'Записка с Baker Street 🕵🏻‍♂',
     'description-photo': 'images/Holmes/description.png',
     'description': 'Знаменитому сыщику Шерлоку Холмсу ради справедливости необходимо преступить закон! Но разве может '
                    'он позволить себе такое, когда у него и так много дел? Помоги сыщику выкрасть секретные документы '
                    'из дома шантажиста и провокатора Силвертона и спаси своим поступком сразу 1️⃣\u00A03️⃣ '
                    'заинтересованных лиц. Но будь осторожен: в доме есть защита пострашнее обычной сигнализации...'
                    '\n\nАвтор: @alulamalula.\nВсе права защищены.',
     'game': {
         'photo': 'images/Holmes/home.png',
         'text': 'И вот перед тобой вырисовываются мрачные очертания особняка Силвертона, освещённого только '
                 'далёкими фонарями и луной 🌕. С лёгкостью перелезши через ребристый забор, ты оказываешься в '
                 'тёмном саду. Как ты проникнешь в дом?',
         'variants': {
             'Через чердак 🏠': {
                 'photo': 'images/Holmes/attic.png',
                 'text': 'Цепляться за скользкие водосточные трубы и карнизы очень трудно и опасно... 🏛 Но у тебя всё '
                         'получилось! Теперь ты на чердаке. Но посмотри, ведь у тебя порвался один из трёх карманов! '
                         'Хорошо, ничего не выпало. В одном кармане лежали отмычки, в другом фонарик, а в третьем - '
                         'пакетик кошачьего корма. Теперь один предмет придётся оставить здесь (его нельзя будет '
                         'использовать в дальнейшем). Какой?',
                 'variants': things
             },
             'Через входную дверь 🚪': {
                 'photo': 'images/Holmes/siren.png',
                 'text': 'Как только ты открыл_а дверь отмычкой, сработала сигнализация 🛎, в доме все проснулись и '
                         'вызвали полицию...',
                 'variants': {},
                 'win': False
             },
             'Через приоткрытое окно 🖼': {
                 'photo': 'images/Holmes/storage.png',
                 'text': 'Небольшая разминка перед «операцией» не прошла даром, и ты легко проник_ла в маленькую '
                         'комнатку, оказавшуюся кладовкой 📦. Но оказывается, пока ты пробирался через кусты, у тебя '
                         'порвался один из трёх карманов! Хорошо, ничего не выпало. В одном кармане лежали отмычки, в '
                         'другом фонарик, а в третьем - пакетик кошачьего корма. Теперь один предмет придётся оставить '
                         'здесь (его нельзя будет использовать в дальнейшем). Какой?',
                 'variants': things
             }
         }
     },
     'win': 'Браво! Шерлок Холмс будет очень доволен! 😉',
     'lose': 'Игра проиграна. 🙁 Но Холмс готов дать тебе ещё один шанс /again'}
]

try:
    with shelve.open('users.mdb') as db:
        users = db['users']
except Exception as e:
    print(e)
    users = {}
