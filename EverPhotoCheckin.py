import requests
import json
import os

def checkin(token):
    url = 'https://openapi.everphoto.cn/sf/3/v4/PostCheckIn'
    headers = {
        "user-agent": "EverPhoto/4.5.0",
        "content-type": "application/json",
        "authorization": f"Bearer {token}",
    }
    res = json.loads(requests.post(url, headers=headers).text)
    continuity = res['data']['continuity']  # 连续签到天数
    total_reward = res['data']['total_reward']//1024//1024  # 总奖励空间
    tomorrow_reward = res['data']['tomorrow_reward']//1024//1024  # 明日奖励
    print(res)
    print(f'已连续签到: {continuity}天, 共获得: {total_reward}MB, 明日奖励: {tomorrow_reward}MB')
    if res['data']['checkin_result']==True:
        print(f'签到成功!')
    if res['data']['checkin_result']!=True:
        print(f'签到失败')
        # raise Exception('Check-in ERROR')

if __name__ == '__main__':
    checkin(os.environ['token'])
