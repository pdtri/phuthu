var myApp = angular.module("myApp", []);
var myApp = angular.module('myApp').config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});
myApp.controller("nhapCtrl", ['$scope', '$http', '$cookies',
 function ($scope, $http, $cookies) {
    $http.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
    // To send the csrf code.
    $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
    // This function is called when the form is submitted.
    $scope.submit = function ($event) {
        // Prevent page reload.
        $event.preventDefault();
        // Send the data.
        var in_data = jQuery.param({'ten': $scope.congtac.ten, 'diachi': $scope.congtac.diachi,'congtac': $scope.congtac.congtac, 'csrfmiddlewaretoken': $cookies.csrftoken});
        $http.post('/add', in_data)
            success(function(out_data) {
            // Reset the form in case of success.
            alert("thanh cong");
            $scope.congtac = angular.copy({});
        });
    }
 }]);
 myApp.controller("timCtrl", ['$scope', '$http', '$cookies',
 function ($scope, $http, $cookies) {
    $http.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
    // To send the csrf code.
    $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
    // This function is called when the form is submitted.
    $scope.submit = function ($event) {
        // Prevent page reload.
        $event.preventDefault();
        // Send the data.
        var in_data = jQuery.param({'hovaten': $scope.tpc.hovaten,  'csrfmiddlewaretoken': $cookies.csrftoken});
        $http.post('/search', in_data)
          success(function(out_data) {
            // Reset the form in case of success.
            alert("thanh cong");
            $scope.tpc = angular.copy({});
           });
               // Simple GET request example :
               // 2 $http.get('/someUrl').
               // success(function(data, status, headers, config) {
               // this callback will be called asynchronously
               // when the response is available
              //   }).
          error(function(out_data) {
              // called asynchronously if an error occurs
              // or server returns response with an error status.
              alert("that bai");
           });
    } //ket thuc submit
 }]);
 var app1 = angular
     .module("myModule", [])
     .controller("myController", function ($scope){
         var employees = [
              { name: "Ben", gender: "Male", salary: 55000, city: "London" },
              { name: "Sara", gender: "Female", salary: 68000, city: "Chennai" },
              { name: "Mark", gender: "Male", salary: 57000, city: "London" },
              { name: "Pam", gender: "Female", salary: 53000, city: "Chennai" },
              { name: "Todd", gender: "Male", salary: 60000, city: "London" },
          ];

    });

var app2 = angular.module('myApp', []);
		app.controller('myCtrl', function($scope,$http) {
			$http.get("{% url 'ngtpc.json' %}")
		    .then(function(response) {
		        $scope.mydict = response.data;
		    });
		});

/*
  Developer: Hafiz Faraz Mukhtar
  Blog:      http://blog.hfarazm.com/
  Contact:   http://www.fb.com/h.farazmukhtar/
  Liscense:  MIT license 2014
*/

var GuitarApp = angular.module('GuitarApp', ['ngRoute','GuitarControllers']);

GuitarApp.config(['$routeProvider', function($routeProvider)
{
  $routeProvider.
  when('/list', {
    templateUrl: 'partials/list.html',
    controller: 'ListController'
  }).

  when('/details/:guitarID', {
    templateUrl: 'partials/details.html',
    controller: 'DetailsController'
  }).

  when('/test/:guitarID', {
    templateUrl: 'partials/test.html',
    controller: 'DetailsController'
  }).

  otherwise({
    redirectTo: '/list'
  });

}]);

