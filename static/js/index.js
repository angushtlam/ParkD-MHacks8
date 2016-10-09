/**
 * Created by angus on 10/9/16.
 */
$(document).ready(function () {
    $("#btn-start").click(function () {
        console.log("test");
        $("#circle").css("display", "block");

        var ms = 0;
        var interval = setInterval(function () {
            $("#circle").css({
                "width": ms * 10,
                "height": ms * 10
            });
            ms++;

            if (ms > 300) {
                $("#hero").addClass("animated fadeOut");
                clearInterval(interval);

                window.location.href = "map";
            }
        }, 1);
    });
});