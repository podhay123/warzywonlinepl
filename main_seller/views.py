from django.shortcuts import render


# Create your views here.
def main(request):
    # articles = Article.objects.all()
    # print(articles)
    # w render jeszcze {"xx": xx}
    return render(request, "main/index.html")
