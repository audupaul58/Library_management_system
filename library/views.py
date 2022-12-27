from .forms import *
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, CreateView, ListView, View, UpdateView, DeleteView
from .models import *
from .forms import IssueBookForm, CreateBookForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class Index_Page(TemplateView):
    template_name = 'index.html'
    
class home_Page(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'


class MyBookIsssued_view(LoginRequiredMixin, ListView):
    queryset = BookIssued.objects.all()
    context_object_name = 'mybook'
    template_name = 'library/mybook.html'


class Create_Book(LoginRequiredMixin, CreateView):
    form_class = CreateBookForm
    template_name = "library/add_book.html"
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)
    


class Book_List(LoginRequiredMixin, ListView):
    queryset = Book.objects.all()
    template_name  = "library/view_books.html"
    context_object_name = "books"

class Student_List(LoginRequiredMixin, ListView):
    queryset = Student.objects.all()
    template_name  = "library/view_students.html"
    context_object_name = "students"
    
   
    
    

class IssueBooks(CreateView):
    form_class = IssuedBooksForm
    template_name = "library/issue_book.html"
    success_url = reverse_lazy('view_issued_book')
     
    def form_valid(self, form):
         form.save()
         return redirect(self.success_url)
    
    

'''
class Book_Issued(LoginRequiredMixin, View):
    template_name = "library/issue_book.html"
    success_url = reverse_lazy('view_issued_book')
    
    def get(self, request):
        form = IssueBookForm(request.GET or None)
        context = {
            "form": form
        }
        
        return render (request, self.template_name, context)
       
    
    def post(self, request):
        form = IssueBookForm()
        if form.is_valid():
            obj = BookIssued()
            obj.student_id = request.POST['name2']
            obj.isbn = request.POST['isbn2']
            obj.save()
           
            
        return redirect(self.success_url)

'''

class Profile_View(LoginRequiredMixin, TemplateView):
    queryset = Student.objects.all()
    template_name  = "profile.html"



class Update_User(LoginRequiredMixin, UpdateView):
    model  = Student
    fields = ('classroom', 'branch', 'roll_no', 'phone')
    template_name ="edit_profile.html"
    success_url = reverse_lazy("profile")
    
    
    

class Student_Book_Issued(LoginRequiredMixin, ListView):
    queryset = BookIssued.objects.all()
    context_object_name = 'student_books'
    template_name = 'library/mystudent_issued_books.html'
    
    # return only book taken by each student on the student dashboard
    def get_queryset(self):
        user = self.request.user
        return BookIssued.objects.filter(student__user=user)
    
   

class Delete_Book(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'delete_book.html'
    success_url = reverse_lazy('view_books')
    
   
class Delete_Student(DeleteView):
    model = Student
    template_name = 'delete_book.html'
    success_url = reverse_lazy('view_students')
    
    
    
    




























    '''
@login_required(login_url = '/admin_login')
def issue_book(request):
    form = forms.IssueBookForm()
    if request.method == "POST":
        form = forms.IssueBookForm(request.POST)
        if form.is_valid():
            obj = models.IssuedBook()
            obj.student_id = request.POST['name2']
            obj.isbn = request.POST['isbn2']
            obj.save()
            alert = True
            return render(request, "issue_book.html", {'obj':obj, 'alert':alert})
    return render(request, "issue_book.html", {'form':form})
'''

'''    
@login_required(login_url = '/admin_login')
def view_issued_book(request):
    issuedBooks = IssuedBook.objects.all()
    details = []
    for i in issuedBooks:
        days = (date.today()-i.issued_date)
        d=days.days
        fine=0
        if d>14:
            day=d-14
            fine=day*5
        books = list(models.Book.objects.filter(isbn=i.isbn))
        students = list(models.Student.objects.filter(user=i.student_id))
        i=0
        for l in books:
            t=(students[i].user,students[i].user_id,books[i].name,books[i].isbn,issuedBooks[0].issued_date,issuedBooks[0].expiry_date,fine)
            i=i+1
            details.append(t)
    return render(request, "view_issued_book.html", {'issuedBooks':issuedBooks, 'details':details})


    
@login_required(login_url = '/student_login')
def student_issued_books(request):
    student = Student.objects.filter(user_id=request.user.id)
    issuedBooks = IssuedBook.objects.filter(student_id=student[0].user_id)
    li1 = []
    li2 = []

    for i in issuedBooks:
        books = Book.objects.filter(isbn=i.isbn)
        for book in books:
            t=(request.user.id, request.user.get_full_name, book.name,book.author)
            li1.append(t)

        days=(date.today()-i.issued_date)
        d=days.days
        fine=0
        if d>15:
            day=d-14
            fine=day*5
        t=(issuedBooks[0].issued_date, issuedBooks[0].expiry_date, fine)
        li2.append(t)
    return render(request,'student_issued_books.html',{'li1':li1, 'li2':li2})
    '''


    
    
    
        
'''
@login_required(login_url = '/student_login')
def edit_profile(request):
    student = Student.objects.get(user=request.user)
    if request.method == "POST":
        email = request.POST['email']
        phone = request.POST['phone']
        branch = request.POST['branch']
        classroom = request.POST['classroom']
        roll_no = request.POST['roll_no']

        student.user.email = email
        student.phone = phone
        student.branch = branch
        student.classroom = classroom
        student.roll_no = roll_no
        student.user.save()
        student.save()
        alert = True
        return render(request, "edit_profile.html", {'alert':alert})
    return render(request, "edit_profile.html")

def delete_book(request, myid):
    books = Book.objects.filter(id=myid)
    books.delete()
    return redirect("/view_books")

def delete_student(request, myid):
    students = Student.objects.filter(id=myid)
    students.delete()
    return redirect("/view_students")
'''

      
'''
def student_registration(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        branch = request.POST['branch']
        classroom = request.POST['classroom']
        roll_no = request.POST['roll_no']
        image = request.FILES['image']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            passnotmatch = True
            return render(request, "student_registration.html", {'passnotmatch':passnotmatch})

        user = User.objects.create_user(username=username, email=email, password=password,first_name=first_name, last_name=last_name)
        student = Student.objects.create(user=user, phone=phone, branch=branch, classroom=classroom,roll_no=roll_no, image=image)
        user.save()
        student.save()
        alert = True
        return render(request, "student_registration.html", {'alert':alert})
    return render(request, "student_registration.html")
    
   

def student_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                return HttpResponse("You are not a student!!")
            else:
                return redirect("/profile")
        else:
            alert = True
            return render(request, "student_login.html", {'alert':alert})
    return render(request, "student_login.html")

def admin_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                return redirect("/add_book")
            else:
                return HttpResponse("You are not an admin.")
        else:
            alert = True
            return render(request, "admin_login.html", {'alert':alert})
    return render(request, "admin_login.html")
    
   
@login_required(login_url = '/admin_login')
def view_students(request):
    students = Student.objects.all()
    return render(request, "view_students.html", {'students':students})
'''

    
"""
@login_required(login_url = '/admin_login')
def view_books(request):
    books = Book.objects.all()
    return render(request, "view_books.html", {'books':books})
"""


