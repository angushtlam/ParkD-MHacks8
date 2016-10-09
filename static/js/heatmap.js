/**
 * Created by karenx on 10/9/16.
 */

var currentHeatLayer = null;

function loadTrafficHeatMap(map, timeId) {
    if (currentHeatLayer != null) {
        map.removeLayer(currentHeatLayer);
    }

    $.ajax({
        url: "/api/lot/nearby",
        success: function (data, result) {
            var heatIndices = [];
            var llr = [];

            var json_data = JSON.parse(data);

            var keys = Object.keys(json_data);
            var values = keys.map(function(v) { return json_data[v]; });
            
            var divisor = 10000;

            for (var i = 0; i < values.length; i++) {
                var lot = values[i];

                var collegeVenues = lot["categories"]["college"];
                for (var venueIndex = 0; venueIndex < collegeVenues.length; venueIndex++) {
                    var lat = collegeVenues[venueIndex]["latitude"];
                    llr.push(lat);
                    var lng = collegeVenues[venueIndex]["longitude"];
                    llr.push(lng);

                    var rad = 0;

                    switch (timeId) {
                        case 0:
                            rad = (Math.max(collegeVenues[venueIndex]["check_ins"], 1000) / divisor);
                            break;
                        case 1:
                            rad = (Math.max(collegeVenues[venueIndex]["check_ins"], 1000) / divisor) / 2;
                            break;
                        case 2:
                            rad = (Math.max(collegeVenues[venueIndex]["check_ins"], 1000) / divisor) / 2;
                            break;
                        case 3:
                            rad = 0;
                            break;
                    }

                    llr.push(rad);

                    heatIndices.push(llr);
                    llr = [];
                }

                var workVenues = lot["categories"]["work"];
                for (var venueIndex = 0; venueIndex < workVenues.length; venueIndex++) {
                    var lat = workVenues[venueIndex]["latitude"];
                    llr.push(lat);
                    var lng = workVenues[venueIndex]["longitude"];
                    llr.push(lng);

                    var rad = 0;

                    switch (timeId) {
                        case 0:
                            rad = (Math.max(workVenues[venueIndex]["check_ins"], 1000) / divisor) / 3;
                            break;
                        case 1:
                            rad = (Math.max(workVenues[venueIndex]["check_ins"], 1000) / divisor);
                            break;
                        case 2:
                            rad = (Math.max(workVenues[venueIndex]["check_ins"], 1000) / divisor) / 2;
                            break;
                        case 3:
                            rad = 0;
                            break;
                    }

                    llr.push(rad);

                    heatIndices.push(llr);
                    llr = [];
                }

                var nightlife = lot["categories"]["nightlife"];
                for (var venueIndex = 0; venueIndex < nightlife.length; venueIndex++) {
                    var lat = nightlife[venueIndex]["latitude"];
                    llr.push(lat);
                    var lng = nightlife[venueIndex]["longitude"];
                    llr.push(lng);

                    var rad = 0;

                     switch (timeId) {
                        case 0:
                            rad = 0;
                            break;
                        case 1:
                            rad = 0;
                            break;
                        case 2:
                            rad = (Math.max(nightlife[venueIndex]["check_ins"], 1000) / divisor) / 4;
                            break;
                        case 3:
                            rad = (Math.max(nightlife[venueIndex]["check_ins"], 1000) / divisor);
                            break;
                    }

                    llr.push(rad);

                    heatIndices.push(llr);
                    llr = [];
                }

                var foodLife = lot["categories"]["food"];
                for (var venueIndex = 0; venueIndex < foodLife.length; venueIndex++) {
                    var lat = foodLife[venueIndex]["latitude"];
                    llr.push(lat);
                    var lng = foodLife[venueIndex]["longitude"];
                    llr.push(lng);

                    var rad = 0;

                    switch (timeId) {
                        case 0:
                            rad = (Math.max(foodLife[venueIndex]["check_ins"], 1000) / divisor) / 3;
                            break;
                        case 1:
                            rad = (Math.max(foodLife[venueIndex]["check_ins"], 1000) / divisor) / 2;
                            break;
                        case 2:
                            rad = (Math.max(foodLife[venueIndex]["check_ins"], 1000) / divisor);
                            break;
                        case 3:
                            rad = (Math.max(foodLife[venueIndex]["check_ins"], 1000) / divisor) / 2;
                            break;
                    }

                    llr.push(rad);

                    heatIndices.push(llr);
                    llr = [];
                }
            }

            var finalRadius = 30;
            var currentRadius = 0;
            var delayHeatLayer = setInterval(function () {
                if (currentHeatLayer != null) {
                    map.removeLayer(currentHeatLayer);
                }

                currentHeatLayer = L.heatLayer(heatIndices, {radius: currentRadius}).addTo(map);

                if (currentRadius > finalRadius) {
                    clearInterval(delayHeatLayer);
                }

                currentRadius++;
            }, 15);
        }

    });
}