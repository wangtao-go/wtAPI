import requests
def get_token():
    # 接口地址
    url = "http://101.126.75.103:8080/admin/login"

    # POST 请求的数据（JSON 格式）
    data = {
        "client_type": "api",
        "username": "admin",
        "password": "MDcWz6iZtZvyfgqotfoxoHEPk2UD03nHWXqQT05gVbZc1JT0HvNJu9hh",
        "app_id": "573197216",
        "app_secret": "gG9Y9b8L9zVmgtTZJ"
    }

    # 发送 POST 请求
    response = requests.post(url, json=data)

    # 获取返回值
    if response.status_code == 200:
        result = response.json()  # 获取 JSON 格式的返回数据
        return result['token']
    else:
        print("请求失败，状态码：", response.status_code)
        print("返回内容：", response.text)


def get_sampleType(sample_id):
    url = "http://101.126.75.103:8080/admin/samples/{sample_id}/status"

    # 你的 Bearer Token
    token = get_token()  # 请替换为实际 token

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(url, headers=headers)

    print("状态码:", response.status_code)
    print("返回内容:", response.text)  # 或 response.json()