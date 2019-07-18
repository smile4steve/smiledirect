# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .datasource import DataSource
from .serializers import LaunchPadSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def get_one_launchpad(request, pk):
    # get just one by sequence number, not the lp_id, would be nicer to use padid
    if request.method == 'GET':
        return Response( _get_one_lp(pk) )
    elif request.method == 'POST':
        return Response({})


@api_view(['GET','POST'])
def get_all_launchpads(request):
    # get them all
    if request.method == 'GET':
        return Response( _get_all_lp() )
    elif request.method == 'POST':
        return Response({})


def _get_all_lp():
    ds  = DataSource.factory()
    rec = ds.get_all_lp()
    return rec


def _get_one_lp(id):
    ds  = DataSource.factory()
    rec = ds.get_lp_by_id( id )
    return rec


