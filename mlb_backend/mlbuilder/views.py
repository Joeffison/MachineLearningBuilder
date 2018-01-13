# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from django.conf import settings
from django.contrib import messages
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.http import HttpResponse, JsonResponse
from rest_framework import status


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
    response_data = {"message": "Something went wrong."}

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

        response_data = mlbuilder(csv_file)

    except Exception as e:
        #logging.getLogger("error_logger").error("Unable to upload file. " + repr(e))
        messages.error(request, "Unable to upload file. " + repr(e))
        return HttpResponse(e.message + repr(e), status=status.HTTP_400_BAD_REQUEST)

    return JsonResponse(response_data, status=status.HTTP_202_ACCEPTED, safe=False)


def mlbuilder(csv_file):
    #TODO: It must have a better way, as the data is in <class 'django.core.files.uploadedfile.InMemoryUploadedFile'>.
    content = csv_file.read().decode("utf-8")
    #TODO: Fix encoding
    predictors = content.split("\n")[0].replace("\ufeff", "").replace("\r", "").split(",")
    targets = predictors[-1]
    predictors = predictors[:-1]
    print predictors
    path = default_storage.save(os.path.join("tmp", csv_file.name), ContentFile(content))
    tmp_file = os.path.join(settings.MEDIA_ROOT, path)

    return __mlbuilder(tmp_file, predictors, targets)

def __mlbuilder(csv_file, predictors, targets):
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import classification_report
    import sklearn.metrics

    historical_data = pd.read_csv(csv_file)
    #, error_bad_lines=False, parse_dates=["transaction_date"], index_col="transaction_date"

    pred_train, pred_test, tar_train, tar_test = train_test_split(historical_data[predictors], historical_data[targets],
                                                                  test_size=.3)
    decision_tree = __decision_tree(pred_train, tar_train)
    predictions = decision_tree.predict(pred_test)
    # Analyze accuracy of predictions
    print sklearn.metrics.confusion_matrix(tar_test, predictions)

    return [
        {"name": "Decision Tree",
         "accuracy_score": sklearn.metrics.accuracy_score(tar_test, predictions),
         #"model": decision_tree
        }
    ]

def __decision_tree(X, Y):
    from sklearn import tree
    model = tree.DecisionTreeClassifier()
    model = model.fit(X, Y)
    return model
