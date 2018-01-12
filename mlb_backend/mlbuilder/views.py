# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib import messages
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from pip.utils import logging
from rest_framework import status
from rest_framework.response import Response

def __404_page():
    return HttpResponse("404 - Page not found ;)")
    #content = {"please move along": "404 - Page not found ;)"}
    #return Response(content, status=status.HTTP_404_NOT_FOUND)

def index(request):
    return __404_page()

def upload_csv(request):
    data = {}
    if "GET" == request.method:
        return __404_page()

    # if not GET, then proceed
    try:
        csv_file = request.FILES["file"]
        print type(csv_file)
        print dir(csv_file)

        if not csv_file.name.endswith(".csv"):
            messages.error(request, "This is not a CSV file")
            return HttpResponse(messages)

        # if file is too large, return
        if csv_file.multiple_chunks():
            messages.error(request, "Uploaded file is too big (%.2f MB)." % (csv_file.size / (1000 * 1000),))
            return HttpResponse(messages)

        mlbuilder(csv_file)

    except Exception as e:
        #logging.getLogger("error_logger").error("Unable to upload file. " + repr(e))
        messages.error(request, "Unable to upload file. " + repr(e))
        return HttpResponse(e.message, status=status.HTTP_400_BAD_REQUEST)

    return HttpResponse("Page found <3")


def mlbuilder(csv_file):
    print "--- data science ---"
    #from pandas import Series, DataFrame
    import pandas as pd
    #import numpy as np
    import os
    #import matplotlib
    #import matplotlib.pylab as plt
    #from sklearn.model_selection import train_test_split
    #from sklearn.cluster import KMeans
    #from sklearn.metrics import classification_report
    #import sklearn.metrics

    path = default_storage.save(os.path.join('tmp', csv_file.name), ContentFile(csv_file.read()))
    tmp_file = os.path.join(settings.MEDIA_ROOT, path)
    historical_data = pd.read_csv(tmp_file)
    #, error_bad_lines=False, parse_dates=["transaction_date"], index_col="transaction_date"
    print historical_data

def read_file(csv_file):
    file_data = csv_file.read().decode("utf-8")
    lines = file_data.split("\n")
    # loop over the lines and save them in db. If error , store as string and then display
    for line in lines:
        # fields = line.split(",")
        data_dict = {}
        print line
        # data_dict["name"] = fields[0]
        # data_dict["start_date_time"] = fields[1]
        # data_dict["end_date_time"] = fields[2]
        # data_dict["notes"] = fields[3]
        try:
            print ''
            # form = EventsForm(data_dict)
            # if form.is_valid():
            #    form.save()
            # else:
            # logging.getLogger("error_logger").error(form.errors.as_json())
        except Exception as e:
            # logging.getLogger("error_logger").error(form.errors.as_json())
            pass
