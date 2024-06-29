import requests
import json


def omr_response(file):
    url = 'http://172.233.221.4:8080/upload/'

    with open(f'/home/nazarbek/CamTest-admin/{file}', 'rb') as f:
        files = {'file': f}
        response = requests.post(url, files=files)

    return response.json()


def compare_answers(user_answers, correct_answers):
    correct_answers = json.loads(correct_answers)
    correct_count_1 = 0
    correct_count_2 = 0
    correct_count_3 = 0
    res = []

    for key, user_answer in user_answers.items():
        if key in correct_answers:
            if user_answer == correct_answers[key]:
                res.append([user_answer, 1])
                if int(key) < 31:
                    correct_count_1 += 1
                elif 30 < int(key) < 61:
                    correct_count_2 += 1
                elif 60 < int(key) < 91:
                    correct_count_3 += 1
            else:
                if user_answer == 'error':
                    res.append(['-', 0])
                else:
                    res.append([user_answer, 0])
        else:
            print('error')
    find_answers = [correct_count_1, correct_count_2, correct_count_3]
    data = {
        'find_ans': find_answers,
        'result': res
    }
    return data
