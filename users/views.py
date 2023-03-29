from django.shortcuts import render,redirect
#from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm
from django.contrib import messages
from .forms import UserRegistrationForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request,f'Account Created Successfully \
                 for user {username} !!!')
        return redirect('home')
        return redirect('login')   
    else:
        form = UserRegistrationForm()

    return render(request,'register.html',{'form':form})




@login_required
def profile(request):
        if request.method == 'POST':
            u_form = UserUpdateForm(request.POST, instance=request.user)
            p_form = ProfileUpdateForm(request.POST,
                                    request.FILES,
                                    instance=request.user.profile)
            
            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()
                messages.success(request, f'Your account has been updated!')
                return redirect('profile')
        else:
            u_form = UserUpdateForm(instance=request.user)
            p_form = ProfileUpdateForm(instance=request.user.profile)
            
        
        context = {
            'u_form': u_form,
            'p_form': p_form
        }    
        
        return render(request,'profile.html',context)
  
  



  
     

        
        
    
'''
Form.is_valid()
The primary task of a Form object is to validate data. With a bound Form instance, 
call the is_valid() method to run validation and return a boolean designating 
whether the data was valid:

For eg:

Form.is_valid()
The primary task of a Form object is to validate data. With a bound Form instance, call the is_valid() method to run validation and return a boolean designating whether the data was valid:

>>> data = {'subject': 'hello',
...         'message': 'Hi there',
...         'sender': 'foo@example.com',
...         'cc_myself': True}
>>> f = ContactForm(data)
>>> f.is_valid()
True
Let’s try with some invalid data. In this case, subject is blank (an error, because all fields are required by default) and sender is not a valid email address:

>>> data = {'subject': '',
...         'message': 'Hi there',
...         'sender': 'invalid email address',
...         'cc_myself': True}
>>> f = ContactForm(data)
>>> f.is_valid()
False
'''


'''
cleaned_data()

Form.cleaned_data
Each field in a Form class is responsible not only for validating data, but also for “cleaning” 
it – normalizing it to a consistent format. This is a nice feature, 
because it allows data for a particular field to be input in a variety of ways,
always resulting in consistent output.For example, DateField normalizes input into a Python 
datetime.date object. Regardless of whether you pass it a string in the format '1994-07-15',
a datetime.date object, or a number of other formats,
DateField will always normalize it to a datetime.date object as long as it’s valid.

Once you’ve created a Form instance with a set of data and validated it,
 you can access the clean data via its cleaned_data attribute:

>>> data = {'subject': 'hello',
...         'message': 'Hi there',
...         'sender': 'foo@example.com',
...         'cc_myself': True}
>>> f = ContactForm(data)
>>> f.is_valid()
True
>>> f.cleaned_data
{'cc_myself': True, 'message': 'Hi there', 'sender': 'foo@example.com', 'subject': 'hello'}
Note that any text-based field – such as CharField or EmailField – always cleans the input into a string. We’ll cover the encoding implications later in this document.

If your data does not validate, the cleaned_data dictionary contains only the valid fields:

>>> data = {'subject': '',
...         'message': 'Hi there',
...         'sender': 'invalid email address',
...         'cc_myself': True}
>>> f = ContactForm(data)
>>> f.is_valid()
False
>>> f.cleaned_data
{'cc_myself': True, 'message': 'Hi there'}
cleaned_data will always only contain a key for fields defined in the Form, even if you pass extra data when you define the Form. In this example, we pass a bunch of extra fields to the ContactForm constructor, but cleaned_data contains only the form’s fields:

>>> data = {'subject': 'hello',
...         'message': 'Hi there',
...         'sender': 'foo@example.com',
...         'cc_myself': True,
...         'extra_field_1': 'foo',
...         'extra_field_2': 'bar',
...         'extra_field_3': 'baz'}
>>> f = ContactForm(data)
>>> f.is_valid()
True
>>> f.cleaned_data # Doesn't contain extra_field_1, etc.
{'cc_myself': True, 'message': 'Hi there', 'sender': 'foo@example.com', 'subject': 'hello'}





'''




