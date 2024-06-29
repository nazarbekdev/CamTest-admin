def score_calculator(compulsory_sub_ans, sub1_ans, sub2_ans, language, blok1, blok_2):
    if language == 'ingliz':
        if blok1 == 'Inliz tili':
            ball = compulsory_sub_ans * 1.1 + 30 * 2.1 + sub2_ans * 3.1
            correct = compulsory_sub_ans + 30 + sub2_ans
            incorrect = 90 - correct
            result = {
                'ball': ball,
                'correct': correct,
                'incorrect': incorrect,
                'lan_status': 1,
                'description': ''
            }
            return result
        elif blok_2 == 'Inliz tili':
            ball = compulsory_sub_ans * 1.1 + sub1_ans * 2.1 + 30 * 3.1
            correct = compulsory_sub_ans + sub1_ans + 30
            incorrect = 90 - correct
            result = {
                'ball': ball,
                'correct': correct,
                'incorrect': incorrect,
                'lan_status': 2,
                'description': ''
            }
            return result
        else:
            ball = compulsory_sub_ans * 1.1
            correct = compulsory_sub_ans
            incorrect = 90 - correct
            result = {
                'ball': ball,
                'correct': correct,
                'incorrect': incorrect,
                'lan_status': 0,
                'description': """Abiturent tomonidan belgilangan 'Chet tili' tanlangan 'Asosiy fan' larga mos kelmadi!
                               Ushbu sababga ko'ra tanlangan fanlar javobini tekshirish imkoni yo'q.
                               Abiturentlardan hushyorlikni so'rab qolamiz!"""
            }
            return result
    elif language == 'nemis':
        if blok1 == 'Nemis tili':
            ball = compulsory_sub_ans * 1.1 + 30 * 2.1 + sub2_ans * 3.1
            correct = compulsory_sub_ans + 30 + sub2_ans
            incorrect = 90 - correct
            result = {
                'ball': ball,
                'correct': correct,
                'incorrect': incorrect,
                'lan_status': 1,
                'description': ''
            }
            return result
        elif blok_2 == 'Nemis tili':
            ball = compulsory_sub_ans * 1.1 + sub1_ans * 2.1 + 30 * 3.1
            correct = compulsory_sub_ans + sub1_ans + 30
            incorrect = 90 - correct
            result = {
                'ball': ball,
                'correct': correct,
                'incorrect': incorrect,
                'lan_status': 2,
                'description': ''
            }
            return result
        else:
            ball = compulsory_sub_ans * 1.1
            correct = compulsory_sub_ans
            incorrect = 90 - correct
            result = {
                'ball': ball,
                'correct': correct,
                'incorrect': incorrect,
                'lan_status': 0,
                'description': """Abiturent tomonidan belgilangan 'Chet tili' tanlangan 'Asosiy fan' larga mos kelmadi!
                               Ushbu sababga ko'ra tanlangan fanlar javobini tekshirish imkoni yo'q.
                               Abiturentlardan hushyorlikni so'rab qolamiz!"""
            }
            return result
    elif language == 'fransuz':
        if blok1 == 'Fransuz tili':
            ball = compulsory_sub_ans * 1.1 + 30 * 2.1 + sub2_ans * 3.1
            correct = compulsory_sub_ans + 30 + sub2_ans
            incorrect = 90 - correct
            result = {
                'ball': ball,
                'correct': correct,
                'incorrect': incorrect,
                'lan_status': 1,
                'description': ''
            }
            return result
        elif blok_2 == 'Fransuz tili':
            ball = compulsory_sub_ans * 1.1 + sub1_ans * 2.1 + 30 * 3.1
            correct = compulsory_sub_ans + sub1_ans + 30
            incorrect = 90 - correct
            result = {
                'ball': ball,
                'correct': correct,
                'incorrect': incorrect,
                'lan_status': 2,
                'description': ""
            }
            return result
        else:
            ball = compulsory_sub_ans * 1.1
            correct = compulsory_sub_ans
            incorrect = 90 - correct
            result = {
                'ball': ball,
                'correct': correct,
                'incorrect': incorrect,
                'lan_status': 0,
                'description': """Abiturent tomonidan belgilangan 'Chet tili' tanlangan 'Asosiy fan' larga mos kelmadi!
                               Ushbu sababga ko'ra tanlangan fanlar javobini tekshirish imkoni yo'q.
                               Abiturentlardan hushyorlikni so'rab qolamiz!"""
            }
            return result
    elif language == 'error':
        ball = compulsory_sub_ans * 1.1 + sub1_ans * 2.1 + sub2_ans * 3.1
        correct = compulsory_sub_ans + sub1_ans + sub2_ans
        incorrect = 90 - compulsory_sub_ans - sub1_ans - sub2_ans
        result = {
            'ball': ball,
            'correct': correct,
            'incorrect': incorrect,
            'lan_status': 3,
            'description': ""
        }
        return result
