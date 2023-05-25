import requests

bot_token = '5056305564:AAGVurTwV5WFJrl2R7gRGiuj9pwWrpsoMIk'
chat_id = 1544841898 

def send_message_to_telegram(message):
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    params = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(url, data=params)
    
    if response.status_code == 200:
        print('Xabar muvaffaqiyatli jo\'natildi')
    else:
        print('Xabar jo\'natishda xatolik yuz berdi')


def send_file_to_telegram(file_path, message):
    url = f'https://api.telegram.org/bot{bot_token}/sendDocument'
    files = {'document': open(file_path, 'rb')}
    params = {
        'chat_id': chat_id,
        'caption': message
        }
    response = requests.post(url, files=files, data=params)

    if response.status_code == 200:
        print('Fayl muvaffaqiyatli jo\'natildi')
    else:
        print('Fayl jo\'natishda xatolik yuz berdi')
