angular.module('starter.services', [])

.factory('Chats', function ($http) {
    function getData(callback) {
        $http.get('https://flashpay.herokuapp.com/getPayments')
            .success(callback);
    }

    return {
        all: getData,
        remove: function (chat) {
            chats.splice(chats.indexOf(chat), 1);
        },
        get: function (chatId) {
            for (var i = 0; i < chats.length; i++) {
                if (chats[i].id === parseInt(chatId)) {
                    return chats[i];
                }
            }
            return null;
        }
    };
});
