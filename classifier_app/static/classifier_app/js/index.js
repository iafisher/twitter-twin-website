$(document).ready(function () {
    var csrftoken = $("[name=csrfmiddlewaretoken]").val();
    // Set up jQuery's AJAX functions to automatically include the CSRF token.
    //   Copied from docs.djangoproject.com/en/dev/ref/csrf/#ajax
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });


    $("#handle-input-button").click(function () {
        // Twitter usernames cannot be longer than 15 characters.
        var handle = $("#handle-input").val().slice(0, 15);
        var url = '/ajax_classify/' + handle;
        $.get(url, displayCoefficients);
    });

    $("#tweet-input-button").click(function () {
        // Tweets cannot be longer than 280 characters.
        var tweet = $("#tweet-input").val().slice(0, 280);
        $.post('/ajax_classify_tweet/', {'tweet': tweet}, displayCoefficients);
    });

    openTab(null, "handle");
});


function displayCoefficients(data) {
    var coefficients = data['coefficients'];
    // Remove any coefficients that might already be there.
    $(".coefficient").detach();
    for (var i = 0; i < coefficients.length; i++) {
        var elem = makeCoefficientElement(coefficients, i);
        $("#img-row div:nth-child(" + (i+1) + ")").append(elem);
    }
}


function makeCoefficientElement(coefficients, i) {
    var perc = ("" + (coefficients[i] * 100).toFixed(1)) + "%";
    var classes = ["coefficient"];
    if (isMax(coefficients, i)) {
        classes.push("coefficient-green");
    } else if (coefficients[i] > 0.1) {
        classes.push("coefficient-yellow");
    } else {
        classes.push("coefficient-red");
    }
    return "<p class=\"" + classes.join(" ") + "\">" + perc + "</p>";
}


function isMax(coefficients, i) {
    for (var j = 0; j < coefficients.length; j++) {
        if (coefficients[j] > coefficients[i]) {
            return false;
        }
    }
    return true;
}


function openTab(evt, tabName) {
    $(".tabcontent").hide();
    $(".tablinks").removeClass("active");
    $("#tablink-" + tabName).addClass("active");
    $("#tab-" + tabName).show().addClass("active");
}


// Return true if an HTTP method is safe without a CSRF token
//   Copied from docs.djangoproject.com/en/dev/ref/csrf/#ajax
function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
