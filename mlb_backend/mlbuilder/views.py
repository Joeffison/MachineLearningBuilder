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
from .serializers import MLModelSerializer


def mlmodel_list(request):
    """
    List all ML Models, or create a new one.
    """
    if request.method == 'GET':
        models = MLModel.objects.all()
        serializer = MLModelSerializer(models, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        return ___build_based_on_csv(request)
        # serializer = MLModelSerializer(data=JSONParser().parse(request))
        # if serializer.is_valid():
        #    serializer.save()
        #    return JsonResponse(serializer.data, status=201)
        # return JsonResponse(serializer.errors, status=400)
    return HttpResponse(status=404)

def mlmodel_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        model = MLModel.objects.get(pk=pk)
    except MLModel.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MLModelSerializer(model)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        pass
        # data = JSONParser().parse(request)
        # serializer = MLModelSerializer(model, data=data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return JsonResponse(serializer.data)
        # return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        pass
        # model.delete()
        # return HttpResponse(status=204)
    return HttpResponse(status=404)

def ___build_based_on_csv(request):
    try:
        csv_file = request.FILES["file"]

        if not csv_file.name.endswith(".csv"):
            messages.error(request, "This is not a CSV file")
            return HttpResponse(messages)

        # if file is too large, return
        if csv_file.multiple_chunks():
            messages.error(request, "Uploaded file is too big (%.2f MB)." % (csv_file.size / (1000 * 1000),))
            return HttpResponse(messages)

        # TODO: It MUST have a better way, as csv_file is <class 'django.core.files.uploadedfile.InMemoryUploadedFile'>.
        content = csv_file.read().decode("utf-8")
        # TODO: Fix encoding
        predictors = content.split("\n")[0].replace("\ufeff", "").replace("\r", "").split(",")
        n_targets = 1
        targets = predictors[-n_targets:]
        predictors = predictors[:-n_targets]
        path = default_storage.save(os.path.join("tmp", csv_file.name), ContentFile(content))
        tmp_file = os.path.join(settings.MEDIA_ROOT, path)

        models = __mlbuilder(tmp_file, predictors, targets)
        serializer = MLModelSerializer(models, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, safe=False)
    except Exception as e:
        return HttpResponse(e.message + repr(e), status=status.HTTP_400_BAD_REQUEST)

def __mlbuilder(csv_file, predictors, targets):
    import pandas as pd
    from sklearn.model_selection import train_test_split

    historical_data = pd.read_csv(csv_file)
    pred_train, pred_test, tar_train, tar_test = train_test_split(historical_data[predictors], historical_data[targets],
                                                                  test_size=.3)

    if len(targets) == 1:
        tar_train = tar_train.values.ravel()
        tar_test = tar_test.values.ravel()
    implemented_models = [
        ("Decision Tree", __decision_tree),
        ("Random Forest", __random_forest),
        ("Logistic Regression", __logistic_regression),
        ("Gaussian Naive Bayes", __gaussian_naive_bayes)
    ]

    # "Predictors_Correlation": historical_data.corr()[targets],
    models = [MLModel.create_from_results(model[0], model[1](pred_train, tar_train), pred_test, tar_test,
                                          csv_file, predictors, targets)
              for model in implemented_models]

    return models

def __decision_tree(X, Y):
    from sklearn.tree import DecisionTreeClassifier
    return DecisionTreeClassifier().fit(X, Y)

def __random_forest(X, Y):
    from sklearn.ensemble import RandomForestClassifier
    return RandomForestClassifier().fit(X, Y)

# Despite its name, it's a classification algorithm
# which predicts the probability of occurrence of an event by fitting data to a logit function.
def __logistic_regression(X, Y):
    from sklearn.linear_model import LogisticRegression
    return LogisticRegression().fit(X, Y)

def __gaussian_naive_bayes(X, Y):
    from sklearn.naive_bayes import GaussianNB
    return GaussianNB().fit(X, Y)
