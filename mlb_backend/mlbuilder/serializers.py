from rest_framework import serializers
from .models import MLModel
from .constants import template_code


class MLModelSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    code_create_model = serializers.SerializerMethodField()
    code_load_model = serializers.SerializerMethodField()
    references = serializers.SerializerMethodField()
    predictors = serializers.SerializerMethodField()

    class Meta:
        model = MLModel
        fields = ('id', 'name', 'code_create_model', 'code_load_model', 'accuracy_score', 'model_file',
                  'references', 'created', 'predictors')

    def get_name(self, obj):
        return obj.algorithm.name

    def get_code_create_model(self, obj):
        return template_code.template_model_creation.format(model_import=obj.algorithm.model_import,
                                                            csv_file=obj.data_file, model_file=obj.model_file,
                                                            predictors=str(obj.predictors.split(', ')),
                                                            targets=str(obj.targets.split(', ')))

    def get_code_load_model(self, obj):
        return template_code.template_model_predictor.format(model_file=obj.model_file,
                                                             predictors=str(obj.predictors.split(', ')))

    def get_references(self, obj):
        return {'url': obj.algorithm.reference_url, 'description': obj.algorithm.reference_description}

    def get_predictors(self, obj):
        return obj.predictors.split(', ')
