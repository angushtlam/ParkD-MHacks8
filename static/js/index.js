/**
 * Created by angus on 10/9/16.
 */
$(document).ready(function () {
    $("#btn-start").click(function () {
        console.log("sup");
        $("#circle").css("display", "block");

        var ms = 0;
        var interval = setInterval(function () {
            $("#circle").css({
                "width": ms * 15,
                "height": ms * 6
            });
            ms++;

            if (ms > 300) {
                $("#hero").addClass("animated fadeOut");
                clearInterval(interval);

                window.location.href = "map";
            }
        }, 2);
    });

    $("#btn-help").click(function () {
        console.log("m8");
        $("#circle").css({
            "display": "block",
            "background-color": "#000"
        });

        var ms = 0;
        var interval = setInterval(function () {
            $("#circle").css({
                "width": ms * 12,
                "height": ms * 9
            });
            ms++;

            if (ms > 300) {
                $("#hero").addClass("animated fadeOut");
                clearInterval(interval);

                window.location.href = "about";
            }
        }, 2);
    });
});