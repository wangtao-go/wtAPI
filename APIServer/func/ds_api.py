import json,httpx
def get_llm_res_json(input_text, max_iter=5, show_iter=False):
    api_url = 'https://api.coze.cn/v3/chat'
    acc_token = 'pat_usTgdg9ifgCBmhdBkAZAbjWeif1y4bFrmrDutDwf1xswjBOzjLH3FxnBklELdChn'
    bot_id = '7477798307839574057'

    headers = {
        'Authorization': f'Bearer {acc_token}',
        'Content-Type': 'application/json'
    }
    data = {
        "bot_id": f"{bot_id}",
        "user_id": "123123",
        "stream": True,
        "auto_save_history": True,
        "additional_messages": [
            {
                "role": "user",
                "content": f"{input_text}",
                "content_type": "text",
            }
        ]
    }

    def get_resp():
        res = []
        with httpx.stream('POST', api_url, json=data, headers=headers, timeout=300) as response:
            for r in response.iter_lines():
                res.append(r)
        res_part = res[res.index('event:conversation.message.completed') + 1]
        res_part = json.loads(res_part.split('data:')[-1])
        res_content = res_part['content']
        res_text = json.loads(res_content)['output']
        return (res_text)

    res_json = {}
    for _ in range(max_iter):
        if show_iter and _ > 0:
            print('retry:', _)
        try:
            res_text = get_resp()

            ################
            def safe_json_parse(text):
                text = text.strip()
                # 去除可能包裹的 ```json 标记
                if text.startswith('```json'):
                    text = text[7:]
                if text.endswith('```'):
                    text = text[:-3]
                return text

            res_text = safe_json_parse(res_text)
            res_json = json.loads(res_text)
            break
        except:
            res_json = {}

    return res_json
