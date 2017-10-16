var myApp = angular.module("myApp", []);
  var myApp = angular.module('myApp').config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});

myApp.controller("MyFormCtrl", ['$scope', '$http', '$cookies',
function ($scope, $http, $cookies) {
    $http.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
    // To send the csrf code.
    $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
    // This function is called when the form is submitted.
    $scope.submit = function ($event) {
        // Prevent page reload.
        $event.preventDefault();
        // Send the data.
        var in_data = jQuery.param({
            'ten': $scope.congtac.ten,
            'diachi': $scope.congtac.diachi,
            'congtac': $scope.congtac.congtac,
            'csrfmiddlewaretoken': $cookies.csrftoken
            });

        $http.post('/add', in_data)
          .success(function(out_data) {
            // Reset the form in case of success.
            $scope.card = angular.copy({});
        });
    }
 }]);