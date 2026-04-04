from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

def _sucessive_divisions(base : int, value : int):
    rests = []

    while True:
        
        quotient = value // base
        rest = value % base

        rests.append(rest)
        value = quotient

        if quotient < base:
            break
    
    rests.append(quotient)

    return rests


@api_view(['GET'])
def decimal_to_binary(request):
    
    if not 'value' in request.query_params:
        return Response(
            data={'error': 'The value must exists'},
            status=status.HTTP_400_BAD_REQUEST
        )
    value = request.query_params.get('value')

    try:
        value = int(value)
    except (TypeError, ValueError):
        return Response(data={'error' : 'The value must be a number'},
                        status=status.HTTP_400_BAD_REQUEST)
    
    rests = _sucessive_divisions(2, value)

    binary = ''.join([str(digit) for digit in rests[::-1]])

    return Response(
        data={'binary': binary}, status=status.HTTP_200_OK
    )


@api_view(['GET'])
def binary_to_decimal(request):

    if not 'value' in request.query_params:
        return Response(
            data={'error': 'The value must exists'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    value = str(request.query_params.get('value'))

    digits = [int(digit) for digit in value]

    digits_weights = zip(digits[::-1], range(len(digits)))

    decimal_value = int(sum([digit[0]*2**digit[1] for digit in digits_weights]))

    return Response(
        data={'decimal': decimal_value},
        status=status.HTTP_200_OK,
    )

@api_view(['GET'])
def decimal_to_octal(request):

    if not 'value' in request.query_params:
        return Response(
            data={'error': 'The value must exists'},
            status=status.HTTP_400_BAD_REQUEST
        )
    value = request.query_params.get('value')

    try:
        value = int(value)
    except (TypeError, ValueError):
        return Response(data={'error' : 'The value must be a number'},
                        status=status.HTTP_400_BAD_REQUEST)
    
    rests = _sucessive_divisions(8, value)

    octal = ''.join([str(digit) for digit in rests[::-1]])

    return Response(
        data={'octal': octal}, status=status.HTTP_200_OK
    )

@api_view(['GET'])
def decimal_to_hex(request):

    hex_simbols = {10 : 'A', 
                   11 : 'B',
                   12 : 'C',
                   13 : 'D',
                   14 : 'E',
                   15 : 'F'}

    if not 'value' in request.query_params:
        return Response(
            data={'error': 'The value must exists'},
            status=status.HTTP_400_BAD_REQUEST
        )
    value = request.query_params.get('value')

    try:
        value = int(value)
    except (TypeError, ValueError):
        return Response(data={'error' : 'The value must be a number'},
                        status=status.HTTP_400_BAD_REQUEST)
    
    rests = _sucessive_divisions(16, value)

    for i, rest in enumerate(rests):
        if rest in hex_simbols:
            rests[i] = hex_simbols[rest]

    hex = ''.join([str(digit) for digit in rests[::-1]])

    return Response(
        data={'hex': hex}, status=status.HTTP_200_OK
    )
