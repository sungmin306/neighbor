from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Account, Post, comment
from django.http import HttpResponse, JsonResponse
from django.views import View
from MISSION24.settings import SECRET_KEY
import json
import bcrypt
import jwt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PostSerializer, commentSerializer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

# Create your views here.
# @csrf_exempt
# @method_decorator
def home(request):
    return render(request, 'SignUp.html')
@csrf_exempt
def SignUp(request):
    global dic
    dic = {}
    n=1
    print("SugnUp으로 들어옴")
    if(request.method == 'POST'):
        print("if문 들어옴")
        data = json.load(request)
        print(data['home_num'])
        print("돌아간다.")
        if Account.objects.filter(email = data['email']).exists():
            dic['message'] = '이메일이 이미 존재합니다.' 
            n=0
            #return JsonResponse({'message' : '이메일이 이미 존재합니다.'},status=400)
        elif Account.objects.filter(name = data['name']).exists():
            dic['message'] = '닉네임이 이미 존재합니다.'
            n=0
            #return JsonResponse({'message' : '닉네임이 이미 존재합니다.'},status=400)
        else: 
            password=data['password']
            check_password=data['check_password']
            if password != check_password:
                dic['message'] = '비밀번호가 같지 않습니다.'
                n=0
            #return JsonResponse({'message' : '비밀번호가 같습니다.'},status=400)
        if n==1:
            Account.objects.create(
                email = data['email'],
                name = data['name'],
                password=data['password'],
                #password = bcrypt.hashpw(data["password"].encode("UTF-8"), bcrypt.gensalt()).decode("UTF-8"),
                home = data['home'],
                home_num = data['home_num'],
                bank = data['bank'],
                bank_num=data['bank_num'],
            ).save()
            dic['message'] = '로그인 성공'   
        #return HttpResponse(status=200)
    if n==1:
        return JsonResponse(dic,status=200)
    else:
        return JsonResponse(dic,status=400)
    #return render(request, 'SignUp.html')

# class SignUp(View):
#     def post(self, request):
#         data = json.loads(request.body)
#         print(data)
#         print("돌아갑니다.")
#         try:
#             print("계정을 생성합니다.")
#             if Account.objects.filter(email = data['email']).exists():
#                 return JsonResponse({'message' : '이메일이 이미 존재합니다.'},status=400)
#             if Account.objects.filter(name = data['name']).exists():
#                 return JsonResponse({'message' : '닉네임이 이미 존재합니다.'},status=400)
#             password=data['password']
#             check_password=data['check_password']
#             if password == check_password:
#                 return JsonResponse({'message' : '비밀번호가 같습니다.'},status=400)
#             Account.objects.create(
#                 email = data['email'],
#                 name = data['name'],
#                 password1 = bcrypt.hashpw(data["password1"].encode("UTF-8"), bcrypt.gensalt()).decode("UTF-8"),
#                 home = data['home'],
#                 home_num = data['home_num'],
#                 bank = data['bank'],
#                 bank_num=data['bank_num'],
#             ).save()   
#             return HttpResponse(status=200)
#         except KeyError:
#             return JsonResponse({"message" : "INVALID_KEYS"}, status=400)
# # @csrf_exempt
# @method_decorator
@csrf_exempt
def SignIn(request):
    if(request.method == 'POST'):
        global dic
        dic ={}
        data = json.load(request)
        if Account.objects.filter(email=data["email"]).exists():
            user = Account.objects.get(email=data["email"])
        print(user['password'])
        if user['password'] == data['password']:    
            dic['message']=="일치"
            return JsonResponse(dic,status=200)
        else:
            dic['message']=='불일치'
            return JsonResponse(dic,status=400)
    

# class SignIn(View):
#     def post(self, request):
#         data = json.loads(request.body)
#         try:
#             if Account.objects.filter(email=data["email"]).exists():
#                 user = Account.objects.get(email=data["email"])
#                 if bcrypt.checkpw(data['password'].encode('UTF-8'), user.password.encode('UTF-8')):
#                     token = jwt.encode({'user' : user.id}, SECRET_KEY, algorithm='HS256').decode('UTF-8')
#                     return JsonResponse({"token" : token}, status=200)
#                 return HttpResponse(status=401)
#             return HttpResponse(status=400)
#         except KeyError:
#             return JsonResponse({'message' : "INVALID_KEYS"}, status=400)

# class CreatePostsView(APIView):
#     def post(self, request):
#         data = json.loads(request.body)
#         Post.objects.create(
#                 title = data['title'],
#                 content = data['content'],
#             ).save()
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(data=serializer.data)

@csrf_exempt
@api_view(('GET','POST'))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def CreatepostsViews(request):
    print("값 넘어왔습니다.")
    L=['커피/디저트','패스트푸드','도시락','아시안','분식','한식','중식','일식','양식']
    global dic
    dic={}
    if (request.method == 'POST'):
        print("조건문에 들어왔습니다.")
        data = json.load(request)
        p=Post()
        p.title=data['title']
        dic['title']=data['title']
        p.shopName=data['shopName']
        dic['shopName']=data['shopName']
        p.content=data['content']
        dic['content']=data['content']
        p.peoNum=data['peoNum']
        dic['peoNum']=data['peoNum']
        p.useTime=data['useTime']
        dic['useTime']=data['useTime']
        p.place=data['place']
        dic['place']=data['place']
        for i in range(9):
            if int(data['category']) == L[i]:
                p.category=L[i]
                dic['category']=L[i]
        p.save()
        posts=Post.objects.all()
        #posts=json(posts)
        serializer = PostSerializer(posts, many=True)
        return Response(data=serializer.data)
        #return JsonResponse(dic,status=200)

# @csrf_exempt


        
