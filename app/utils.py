from .models import Author

def check_and_create(id,name=None,email=None):
    print('11111111111111111111111111111111111')
    if Author.objects.filter(id=id):
        pass
    else:
        print('5555555555555555553333333333333333333333333')
        Author.objects.create(id=id,name='rahul',email='rahul@gmail.com')
        