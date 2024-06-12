from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.db.models import Q, Count, F

from .models import Post

# Create your views here.
def mainpage(request):
    posts = Post.objects.all()
    return render(request, 'main/mainpage.html', {'posts':posts})

def mainlistpage(request):
    if request.user.is_authenticated:
        
        # 입력 파라미터
        department = request.GET.get('depa','')
        keyword = request.GET.get('kw', '')
        sort = request.GET.get('so', '')
        end = request.GET.get('en', '')
        place = request.GET.get('pl', '')
        income = request.GET.get('inc', '')

        # 검색
        posts = Post.objects.all()

        if department == '교내':
            posts = posts.filter(department='교내')
        elif department == '학과':
            posts = posts.filter(~Q(department='교내'))

        if keyword:
            posts = posts.filter(
                Q(title__icontains=keyword) |  # 제목에서 검색
                Q(organization__icontains=keyword) | #기관에서 검색
                Q(body__icontains=keyword)  # 내용에서 검색
            ).distinct()
        print(keyword)
        #마감 공고 제외 여부
        if end == 'exclude':
            posts = posts.filter(day_left__gte=0) #day_left>=0
    
        #근로 장소
        place_mapping = {
            '1': '경영/사회과학관',
            '2': '과학관',
            '3': '다향관',
            '4': '명진관',
            '5': '법학/만해관',
            '6': '본관',
            '7': '신공학관',
            '8': '남산학사',
            '9': '중앙도서관',
            '10': '원흥관',
            '11': '학림관',
            '12': '학술문화관',
            '13': '혜화관',
            '14': '기타'
        }
        if place in place_mapping:
            posts = posts.filter(place=place_mapping[place])
        
        #소득 분위 반영 여부
        if income == 'apply':
            posts = posts.filter(is_income_bracket = 1)


        # 정렬
        if sort == 'deadline':
            posts = posts.order_by('-deadline','-pub_date')
        elif sort ==  'inquiry':
            posts = posts.order_by('-inquiry','-pub_date')
        elif sort ==  'scrap':
            posts = posts.order_by('-scrap','-pub_date')
        else:
            posts = posts.order_by('-pub_date')
        
        #페이지 나누기 추후 추가
        #paginator = Paginator(content_list,5)
        #page = request.GET.get('page','')
        #posts = paginator.get_page(page)
        
        context = {
            'posts': posts, 
            'kw': keyword,
            'so': sort, 
            'en': end, 
            'pl': place,
            'inc': income,
        }

        return render(request,'main/mainlistpage.html', context)
    return redirect('accounts:login')

def post_edit(request):
    return render(request, 'main/post_edit.html')

def post_detail(request, post_id):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=post_id)
        return render(request, 'main/post_detail.html', {'post':post})
    return redirect('accounts:login')

def scraps(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.user in post.scrap.all():
        post.scrap.remove(request.user)
        post.scrap_count -= 1
        post.save()
    else:
        post.scrap.add(request.user)
        post.scrap_count += 1
        post.save()
    return redirect('main:mainlistpage')