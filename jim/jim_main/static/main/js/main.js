var jim = {
    lovingJim: function (jimSt) {
        alert("Your Loving Jim is " + jimSt);
    }
};
defer = $.Deferred();

defer.promise(jim);

function getLovingJim() {
    console.log('hehe')
    $.ajax({
        async: true,
        url: '/lovingJimJson.json',
        method: 'get',
        dataType: 'json',
        success: function (data) {
            defer.resolve(data['lovingJim']['title'])
            document.cookie = "lovingJim=" + data['lovingJim']['title'];
        },
        error: function (error) {
            console.log(error)
        }
    })
}

getLovingJim()

jim.done(function (jimSt) {
    jim.lovingJim(jimSt);
})
