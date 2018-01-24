# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pickle

from django.core.files.storage import default_storage
from django.db import models
from sklearn.metrics import accuracy_score


# Create your models here.
class MLAlgorithm(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    enabled = models.BooleanField(blank=False, null=False)

    name = models.CharField(max_length=100, blank=False, null=False)
    model_import = models.CharField(max_length=100, blank=False, null=False)
    reference_url = models.CharField(max_length=100, blank=False, null=False)
    reference_description = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        ordering = ('created',)

class MLModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    accuracy_score = models.FloatField(blank=False, null=False)
    model_file = models.CharField(max_length=100, blank=False, null=False)

    algorithm = models.ForeignKey(MLAlgorithm, on_delete=models.PROTECT)

    data_file = models.CharField(max_length=100, blank=False, null=False)
    predictors = models.CharField(max_length=10000, blank=False, null=False)
    targets = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        ordering = ('created',)

    @staticmethod
    def create_from_results(algorithm, model, pred_test, tar_test, csv_file, predictors, targets):
        predictions = model.predict(pred_test)
        model_file = csv_file[:-3] + algorithm + ".mlbuilder.model"
        ml_model = default_storage.open(model_file, "wb")
        pickle.dump(model, ml_model)

        # confusion_matrix = confusion_matrix(tar_test, predictions)
        return MLModel.objects.create(algorithm=MLAlgorithm.objects.get(name=algorithm),
                                      accuracy_score=accuracy_score(tar_test, predictions),
                                      data_file=csv_file, model_file=model_file,
                                      predictors=predictors, targets=targets)
