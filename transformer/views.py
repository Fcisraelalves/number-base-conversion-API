from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

@api_view(['GET'])
def decimal_to_binary(request):
    
    value = request.query_params.get('value')

    try:
        value = int(value)
    except (TypeError, ValueError):
        return Response(data={'error' : 'The value must be a number'},
                        status=status.HTTP_400_BAD_REQUEST)
    
    rests = []
    while True:
        
        quotient = value // 2
        rest = value % 2

        rests.append(rest)
        value = quotient

        if quotient == 1:
            break
    rests.append(1)

    binary = ''.join([str(digit) for digit in rests[::-1]])

    return Response(
        data={'binary': binary}, status=status.HTTP_200_OK
    )


   