from rest_framework.permissions import BasePermission

class BookPermission(BasePermission):
    def has_permission(self, request, view):  
        print("current_user:",request.user,request.user.id)
        print(" permission executing ....",view.action,request.data)
        
        if view.action == 'create':
            login_user = request.user.id
            book_author = request.data.get('author')
            print("\n checking user ",login_user,book_author)
            if str(login_user) == str(book_author) :
                print(" you are actual user")
                return True
            else:
                print(" you are not acutal user")
                return False
        
        elif view.action == 'destroy':
            login_user = request.user.id
            book_author = view.get_object()
            if str(login_user) == str(book_author.author.id):
                return True
            else:
                return False
            
        return True
