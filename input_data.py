def find_request(request):

    data = {

        "ever" : (
        '@everyone всем привет','@everyone  всем привет'
        ),

        "mine" : (
        "minecraft","майнкрафт"
        ),

        "dis_cor" : (
        "скинь ссылку на дискорд","дискорд"
        ),

        "test" : (
        "проверка","test","тест","ты тут","ты тут?","петя ты тут?","петя ты тут"
        ),

        "slip" : (
        "я спать","я спать пошёл","спать все","спать"
        ),

        "hello" : (
        "привет","прюэт","здарова","здорова","даров","халло","датути","здрассте","драсте","ну привет","здравствуйте","прив","hello","всем привет","всем прив","Привет"
        ),
        "yes" : (
        "так точно","Так точно"
        ),

        "what" : (
        "чё как оно?","чё, как оно?","че как оно?","че как оно","че, как оно?","как дела","как делишки"
        ),

        "progg" : (
        "ладн я пошёл","ладно я пошёл","я пошел","я пошёл"
        ),

        "hello" : (
        "привет","прюэт","здарова","здорова","даров","халло","датути","здрассте","драсте","ну привет","здравствуйте","прив","hello","всем привет","всем прив"
        ),

        "hi" : (
        "ку ку","ку","куку","куу","всем ку"
        ),

        "canal" : (
        "кинь ссылку на оф канал","скинь ссылку на оф канал","скинь канал","скинь ссылу на канал","канал фолена","оф канал артёма","скинь канал форена","скинь канал артёма","оф канал"
        ),

        "crow" : (
        "да ты крут","круто","крутой","крут","е бой","ее бой","еее бой","ееее бой","ее","еее","ееее"
        ),

        "nice" : (
        "найс","nice","есс"
        ),

        "timen" : (
        "текущее время","сейчас времени","который час","сколько сейчас времяни","сколько сейчас","какой час","время","time"
        ),

        "date" : (
        "сакое сегодня число","сакое число","скачжи число","скажи дату","какая дата","какая сегодня дата", "дата"
        ),

        "ly" : (
        "ля","ляя","ляяя","да ля","да ляя","да ляяя"
        ),

        "fun" : (
        "смех","хах","аха","хаха","хахаха","ахахах","лол","лоол"
        ),

        "M" : (
        "ну ща","ну щас","ну сейчас","погоди","подожди","погодь","ща"
        ),

        "gg" : (
        'GG','gg','Gg','gG','гг','ГГ','гГ','Гг'
        ),

        ")" : (
        ')'
        ),

        "(" : (
        '('
        ),

        #FOR PROGTAMER
        "res" : (
        'restart','перезагрузка','перезапуск','рестарт','rest','res'
        ),

        "clss" : (
        'cls', 'clear'
        ),

        "*" : (
        '*', 'передай', 'скажи всем'
        ),

        "sp" : (
        'spam', 'sp', 'поспамь', 'заспамь', 'заспамь беседу', 'поспамь здесь'
        ),

        "Disc_d" : (
        'поменяй на D', 'смени диск на D', 'd:', ':d'
        ),

        "Disc_c" : (
        'поменяй на C', 'смени диск на C', 'c:', ':c'
        ),

        "cd" : (
        'cd', 'поменяй директорию', 'смени директорию', 'измени директорию'
        )
    }

    for key, value in data.items():

        if (request.lower() or request or request.uppend()) in value:
            return key
            break

        else:
            continue