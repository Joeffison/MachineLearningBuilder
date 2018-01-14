# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from django.conf import settings
from django.contrib import messages
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.http import HttpResponse, JsonResponse
from rest_framework import status

from .models import MLModel


def __404_page():
    return HttpResponse("404 - Page not found ;)")
    #content = {"please move along": "404 - Page not found ;)"}
    #return Response(content, status=status.HTTP_404_NOT_FOUND)

def index(request):
    return __404_page()

def upload_csv(request):
    if "GET" == request.method:
        return __404_page()

    # if not GET, then proceed
    try:
        csv_file = request.FILES["file"]

        if not csv_file.name.endswith(".csv"):
            messages.error(request, "This is not a CSV file")
            return HttpResponse(messages)

        # if file is too large, return
        if csv_file.multiple_chunks():
            messages.error(request, "Uploaded file is too big (%.2f MB)." % (csv_file.size / (1000 * 1000),))
            return HttpResponse(messages)

        return JsonResponse(mlbuilder(csv_file), status=status.HTTP_202_ACCEPTED, safe=False)
    except Exception as e:
        return HttpResponse(e.message + repr(e), status=status.HTTP_400_BAD_REQUEST)

def mlbuilder(csv_file):
    #TODO: It must have a better way, as the data is in <class 'django.core.files.uploadedfile.InMemoryUploadedFile'>.
    content = csv_file.read().decode("utf-8")
    #TODO: Fix encoding
    predictors = content.split("\n")[0].replace("\ufeff", "").replace("\r", "").split(",")
    targets = predictors[-1]
    predictors = predictors[:-1]
    path = default_storage.save(os.path.join("tmp", csv_file.name), ContentFile(content))
    tmp_file = os.path.join(settings.MEDIA_ROOT, path)

    return __mlbuilder(tmp_file, predictors, targets)

def __mlbuilder(csv_file, predictors, targets):
    import pandas as pd
    from sklearn.model_selection import train_test_split

    historical_data = pd.read_csv(csv_file)
    pred_train, pred_test, tar_train, tar_test = train_test_split(historical_data[predictors], historical_data[targets],
                                                                  test_size=.3)

    implemented_models = [
        ("Decision Tree", __decision_tree),
        ("Logistic Regression", __logistic_regression),
    ]

    return {
        #"Predictors_Correlation": historical_data.corr()[targets],
        "models": [MLModel(model[0], model[1](pred_train, tar_train), pred_test, tar_test).to_json()
                   for model in implemented_models]
    }

def __decision_tree(X, Y):
    from sklearn.tree import DecisionTreeClassifier
    return DecisionTreeClassifier().fit(X, Y)

# Despite its name, it's a classification algorithm
# which predicts the probability of occurrence of an event by fitting data to a logit function.
def __logistic_regression(X, Y):
    from sklearn.linear_model import LogisticRegression
    return LogisticRegression().fit(X, Y)
