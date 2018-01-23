function mlbCtrl(mlbModelService, mlbUtilsService, mlbConstants) {
  var vm = this;
  vm.title = mlbConstants.PROJECT_NAME;

  vm.uploadURL = mlbModelService.uploadURL;
  vm.downloadMLModel = mlbModelService.downloadMLModel;
  vm.downloadCreateModel = mlbModelService.downloadCreateModel;
  vm.downloadLoadModel = mlbModelService.downloadLoadModel;
  vm.printJson = mlbUtilsService.prettyPrintJson;
  vm.models = [];
  vm.onSuccessCSVUpload = function (response) {
    updateModels(response.data);
  };

  vm.onErrorCSVUpload = function () {
    updateModels(mlbModelService.models);
  };

  function updateModels(newData) {
    mlbUtilsService.replaceArray(vm.models, newData);
    mlbUtilsService.activateTooltips();

    angular.forEach(vm.models, function (item) {
      item.downloadMLModel = mlbModelService.downloadMLModel(item);
    });
  }
}

angular.module('app')
  .controller('MlbController', ['mlbModelService', 'mlbUtilsService', 'mlbConstants',
    mlbCtrl]);
