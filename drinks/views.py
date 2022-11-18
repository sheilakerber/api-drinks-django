from django.http import JsonResponse
from .models import Drink, Coffee
from .serializers import DrinkSerializer, CoffeeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

""" DRINKS IN GENERAL """
@api_view(['GET', 'POST'])
def drink_list(request, format=None):
    
    if request.method == 'GET':
        # get drinks > serialize them > return json
        drinks = Drink.objects.all()
        serialized = DrinkSerializer(drinks, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
        # return JsonResponse({'drinks': serialized.data}, safe=False)  # old way

    if request.method == 'POST':
        # take de data about the new drink and deserialize it
        serialized = DrinkSerializer(data=request.data)

        # check if data is valid
        if serialized.is_valid():
            # add the drink to the database
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id, format=None):

    # validation to the data 
    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DrinkSerializer(drink)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = DrinkSerializer(drink, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


""" COFFEES """
## list all the coffees
@api_view(['GET'])      
def coffees_list(request, format=None):
    coffees = Coffee.objects.all()
    serialized = CoffeeSerializer(coffees, many=True)
    return Response(serialized.data, status=status.HTTP_200_OK)

## add a new coffee
@api_view(['POST'])
def add_coffee(request, format=None):
    serialized = CoffeeSerializer(data=request.data)
    if serialized.is_valid():
        serialized.save()
        return Response(serialized.data, status=status.HTTP_200_OK)

## edit a coffe
@api_view(['PUT'])
def update_coffee(request, id, format=None):
    try:
        coffee = Coffee.objects.get(pk=id)
    except Coffee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serialized = CoffeeSerializer(coffee, data=request.data)

    if serialized.is_valid():
        serialized.save()
        return Response(serialized.data, status=status.HTTP_200_OK)

    return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

## delete a coffee
@api_view(['DELETE'])
def delete_coffee(request, id, format=None):
    try:
        coffee = Coffee.objects.get(pk=id)
    except Coffee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    coffee.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)



