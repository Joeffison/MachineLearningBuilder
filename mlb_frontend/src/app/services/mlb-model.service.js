function mlbModelService(mlbResources, mlbUtilsService) {
  var service = this;

  var mlPlan = {
    username: "trial",
    plan: ["classification"]
  };

  service.uploadURL = mlbResources.mlbuilder_upload_file;

  service.downloadMLModel = function(model) {
    return mlbResources.get_file + model.ml_model;
  };

  service.downloadCreateModel = function(model) {
    return mlbUtilsService.stringToFile(model.code_create_model, "code_create_model.py");
  };

  service.downloadLoadModel = function(model) {
    return mlbUtilsService.stringToFile(model.code_load_model, "code_load_model.py");
  };

  return service;
}

angular.module("app")
  .factory("mlbModelService", ["mlbResources", "mlbUtilsService",
    mlbModelService]);
