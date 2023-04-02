from rest_framework import serializers

from UserSystem.models import User, Patient, Doctor




class PatientSignupSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={"input_type":"password"}, write_only=True)
    class Meta:
        model=User
        fields=['username','email','password','password2','name',
                ]
        extra_kwargs={
            'password': {'write_only':True}
        }

        # model = Patient
        # fields = ('address', 'phone', 'age', 'gender')

    def save(self, **kwargs):
        user= User(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
            name=self.validated_data['name']
            
        )
        password=self.validated_data['password']
        password2=self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({"Error":"Passwords do not match."})
        
        user.set_password(password)
        user.is_patient=True
        user.save()
        # address= self.validated_data['address']
        # phone= self.validated_data['phone']
        # age= self.validated_data['age']
        # gender= self.validated_data['gender']

        Patient.objects.create(user=user)
        # patient = Patient.objects.create(
        # user=user,
        # address=self.validated_data['address'],
        # phone=self.validated_data['phone'],
        # age=self.validated_data['age'],
        # gender=self.validated_data['gender']
        # )
        return user

class DoctorSignupSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={"input_type":"password"}, write_only=True)
    class Meta:
        model=User
        fields=['username','email','password','password2','name']
        extra_kwargs={
            'password': {'write_only':True}
        }

    def save(self, **kwargs):
        user= User(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
            name=self.validated_data['name']
            
        )
        password=self.validated_data['password']
        password2=self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({"Error":"Passwords do not match."})
        
        user.set_password(password)
        user.is_doctor=True
        user.save()
        
        
        Doctor.objects.create(user=user)

        return user

class DoctorSerializer(serializers.ModelSerializer):

    user = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Doctor
        fields = (
        'user',
        'id',
        'address',
        'phone',
        'age',
        'gender',
    )


class PatientSerializer(serializers.ModelSerializer):

    user = serializers.SlugRelatedField(
    many=False,
    read_only=True,
    slug_field='name'
    )

    class Meta:
        model = Patient
        fields = (
    'address',
    'phone',
    'age',
    'gender',
    'patient',
    
    )
    
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=['username','email', 'is_doctor', 'is_patient',]
