function mlbModelService(mlbResources, mlbUtilsService) {
  var service = this;

  service.models = [];
  /* var mlPlan = {
    username: 'trial',
    plan: ['classification']
  }; */

  service.uploadURL = mlbResources.MLBUILDER_CREATE;

  service.predict = function (id, predictors) {

  };

  service.downloadMLModel = function (model) {
    return mlbResources.GET_FILE + model.model_file;
  };

  service.downloadCreateModel = function (model) {
    return mlbUtilsService.stringToFile(model.code_create_model, 'code_create_model.py');
  };

  service.downloadLoadModel = function (model) {
    return mlbUtilsService.stringToFile(model.code_load_model, 'code_load_model.py');
  };

  return service;
}

angular.module('app')
  .factory('mlbModelService', ['mlbResources', 'mlbUtilsService',
    mlbModelService]);
