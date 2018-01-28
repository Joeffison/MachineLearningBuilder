/* eslint no-undef: off */
BACKEND_URL = 'http://127.0.0.1:8000';

angular.module('app').constant('mlbResources', {
  BACKEND_URL: BACKEND_URL,
  GET_FILE: BACKEND_URL + '/get_file/',
  MLBUILDER_CREATE: BACKEND_URL + '/mlbuilder/',
  MLBUILDER_PREDICT: BACKEND_URL + '/mlbuilder/{id}/predict/'
});
