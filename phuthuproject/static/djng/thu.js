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
        $http.post('/thu', in_data)
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
        var in_data = jQuery.param({'hovaten': $scope.congtac.ten,  'csrfmiddlewaretoken': $cookies.csrftoken});
        $http.post('/tim_congtac', in_data)
          success(function(out_data) {
            // Reset the form in case of success.
            alert("thanh cong");
            $scope.congtac = angular.copy({});
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

//myApp.controller("MyFormCtrl", ['$scope', '$http', '$cookies',

            /*
             * Author: thehalfheart@gmail.com
             * Website: freetuts.net
             */
var myTaps=  angular.module('ngTabExample', [])

myApp.controller('TabController', function($scope){
                    // $scope index lưu trữ tab hiện tại, ban đầu gán nó = tab1
                    $scope.current_tab = 1;

                    // Hàm đổi tab
                    $scope.changeTab = function(index){
                        $scope.current_tab = index;
                    };
                    // Hàm kiểm tra có phải tab hiện tại hay không
                    // hàm này sẽ trả về true/false và dùng kết hợp
                    // với ng-class để active menu
                    $scope.isActiveTab = function(index){
                        return index === $scope.current_tab;
                    };
                });
myApp.controller("MyFormCtrl",
                              ['$scope', '$http', '$cookies',
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
                                              'id': $scope.congtac.id,
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
                                                     }; //het lenh scope
                                             }]);




myApp.controller("PanelController",
              function(){
                  this.tab = 1;
                  this.selectTab = function(setTab){
                        this.tab = setTab;
                         };
                  this.isSelected = function(checkTab){
                        return this.tab === checkTab;
                         };
              //het fun
              });// het control


