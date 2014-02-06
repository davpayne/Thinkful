var app = angular.module('PartyApp', [
    'ngRoute', 'ui.bootstrap']);
    
    app.config(['$routeProvider', 
        function($routeProvider) {
        $routeProvider
            .when('/', {
                templateUrl: '../static/home.html',
                controller: 'HomePageController',
            })
            .when('/party', {
                templateUrl: '../static/party.html',
                controller: 'PartyController'
            })
            .when('/secondPage', {
                templateUrl: '../static/secondPage.html',
                controller: 'SecondController'
            })
            .otherwise({ redirectTo: '/' });
    }])
    /*
    function PartyController($scope){
        $scope.RETRIEVE_DEFAULT_NR = 5;
        $scope.state = {};
        $scope.state.partyList = [];
        $scope.state.retrieveNr = $scope.RETRIEVE_DEFAULT_NR;
        $scope.state.pageName = 'partyList';
    }*/
    
    .controller('PartyController', [
        '$scope',
        '$http',
        function($scope, $http, windowAlert) {
            $scope.RETRIEVE_DEFAULT_NR = 5;
            $scope.state = {};
            $scope.state.partyList = [];
            $scope.state.retrieveNr = $scope.RETRIEVE_DEFAULT_NR;
            $scope.state.pageName = 'partyList';}])/*
            $scope.state.categories = [
                {name: 'Food'},
                {name: 'Beverages'},
                {name: 'Miscellaneous'}
                }];
            $scope.addItem = function() {
                if (!$scope.state.newItem) {
                     $http
                        .post('/partyAdd', {
                            item: $scope.state.newItem
                        })
                        .success(function(data, status, headers, config) {
                            if (data.success) {
                                $scope.retrieveCategory(
                                    $scope.state.retrieveNr
                                );
                            }
                        })
                        .error(function(data, status, headers, config) {
                        });
                } 
            };

            $scope.retrieveCategory = function(n) {
                $http
                    .get('/partyRetrieve/' + n)
                    .success(function(data, status, headers, config) {
                        if (data.success) {
                            $scope.state.partyList = data.partyList;
                        } 
                    })
                    .error(function(data, status, headers, config) {
                    });
            };

            $scope.setAndRetrieveCategory = function(n) {
                $scope.state.retrieveNr = n;
                $scope.retrieveCategory($scope.state.retrieveNr);
            };
        }
    ])
    /*
    .controller('PartyController', [
        '$scope',
        '$http',
        function($scope, $http) {
            $scope.RETRIEVE_DEFAULT_NR = 5;
            $scope.state = {};
            $scope.state.partyList = [];
            $scope.state.retrieveNr = $scope.RETRIEVE_DEFAULT_NR;
            $scope.state.pageName = 'partyList';

            $scope.addItem = function() {
                if ($scope.state.newItem) {
                    $http
                        .post('/partyAdd', {
                            item: $scope.state.newItem
                        })
                        .success(function(data, status, headers, config) {
                            if (data.success) {
                                $scope.retrieveCategory(
                                    $scope.state.retrieveNr
                                );
                            } 
                        })
                        .error(function(data, status, headers, config) {
                        });
                }
            };

            $scope.retrieveCategory = function(n) {
                $http
                    .get('/partyRetrieve/' + n)
                    .success(function(data, status, headers, config) {
                        if (data.success) {
                            $scope.state.partyList = data.partyList;
                        } 
                    })
                    .error(function(data, status, headers, config) {
                    });
            };

            $scope.setAndRetrieveCategory = function(n) {
                $scope.state.retrieveNr = n;
                $scope.retrieveCategory($scope.state.retrieveNr);
            };
        }
    )]*/
    .directive('navtabs', function() {
        return {
            restrict: 'E',
            replace: true,
            templateUrl: '../static/navtabs.html',
            scope: {
                pageName: '='
            },
            controller: [
                '$scope',
                function($scope) {
                    this.selectTabIfOnPage = function(tab) {
                        if (tab.name === $scope.pageName) {
                            tab.selected = true;
                        }
                    };
                }
            ]
        };
    })

    .directive('tab', function() {
        return {
            require: '^navtabs',
            restrict: 'E',
            replace: true,
            transclude: true,
            scope: {},
            template: '<li ng-class="{ active: selected }"><a href="{{ href }}" ng-transclude></a></li>',
            link: function(scope, element, attr, navtabsCtrl) {
                scope.name = attr.name;
                scope.href = attr.href;
                scope.selected = false;
                navtabsCtrl.selectTabIfOnPage(scope);
            }
        };
    })

    function SecondController($scope){
        $scope.state = {};
        $scope.state.pageName = 'secondPage';
    }
    
    function HomePageController($scope){
        $scope.state = {};
        $scope.state.pageName = 'homePage';
    }
    ;
