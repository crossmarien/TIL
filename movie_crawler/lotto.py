def get_lotto(draw_no):
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=' + str(draw_no)
    response = requests.get(url)
    lotto_data = response.json()
    numbers = []
    for key in lotto_data:
        if 'drwtNo' in key:
            numbers.append(lotto_data[key])
    bonus_number = lotto_data['bnusNo']
    final_dict = {
        'numbers' : numbers,
        'bonus' : bonus_number,
    }
    return final_dict