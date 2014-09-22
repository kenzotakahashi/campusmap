var mapControllers = angular.module('mapControllers', []);


mapControllers.controller('DirectionCtrl', function ($scope, $http, $routeParams) {
  // $http.get('../api/v1/direction/' + $routeParams.topicId).success(function(data) {
  //   $scope.result = data;
  // }); 
  $scope.room = 305;
  $scope.entrance = 'N'

  $scope.valid = function() {
    if ($scope.room == 305) {
      return true;
    }
    return false;
  }

  $scope.getDirection = function() {
    // console.log($scope.entrance);
    // console.log($scope.room);
    $http.get('../api/v1/direction/' + $scope.room +'/'+ $scope.entrance).success(function(data) {
      $scope.direction = data.direction;
      console.log($scope.direction)
    }); 
  }


});



// utteranceControllers.controller('EditCtrl', function ($scope, $http, $routeParams, $location) {
// 	$scope.utterance;
// 	$scope.nodeSelected = false;
// 	$scope.selectedNode;	

// 	$scope.editUtterance;
// 	$scope.editNodeSelected = false;
// 	$scope.editSelectedNode;

// 	$scope.tooltipCreate = {"title": "Create"};
// 	$scope.tooltipEdit = {"title": "Edit"};
// 	$scope.tooltipDelete = {"title": "Delete"};

// 	$http.get('../api/v1.0/topics/' + $routeParams.topicId).success(function(data) {
// 		checkTree(data.tree);
// 		$scope.user = data.user;
// 	});


// });