from rest_framework import serializers
from ..models import CarList,ShowRoomList,Review


# # Validators (Here i use this to check that the chassisNumber must be alphanumeric)

# def alphanumeric(value):
#     if not str(value).isalnum():
#         raise serializers.ValidationError("Only alphanumeric characters are allowed")

               #// using serializer class
# class CarSerializer(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     name=serializers.CharField()
#     description=serializers.CharField()
#     active=serializers.BooleanField(read_only=True)
#     chassisNumber=serializers.CharField(validators=[alphanumeric])
#     price=serializers.DecimalField(max_digits=9,decimal_places=2)

#     def create(self,validated_data):
#         return CarList.objects.create(**validated_data) #The double asterisk (**) is the "unpacking" operator. It is used to unpack the contents of a dictionary and pass them as keyword arguments to a function or method. In this case, validated_data is a dictionary containing the validated input data for creating a new instance of the CarList model.
    
#     def update(self,instance,validated_data):#instance means data which is already present and validated_data means new data
#         instance.name=validated_data.get('name',instance.name)#so here basically it puts validated_data into instance that is updated data in place of old data
#         instance.description=validated_data.get('description',instance.description)
#         instance.active=validated_data.get('active',instance.active)
#         instance.chassisNumber=validated_data.get('chassisNumber',instance.chassisNumber)
#         instance.price=validated_data.get('price',instance.price)
#         instance.save()
#         return instance
    
#              # Field-level validation(here i used it which validates that the price must be greater or else it will raise validation error)
#     def validate_price(self,value):
#         if value <= 20000.00:
#             raise serializers.ValidationError("Price must be greater than 20000.00")
#         return value

#             # Object-level validation  (Here i need to take care that name and desc should not be same so for that i used validator)
#     def validate(self,data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("name and description must not be same") 
#         return data  
    
#     # def validate_chassisNumber(self,value):
#     #     if value!=alphanumeric:
#     #         raise serializers.ValidationError("chassisNumber must only be alphanumeric")



                # Using ModelSerializer class

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields='__all__'



class CarSerializer(serializers.ModelSerializer):
    discounted_price = serializers.SerializerMethodField()
    Reviews=ReviewSerializer(many=True,read_only=True)

    class Meta:
        model=CarList
        # fields=['name','description','active','chassisNumber','price']
        # #                  or 
        fields='__all__'

        # # if we don't want any particular field and want all other fields then
        # exclude=['price','name']

    def get_discounted_price(self,object):
        discountprice = object.price - 5000
        return discountprice
        
    
             # Field-level validation(here i used it which validates that the price must be greater or else it will raise validation error)
    def validate_price(self,value):
        if value <= 20000.00:
            raise serializers.ValidationError("Price must be greater than 20000.00")
        return value

            # Object-level validation  (Here i need to take care that name and desc should not be same so for that i used validator)
    def validate(self,data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("name and description must not be same") 
        return data  
    

class ShowRoomSerializer(serializers.ModelSerializer):
           # # nested serializers (here it is helping us to see all info about cars in showroom using showroom field)
    Showrooms = CarSerializer(many=True,read_only=True)
           # # StringRelatedField (used to reperesent target of relationships using __str__  method)
    Showrooms = serializers.StringRelatedField(many=True) 
           # # PrimaryKeyRelatedField (returns only primary key in output)
    # Showrooms = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
           # # HyperlinkRelatedField(returns links of particular car) Note: for this to work we need to use context={'request':request} in showroom_View
    # Showrooms= serializers.HyperlinkedRelatedField(

    #     many = True,
    #     read_only = True,
    #     view_name = 'car_detail'
    # )

    class Meta:
        model=ShowRoomList
        fields='__all__'

