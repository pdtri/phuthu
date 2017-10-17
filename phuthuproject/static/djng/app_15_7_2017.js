/*
var myApp = angular.module("myApp",[]);
//var myApp = angular.module('myApp', [/* other dependencies /, 'djng.forms']);
var myApp = angular.module('myApp').config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');'ngCookies'
});
*/
  var myApp = angular.module("myApp", []);
  var myApp = angular.module('myApp').config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});
    myApp.controller("MyFormCtrl", ['$scope', '$http', '$cookies',
        function ($scope, $http, $cookies) {
            $scope.userprofile = {};
            $http.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
            $cookies.csrftoken = document.getElementsByName("csrfmiddlewaretoken")[0].value;
            $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
            $scope.submit = function ($event) {
                console.log($cookies.csrftoken);
                $event.preventDefault();
                var in_data = {
                    fname: $scope.userprofile.fname,
                    csrfmiddlewaretoken: $cookies.csrftoken
                };
                $http.post("{% url 'add_angularjs' %}", in_data)
                  .success(function(out_data) {
                    $scope.card = angular.copy({});
                });
            }
     }]);

/* myApp.controller("LoginCtrl", function($scope){
 $scope.username = 'thehalfheart';
 $scope.password = 'freetuts.net';
 this.checkLogin=function(){
   alert($scope.username + ' - ' + $scope.password);
 };
 $scope.CtrlTmp = this;
 return $scope.CtrlTmp;

});
*/