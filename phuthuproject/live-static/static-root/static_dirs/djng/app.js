var myApp = angular.module("myApp",[]);
myApp.controller("LoginCtrl", function($scope){
 $scope.username = 'thehalfheart';
 $scope.password = 'freetuts.net';
 this.checkLogin=function(){
   alert($scope.username + ' - ' + $scope.password);
 };
 $scope.CtrlTmp = this;
 return $scope.CtrlTmp;

});