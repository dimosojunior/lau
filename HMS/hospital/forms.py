from hospital.models import *
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

choose_huduma = (
    ('dawa', 'dawa'),
    ('vipimo', 'vipimo')

    )
choose_huduma_vipimo_watoto = (
    ('vipimo', 'vipimo'),
    ('dawa', 'dawa')

    )
accepti = (
    ('yes', 'yes'),
    ('no', 'no')

    )
tribe_choices = (
        
        ('', 'CHOICE TRIBE'),
        ('LUGURU', 'LUGURU'),
        ('SUKUMA', 'SUKUMA'),
        ('HAYA', 'HAYA'),
        ('NYAMWEZI', 'NYAMWEZI'),
        ('NYAKYUSA', 'NYAKYUSA'),
        ('FIPA', 'FIPA'),
        ('SHIRAZI', 'SHIRAZI'),
        ('MANYEMA', 'MANYEMA'),
        ('WAHA', 'WAHA'),
        ('HEHE', 'HEHE'),
        ('POGOLO', 'POGOLO'),
        ('IRAKI', 'IRAKI'),
        ('KULIA', 'KULIA'),
        ('GOGO', 'GOGO'),
        ('SAFWA', 'SAFWA'),
        ('MWELA', 'MWELA'),
        ('HINDI', 'HINDI'),
        ('NGONI', 'NGONI'),
        ('ZARAMO', 'ZARAMO'),
        ('MAKONDE', 'MAKONDE'),
        ('JITA', 'JITA'),
        ('SUKUMA', 'SUKUMA')
    )


class WatotoForm(ModelForm):

    fname = forms.CharField(
            label='First Name',
            widget=forms.TextInput(attrs={'placeholder' :'Enter first name'})

        )
    sname = forms.CharField(
            label='Middle Name',
            widget=forms.TextInput(attrs={'placeholder' :'Enter middle name'})

        ) 
    tname = forms.CharField(
            label='Last Name',
            widget=forms.TextInput(attrs={'placeholder' :'Enter last name'})

        )
    year = forms.CharField(
            label='Age',
            widget=forms.TextInput(attrs={'placeholder' :'Enter age'})
       ) 
    
    tribe = forms.ChoiceField(
        label='Tribe',
        required=False,
        choices = tribe_choices
        
  
       )   

    
    residence = forms.CharField(
            label='Search for Residence',
            widget=forms.TextInput(attrs={'placeholder' :'Enter residence'})
       )  
    next_kin = forms.CharField(
            label='Next of Kin',
            widget=forms.TextInput(attrs={'placeholder' :'next of kin'})
       )  
    next_kin_residence = forms.CharField(
            label='Next of kin residence',
            widget=forms.TextInput(attrs={'placeholder' :'resience for next of kin'})
       )  
    phone = forms.IntegerField(
            label='Phone Number',
            widget=forms.NumberInput(attrs={'placeholder' :'Enter phone number'})
      
       )
    
    class Meta:
        model = WatotoService
        fields = [
            "fname",
            "sname",
            "tname",
            "gender",
            "year",
            "tribe",
            "residence",
            "next_kin",
            "next_kin_residence",
            "phone",
            "payment_type",
            "patient_type",
            "service_time",
            "opd"
            ]


class WazeeForm(ModelForm):

    fname = forms.CharField(
            label='First Name',
            widget=forms.TextInput(attrs={'placeholder' :'Enter first name'})

        )
    sname = forms.CharField(
            label='Middle Name',
            widget=forms.TextInput(attrs={'placeholder' :'Enter middle name'})

        ) 
    tname = forms.CharField(
            label='Last Name',
            widget=forms.TextInput(attrs={'placeholder' :'Enter last name'})

        )
    year = forms.CharField(
            label='Age',
            widget=forms.TextInput(attrs={'placeholder' :'Enter age'})
       )   

    
    tribe = forms.ChoiceField(
        label='Tribe',
        required=False,
        choices = tribe_choices
        
  
       )    
    residence = forms.CharField(
            label='Search for Residence',
            widget=forms.TextInput(attrs={'placeholder' :'Enter residence'})
       )  
    next_kin = forms.CharField(
            label='Next of Kin',
            widget=forms.TextInput(attrs={'placeholder' :'next of kin'})
       )  
    next_kin_residence = forms.CharField(
            label='Next of kin residence',
            widget=forms.TextInput(attrs={'placeholder' :'resience for next of kin'})
       )  
    phone = forms.IntegerField(
            label='Phone Number',
            widget=forms.NumberInput(attrs={'placeholder' :'Enter phone number'})
      
       )
    class Meta:
        model = WazeeService
        fields = [
            "fname",
            "sname",
            "tname",
            "gender",
            "year",
            "tribe",
            "residence",
            "next_kin",
            "next_kin_residence",
            "phone",
            "payment_type",
            "patient_type",
            "service_time",
            "opd"
            ]



class WajawazitoForm(ModelForm):

    fname = forms.CharField(
            label='First Name',
            widget=forms.TextInput(attrs={'placeholder' :'Enter first name'})

        )
    sname = forms.CharField(
            label='Middle Name',
            widget=forms.TextInput(attrs={'placeholder' :'Enter middle name'})

        ) 
    tname = forms.CharField(
            label='Last Name',
            widget=forms.TextInput(attrs={'placeholder' :'Enter last name'})

        )
    year = forms.CharField(
            label='Age',
            widget=forms.TextInput(attrs={'placeholder' :'Enter age'})
       )   

    
    tribe = forms.ChoiceField(
        label='Tribe',
        required=False,
        choices = tribe_choices
        
  
       )    
    residence = forms.CharField(
            label='Search for Residence',
            widget=forms.TextInput(attrs={'placeholder' :'Enter residence'})
       )  
    next_kin = forms.CharField(
            label='Next of Kin',
            widget=forms.TextInput(attrs={'placeholder' :'next of kin'})
       )  
    next_kin_residence = forms.CharField(
            label='Next of kin residence',
            widget=forms.TextInput(attrs={'placeholder' :'resience for next of kin'})
       )  
    phone = forms.IntegerField(
            label='Phone Number',
            widget=forms.NumberInput(attrs={'placeholder' :'Enter phone number'})
      
       )
    class Meta:
        model = WajawazitoService
        fields = [
            "fname",
            "sname",
            "tname",
            "gender",
            "year",
            "tribe",
            "residence",
            "next_kin",
            "next_kin_residence",
            "phone",
            "payment_type",
            "patient_type",
            "service_time",
            "opd"
            ]

class KawaidaForm(ModelForm):

    fname = forms.CharField(
            label='First Name',
            widget=forms.TextInput(attrs={'placeholder' :'Enter first name'})

        )
    sname = forms.CharField(
            label='Middle Name',
            widget=forms.TextInput(attrs={'placeholder' :'Enter middle name'})

        ) 
    tname = forms.CharField(
            label='Last Name',
            widget=forms.TextInput(attrs={'placeholder' :'Enter last name'})

        )
    year = forms.CharField(
            label='Age',
            widget=forms.TextInput(attrs={'placeholder' :'Enter age'})
       )   

     
    tribe = forms.ChoiceField(
        label='Tribe',
        required=False,
        choices = tribe_choices
        
  
       )   
    residence = forms.CharField(
            label='Search for Residence',
            widget=forms.TextInput(attrs={'placeholder' :'Enter residence'})
       )  
    next_kin = forms.CharField(
            label='Next of Kin',
            widget=forms.TextInput(attrs={'placeholder' :'next of kin'})
       )  
    next_kin_residence = forms.CharField(
            label='Next of kin residence',
            widget=forms.TextInput(attrs={'placeholder' :'resience for next of kin'})
       )  
    phone = forms.IntegerField(
            label='Phone Number',
            widget=forms.NumberInput(attrs={'placeholder' :'Enter phone number'})
      
       )
    class Meta:
        model = KawaidaService
        fields = [
            "fname",
            "sname",
            "tname",
            "gender",
            "year",
            "tribe",
            "residence",
            "next_kin",
            "next_kin_residence",
            "phone",
            "payment_type",
            "patient_type",
            "service_time",
            "opd"
            ]

class MedicineForm(forms.ModelForm):
    
    name = forms.CharField(
        label = False,
        widget = forms.TextInput(attrs={'placeholder':'name of midicine', 'class':'input'})
    )
   
    description = forms.CharField(
        label = False,
        widget = forms.TextInput(attrs={'placeholder':'description', 'class':'input'})
    )
  

    
   


    class Meta:
        model = Medicine
        fields = ["name", "description", "watotoservice"]

class UpdateMedicineForm(forms.ModelForm):
    
    

    class Meta:
        model = Medicine
        fields = '__all__'

class MyUserForm(UserCreationForm):
    
    

    class Meta:
        model = MyUser
        fields = [
        "email",
        "password1",
        "password2",
         "first_name", 
         "middle_name",
         "last_name",
         "company_name",
         "phone",
         "is_admin",
         "is_active",
         "is_staff",
         "is_superuser",
         "is_doctor",
         "is_accountancy"



         ]
        
class UserLoginForm(forms.ModelForm):
    password=forms.CharField(
        
        widget = forms.PasswordInput(attrs={'placeholder':'password', 'class':'input'})

    ) 
    email=forms.CharField(
        
        widget = forms.EmailInput(attrs={'placeholder':'email', 'class':'input'})

    )  

    class Meta:
        model=MyUser
        fields=('email', 'password')

    def clean(self):
        if self.is_valid():
            email=self.cleaned_data['email']
            password=self.cleaned_data['password']

            if not authenticate(email=email, password=password):
                raise forms.ValidationError("username or password incorrect")



class WazeeDoziForm(forms.ModelForm):

    name = forms.CharField(
        label='Patient Name',
        widget=forms.TextInput(attrs={'id' :'tag'})
  
       )
    huduma = forms.ChoiceField(
        label='Aina Ya Huduma',
        choices = choose_huduma
  
       )
    
    class Meta:
        model = WazeeDozi
        fields = [
            'name',
            'accepted',
            'huduma',
            'accepted_quantity',
            'accepted_date',
            'phone_number',
            'invoice_date',
            'line_one',
            'line_one_description',
            'line_one_quantity',
            'line_one_unit_price',
            'line_one_total_price',
            'accepted_line_one',


            'line_two',
            'line_two_description',
            'line_two_quantity',
            'line_two_unit_price',
            'line_two_total_price',
            'accepted_line_two',
            
            'line_three',
            'line_three_description',
            'line_three_quantity',
            'line_three_unit_price',
            'line_three_total_price',
            'accepted_line_three',

            'line_four',
            'line_four_description',
            'line_four_quantity',
            'line_four_unit_price',
            'line_four_total_price',
            'accepted_line_four',

            'line_five',
            'line_five_description',
            'line_five_quantity',
            'line_five_unit_price',
            'line_five_total_price',
            'accepted_line_five',

            'line_six',
            'line_six_description',
            'line_six_quantity',
            'line_six_unit_price',
            'line_six_total_price',
            'accepted_line_six',

            'line_seven',
            'line_seven_description',
            'line_seven_quantity',
            'line_seven_unit_price',
            'line_seven_total_price',
            'accepted_line_seven',

            'line_eight',
            'line_eight_description',
            'line_eight_quantity',
            'line_eight_unit_price',
            'line_eight_total_price',
            'accepted_line_eight',

            'line_nine',
            'line_nine_description',
            'line_nine_quantity',
            'line_nine_unit_price',
            'line_nine_total_price',
            'accepted_line_nine',

            'line_ten',
            'line_ten_description',
            'line_ten_quantity',
            'line_ten_unit_price',
            'line_ten_total_price',
            'accepted_line_ten',

            'total',
            'paid',
            'invoice_type'

        ]
    def clean_invoice_number(self):
        invoice_number = self.cleaned_data.get('invoice_number')
        if not invoice_number:
            raise forms.ValidationError('This field is required')
        return invoice_number

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError('This field is required')
        return name

class WazeeDoziUpdateForm(forms.ModelForm):

    name = forms.CharField(
            label=False,
            widget=forms.TextInput(attrs={'id' :'tag'})
      
       )
    huduma = forms.ChoiceField(
        label='Aina Ya Huduma',
        required=False,
        choices = choose_huduma
  
       )
    line_one = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_one_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_one_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_one_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_one_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_two = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_two_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_two_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_two_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_two_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_three = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_three_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_three_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_three_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_three_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_four = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_four_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_four_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_four_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_four_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_five = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_five_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_five_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_five_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_five_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_six = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_six_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_six_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_six_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_six_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_seven = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_seven_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_seven_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_seven_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_seven_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_eight = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_eight_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_eight_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_eight_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_eight_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_nine = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_nine_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_nine_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_nine_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_nine_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_ten = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_ten_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_ten_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_ten_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_ten_total_price = forms.IntegerField(
            label=False,
            required=False,

            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    total = forms.IntegerField(
            label='Total Amount',
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    class Meta:
        model = WazeeDozi
        fields = [
            'name',
            'huduma',
            'accepted',
            'accepted_quantity',
            'accepted_date',
            'phone_number',
            'invoice_date',
            'line_one',
            'line_one_description',
            'line_one_quantity',
            'line_one_unit_price',
            'line_one_total_price',
            'accepted_line_one',


            'line_two',
            'line_two_description',
            'line_two_quantity',
            'line_two_unit_price',
            'line_two_total_price',
            'accepted_line_two',
            
            'line_three',
            'line_three_description',
            'line_three_quantity',
            'line_three_unit_price',
            'line_three_total_price',
            'accepted_line_three',

            'line_four',
            'line_four_description',
            'line_four_quantity',
            'line_four_unit_price',
            'line_four_total_price',
            'accepted_line_four',

            'line_five',
            'line_five_description',
            'line_five_quantity',
            'line_five_unit_price',
            'line_five_total_price',
            'accepted_line_five',

            'line_six',
            'line_six_description',
            'line_six_quantity',
            'line_six_unit_price',
            'line_six_total_price',
            'accepted_line_six',

            'line_seven',
            'line_seven_description',
            'line_seven_quantity',
            'line_seven_unit_price',
            'line_seven_total_price',
            'accepted_line_seven',

            'line_eight',
            'line_eight_description',
            'line_eight_quantity',
            'line_eight_unit_price',
            'line_eight_total_price',
            'accepted_line_eight',

            'line_nine',
            'line_nine_description',
            'line_nine_quantity',
            'line_nine_unit_price',
            'line_nine_total_price',
            'accepted_line_nine',

            'line_ten',
            'line_ten_description',
            'line_ten_quantity',
            'line_ten_unit_price',
            'line_ten_total_price',
            'accepted_line_ten',

            'total',
            'paid',
            'invoice_type'

        ]





class WajawazitoDoziForm(forms.ModelForm):

    name = forms.CharField(
        label='Patient Name',
        widget=forms.TextInput(attrs={'id' :'tag'})
  
       )
    huduma = forms.ChoiceField(
        label='Aina Ya Huduma',
        choices = choose_huduma
  
       )
    class Meta:
        model = WajawazitoDozi
        fields = [
            'name',
            'accepted',
            'huduma',
            'accepted_quantity',
            'accepted_date',
            'phone_number',
            'invoice_date',
            'line_one',
            'line_one_description',
            'line_one_quantity',
            'line_one_unit_price',
            'line_one_total_price',
            'accepted_line_one',


            'line_two',
            'line_two_description',
            'line_two_quantity',
            'line_two_unit_price',
            'line_two_total_price',
            'accepted_line_two',
            
            'line_three',
            'line_three_description',
            'line_three_quantity',
            'line_three_unit_price',
            'line_three_total_price',
            'accepted_line_three',

            'line_four',
            'line_four_description',
            'line_four_quantity',
            'line_four_unit_price',
            'line_four_total_price',
            'accepted_line_four',

            'line_five',
            'line_five_description',
            'line_five_quantity',
            'line_five_unit_price',
            'line_five_total_price',
            'accepted_line_five',

            'line_six',
            'line_six_description',
            'line_six_quantity',
            'line_six_unit_price',
            'line_six_total_price',
            'accepted_line_six',

            'line_seven',
            'line_seven_description',
            'line_seven_quantity',
            'line_seven_unit_price',
            'line_seven_total_price',
            'accepted_line_seven',

            'line_eight',
            'line_eight_description',
            'line_eight_quantity',
            'line_eight_unit_price',
            'line_eight_total_price',
            'accepted_line_eight',

            'line_nine',
            'line_nine_description',
            'line_nine_quantity',
            'line_nine_unit_price',
            'line_nine_total_price',
            'accepted_line_nine',

            'line_ten',
            'line_ten_description',
            'line_ten_quantity',
            'line_ten_unit_price',
            'line_ten_total_price',
            'accepted_line_ten',

            'total',
            'paid',
            'invoice_type'

        ]
    def clean_invoice_number(self):
        invoice_number = self.cleaned_data.get('invoice_number')
        if not invoice_number:
            raise forms.ValidationError('This field is required')
        return invoice_number

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError('This field is required')
        return name

class WajawazitoDoziUpdateForm(forms.ModelForm):

    name = forms.CharField(
            label=False,
            widget=forms.TextInput(attrs={'id' :'tag'})
      
       )
    huduma = forms.ChoiceField(
        label='Aina Ya Huduma',
        required=False,
        choices = choose_huduma
  
       )
    line_one = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_one_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_one_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_one_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_one_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_two = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_two_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_two_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_two_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_two_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_three = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_three_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_three_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_three_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_three_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_four = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_four_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_four_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_four_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_four_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_five = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_five_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_five_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_five_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_five_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_six = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_six_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_six_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_six_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_six_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_seven = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_seven_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_seven_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_seven_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_seven_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_eight = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_eight_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_eight_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_eight_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_eight_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_nine = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_nine_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_nine_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_nine_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_nine_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_ten = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_ten_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_ten_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_ten_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_ten_total_price = forms.IntegerField(
            label=False,
            required=False,

            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    total = forms.IntegerField(
            label='Total Amount',
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    class Meta:
        model = WajawazitoDozi
        fields = [
            'name',
            'huduma',
            'accepted',
            'accepted_quantity',
            'accepted_date',
            'phone_number',
            'invoice_date',
            'line_one',
            'line_one_description',
            'line_one_quantity',
            'line_one_unit_price',
            'line_one_total_price',
            'accepted_line_one',


            'line_two',
            'line_two_description',
            'line_two_quantity',
            'line_two_unit_price',
            'line_two_total_price',
            'accepted_line_two',
            
            'line_three',
            'line_three_description',
            'line_three_quantity',
            'line_three_unit_price',
            'line_three_total_price',
            'accepted_line_three',

            'line_four',
            'line_four_description',
            'line_four_quantity',
            'line_four_unit_price',
            'line_four_total_price',
            'accepted_line_four',

            'line_five',
            'line_five_description',
            'line_five_quantity',
            'line_five_unit_price',
            'line_five_total_price',
            'accepted_line_five',

            'line_six',
            'line_six_description',
            'line_six_quantity',
            'line_six_unit_price',
            'line_six_total_price',
            'accepted_line_six',

            'line_seven',
            'line_seven_description',
            'line_seven_quantity',
            'line_seven_unit_price',
            'line_seven_total_price',
            'accepted_line_seven',

            'line_eight',
            'line_eight_description',
            'line_eight_quantity',
            'line_eight_unit_price',
            'line_eight_total_price',
            'accepted_line_eight',

            'line_nine',
            'line_nine_description',
            'line_nine_quantity',
            'line_nine_unit_price',
            'line_nine_total_price',
            'accepted_line_nine',

            'line_ten',
            'line_ten_description',
            'line_ten_quantity',
            'line_ten_unit_price',
            'line_ten_total_price',
            'accepted_line_ten',

            'total',
            'paid',
            'invoice_type'

        ]




class WajawazitoVipimoForm(forms.ModelForm):

    name = forms.CharField(
        label='Patient Name',
        widget=forms.TextInput(attrs={'id' :'tag'})
  
       )
    huduma = forms.ChoiceField(
        label='TYPE OF INFORMATIONS',
        choices = choose_huduma_vipimo_watoto
  
       )
    class Meta:
        model = WajawazitoVipimo
        fields = [
            'name',
            'accepted',
            'huduma',
            'accepted_quantity',
            'accepted_date',
            'phone_number',
            'invoice_date',
            'line_one',
            'line_one_description',
            'line_one_quantity',
            'line_one_unit_price',
            'line_one_total_price',
            'accepted_line_one',


            'line_two',
            'line_two_description',
            'line_two_quantity',
            'line_two_unit_price',
            'line_two_total_price',
            'accepted_line_two',
            
            'line_three',
            'line_three_description',
            'line_three_quantity',
            'line_three_unit_price',
            'line_three_total_price',
            'accepted_line_three',

            'line_four',
            'line_four_description',
            'line_four_quantity',
            'line_four_unit_price',
            'line_four_total_price',
            'accepted_line_four',

            'line_five',
            'line_five_description',
            'line_five_quantity',
            'line_five_unit_price',
            'line_five_total_price',
            'accepted_line_five',

            'line_six',
            'line_six_description',
            'line_six_quantity',
            'line_six_unit_price',
            'line_six_total_price',
            'accepted_line_six',

            'line_seven',
            'line_seven_description',
            'line_seven_quantity',
            'line_seven_unit_price',
            'line_seven_total_price',
            'accepted_line_seven',

            'line_eight',
            'line_eight_description',
            'line_eight_quantity',
            'line_eight_unit_price',
            'line_eight_total_price',
            'accepted_line_eight',

            'line_nine',
            'line_nine_description',
            'line_nine_quantity',
            'line_nine_unit_price',
            'line_nine_total_price',
            'accepted_line_nine',

            'line_ten',
            'line_ten_description',
            'line_ten_quantity',
            'line_ten_unit_price',
            'line_ten_total_price',
            'accepted_line_ten',

            'total',
            'paid',
            'invoice_type'

        ]
    def clean_invoice_number(self):
        invoice_number = self.cleaned_data.get('invoice_number')
        if not invoice_number:
            raise forms.ValidationError('This field is required')
        return invoice_number

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError('This field is required')
        return name

class WajawazitoVipimoUpdateForm(forms.ModelForm):

    name = forms.CharField(
            label=False,
            widget=forms.TextInput(attrs={'id' :'tag'})
      
       )
    huduma = forms.ChoiceField(
        label='TYPE OF INFORMATIONS',
        required=False,
        choices = choose_huduma_vipimo_watoto
  
       )
    line_one = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_one_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_one_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_one_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_one_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_two = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_two_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_two_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_two_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_two_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_three = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_three_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_three_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_three_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_three_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_four = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_four_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_four_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_four_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_four_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_five = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_five_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_five_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_five_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_five_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_six = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_six_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_six_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_six_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_six_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_seven = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_seven_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_seven_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_seven_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_seven_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_eight = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_eight_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_eight_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_eight_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_eight_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_nine = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_nine_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_nine_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_nine_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_nine_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_ten = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_ten_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_ten_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_ten_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_ten_total_price = forms.IntegerField(
            label=False,
            required=False,

            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    total = forms.IntegerField(
            label='Total Amount',
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    class Meta:
        model = WajawazitoVipimo
        fields = [
            'name',
            'huduma',
            'accepted',
            'accepted_quantity',
            'accepted_date',
            'phone_number',
            'invoice_date',
            'line_one',
            'line_one_description',
            'line_one_quantity',
            'line_one_unit_price',
            'line_one_total_price',
            'accepted_line_one',


            'line_two',
            'line_two_description',
            'line_two_quantity',
            'line_two_unit_price',
            'line_two_total_price',
            'accepted_line_two',
            
            'line_three',
            'line_three_description',
            'line_three_quantity',
            'line_three_unit_price',
            'line_three_total_price',
            'accepted_line_three',

            'line_four',
            'line_four_description',
            'line_four_quantity',
            'line_four_unit_price',
            'line_four_total_price',
            'accepted_line_four',

            'line_five',
            'line_five_description',
            'line_five_quantity',
            'line_five_unit_price',
            'line_five_total_price',
            'accepted_line_five',

            'line_six',
            'line_six_description',
            'line_six_quantity',
            'line_six_unit_price',
            'line_six_total_price',
            'accepted_line_six',

            'line_seven',
            'line_seven_description',
            'line_seven_quantity',
            'line_seven_unit_price',
            'line_seven_total_price',
            'accepted_line_seven',

            'line_eight',
            'line_eight_description',
            'line_eight_quantity',
            'line_eight_unit_price',
            'line_eight_total_price',
            'accepted_line_eight',

            'line_nine',
            'line_nine_description',
            'line_nine_quantity',
            'line_nine_unit_price',
            'line_nine_total_price',
            'accepted_line_nine',

            'line_ten',
            'line_ten_description',
            'line_ten_quantity',
            'line_ten_unit_price',
            'line_ten_total_price',
            'accepted_line_ten',

            'total',
            'paid',
            'invoice_type'

        ]







class WazeeVipimoForm(forms.ModelForm):

    name = forms.CharField(
        label='Patient Name',
        widget=forms.TextInput(attrs={'id' :'tag'})
  
       )
    huduma = forms.ChoiceField(
        label='TYPE OF INFORMATIONS',
        choices = choose_huduma_vipimo_watoto
  
       )
    class Meta:
        model = WazeeVipimo
        fields = [
            'name',
            'accepted',
            'huduma',
            'accepted_quantity',
            'accepted_date',
            'phone_number',
            'invoice_date',
            'line_one',
            'line_one_description',
            'line_one_quantity',
            'line_one_unit_price',
            'line_one_total_price',
            'accepted_line_one',


            'line_two',
            'line_two_description',
            'line_two_quantity',
            'line_two_unit_price',
            'line_two_total_price',
            'accepted_line_two',
            
            'line_three',
            'line_three_description',
            'line_three_quantity',
            'line_three_unit_price',
            'line_three_total_price',
            'accepted_line_three',

            'line_four',
            'line_four_description',
            'line_four_quantity',
            'line_four_unit_price',
            'line_four_total_price',
            'accepted_line_four',

            'line_five',
            'line_five_description',
            'line_five_quantity',
            'line_five_unit_price',
            'line_five_total_price',
            'accepted_line_five',

            'line_six',
            'line_six_description',
            'line_six_quantity',
            'line_six_unit_price',
            'line_six_total_price',
            'accepted_line_six',

            'line_seven',
            'line_seven_description',
            'line_seven_quantity',
            'line_seven_unit_price',
            'line_seven_total_price',
            'accepted_line_seven',

            'line_eight',
            'line_eight_description',
            'line_eight_quantity',
            'line_eight_unit_price',
            'line_eight_total_price',
            'accepted_line_eight',

            'line_nine',
            'line_nine_description',
            'line_nine_quantity',
            'line_nine_unit_price',
            'line_nine_total_price',
            'accepted_line_nine',

            'line_ten',
            'line_ten_description',
            'line_ten_quantity',
            'line_ten_unit_price',
            'line_ten_total_price',
            'accepted_line_ten',

            'total',
            'paid',
            'invoice_type'

        ]
    def clean_invoice_number(self):
        invoice_number = self.cleaned_data.get('invoice_number')
        if not invoice_number:
            raise forms.ValidationError('This field is required')
        return invoice_number

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError('This field is required')
        return name

class WazeeVipimoUpdateForm(forms.ModelForm):

    name = forms.CharField(
            label=False,
            widget=forms.TextInput(attrs={'id' :'tag'})
      
       )
    huduma = forms.ChoiceField(
        label='TYPE OF INFORMATIONS',
        required=False,
        choices = choose_huduma_vipimo_watoto
  
       )
    line_one = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_one_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_one_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_one_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_one_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_two = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_two_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_two_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_two_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_two_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_three = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_three_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_three_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_three_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_three_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_four = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_four_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_four_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_four_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_four_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_five = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_five_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_five_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_five_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_five_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_six = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_six_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_six_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_six_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_six_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_seven = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_seven_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_seven_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_seven_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_seven_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_eight = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_eight_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_eight_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_eight_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_eight_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_nine = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_nine_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_nine_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_nine_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_nine_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_ten = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_ten_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_ten_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_ten_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_ten_total_price = forms.IntegerField(
            label=False,
            required=False,

            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    total = forms.IntegerField(
            label='Total Amount',
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    class Meta:
        model = WazeeVipimo
        fields = [
            'name',
            'huduma',
            'accepted',
            'accepted_quantity',
            'accepted_date',
            'phone_number',
            'invoice_date',
            'line_one',
            'line_one_description',
            'line_one_quantity',
            'line_one_unit_price',
            'line_one_total_price',
            'accepted_line_one',


            'line_two',
            'line_two_description',
            'line_two_quantity',
            'line_two_unit_price',
            'line_two_total_price',
            'accepted_line_two',
            
            'line_three',
            'line_three_description',
            'line_three_quantity',
            'line_three_unit_price',
            'line_three_total_price',
            'accepted_line_three',

            'line_four',
            'line_four_description',
            'line_four_quantity',
            'line_four_unit_price',
            'line_four_total_price',
            'accepted_line_four',

            'line_five',
            'line_five_description',
            'line_five_quantity',
            'line_five_unit_price',
            'line_five_total_price',
            'accepted_line_five',

            'line_six',
            'line_six_description',
            'line_six_quantity',
            'line_six_unit_price',
            'line_six_total_price',
            'accepted_line_six',

            'line_seven',
            'line_seven_description',
            'line_seven_quantity',
            'line_seven_unit_price',
            'line_seven_total_price',
            'accepted_line_seven',

            'line_eight',
            'line_eight_description',
            'line_eight_quantity',
            'line_eight_unit_price',
            'line_eight_total_price',
            'accepted_line_eight',

            'line_nine',
            'line_nine_description',
            'line_nine_quantity',
            'line_nine_unit_price',
            'line_nine_total_price',
            'accepted_line_nine',

            'line_ten',
            'line_ten_description',
            'line_ten_quantity',
            'line_ten_unit_price',
            'line_ten_total_price',
            'accepted_line_ten',

            'total',
            'paid',
            'invoice_type'

        ]




class KawaidaVipimoUpdateForm(forms.ModelForm):

    name = forms.CharField(
            label=False,
            widget=forms.TextInput(attrs={'id' :'tag'})
      
       )
    huduma = forms.ChoiceField(
        label='Aina Ya Huduma',
        required=False,
        choices = choose_huduma
  
       )
    line_one = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_one_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_one_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_one_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_one_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_two = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_two_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_two_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_two_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_two_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_three = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_three_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_three_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_three_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_three_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_four = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_four_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_four_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_four_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_four_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_five = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_five_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_five_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_five_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_five_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_six = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_six_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_six_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_six_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_six_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_seven = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_seven_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_seven_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_seven_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_seven_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_eight = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_eight_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_eight_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_eight_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_eight_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_nine = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_nine_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_nine_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_nine_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_nine_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_ten = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_ten_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_ten_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_ten_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_ten_total_price = forms.IntegerField(
            label=False,
            required=False,

            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    total = forms.IntegerField(
            label='Total Amount',
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    class Meta:
        model = KawaidaVipimo
        fields = [
            'name',
            'huduma',
            'accepted_quantity',
            'accepted_date',
            'phone_number',
            'invoice_date',
            'line_one',
            'line_one_description',
            'line_one_quantity',
            'line_one_unit_price',
            'line_one_total_price',
            'accepted_line_one',


            'line_two',
            'line_two_description',
            'line_two_quantity',
            'line_two_unit_price',
            'line_two_total_price',
            'accepted_line_two',
            
            'line_three',
            'line_three_description',
            'line_three_quantity',
            'line_three_unit_price',
            'line_three_total_price',
            'accepted_line_three',

            'line_four',
            'line_four_description',
            'line_four_quantity',
            'line_four_unit_price',
            'line_four_total_price',
            'accepted_line_four',

            'line_five',
            'line_five_description',
            'line_five_quantity',
            'line_five_unit_price',
            'line_five_total_price',
            'accepted_line_five',

            'line_six',
            'line_six_description',
            'line_six_quantity',
            'line_six_unit_price',
            'line_six_total_price',
            'accepted_line_six',

            'line_seven',
            'line_seven_description',
            'line_seven_quantity',
            'line_seven_unit_price',
            'line_seven_total_price',
            'accepted_line_seven',

            'line_eight',
            'line_eight_description',
            'line_eight_quantity',
            'line_eight_unit_price',
            'line_eight_total_price',
            'accepted_line_eight',

            'line_nine',
            'line_nine_description',
            'line_nine_quantity',
            'line_nine_unit_price',
            'line_nine_total_price',
            'accepted_line_nine',

            'line_ten',
            'line_ten_description',
            'line_ten_quantity',
            'line_ten_unit_price',
            'line_ten_total_price',
            'accepted_line_ten',

            'total',
            'paid',
            'invoice_type'

        ]

class KawaidaVipimoForm(forms.ModelForm):

    name = forms.CharField(
        label='Patient Name',
        widget=forms.TextInput(attrs={'id' :'tag'})
  
       )
    huduma = forms.ChoiceField(
        label='TYPE OF INFORMATIONS',
        choices = choose_huduma_vipimo_watoto
  
       )
    class Meta:
        model = KawaidaVipimo
        fields = [
            'name',
            'huduma',
            'accepted_quantity',
            'accepted_date',
            'phone_number',
            'invoice_date',
            'line_one',
            'line_one_description',
            'line_one_quantity',
            'line_one_unit_price',
            'line_one_total_price',
            'accepted_line_one',


            'line_two',
            'line_two_description',
            'line_two_quantity',
            'line_two_unit_price',
            'line_two_total_price',
            'accepted_line_two',
            
            'line_three',
            'line_three_description',
            'line_three_quantity',
            'line_three_unit_price',
            'line_three_total_price',
            'accepted_line_three',

            'line_four',
            'line_four_description',
            'line_four_quantity',
            'line_four_unit_price',
            'line_four_total_price',
            'accepted_line_four',

            'line_five',
            'line_five_description',
            'line_five_quantity',
            'line_five_unit_price',
            'line_five_total_price',
            'accepted_line_five',

            'line_six',
            'line_six_description',
            'line_six_quantity',
            'line_six_unit_price',
            'line_six_total_price',
            'accepted_line_six',

            'line_seven',
            'line_seven_description',
            'line_seven_quantity',
            'line_seven_unit_price',
            'line_seven_total_price',
            'accepted_line_seven',

            'line_eight',
            'line_eight_description',
            'line_eight_quantity',
            'line_eight_unit_price',
            'line_eight_total_price',
            'accepted_line_eight',

            'line_nine',
            'line_nine_description',
            'line_nine_quantity',
            'line_nine_unit_price',
            'line_nine_total_price',
            'accepted_line_nine',

            'line_ten',
            'line_ten_description',
            'line_ten_quantity',
            'line_ten_unit_price',
            'line_ten_total_price',
            'accepted_line_ten',

            'total',
            'paid',
            'invoice_type'

        ]

        
    def clean_invoice_number(self):
        invoice_number = self.cleaned_data.get('invoice_number')
        if not invoice_number:
            raise forms.ValidationError('This field is required')
        return invoice_number

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError('This field is required')
        return name

class KawaidaDoziForm(forms.ModelForm):

    name = forms.CharField(
        label='Patient Name',
        widget=forms.TextInput(attrs={'id' :'tag'})
  
       )
    huduma = forms.ChoiceField(
        label='Aina Ya Huduma',
        choices = choose_huduma
  
       )
    class Meta:
        model = KawaidaDozi
        fields = [
            'name',
            'accepted',
            'huduma',
            'accepted_quantity',
            'accepted_date',
            'phone_number',
            'invoice_date',
            'line_one',
            'line_one_description',
            'line_one_quantity',
            'line_one_unit_price',
            'line_one_total_price',
            'accepted_line_one',


            'line_two',
            'line_two_description',
            'line_two_quantity',
            'line_two_unit_price',
            'line_two_total_price',
            'accepted_line_two',
            
            'line_three',
            'line_three_description',
            'line_three_quantity',
            'line_three_unit_price',
            'line_three_total_price',
            'accepted_line_three',

            'line_four',
            'line_four_description',
            'line_four_quantity',
            'line_four_unit_price',
            'line_four_total_price',
            'accepted_line_four',

            'line_five',
            'line_five_description',
            'line_five_quantity',
            'line_five_unit_price',
            'line_five_total_price',
            'accepted_line_five',

            'line_six',
            'line_six_description',
            'line_six_quantity',
            'line_six_unit_price',
            'line_six_total_price',
            'accepted_line_six',

            'line_seven',
            'line_seven_description',
            'line_seven_quantity',
            'line_seven_unit_price',
            'line_seven_total_price',
            'accepted_line_seven',

            'line_eight',
            'line_eight_description',
            'line_eight_quantity',
            'line_eight_unit_price',
            'line_eight_total_price',
            'accepted_line_eight',

            'line_nine',
            'line_nine_description',
            'line_nine_quantity',
            'line_nine_unit_price',
            'line_nine_total_price',
            'accepted_line_nine',

            'line_ten',
            'line_ten_description',
            'line_ten_quantity',
            'line_ten_unit_price',
            'line_ten_total_price',
            'accepted_line_ten',

            'total',
            'paid',
            'invoice_type'

        ]
    def clean_invoice_number(self):
        invoice_number = self.cleaned_data.get('invoice_number')
        if not invoice_number:
            raise forms.ValidationError('This field is required')
        return invoice_number

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError('This field is required')
        return name

class KawaidaDoziUpdateForm(forms.ModelForm):

    name = forms.CharField(
            label=False,
            widget=forms.TextInput(attrs={'id' :'tag'})
      
       )
    huduma = forms.ChoiceField(
        label='TYPE OF INFORMATIONS',
        required=False,
        choices = choose_huduma_vipimo_watoto
  
       )
    line_one = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_one_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_one_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_one_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_one_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_two = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_two_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_two_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_two_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_two_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_three = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_three_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_three_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_three_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_three_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_four = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_four_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_four_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_four_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_four_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_five = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_five_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_five_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_five_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_five_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_six = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_six_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_six_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_six_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_six_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_seven = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_seven_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_seven_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_seven_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_seven_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_eight = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_eight_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_eight_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_eight_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_eight_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_nine = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_nine_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_nine_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_nine_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_nine_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_ten = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_ten_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_ten_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_ten_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_ten_total_price = forms.IntegerField(
            label=False,
            required=False,

            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    total = forms.IntegerField(
            label='Total Amount',
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    class Meta:
        model = KawaidaDozi
        fields = [
            'name',
            'huduma',
            'accepted',
            'accepted_quantity',
            'accepted_date',
            'phone_number',
            'invoice_date',
            'line_one',
            'line_one_description',
            'line_one_quantity',
            'line_one_unit_price',
            'line_one_total_price',
            'accepted_line_one',


            'line_two',
            'line_two_description',
            'line_two_quantity',
            'line_two_unit_price',
            'line_two_total_price',
            'accepted_line_two',
            
            'line_three',
            'line_three_description',
            'line_three_quantity',
            'line_three_unit_price',
            'line_three_total_price',
            'accepted_line_three',

            'line_four',
            'line_four_description',
            'line_four_quantity',
            'line_four_unit_price',
            'line_four_total_price',
            'accepted_line_four',

            'line_five',
            'line_five_description',
            'line_five_quantity',
            'line_five_unit_price',
            'line_five_total_price',
            'accepted_line_five',

            'line_six',
            'line_six_description',
            'line_six_quantity',
            'line_six_unit_price',
            'line_six_total_price',
            'accepted_line_six',

            'line_seven',
            'line_seven_description',
            'line_seven_quantity',
            'line_seven_unit_price',
            'line_seven_total_price',
            'accepted_line_seven',

            'line_eight',
            'line_eight_description',
            'line_eight_quantity',
            'line_eight_unit_price',
            'line_eight_total_price',
            'accepted_line_eight',

            'line_nine',
            'line_nine_description',
            'line_nine_quantity',
            'line_nine_unit_price',
            'line_nine_total_price',
            'accepted_line_nine',

            'line_ten',
            'line_ten_description',
            'line_ten_quantity',
            'line_ten_unit_price',
            'line_ten_total_price',
            'accepted_line_ten',

            'total',
            'paid',
            'invoice_type'

        ]


class DoziForm(forms.ModelForm):

    name = forms.CharField(
        label='Patient Name',
        widget=forms.TextInput(attrs={'id' :'tag'})
  
       )
    huduma = forms.ChoiceField(
        label='Aina Ya Huduma',
        choices = choose_huduma
  
       )
    class Meta:
        model = Dozi
        fields = [
            'name',
            'accepted',
            'huduma',
            'accepted_quantity',
            'accepted_date',
            'phone_number',
            'invoice_date',
            'line_one',
            'line_one_description',
            'line_one_quantity',
            'line_one_unit_price',
            'line_one_total_price',
            'accepted_line_one',


            'line_two',
            'line_two_description',
            'line_two_quantity',
            'line_two_unit_price',
            'line_two_total_price',
            'accepted_line_two',
            
            'line_three',
            'line_three_description',
            'line_three_quantity',
            'line_three_unit_price',
            'line_three_total_price',
            'accepted_line_three',

            'line_four',
            'line_four_description',
            'line_four_quantity',
            'line_four_unit_price',
            'line_four_total_price',
            'accepted_line_four',

            'line_five',
            'line_five_description',
            'line_five_quantity',
            'line_five_unit_price',
            'line_five_total_price',
            'accepted_line_five',

            'line_six',
            'line_six_description',
            'line_six_quantity',
            'line_six_unit_price',
            'line_six_total_price',
            'accepted_line_six',

            'line_seven',
            'line_seven_description',
            'line_seven_quantity',
            'line_seven_unit_price',
            'line_seven_total_price',
            'accepted_line_seven',

            'line_eight',
            'line_eight_description',
            'line_eight_quantity',
            'line_eight_unit_price',
            'line_eight_total_price',
            'accepted_line_eight',

            'line_nine',
            'line_nine_description',
            'line_nine_quantity',
            'line_nine_unit_price',
            'line_nine_total_price',
            'accepted_line_nine',

            'line_ten',
            'line_ten_description',
            'line_ten_quantity',
            'line_ten_unit_price',
            'line_ten_total_price',
            'accepted_line_ten',

            'total',
            'paid',
            'invoice_type'

        ]

        
    def clean_invoice_number(self):
        invoice_number = self.cleaned_data.get('invoice_number')
        if not invoice_number:
            raise forms.ValidationError('This field is required')
        return invoice_number

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError('This field is required')
        return name


class DoziSearchForm(forms.ModelForm):
    generate_invoice = forms.BooleanField(required=False)
    name = forms.CharField(
            label='Patient Name',
            widget=forms.TextInput(attrs={'id' :'tage'})
      
       )
    class Meta:
        model = Dozi
        fields = ['name', 'generate_invoice']

class SearchForm(forms.ModelForm):
    #generate_invoice = forms.BooleanField(required=False)
    line_one_quantity = forms.IntegerField(
            label=False,
            widget=forms.NumberInput(attrs={'name' :'date'})
      
       )
    class Meta:
        model = Dozi
        fields = ['line_one_quantity']







class DoziUpdateForm(forms.ModelForm):

    name = forms.CharField(
            label=False,
            widget=forms.TextInput(attrs={'id' :'tag'})
      
       )
    huduma = forms.ChoiceField(
        label='Aina Ya Huduma',
        required=False,
        choices = choose_huduma
  
       )
    line_one = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_one_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_one_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_one_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_one_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_two = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_two_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_two_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_two_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_two_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_three = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_three_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_three_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_three_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_three_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_four = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_four_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_four_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_four_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_four_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_five = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_five_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_five_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_five_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_five_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_six = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_six_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_six_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_six_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_six_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_seven = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_seven_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_seven_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_seven_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_seven_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_eight = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_eight_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_eight_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_eight_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_eight_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_nine = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_nine_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_nine_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_nine_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_nine_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_ten = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_ten_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_ten_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_ten_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_ten_total_price = forms.IntegerField(
            label=False,
            required=False,

            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    total = forms.IntegerField(
            label='Total Amount',
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    class Meta:
        model = Dozi
        fields = [
            'name',
            'huduma',
            'accepted',
            'accepted_quantity',
            'accepted_date',
            'phone_number',
            'invoice_date',
            'line_one',
            'line_one_description',
            'line_one_quantity',
            'line_one_unit_price',
            'line_one_total_price',
            'accepted_line_one',


            'line_two',
            'line_two_description',
            'line_two_quantity',
            'line_two_unit_price',
            'line_two_total_price',
            'accepted_line_two',
            
            'line_three',
            'line_three_description',
            'line_three_quantity',
            'line_three_unit_price',
            'line_three_total_price',
            'accepted_line_three',

            'line_four',
            'line_four_description',
            'line_four_quantity',
            'line_four_unit_price',
            'line_four_total_price',
            'accepted_line_four',

            'line_five',
            'line_five_description',
            'line_five_quantity',
            'line_five_unit_price',
            'line_five_total_price',
            'accepted_line_five',

            'line_six',
            'line_six_description',
            'line_six_quantity',
            'line_six_unit_price',
            'line_six_total_price',
            'accepted_line_six',

            'line_seven',
            'line_seven_description',
            'line_seven_quantity',
            'line_seven_unit_price',
            'line_seven_total_price',
            'accepted_line_seven',

            'line_eight',
            'line_eight_description',
            'line_eight_quantity',
            'line_eight_unit_price',
            'line_eight_total_price',
            'accepted_line_eight',

            'line_nine',
            'line_nine_description',
            'line_nine_quantity',
            'line_nine_unit_price',
            'line_nine_total_price',
            'accepted_line_nine',

            'line_ten',
            'line_ten_description',
            'line_ten_quantity',
            'line_ten_unit_price',
            'line_ten_total_price',
            'accepted_line_ten',

            'total',
            'paid',
            'invoice_type'

        ]



class VipimoForm(forms.ModelForm):

    name = forms.CharField(
        label='Patient Name',
        widget=forms.TextInput(attrs={'id' :'tag'})
  
       )
    huduma = forms.ChoiceField(
        label='TYPE OF INFORMATIONS',
        choices = choose_huduma_vipimo_watoto
  
       )
    class Meta:
        model = Vipimo
        fields = [
            'name',
            'huduma',
            'accepted_quantity',
            'accepted_date',
            'phone_number',
            'invoice_date',
            'line_one',
            'line_one_description',
            'line_one_quantity',
            'line_one_unit_price',
            'line_one_total_price',
            'accepted_line_one',


            'line_two',
            'line_two_description',
            'line_two_quantity',
            'line_two_unit_price',
            'line_two_total_price',
            'accepted_line_two',
            
            'line_three',
            'line_three_description',
            'line_three_quantity',
            'line_three_unit_price',
            'line_three_total_price',
            'accepted_line_three',

            'line_four',
            'line_four_description',
            'line_four_quantity',
            'line_four_unit_price',
            'line_four_total_price',
            'accepted_line_four',

            'line_five',
            'line_five_description',
            'line_five_quantity',
            'line_five_unit_price',
            'line_five_total_price',
            'accepted_line_five',

            'line_six',
            'line_six_description',
            'line_six_quantity',
            'line_six_unit_price',
            'line_six_total_price',
            'accepted_line_six',

            'line_seven',
            'line_seven_description',
            'line_seven_quantity',
            'line_seven_unit_price',
            'line_seven_total_price',
            'accepted_line_seven',

            'line_eight',
            'line_eight_description',
            'line_eight_quantity',
            'line_eight_unit_price',
            'line_eight_total_price',
            'accepted_line_eight',

            'line_nine',
            'line_nine_description',
            'line_nine_quantity',
            'line_nine_unit_price',
            'line_nine_total_price',
            'accepted_line_nine',

            'line_ten',
            'line_ten_description',
            'line_ten_quantity',
            'line_ten_unit_price',
            'line_ten_total_price',
            'accepted_line_ten',

            'total',
            'paid',
            'invoice_type'

        ]

        
    def clean_invoice_number(self):
        invoice_number = self.cleaned_data.get('invoice_number')
        if not invoice_number:
            raise forms.ValidationError('This field is required')
        return invoice_number

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError('This field is required')
        return name
        

class VipimoUpdateForm(forms.ModelForm):

    name = forms.CharField(
            label=False,
            widget=forms.TextInput(attrs={'id' :'tag'})
      
       )
    huduma = forms.ChoiceField(
        label='TYPE OF INFORMATIONS',
        required=False,
        choices = choose_huduma_vipimo_watoto
  
       )
    line_one = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_one_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_one_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_one_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_one_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_two = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_two_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_two_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_two_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_two_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_three = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_three_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_three_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_three_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_three_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_four = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_four_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_four_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_four_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_four_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_five = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_five_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_five_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_five_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_five_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_six = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_six_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_six_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_six_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_six_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_seven = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_seven_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_seven_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_seven_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_seven_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_eight = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_eight_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_eight_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_eight_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_eight_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_nine = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_nine_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_nine_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_nine_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_nine_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_ten = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_ten_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_ten_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_ten_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_ten_total_price = forms.IntegerField(
            label=False,
            required=False,

            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    total = forms.IntegerField(
            label='Total Amount',
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    class Meta:
        model = Vipimo
        fields = [
            'name',
            'huduma',
            'accepted_quantity',
            'accepted_date',
            'phone_number',
            'invoice_date',
            'line_one',
            'line_one_description',
            'line_one_quantity',
            'line_one_unit_price',
            'line_one_total_price',
            'accepted_line_one',


            'line_two',
            'line_two_description',
            'line_two_quantity',
            'line_two_unit_price',
            'line_two_total_price',
            'accepted_line_two',
            
            'line_three',
            'line_three_description',
            'line_three_quantity',
            'line_three_unit_price',
            'line_three_total_price',
            'accepted_line_three',

            'line_four',
            'line_four_description',
            'line_four_quantity',
            'line_four_unit_price',
            'line_four_total_price',
            'accepted_line_four',

            'line_five',
            'line_five_description',
            'line_five_quantity',
            'line_five_unit_price',
            'line_five_total_price',
            'accepted_line_five',

            'line_six',
            'line_six_description',
            'line_six_quantity',
            'line_six_unit_price',
            'line_six_total_price',
            'accepted_line_six',

            'line_seven',
            'line_seven_description',
            'line_seven_quantity',
            'line_seven_unit_price',
            'line_seven_total_price',
            'accepted_line_seven',

            'line_eight',
            'line_eight_description',
            'line_eight_quantity',
            'line_eight_unit_price',
            'line_eight_total_price',
            'accepted_line_eight',

            'line_nine',
            'line_nine_description',
            'line_nine_quantity',
            'line_nine_unit_price',
            'line_nine_total_price',
            'accepted_line_nine',

            'line_ten',
            'line_ten_description',
            'line_ten_quantity',
            'line_ten_unit_price',
            'line_ten_total_price',
            'accepted_line_ten',

            'total',
            'paid',
            'invoice_type'

        ]






class AvailableMedicinesForm(forms.ModelForm):

    medicine_name = forms.CharField(
        label='Medicine Name ',
        widget=forms.TextInput(attrs={'id' :'medicine_name'})
  
       )
    
    class Meta:
        model = AvailableMedicines
        fields = '__all__'