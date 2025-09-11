import requests
from APIServer.func.getSamContext import get_sampleContext
from APIServer.func.ds_api import get_llm_res_json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views import View

def fetch_sample_sibling(sample):
    HOST2 = '101.126.75.103'
    PORT2 = 8080
    url = f'http://{HOST2}:{PORT2}/api/v1/reports/json/{sample}/sibling'
    print(url)
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        fJson=response.json()
        # with open(f"{sample}_sibling.json", "w", encoding="utf-8") as f:
        #     json.dump(fJson, f, ensure_ascii=False)
        return fJson
    except Exception as e:
        raise ValueError(f"Error fetching {sample}")

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name='dispatch')
class Context_summary(View):
    @csrf_exempt
    def post(self, request):
        # POST处理逻辑
        # 这里可以处理各种POST请求数据
        data = {}

        # 处理JSON数据
        if request.content_type == 'application/json':
            import json
            data = json.loads(request.body)

        # 处理表单数据
        elif request.content_type == 'application/x-www-form-urlencoded':
            data = request.POST.dict()

        # 处理multipart表单数据（包含文件上传）
        elif request.content_type.startswith('multipart/form-data'):
            data = request.POST.dict()
            # 文件可以通过 request.FILES 获取
        print(data)
        sample_id=data["sample_id"]
        recom=self.summary_context(sample_id)
        return JsonResponse(recom,safe=False)

    def summary_context(self,sample):
        # sample = 'TY000900'
        sibling_json = fetch_sample_sibling(sample)
        sample_ids = []
        for sam in sibling_json['samples']:
            sample_ids.append(sam['sample_id'])

        all_Context = ''
        for sam in sample_ids:
            all_Context += get_sampleContext(sam)

        # with open(f'{sample}_summary.txt','w') as f:
        #     f.write(all_Context)

        my_prompt = '*********下面是我的不同时间段测的时序样本，请列举所有样本的样本ID，并充分总结分析疾病相关指标的变化：*********'
        my_prompt += all_Context
        my_prompt += '格式要求：{"recom":"推荐文本"}'
        my_prompt += '   #### 格式要求:你必须用非常严格的JSON 格式数据。不要在开头返回 json这个词，你返回的格式必须可以直接被 json.loads 读取为字典。注意：总结文本不少于2000个字。'
        recom = get_llm_res_json(my_prompt)

        return recom









