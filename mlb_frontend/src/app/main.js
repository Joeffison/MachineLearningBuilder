angular
  .module('app')
  .component('app', {
    templateUrl: 'app/main.html'
  });

(function($){
  $(function(){

    $('.button-collapse').sideNav();
    $('.parallax').parallax();

  }); // end of document ready
})(jQuery); // end of jQuery name space
