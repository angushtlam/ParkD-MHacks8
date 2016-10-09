var map = null;

$(document).ready(function () {
    setUpLeaflet();
    loadAllLotMarkersOnLeafletMap(map);
    loadTrafficHeatMap(map, 2);
    removeLoadingScreen();
    attachTimeButtonBehaviors();
});

function setUpLeaflet() {
    map = L.map("map", {closePopupOnClick: false}).setView([userLat, userLong], 15);

    L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        minZoom: 14,
        maxZoom: 17,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);
}

function removeLoadingScreen() {
    var loading = setInterval(function () {
        $("#modal").addClass("animated rollOut");
        $(".lot-block").addClass("animated lightSpeedIn");

        var modal = setInterval(function () {
            $("#modal").css("display", "none");
            clearInterval(modal);
            clearInterval(loading);
        }, 200);

    }, 1000);
}

function attachTimeButtonBehaviors() {
    $("#btn-time-morning").click(function () {
        loadTrafficHeatMap(map, 0);
    });
    $("#btn-time-day").click(function () {
        loadTrafficHeatMap(map, 1);
    });
    $("#btn-time-afternoon").click(function () {
        loadTrafficHeatMap(map, 2);
    });
    $("#btn-time-midnight").click(function () {
        loadTrafficHeatMap(map, 3);
    });
}
