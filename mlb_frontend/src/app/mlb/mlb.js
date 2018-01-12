angular.module('app').controller('mlbCtrl', function($scope, $http) {
  $scope.title = "Machine Learning Builder";

  $scope.uploadURL = 'http://127.0.0.1:8000/mlbuilder/upload/csv/';
  $scope.mlPlan = {
    username: "trial",
    plan: ["classification"]
  };

  $scope.onSuccessCSVUpload = function (data) {
    console.log("csvupload", "" + prettyPrintJson(data));
  };

  function prettyPrintJson(json) {
    return JSON ? JSON.stringify(json, null, '  ') : 'your browser doesnt support JSON so cant pretty print';
  }

});
