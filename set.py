import requests

from city_name import city_name

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.90 Safari/537.36 2345Explorer/9.2.1.17116'
}

'''
train_info = {}
train_info['车编号'] = set[3]
train_info['预约'] = set[11]
train_info['出发时间'] = set[8]
train_info['到达时间'] = set[9]
train_info['all_time'] = set[10]
train_info['商务座'] = set[-12]
train_info['一等座'] = set[-6]
train_info['二等座'] = set[-7]
train_info['高级软卧'] = set[-16]
train_info['软卧'] = set[-14]
# train_info['动卧'] = set[-] 2
train_info['硬卧'] = set[-9]
# train_info['软座'] = set[-] 1
train_info['硬座'] = set[-8]
train_info['无座'] = set[-11]
'''


def choose_ticket():
    from_station = input("请输入起点站>>>")
    to_station = input("请输入终点站>>>")
    params = {
        'leftTicketDTO.train_date': input('请按照1970-01-01格式输入日期>>>'),
        'leftTicketDTO.from_station': city_name[from_station],
        'leftTicketDTO.to_station': city_name[to_station],
        'purpose_codes': 'ADULT'
    }
    base_url = 'https://kyfw.12306.cn/otn/leftTicket/queryO'
    response = requests.get(base_url, headers=headers, params=params, verify=False)

    train_list = []
    print('  -------------------------------------------------------------------------')
    print('  │ 车编号 │ 起点站 │ 终点站 │ 出发时 │ 到站时 │ 总用时 │ 一等座 │ 硬卧 │ 硬座 │')
    print('  -------------------------------------------------------------------------')
    print('  -------------------------------------------------------------------------')

    for each in response.json()['data']['result']:
        seat = each.split('|')
        if seat[11] == 'Y' and (not(seat[-8] == ''or seat[-8] == '无') or not(seat[-9] == ''or seat[-9] == '无') or not(seat[-6] == ''or seat[-6] == '无') or not(seat[-7] == ''or seat[-7] == '无')):
            print('  │%7s│%6s│%6s│%7s│%7s│%7s│%7s│%5s│%5s│' % (seat[3], from_station, to_station, seat[8], seat[9], seat[10], seat[-6], seat[-9], seat[-8]))
            print('  -------------------------------------------------------------------------')
            train_list.append(seat)

    huoche = input("请输入想购买的的车次：").upper()
    for each in train_list:
        if huoche in each:
            train_info = {}
            train_info['车编号'] = each[3]
            train_info['预约'] = each[11]
            train_info['出发时间'] = each[8]
            train_info['到达时间'] = each[9]
            train_info['历时'] = each[10]
            train_info['商务座'] = each[-12]
            train_info['一等座'] = each[-6]
            train_info['二等座'] = each[-7]
            train_info['高级软卧'] = each[-16]
            train_info['软卧'] = each[-14]
            train_info['硬卧'] = each[-9]
            train_info['硬座'] = each[-8]
            train_info['无座'] = each[-11]
            return train_info


if __name__ == '__main__':
    choose_ticket()
