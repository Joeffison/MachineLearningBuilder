BACKEND_URL = "http://127.0.0.1:8000";

angular.module("app").constant("mlbResources", {
  backend_url: BACKEND_URL,
  get_file: BACKEND_URL + "/get_file/",
  mlbuilder_upload_file: BACKEND_URL + "/mlbuilder/upload/csv/",
});
