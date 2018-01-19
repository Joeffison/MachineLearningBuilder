function mlbCtrl(mlbModelService, mlbUtilsService, mlbConstants,
                 $scope) {
  $scope.title = mlbConstants.project_name;

  $scope.uploadURL = mlbModelService.uploadURL;
  $scope.downloadMLModel = mlbModelService.downloadMLModel;
  $scope.downloadCreateModel = mlbModelService.downloadCreateModel;
  $scope.downloadLoadModel = mlbModelService.downloadLoadModel;

  $scope.models = [];
  $scope.onSuccessCSVUpload = function(response) {
    updateModels(response.data.models);
  };

  $scope.onErrorCSVUpload = function(response) {
    updateModels(mlbModelService.models);
  };

  function updateModels(newData) {
    mlbUtilsService.replaceArray($scope.models, newData);
    mlbUtilsService.activateTooltips();

    angular.forEach($scope.models, function (item) {
      item.downloadMLModel = mlbModelService.downloadMLModel(item);
    });
  }

}

angular.module("app")
  .controller("mlbCtrl", ["mlbModelService", "mlbUtilsService", "mlbConstants",
    "$scope",
    mlbCtrl]);
