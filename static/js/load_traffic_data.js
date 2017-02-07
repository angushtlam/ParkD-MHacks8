/**
 * Created by angus on 10/8/16.
 * IDs to use: 0 is Morning, 1 is Day, 2 is Afternoon, 3 is Midnight
 */

function loadAllTrafficDataMap(map) {
    loadAllTrafficDataMap(map, 1);
}

function loadAllTrafficDataMap(map, timeId) {
    $.ajax({
        url: "/api/lot/nearby",
        success: function (data, result) {
            var json_data = JSON.parse(data);

            var keys = Object.keys(json_data);
            var values = keys.map(function(v) { return json_data[v]; });

            for (var i = 0; i < values.length; i++) {
                var lot = values[i];

                var collegeVenues = lot["categories"]["college"];
                for (var venueIndex = 0; venueIndex < collegeVenues.length; venueIndex++) {
                    var lat = collegeVenues[venueIndex]["latitude"];
                    var lng = collegeVenues[venueIndex]["longitude"];
                    var rad = 0;

                    switch (timeId) {
                        case 0:
                            rad = collegeVenues[venueIndex]["check_ins"];
                            break;
                        case 1:
                            rad = collegeVenues[venueIndex]["check_ins"] / 2;
                            break;
                        case 2:
                            rad = collegeVenues[venueIndex]["check_ins"] / 2;
                            break;
                        case 3:
                            rad = 0;
                            break;
                    }

                    if (rad > 40) rad = 40;
                    else if (rad < 10) rad = 10;

                     L.circle([lat, lng], {
                        color: 'red',
                        fillColor: '#f03',
                        fillOpacity: 0.1,
                        radius: rad
                     }).addTo(map);
                }

                var workVenues = lot["categories"]["work"];
                for (var venueIndex = 0; venueIndex < workVenues.length; venueIndex++) {
                    var lat = workVenues[venueIndex]["latitude"];
                    var lng = workVenues[venueIndex]["longitude"];
                    var rad = 0;

                    switch (timeId) {
                        case 0:
                            rad = workVenues[venueIndex]["check_ins"];
                            break;
                        case 1:
                            rad = workVenues[venueIndex]["check_ins"];
                            break;
                        case 2:
                            rad = workVenues[venueIndex]["check_ins"] / 2;
                            break;
                        case 3:
                            rad = 0;
                            break;
                    }


                    if (rad > 40) rad = 40;
                    else if (rad < 10) rad = 10;

                     L.circle([lat, lng], {
                        color: 'blue',
                        fillColor: '#70E9FF',
                        fillOpacity: 0.1,
                        radius: rad
                     }).addTo(map);
                }

                var nightlife = lot["categories"]["nightlife"];
                for (var venueIndex = 0; venueIndex < nightlife.length; venueIndex++) {
                    var lat = nightlife[venueIndex]["latitude"];
                    var lng = nightlife[venueIndex]["longitude"];
                    var rad = 0;

                    switch (timeId) {
                        case 0:
                            rad = 0;
                            break;
                        case 1:
                            rad = 0;
                            break;
                        case 2:
                            rad = nightlife[venueIndex]["check_ins"] / 5;
                            break;
                        case 3:
                            rad = nightlife[venueIndex]["check_ins"];
                            break;
                    }



                    if (rad > 40) rad = 40;
                    else if (rad < 10) rad = 10;

                     L.circle([lat, lng], {
                        color: 'green',
                        fillColor: '#74FF70',
                        fillOpacity: 0.1,
                        radius: rad
                     }).addTo(map);
                }

                var foodLife = lot["categories"]["food"];
                for (var venueIndex = 0; venueIndex < foodLife.length; venueIndex++) {
                    var lat = foodLife[venueIndex]["latitude"];
                    var lng = foodLife[venueIndex]["longitude"];
                    var rad = 0;

                    switch (timeId) {
                        case 0:
                            rad = foodLife[venueIndex]["check_ins"];
                            break;
                        case 1:
                            rad = foodLife[venueIndex]["check_ins"];
                            break;
                        case 2:
                            rad = foodLife[venueIndex]["check_ins"];
                            break;
                        case 3:
                            rad = foodLife[venueIndex]["check_ins"] / 2;
                            break;
                    }

                    if (rad > 40) rad = 40;
                    else if (rad < 10) rad = 10;

                     L.circle([lat, lng], {
                        color: 'yellow',
                        fillColor: '#FFF520',
                        fillOpacity: 0.1,
                        radius: rad
                     }).addTo(map);
                }
            }
        }

    });
}
