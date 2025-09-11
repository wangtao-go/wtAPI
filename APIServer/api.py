import pandas as pd
import json, os, sys
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.cache import cache
from django.contrib.auth import login
import random


from django.shortcuts import render
from django.http import HttpResponseBadRequest

import os
from django.conf import settings
from django.http import FileResponse
from django.core.files import File
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import FileResponse
from django.core.files import File
import os
from django.http import HttpResponseRedirect

# views.py
import base64
import random
import string
from io import BytesIO

from PIL import Image, ImageDraw, ImageFont
import time
import hashlib
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views import View
class Test(View):
    @csrf_exempt
    def get(self, request):
        response_data = [{
            "alwaysShow": "true",
            "children": [
                {
                    "component": "operation/users/index",
                    "hidden": "false",
                    "meta": {
                        "icon": "Dish",
                        "link": "users",
                        "noCache": "false",
                        "title": "用户信息"
                    },
                    "name": "Users",
                    "path": "users"
                }
            ],
            "component": "Layout",
            "hidden": "false",
            "meta": {
                "icon": "Camera",
                "link": "operation",
                "noCache": "false",
                "title": "业务运营"
            },
            "name": "Operation",
            "path": "/operation",
            "redirect": "noRedirect"
        }]
        return JsonResponse(response_data,safe=False)