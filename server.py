from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route('/')
def render_index():
    return render_template("index.html")


@app.route('/api/lot/all')
def api_lot_all():
    json_data = {
        "results": [
            {
                "id": "10",
                "longitude": -83.0501601,
                "spaces": 1450,
                "private": False,
                "latitude": 42.3285765,
                "address": "621 Cass",
                "name": "First Street Parking Deck"
            },
            {
                "id": "124",
                "longitude": -83.047012,
                "spaces": 24,
                "private": True,
                "latitude": 42.337933,
                "address": "241 Madison",
                "name": "Detroit Athletic Club Valet Lot"
            },
            {
                "id": "206",
                "longitude": -83.0582774,
                "spaces": 274,
                "private": False,
                "latitude": 42.3361209,
                "address": "2201 W Grand River",
                "name": "MGM Grand Detroit Casino Surface Lot"
            },
            {
                "id": "1",
                "longitude": -83.0542696,
                "spaces": 3000,
                "private": False,
                "latitude": 42.3259106,
                "address": "900 W Jefferson Ave",
                "name": "Joe Louis Arena"
            }
        ]
    }

    return json.dumps(json_data)


@app.route('/api/lot/nearby')
def api_lot_surrounding():
    if not request.args:
        return "{\"response\": \"error\"}"

    json_data = {
        "results": {
            "133": {
                "location": {
                    "latitude": 42.3073777,
                    "longitude": -83.2445063
                },
                "categories": {
                    "college": [
                        {
                            "latitude": 42.306202,
                            "name": "T-197",
                            "longitude": -83.244267,
                            "check_ins": 2
                        }
                    ],
                    "work": [
                        {
                            "latitude": 42.307172533333336,
                            "name": "Valley of Detroit Scottish Rite Center",
                            "longitude": -83.24406145,
                            "check_ins": 497
                        },
                        {
                            "latitude": 42.30777651,
                            "name": "Farmers Insurance",
                            "longitude": -83.24332456,
                            "check_ins": 0
                        },
                        {
                            "latitude": 42.30686907646464,
                            "name": "St Paul Lutheran Church",
                            "longitude": -83.2433997320917,
                            "check_ins": 22
                        },
                        {
                            "latitude": 42.304245717083695,
                            "name": "power operations engineering engines",
                            "longitude": -83.24121444162226,
                            "check_ins": 2
                        },
                        {
                            "latitude": 42.303639,
                            "name": "Executive Health",
                            "longitude": -83.244726,
                            "check_ins": 9
                        },
                        {
                            "latitude": 42.303315,
                            "name": "Dearborn Dental & Associates",
                            "longitude": -83.242829,
                            "check_ins": 42
                        },
                        {
                            "latitude": 42.31017,
                            "name": "Trillium family dentistry",
                            "longitude": -83.24424,
                            "check_ins": 1
                        },
                        {
                            "latitude": 42.30378,
                            "name": "Dr. Dickieson",
                            "longitude": -83.244653,
                            "check_ins": 5
                        },
                        {
                            "latitude": 42.31046175110064,
                            "name": "Brady Apartments",
                            "longitude": -83.24188885731743,
                            "check_ins": 53
                        },
                        {
                            "latitude": 42.306473,
                            "name": "Performance Driven",
                            "longitude": -83.249068,
                            "check_ins": 2
                        },
                        {
                            "latitude": 42.30666732788086,
                            "name": "22190 garrison suite 301",
                            "longitude": -83.24793243408203,
                            "check_ins": 3
                        },
                        {
                            "latitude": 42.30408796236334,
                            "name": "UAW 245",
                            "longitude": -83.2438754673667,
                            "check_ins": 10
                        },
                        {
                            "latitude": 42.306823150922526,
                            "name": "Garrison Square Professional Center",
                            "longitude": -83.248266704772,
                            "check_ins": 9
                        },
                        {
                            "latitude": 42.3051104330464,
                            "name": "Comerica",
                            "longitude": -83.24598748064786,
                            "check_ins": 85
                        },
                        {
                            "latitude": 42.30463608560006,
                            "name": "DaVita Dearborn",
                            "longitude": -83.24262077337693,
                            "check_ins": 70
                        },
                        {
                            "latitude": 42.30662677502325,
                            "name": "Dr. Colins And Dr. Mikula Chiropractic Facility",
                            "longitude": -83.24821442988898,
                            "check_ins": 30
                        },
                        {
                            "latitude": 42.30521472479764,
                            "name": "Fidelity Bank Operations Center",
                            "longitude": -83.24936446755827,
                            "check_ins": 6
                        },
                        {
                            "latitude": 42.306312436389355,
                            "name": "team mental health services",
                            "longitude": -83.24800010242699,
                            "check_ins": 10
                        },
                        {
                            "latitude": 42.30704068846783,
                            "name": "First United Methidist Church",
                            "longitude": -83.24732052285279,
                            "check_ins": 116
                        },
                        {
                            "latitude": 42.30374410669756,
                            "name": "UAW HALL",
                            "longitude": -83.24367158124845,
                            "check_ins": 4
                        },
                        {
                            "latitude": 42.306323134799726,
                            "name": "West Village Obgyn",
                            "longitude": -83.24572609660301,
                            "check_ins": 46
                        },
                        {
                            "latitude": 42.305990625441275,
                            "name": "Dearborn Chamber Of Commerce",
                            "longitude": -83.2467873092664,
                            "check_ins": 101
                        },
                        {
                            "latitude": 42.302767616666664,
                            "name": "Dearborn Cadiology",
                            "longitude": -83.24348236666667,
                            "check_ins": 9
                        },
                        {
                            "latitude": 42.306135,
                            "name": "KMS Photography",
                            "longitude": -83.250287,
                            "check_ins": 2
                        },
                        {
                            "latitude": 42.30403891340743,
                            "name": "Querfeld Funeral Home",
                            "longitude": -83.24256326598612,
                            "check_ins": 58
                        },
                        {
                            "latitude": 42.30553352202633,
                            "name": "Michigan Hand Associates",
                            "longitude": -83.24705391660886,
                            "check_ins": 1
                        },
                        {
                            "latitude": 42.30458696071693,
                            "name": "East Parking Deck",
                            "longitude": -83.24799487491903,
                            "check_ins": 166
                        },
                        {
                            "latitude": 42.30553352202633,
                            "name": "Scottrade",
                            "longitude": -83.24705391660886,
                            "check_ins": 6
                        },
                        {
                            "latitude": 42.30592372058741,
                            "name": "Bryant Branch Library",
                            "longitude": -83.24663048090473,
                            "check_ins": 181
                        },
                        {
                            "latitude": 42.30680091419308,
                            "name": "All Brite Dental",
                            "longitude": -83.24800010242699,
                            "check_ins": 29
                        }
                    ],
                    "nightlife": [
                        {
                            "latitude": 42.306514725385874,
                            "name": "Dearborn Brewing",
                            "longitude": -83.24355840682983,
                            "check_ins": 235
                        },
                        {
                            "latitude": 42.30473140783535,
                            "name": "Bar Louie",
                            "longitude": -83.24925810098648,
                            "check_ins": 53
                        },
                        {
                            "latitude": 42.30667371424036,
                            "name": "Nar Bar",
                            "longitude": -83.24320107237043,
                            "check_ins": 225
                        },
                        {
                            "latitude": 42.30617757323883,
                            "name": "Liv Lounge",
                            "longitude": -83.24320107237043,
                            "check_ins": 17
                        },
                        {
                            "latitude": 42.304864,
                            "name": "Double Olive",
                            "longitude": -83.248742,
                            "check_ins": 1
                        },
                        {
                            "latitude": 42.304832018846845,
                            "name": "Red Martini",
                            "longitude": -83.24872149447205,
                            "check_ins": 16
                        },
                        {
                            "latitude": 42.30559012048172,
                            "name": "Cigaro",
                            "longitude": -83.24470146096593,
                            "check_ins": 37
                        },
                        {
                            "latitude": 42.30563093508587,
                            "name": "B-dubs",
                            "longitude": -83.24823533984726,
                            "check_ins": 2
                        },
                        {
                            "latitude": 42.305557501422705,
                            "name": "Beirgarten",
                            "longitude": -83.24773872651241,
                            "check_ins": 158
                        },
                        {
                            "latitude": 42.30592155,
                            "name": "Parisian Bistro BoroBora Ultra Lounge",
                            "longitude": -83.24455445,
                            "check_ins": 9
                        },
                        {
                            "latitude": 42.30518023333333,
                            "name": "The Bar",
                            "longitude": -83.24551598333333,
                            "check_ins": 9
                        },
                        {
                            "latitude": 42.30552012,
                            "name": "Bailey's",
                            "longitude": -83.24580272,
                            "check_ins": 5639
                        },
                        {
                            "latitude": 42.30471396,
                            "name": "Le Cigar",
                            "longitude": -83.248809,
                            "check_ins": 490
                        },
                        {
                            "latitude": 42.305709305416066,
                            "name": "Post Bar",
                            "longitude": -83.24519809761199,
                            "check_ins": 2384
                        },
                        {
                            "latitude": 42.30510500019462,
                            "name": "Moose's Martini Pub",
                            "longitude": -83.24872149447205,
                            "check_ins": 1660
                        }
                    ],
                    "food": [
                        {
                            "latitude": 42.30609966024857,
                            "name": "Brome Burgers & Shakes",
                            "longitude": -83.24529742448385,
                            "check_ins": 249
                        },
                        {
                            "latitude": 42.30618792354987,
                            "name": "Kabuki Sushi",
                            "longitude": -83.2452608303909,
                            "check_ins": 1570
                        },
                        {
                            "latitude": 42.30473140783535,
                            "name": "Bar Louie",
                            "longitude": -83.24925810098648,
                            "check_ins": 53
                        },
                        {
                            "latitude": 42.30609360834016,
                            "name": "Downtown Deli",
                            "longitude": -83.24445052731646,
                            "check_ins": 20
                        },
                        {
                            "latitude": 42.30656876980717,
                            "name": "L.A. Bistro",
                            "longitude": -83.24342587148331,
                            "check_ins": 1119
                        },
                        {
                            "latitude": 42.306415495136484,
                            "name": "Rio Wraps",
                            "longitude": -83.24487397728554,
                            "check_ins": 387
                        },
                        {
                            "latitude": 42.303181951771926,
                            "name": "bd Mongolian",
                            "longitude": -83.24664093614066,
                            "check_ins": 6
                        },
                        {
                            "latitude": 42.306069,
                            "name": "La Shish West",
                            "longitude": -83.2447,
                            "check_ins": 0
                        },
                        {
                            "latitude": 42.3050460418917,
                            "name": "Osteria 222",
                            "longitude": -83.24923378248909,
                            "check_ins": 258
                        },
                        {
                            "latitude": 42.30537072669051,
                            "name": "Los Galanes Tacqueria",
                            "longitude": -83.24778577425496,
                            "check_ins": 11
                        },
                        {
                            "latitude": 42.305801,
                            "name": "Bellacino's Pizza and Grinders",
                            "longitude": -83.245499,
                            "check_ins": 10
                        },
                        {
                            "latitude": 42.30474,
                            "name": "La Fork Poutine & Cr\u00eapes",
                            "longitude": -83.24757,
                            "check_ins": 20
                        },
                        {
                            "latitude": 42.305554,
                            "name": "Stadium",
                            "longitude": -83.244113,
                            "check_ins": 9
                        },
                        {
                            "latitude": 42.305167204206214,
                            "name": "Famous Hamburger",
                            "longitude": -83.24815169997359,
                            "check_ins": 102
                        },
                        {
                            "latitude": 42.305113,
                            "name": "Lue Thai Caf\u00e9",
                            "longitude": -83.248512,
                            "check_ins": 129
                        },
                        {
                            "latitude": 42.306188261342946,
                            "name": "Al-Ajami West Restaurant",
                            "longitude": -83.24361930265314,
                            "check_ins": 1
                        },
                        {
                            "latitude": 42.305227,
                            "name": "Cold Stone Creamery",
                            "longitude": -83.248329,
                            "check_ins": 0
                        },
                        {
                            "latitude": 42.30579954378077,
                            "name": "Los Galanes",
                            "longitude": -83.24762894831342,
                            "check_ins": 25
                        },
                        {
                            "latitude": 42.30546143209739,
                            "name": "Dearborn Food Truck Rally",
                            "longitude": -83.24511445381219,
                            "check_ins": 43
                        },
                        {
                            "latitude": 42.305769571104385,
                            "name": "Yogurtown",
                            "longitude": -83.24504126539868,
                            "check_ins": 614
                        },
                        {
                            "latitude": 42.30552012,
                            "name": "Bailey's",
                            "longitude": -83.24580272,
                            "check_ins": 5639
                        },
                        {
                            "latitude": 42.30535582819231,
                            "name": "Buffalo Wild Wings",
                            "longitude": -83.24823533984726,
                            "check_ins": 5627
                        },
                        {
                            "latitude": 42.305739260685705,
                            "name": "Buddy's Pizza",
                            "longitude": -83.24720336666667,
                            "check_ins": 5600
                        },
                        {
                            "latitude": 42.30450405912192,
                            "name": "iBurger Lounge",
                            "longitude": -83.248747631714,
                            "check_ins": 305
                        },
                        {
                            "latitude": 42.30509442317802,
                            "name": "Jimmy John's",
                            "longitude": -83.24717402458191,
                            "check_ins": 1006
                        },
                        {
                            "latitude": 42.30634451301402,
                            "name": "Westborn Flower Market",
                            "longitude": -83.24223697884008,
                            "check_ins": 4207
                        },
                        {
                            "latitude": 42.30561628782913,
                            "name": "Panera Cares - A Community Cafe",
                            "longitude": -83.24821442988898,
                            "check_ins": 2546
                        },
                        {
                            "latitude": 42.30528088926159,
                            "name": "bd's Mongolian Grill",
                            "longitude": -83.24647933244705,
                            "check_ins": 5042
                        },
                        {
                            "latitude": 42.30518,
                            "name": "Starbucks",
                            "longitude": -83.246951,
                            "check_ins": 5752
                        },
                        {
                            "latitude": 42.30800519263985,
                            "name": "Joe Vicari's Andiamo Italian Steakhouse",
                            "longitude": -83.23796773751292,
                            "check_ins": 1461
                        }
                    ]
                }
            },
            "124": {
                "location": {
                    "latitude": 42.337933,
                    "longitude": -83.047012
                },
                "categories": {
                    "college": [
                        {
                            "latitude": 42.33701381436167,
                            "name": "Detroit Athletic Club University",
                            "longitude": -83.04600965124902,
                            "check_ins": 3
                        },
                        {
                            "latitude": 42.33894836666666,
                            "name": "Lions Locker Room",
                            "longitude": -83.046383,
                            "check_ins": 126
                        },
                        {
                            "latitude": 42.33737117184094,
                            "name": "Grand Valley State University - Detroit",
                            "longitude": -83.04795504067752,
                            "check_ins": 79
                        },
                        {
                            "latitude": 42.338926,
                            "name": "Bodman Training Room",
                            "longitude": -83.045673,
                            "check_ins": 1
                        },
                        {
                            "latitude": 42.33476638793945,
                            "name": "Detroit Training Center",
                            "longitude": -83.04568481445312,
                            "check_ins": 15
                        },
                        {
                            "latitude": 42.339322,
                            "name": "study city",
                            "longitude": -83.051388,
                            "check_ins": 3
                        }
                    ],
                    "work": [
                        {
                            "latitude": 42.3387004099476,
                            "name": "Fox Office",
                            "longitude": -83.05178272796836,
                            "check_ins": 2999
                        },
                        {
                            "latitude": 42.337376460408635,
                            "name": "36th District Court",
                            "longitude": -83.04539613376066,
                            "check_ins": 2556
                        },
                        {
                            "latitude": 42.33692885342871,
                            "name": "Frank Murphy Hall of Justice",
                            "longitude": -83.04221833627771,
                            "check_ins": 2436
                        },
                        {
                            "latitude": 42.33670644262623,
                            "name": "Wayne County Juvenile Detention Facility",
                            "longitude": -83.04132160329671,
                            "check_ins": 2046
                        },
                        {
                            "latitude": 42.33857952985405,
                            "name": "Fox Theatre",
                            "longitude": -83.05218121411987,
                            "check_ins": 12469
                        },
                        {
                            "latitude": 42.33978183383167,
                            "name": "Ford Field Parking Deck",
                            "longitude": -83.04340871733083,
                            "check_ins": 1813
                        },
                        {
                            "latitude": 42.33904929962598,
                            "name": "Campbell Ewald",
                            "longitude": -83.0458995331466,
                            "check_ins": 2387
                        },
                        {
                            "latitude": 42.337666636455374,
                            "name": "Commonwealth//McCann",
                            "longitude": -83.05164115993867,
                            "check_ins": 527
                        },
                        {
                            "latitude": 42.335879768694554,
                            "name": "David Whitney Building",
                            "longitude": -83.05059774172969,
                            "check_ins": 222
                        },
                        {
                            "latitude": 42.33902761325364,
                            "name": "Jack Morton Worldwide",
                            "longitude": -83.04587331452363,
                            "check_ins": 200
                        },
                        {
                            "latitude": 42.33724397474269,
                            "name": "Park Rite",
                            "longitude": -83.04444176185599,
                            "check_ins": 22
                        },
                        {
                            "latitude": 42.336816,
                            "name": "Open Systems Technologies (OST)",
                            "longitude": -83.051547,
                            "check_ins": 8
                        },
                        {
                            "latitude": 42.33250329213254,
                            "name": "One Campus Martius",
                            "longitude": -83.04667559965631,
                            "check_ins": 212
                        },
                        {
                            "latitude": 42.33632462576732,
                            "name": "Vertical Detroit",
                            "longitude": -83.0472786179909,
                            "check_ins": 170
                        },
                        {
                            "latitude": 42.339825,
                            "name": "Ernie Harwell Media Center",
                            "longitude": -83.04926,
                            "check_ins": 6
                        },
                        {
                            "latitude": 42.33983664931378,
                            "name": "On The Field @ Ford Field",
                            "longitude": -83.04572124630442,
                            "check_ins": 98
                        },
                        {
                            "latitude": 42.34027794661684,
                            "name": "Media Lot",
                            "longitude": -83.04931835209405,
                            "check_ins": 356
                        },
                        {
                            "latitude": 42.336010682904465,
                            "name": "Opera House Parking Center",
                            "longitude": -83.0478973614948,
                            "check_ins": 3862
                        },
                        {
                            "latitude": 42.34053833404299,
                            "name": "Tigers Parking Garage",
                            "longitude": -83.04889363118195,
                            "check_ins": 603
                        },
                        {
                            "latitude": 42.33472143501486,
                            "name": "Z-Lot",
                            "longitude": -83.0469063203674,
                            "check_ins": 1076
                        },
                        {
                            "latitude": 42.33325013152354,
                            "name": "Compuware Parking Garage",
                            "longitude": -83.04624037429477,
                            "check_ins": 4315
                        },
                        {
                            "latitude": 42.33774768837438,
                            "name": "Palms Building",
                            "longitude": -83.05173029540029,
                            "check_ins": 1637
                        },
                        {
                            "latitude": 42.33852669245976,
                            "name": "Fox Parking Garage",
                            "longitude": -83.05348152056004,
                            "check_ins": 3298
                        },
                        {
                            "latitude": 42.335857819719365,
                            "name": "Hilton Garden Inn",
                            "longitude": -83.04501593112946,
                            "check_ins": 4676
                        },
                        {
                            "latitude": 42.33615443946605,
                            "name": "Broderick Tower",
                            "longitude": -83.05033557374912,
                            "check_ins": 3683
                        },
                        {
                            "latitude": 42.336056090913424,
                            "name": "Detroit Venture Partners",
                            "longitude": -83.04934501647949,
                            "check_ins": 463
                        }
                    ],
                    "nightlife": [
                        {
                            "latitude": 42.33872708319815,
                            "name": "Elwood Bar & Grill",
                            "longitude": -83.04668084331783,
                            "check_ins": 3719
                        },
                        {
                            "latitude": 42.334647700352164,
                            "name": "The Skip",
                            "longitude": -83.04652353329087,
                            "check_ins": 241
                        },
                        {
                            "latitude": 42.338244963350846,
                            "name": "Tiger Club",
                            "longitude": -83.04949522018433,
                            "check_ins": 1712
                        },
                        {
                            "latitude": 42.33899439673061,
                            "name": "Hockeytown Cafe",
                            "longitude": -83.05260121822357,
                            "check_ins": 11177
                        },
                        {
                            "latitude": 42.336940372827776,
                            "name": "The Park Bar",
                            "longitude": -83.05276215076447,
                            "check_ins": 5952
                        },
                        {
                            "latitude": 42.33758905638648,
                            "name": "The Fillmore Detroit",
                            "longitude": -83.05195051190532,
                            "check_ins": 15308
                        },
                        {
                            "latitude": 42.33676782563287,
                            "name": "La Casa De La Habana Cigar Bar",
                            "longitude": -83.04620891210888,
                            "check_ins": 2678
                        },
                        {
                            "latitude": 42.33632462576732,
                            "name": "Vertical Detroit",
                            "longitude": -83.0472786179909,
                            "check_ins": 170
                        },
                        {
                            "latitude": 42.335362705502654,
                            "name": "Centre Park Bar",
                            "longitude": -83.04536991493714,
                            "check_ins": 273
                        },
                        {
                            "latitude": 42.33474003977068,
                            "name": "Queen's",
                            "longitude": -83.04775578510466,
                            "check_ins": 186
                        },
                        {
                            "latitude": 42.336475,
                            "name": "Rusted Crow Detroit",
                            "longitude": -83.05238,
                            "check_ins": 115
                        },
                        {
                            "latitude": 42.33764106655112,
                            "name": "Cheli's Chili Bar",
                            "longitude": -83.04983220829787,
                            "check_ins": 7906
                        },
                        {
                            "latitude": 42.33523957441603,
                            "name": "Exodos Lounge",
                            "longitude": -83.04217638412987,
                            "check_ins": 1242
                        },
                        {
                            "latitude": 42.33318040099984,
                            "name": "Detroiter Bar/Malaka's",
                            "longitude": -83.04151039020242,
                            "check_ins": 3468
                        },
                        {
                            "latitude": 42.33501780502067,
                            "name": "Punch Bowl Social",
                            "longitude": -83.04619842471024,
                            "check_ins": 2753
                        },
                        {
                            "latitude": 42.334473964329995,
                            "name": "Downtown Louie's",
                            "longitude": -83.05016254230964,
                            "check_ins": 871
                        },
                        {
                            "latitude": 42.334321510651314,
                            "name": "Cafe d'Mongo's",
                            "longitude": -83.04994231981942,
                            "check_ins": 3248
                        },
                        {
                            "latitude": 42.3349864526831,
                            "name": "Cornerstone Barrel House",
                            "longitude": -83.04922396990607,
                            "check_ins": 1008
                        },
                        {
                            "latitude": 42.33472045352259,
                            "name": "Firebird Tavern",
                            "longitude": -83.04331432666741,
                            "check_ins": 2142
                        },
                        {
                            "latitude": 42.33680158500915,
                            "name": "Cliff Bell's",
                            "longitude": -83.05273532867432,
                            "check_ins": 6700
                        },
                        {
                            "latitude": 42.33390936187725,
                            "name": "Loco's Bar & Grill",
                            "longitude": -83.04204528349563,
                            "check_ins": 3838
                        },
                        {
                            "latitude": 42.33401708080596,
                            "name": "Atheneum Suite Hotel",
                            "longitude": -83.04294725057866,
                            "check_ins": 3624
                        },
                        {
                            "latitude": 42.336848154407875,
                            "name": "R.U.B BBQ Pub",
                            "longitude": -83.0513213199351,
                            "check_ins": 5768
                        },
                        {
                            "latitude": 42.336168799999996,
                            "name": "Harbor House",
                            "longitude": -83.04366646666666,
                            "check_ins": 1518
                        },
                        {
                            "latitude": 42.33603540302849,
                            "name": "Detroit Beer Company",
                            "longitude": -83.04887265723872,
                            "check_ins": 15650
                        },
                        {
                            "latitude": 42.33456921120238,
                            "name": "The Old Shillelagh",
                            "longitude": -83.04371810800092,
                            "check_ins": 12548
                        },
                        {
                            "latitude": 42.335310412822444,
                            "name": "Level Two Bar & Rooftop",
                            "longitude": -83.04195613491521,
                            "check_ins": 1467
                        },
                        {
                            "latitude": 42.33443348430577,
                            "name": "The Well Bar",
                            "longitude": -83.04503955686609,
                            "check_ins": 4700
                        },
                        {
                            "latitude": 42.33363939323706,
                            "name": "Bouzouki",
                            "longitude": -83.04291578681867,
                            "check_ins": 1561
                        },
                        {
                            "latitude": 42.33512817634233,
                            "name": "Pappy's Bar & Grill",
                            "longitude": -83.04224789142609,
                            "check_ins": 2789
                        }
                    ],
                    "food": [
                        {
                            "latitude": 42.33872708319815,
                            "name": "Elwood Bar & Grill",
                            "longitude": -83.04668084331783,
                            "check_ins": 3719
                        },
                        {
                            "latitude": 42.335209601480074,
                            "name": "Astoria Pastry Shop",
                            "longitude": -83.04177259334013,
                            "check_ins": 6023
                        },
                        {
                            "latitude": 42.33899439673061,
                            "name": "Hockeytown Cafe",
                            "longitude": -83.05260121822357,
                            "check_ins": 11177
                        },
                        {
                            "latitude": 42.33579228017809,
                            "name": "jose's tacos",
                            "longitude": -83.04675425453506,
                            "check_ins": 255
                        },
                        {
                            "latitude": 42.33764106655112,
                            "name": "Cheli's Chili Bar",
                            "longitude": -83.04983220829787,
                            "check_ins": 7906
                        },
                        {
                            "latitude": 42.33472045352259,
                            "name": "Firebird Tavern",
                            "longitude": -83.04331432666741,
                            "check_ins": 2142
                        },
                        {
                            "latitude": 42.33501802778794,
                            "name": "Wright & Co.",
                            "longitude": -83.04926591756188,
                            "check_ins": 1911
                        },
                        {
                            "latitude": 42.33680158500915,
                            "name": "Cliff Bell's",
                            "longitude": -83.05273532867432,
                            "check_ins": 6700
                        },
                        {
                            "latitude": 42.3342711737235,
                            "name": "Vicente's Cuban Cuisine",
                            "longitude": -83.04722093821528,
                            "check_ins": 3785
                        },
                        {
                            "latitude": 42.334473964329995,
                            "name": "Downtown Louie's",
                            "longitude": -83.05016254230964,
                            "check_ins": 871
                        },
                        {
                            "latitude": 42.33512817634233,
                            "name": "Pappy's Bar & Grill",
                            "longitude": -83.04224789142609,
                            "check_ins": 2789
                        },
                        {
                            "latitude": 42.334321510651314,
                            "name": "Cafe d'Mongo's",
                            "longitude": -83.04994231981942,
                            "check_ins": 3248
                        },
                        {
                            "latitude": 42.334236067332505,
                            "name": "Buffalo Wild Wings",
                            "longitude": -83.0447354162236,
                            "check_ins": 6018
                        },
                        {
                            "latitude": 42.336168799999996,
                            "name": "Harbor House",
                            "longitude": -83.04366646666666,
                            "check_ins": 1518
                        },
                        {
                            "latitude": 42.33432714506075,
                            "name": "Fishbone's Rhythm Kitchen Cafe",
                            "longitude": -83.04317593574524,
                            "check_ins": 10613
                        },
                        {
                            "latitude": 42.33390936187725,
                            "name": "Loco's Bar & Grill",
                            "longitude": -83.04204528349563,
                            "check_ins": 3838
                        },
                        {
                            "latitude": 42.33522397431423,
                            "name": "Pegasus Taverna",
                            "longitude": -83.04167820033085,
                            "check_ins": 6031
                        },
                        {
                            "latitude": 42.336128,
                            "name": "Ashe Supply Co. Caf\u00e9 & Roasterie",
                            "longitude": -83.049322,
                            "check_ins": 429
                        },
                        {
                            "latitude": 42.33318040099984,
                            "name": "Detroiter Bar/Malaka's",
                            "longitude": -83.04151039020242,
                            "check_ins": 3468
                        },
                        {
                            "latitude": 42.33441555658652,
                            "name": "The Standby",
                            "longitude": -83.04582612097596,
                            "check_ins": 616
                        },
                        {
                            "latitude": 42.33411238556305,
                            "name": "7 Greens",
                            "longitude": -83.04654975165481,
                            "check_ins": 372
                        },
                        {
                            "latitude": 42.335034,
                            "name": "Santorini Estiatorio Detroit",
                            "longitude": -83.042416,
                            "check_ins": 1391
                        },
                        {
                            "latitude": 42.3337878985443,
                            "name": "Urban Bean Coffee",
                            "longitude": -83.04962247155655,
                            "check_ins": 1018
                        },
                        {
                            "latitude": 42.33603540302849,
                            "name": "Detroit Beer Company",
                            "longitude": -83.04887265723872,
                            "check_ins": 15650
                        },
                        {
                            "latitude": 42.335431985657685,
                            "name": "Pizza Papalis Taverna",
                            "longitude": -83.04157856311869,
                            "check_ins": 7041
                        },
                        {
                            "latitude": 42.336848154407875,
                            "name": "R.U.B BBQ Pub",
                            "longitude": -83.0513213199351,
                            "check_ins": 5768
                        },
                        {
                            "latitude": 42.33501780502067,
                            "name": "Punch Bowl Social",
                            "longitude": -83.04619842471024,
                            "check_ins": 2753
                        },
                        {
                            "latitude": 42.33456921120238,
                            "name": "The Old Shillelagh",
                            "longitude": -83.04371810800092,
                            "check_ins": 12548
                        },
                        {
                            "latitude": 42.333616,
                            "name": "Orchid Thai",
                            "longitude": -83.04522,
                            "check_ins": 1416
                        },
                        {
                            "latitude": 42.333535688876935,
                            "name": "The Hudson Cafe",
                            "longitude": -83.04834830648495,
                            "check_ins": 6100
                        }
                    ]
                }
            },
            "10": {
                "location": {
                    "latitude": 42.3285765,
                    "longitude": -83.0501601
                },
                "categories": {
                    "college": [
                        {
                            "latitude": 42.328826334278475,
                            "name": "Mt Elliot Makerspace",
                            "longitude": -83.04908763983997,
                            "check_ins": 3
                        },
                        {
                            "latitude": 42.331249,
                            "name": "CMU - Detroit Campus",
                            "longitude": -83.047449,
                            "check_ins": 5
                        },
                        {
                            "latitude": 42.32886505126953,
                            "name": "subway WCCC",
                            "longitude": -83.05253601074219,
                            "check_ins": 1
                        },
                        {
                            "latitude": 42.331962,
                            "name": "The Iron Yard - Detroit",
                            "longitude": -83.04738,
                            "check_ins": 6
                        },
                        {
                            "latitude": 42.326319935712064,
                            "name": "visual arts class",
                            "longitude": -83.05534280157524,
                            "check_ins": 2
                        },
                        {
                            "latitude": 42.32631258916646,
                            "name": "wcccd school library",
                            "longitude": -83.05537950236145,
                            "check_ins": 4
                        },
                        {
                            "latitude": 42.33199691772461,
                            "name": "University of Phoenix Detroit Campus 1001 Woodward",
                            "longitude": -83.04708862304688,
                            "check_ins": 2
                        },
                        {
                            "latitude": 42.32645277875415,
                            "name": "Wayne County Community College District Downtown Campus Bookstore",
                            "longitude": -83.05626031508548,
                            "check_ins": 155
                        },
                        {
                            "latitude": 42.32658905611136,
                            "name": "Wayne County Community College",
                            "longitude": -83.055652136132,
                            "check_ins": 251
                        },
                        {
                            "latitude": 42.326594450639845,
                            "name": "Wayne County Community College (Downtown Campus)",
                            "longitude": -83.05570980851554,
                            "check_ins": 920
                        },
                        {
                            "latitude": 42.32711867133332,
                            "name": "Wayne County Community College District Office Building",
                            "longitude": -83.05431517124603,
                            "check_ins": 619
                        }
                    ],
                    "work": [
                        {
                            "latitude": 42.32685564910629,
                            "name": "Cobo Center",
                            "longitude": -83.04960250854492,
                            "check_ins": 21699
                        },
                        {
                            "latitude": 42.33002904329738,
                            "name": "Comerica Bank",
                            "longitude": -83.05170407910059,
                            "check_ins": 1435
                        },
                        {
                            "latitude": 42.32817474208524,
                            "name": "First Street Parking Garage",
                            "longitude": -83.05190332271631,
                            "check_ins": 1543
                        },
                        {
                            "latitude": 42.33119678468325,
                            "name": "Motor City Wine",
                            "longitude": -83.07288868317568,
                            "check_ins": 2463
                        },
                        {
                            "latitude": 42.33042071781019,
                            "name": "Federal Reserve Building",
                            "longitude": -83.04827489704599,
                            "check_ins": 452
                        },
                        {
                            "latitude": 42.330700288619006,
                            "name": "Quicken Loans Chrysler House",
                            "longitude": -83.04780297726855,
                            "check_ins": 1095
                        },
                        {
                            "latitude": 42.32806681906185,
                            "name": "Foreman Bros. Inc.",
                            "longitude": -83.04842171584203,
                            "check_ins": 3226
                        },
                        {
                            "latitude": 42.33288391933399,
                            "name": "Rakasa's work",
                            "longitude": -83.04643439077535,
                            "check_ins": 653
                        },
                        {
                            "latitude": 42.33075209013738,
                            "name": "Financial District Garage",
                            "longitude": -83.04864194342186,
                            "check_ins": 655
                        },
                        {
                            "latitude": 42.33026927417342,
                            "name": "Fleishman Hillard",
                            "longitude": -83.0449504123406,
                            "check_ins": 113
                        },
                        {
                            "latitude": 42.332691835673785,
                            "name": "Archdiocese of Detroit",
                            "longitude": -83.04896179645131,
                            "check_ins": 293
                        },
                        {
                            "latitude": 42.33238833442021,
                            "name": "Benzinga World Headquarters",
                            "longitude": -83.04668084331783,
                            "check_ins": 285
                        },
                        {
                            "latitude": 42.32928466796875,
                            "name": "AMBR Detroit",
                            "longitude": -83.04833984375,
                            "check_ins": 61
                        },
                        {
                            "latitude": 42.32966055820124,
                            "name": "iProspect",
                            "longitude": -83.04491894953809,
                            "check_ins": 1250
                        },
                        {
                            "latitude": 42.32917333545208,
                            "name": "DoubleTree Suites by Hilton Hotel Detroit Downtown - Fort Shelby",
                            "longitude": -83.05292040109634,
                            "check_ins": 6983
                        },
                        {
                            "latitude": 42.33012354634199,
                            "name": "Penobscot Building",
                            "longitude": -83.04762840270996,
                            "check_ins": 2658
                        },
                        {
                            "latitude": 42.33148304719379,
                            "name": "McNamara Federal Building",
                            "longitude": -83.05321412093198,
                            "check_ins": 1927
                        },
                        {
                            "latitude": 42.32961572826946,
                            "name": "Guardian Building",
                            "longitude": -83.04628232385254,
                            "check_ins": 4273
                        },
                        {
                            "latitude": 42.327890127158646,
                            "name": "Crowne Plaza Detroit Downtown Riverfront",
                            "longitude": -83.04769810574727,
                            "check_ins": 1763
                        },
                        {
                            "latitude": 42.32887034368453,
                            "name": "One Woodward Avenue",
                            "longitude": -83.04543972015381,
                            "check_ins": 3039
                        },
                        {
                            "latitude": 42.33258272338595,
                            "name": "Quicken Loans Headquarters",
                            "longitude": -83.04662840668395,
                            "check_ins": 13513
                        },
                        {
                            "latitude": 42.33007019983283,
                            "name": "One Detroit Center",
                            "longitude": -83.04507101961096,
                            "check_ins": 3141
                        },
                        {
                            "latitude": 42.33099427919384,
                            "name": "Detroit One Parking",
                            "longitude": -83.04603586981769,
                            "check_ins": 2226
                        },
                        {
                            "latitude": 42.328586575523026,
                            "name": "Detroit Free Press",
                            "longitude": -83.05415263640695,
                            "check_ins": 3207
                        },
                        {
                            "latitude": 42.329990419581684,
                            "name": "Carat",
                            "longitude": -83.0449818751281,
                            "check_ins": 2838
                        },
                        {
                            "latitude": 42.330424945788224,
                            "name": "Quicken Loans Qube",
                            "longitude": -83.0466628074646,
                            "check_ins": 12665
                        },
                        {
                            "latitude": 42.3310753291462,
                            "name": "First National Building",
                            "longitude": -83.04580450057983,
                            "check_ins": 5797
                        },
                        {
                            "latitude": 42.330839310788875,
                            "name": "Chrysler House",
                            "longitude": -83.04794979711754,
                            "check_ins": 3545
                        },
                        {
                            "latitude": 42.32976149091639,
                            "name": "Coleman A. Young Municipal Center",
                            "longitude": -83.04377579084637,
                            "check_ins": 5022
                        },
                        {
                            "latitude": 42.33191605864348,
                            "name": "1001 Woodward",
                            "longitude": -83.04754257202148,
                            "check_ins": 1348
                        }
                    ],
                    "nightlife": [
                        {
                            "latitude": 42.32826161170011,
                            "name": "Cobo Joe's",
                            "longitude": -83.05088612530166,
                            "check_ins": 1474
                        },
                        {
                            "latitude": 42.329284,
                            "name": "The Anchor Bar",
                            "longitude": -83.05155848333334,
                            "check_ins": 5638
                        },
                        {
                            "latitude": 42.33119678468325,
                            "name": "Motor City Wine",
                            "longitude": -83.07288868317568,
                            "check_ins": 2463
                        },
                        {
                            "latitude": 42.33190897783369,
                            "name": "The Westin Book Cadillac Detroit",
                            "longitude": -83.05050336137704,
                            "check_ins": 15825
                        },
                        {
                            "latitude": 42.33231460808727,
                            "name": "Hard Rock Cafe Detroit",
                            "longitude": -83.04635971784592,
                            "check_ins": 9164
                        },
                        {
                            "latitude": 42.32941167958362,
                            "name": "London Chop House",
                            "longitude": -83.04759323405888,
                            "check_ins": 1337
                        },
                        {
                            "latitude": 42.33042737775734,
                            "name": "The Whiskey Parlor",
                            "longitude": -83.04613550028334,
                            "check_ins": 266
                        },
                        {
                            "latitude": 42.331535,
                            "name": "Parktoberfest",
                            "longitude": -83.04556,
                            "check_ins": 5
                        },
                        {
                            "latitude": 42.329734897555795,
                            "name": "Buhl Bar",
                            "longitude": -83.04672181606293,
                            "check_ins": 263
                        },
                        {
                            "latitude": 42.329439,
                            "name": "Climax Nightclub",
                            "longitude": -83.047979,
                            "check_ins": 2
                        },
                        {
                            "latitude": 42.33046793687358,
                            "name": "Drive - Table Tennis & Social Club",
                            "longitude": -83.04814380855841,
                            "check_ins": 95
                        },
                        {
                            "latitude": 42.32920528118992,
                            "name": "London Chop House Cigar Bar",
                            "longitude": -83.04742019540764,
                            "check_ins": 218
                        },
                        {
                            "latitude": 42.32794662380864,
                            "name": "Urban Cellars",
                            "longitude": -83.04761945199665,
                            "check_ins": 39
                        },
                        {
                            "latitude": 42.33126792123219,
                            "name": "Richard E. Durant Bar Stool",
                            "longitude": -83.0442949341809,
                            "check_ins": 50
                        },
                        {
                            "latitude": 42.331931,
                            "name": "Venitian Ballroom",
                            "longitude": -83.050799,
                            "check_ins": 7
                        },
                        {
                            "latitude": 42.33139240991084,
                            "name": "The Beach Bar",
                            "longitude": -83.04658645734678,
                            "check_ins": 264
                        },
                        {
                            "latitude": 42.32870438582905,
                            "name": "150 Cafe",
                            "longitude": -83.04755128533674,
                            "check_ins": 164
                        },
                        {
                            "latitude": 42.328473755364314,
                            "name": "World Of Bogner",
                            "longitude": -83.04589033126831,
                            "check_ins": 113
                        },
                        {
                            "latitude": 42.331867,
                            "name": "Cadillac Food Plaza",
                            "longitude": -83.044465,
                            "check_ins": 32
                        },
                        {
                            "latitude": 42.332674,
                            "name": "whoops",
                            "longitude": -83.04952,
                            "check_ins": 1
                        },
                        {
                            "latitude": 42.33096428856115,
                            "name": "Big City Bar & Grill",
                            "longitude": -83.05079340934753,
                            "check_ins": 1742
                        },
                        {
                            "latitude": 42.32593553090683,
                            "name": "Detroit Princess",
                            "longitude": -83.04522514343262,
                            "check_ins": 1154
                        },
                        {
                            "latitude": 42.331621939265304,
                            "name": "24 Grille",
                            "longitude": -83.05011535183809,
                            "check_ins": 3687
                        },
                        {
                            "latitude": 42.331594410160314,
                            "name": "The Motor Bar",
                            "longitude": -83.05039849415974,
                            "check_ins": 1241
                        },
                        {
                            "latitude": 42.32538821283585,
                            "name": "Olympia Club",
                            "longitude": -83.0522096157074,
                            "check_ins": 1002
                        },
                        {
                            "latitude": 42.329428016671784,
                            "name": "Round Bar",
                            "longitude": -83.05296244970077,
                            "check_ins": 1048
                        },
                        {
                            "latitude": 42.33202475701407,
                            "name": "Roast",
                            "longitude": -83.05077601535973,
                            "check_ins": 6796
                        },
                        {
                            "latitude": 42.33055185038616,
                            "name": "Grand Trunk Pub",
                            "longitude": -83.0457615852356,
                            "check_ins": 12965
                        },
                        {
                            "latitude": 42.32720121329311,
                            "name": "Tommy's Detroit Bar & Grill",
                            "longitude": -83.05376989148958,
                            "check_ins": 1477
                        },
                        {
                            "latitude": 42.331515826160334,
                            "name": "The Bathtub Pub",
                            "longitude": -83.04936554313726,
                            "check_ins": 603
                        }
                    ],
                    "food": [
                        {
                            "latitude": 42.33190897783369,
                            "name": "The Westin Book Cadillac Detroit",
                            "longitude": -83.05050336137704,
                            "check_ins": 15825
                        },
                        {
                            "latitude": 42.3323961,
                            "name": "Texas de Brazil - Detroit",
                            "longitude": -83.0470189,
                            "check_ins": 3320
                        },
                        {
                            "latitude": 42.33231460808727,
                            "name": "Hard Rock Cafe Detroit",
                            "longitude": -83.04635971784592,
                            "check_ins": 9164
                        },
                        {
                            "latitude": 42.33143224398473,
                            "name": "Lafayette Coney Island",
                            "longitude": -83.04894268512726,
                            "check_ins": 12018
                        },
                        {
                            "latitude": 42.32941167958362,
                            "name": "London Chop House",
                            "longitude": -83.04759323405888,
                            "check_ins": 1337
                        },
                        {
                            "latitude": 42.33033440085201,
                            "name": "Which Wich Superior Sandwiches",
                            "longitude": -83.0471842328772,
                            "check_ins": 202
                        },
                        {
                            "latitude": 42.33044786215829,
                            "name": "Bon Bon Bon",
                            "longitude": -83.04804942468566,
                            "check_ins": 128
                        },
                        {
                            "latitude": 42.332892751280816,
                            "name": "Dessert Oasis Coffee",
                            "longitude": -83.04914531797931,
                            "check_ins": 292
                        },
                        {
                            "latitude": 42.332804364393,
                            "name": "Calexico - Detroit",
                            "longitude": -83.0472207069397,
                            "check_ins": 120
                        },
                        {
                            "latitude": 42.33265312139813,
                            "name": "Detroit Water Ice Factory",
                            "longitude": -83.04730483605401,
                            "check_ins": 289
                        },
                        {
                            "latitude": 42.331627039906756,
                            "name": "Freshii",
                            "longitude": -83.04759323405888,
                            "check_ins": 175
                        },
                        {
                            "latitude": 42.33141600899818,
                            "name": "The Fountain Detroit",
                            "longitude": -83.04649731491648,
                            "check_ins": 66
                        },
                        {
                            "latitude": 42.33096428856115,
                            "name": "Big City Bar & Grill",
                            "longitude": -83.05079340934753,
                            "check_ins": 1742
                        },
                        {
                            "latitude": 42.32999754161835,
                            "name": "Jimmy John's",
                            "longitude": -83.04678047280707,
                            "check_ins": 1576
                        },
                        {
                            "latitude": 42.33055185038616,
                            "name": "Grand Trunk Pub",
                            "longitude": -83.0457615852356,
                            "check_ins": 12965
                        },
                        {
                            "latitude": 42.33148561085084,
                            "name": "Roasting Plant",
                            "longitude": -83.04604635724223,
                            "check_ins": 3398
                        },
                        {
                            "latitude": 42.331621939265304,
                            "name": "24 Grille",
                            "longitude": -83.05011535183809,
                            "check_ins": 3687
                        },
                        {
                            "latitude": 42.33073985688322,
                            "name": "Carnival Fresh Mex",
                            "longitude": -83.04734678493328,
                            "check_ins": 370
                        },
                        {
                            "latitude": 42.33097398602006,
                            "name": "Dime Store",
                            "longitude": -83.04764042633934,
                            "check_ins": 1314
                        },
                        {
                            "latitude": 42.330306166048416,
                            "name": "Townhouse Detroit",
                            "longitude": -83.04559539647798,
                            "check_ins": 1165
                        },
                        {
                            "latitude": 42.33148882328382,
                            "name": "Central Kitchen + Bar",
                            "longitude": -83.04581563351633,
                            "check_ins": 652
                        },
                        {
                            "latitude": 42.33202475701407,
                            "name": "Roast",
                            "longitude": -83.05077601535973,
                            "check_ins": 6796
                        },
                        {
                            "latitude": 42.33268464656886,
                            "name": "Slices",
                            "longitude": -83.0474936058001,
                            "check_ins": 323
                        },
                        {
                            "latitude": 42.330391997167624,
                            "name": "Woodward Coney Island",
                            "longitude": -83.04597818895284,
                            "check_ins": 691
                        },
                        {
                            "latitude": 42.330549264383365,
                            "name": "Bangkok Crossing",
                            "longitude": -83.04614074398788,
                            "check_ins": 1598
                        },
                        {
                            "latitude": 42.33151450222883,
                            "name": "Starbucks",
                            "longitude": -83.04683815296876,
                            "check_ins": 1662
                        },
                        {
                            "latitude": 42.33046323497224,
                            "name": "QZine",
                            "longitude": -83.04600440753404,
                            "check_ins": 1240
                        },
                        {
                            "latitude": 42.330424945788224,
                            "name": "Quicken Loans Qube",
                            "longitude": -83.0466628074646,
                            "check_ins": 12665
                        },
                        {
                            "latitude": 42.33158495805795,
                            "name": "American Coney Island",
                            "longitude": -83.04843744640789,
                            "check_ins": 7247
                        },
                        {
                            "latitude": 42.33055066599405,
                            "name": "Lunchtime Global",
                            "longitude": -83.04499236272058,
                            "check_ins": 1082
                        }
                    ]
                }
            },
            "1": {
                "location": {
                    "latitude": 42.3259106,
                    "longitude": -83.0542696
                },
                "categories": {
                    "college": [
                        {
                            "latitude": 42.32711867133332,
                            "name": "Wayne County Community College District Office Building",
                            "longitude": -83.05431517124603,
                            "check_ins": 619
                        },
                        {
                            "latitude": 42.326594450639845,
                            "name": "Wayne County Community College (Downtown Campus)",
                            "longitude": -83.05570980851554,
                            "check_ins": 920
                        },
                        {
                            "latitude": 42.326319935712064,
                            "name": "visual arts class",
                            "longitude": -83.05534280157524,
                            "check_ins": 2
                        },
                        {
                            "latitude": 42.32488848348208,
                            "name": "Beat Box",
                            "longitude": -83.0549669265747,
                            "check_ins": 6
                        },
                        {
                            "latitude": 42.32631258916646,
                            "name": "wcccd school library",
                            "longitude": -83.05537950236145,
                            "check_ins": 4
                        },
                        {
                            "latitude": 42.32658905611136,
                            "name": "Wayne County Community College",
                            "longitude": -83.055652136132,
                            "check_ins": 251
                        },
                        {
                            "latitude": 42.328826334278475,
                            "name": "Mt Elliot Makerspace",
                            "longitude": -83.04908763983997,
                            "check_ins": 3
                        },
                        {
                            "latitude": 42.32886505126953,
                            "name": "subway WCCC",
                            "longitude": -83.05253601074219,
                            "check_ins": 1
                        },
                        {
                            "latitude": 42.32645277875415,
                            "name": "Wayne County Community College District Downtown Campus Bookstore",
                            "longitude": -83.05626031508548,
                            "check_ins": 155
                        }
                    ],
                    "work": [
                        {
                            "latitude": 42.32541700126064,
                            "name": "Joe Louis Arena Parking Garage",
                            "longitude": -83.05457208033373,
                            "check_ins": 2305
                        },
                        {
                            "latitude": 42.32685564910629,
                            "name": "Cobo Center",
                            "longitude": -83.04960250854492,
                            "check_ins": 21699
                        },
                        {
                            "latitude": 42.326149980690694,
                            "name": "Salvation Army",
                            "longitude": -83.05857239235048,
                            "check_ins": 396
                        },
                        {
                            "latitude": 42.32817474208524,
                            "name": "First Street Parking Garage",
                            "longitude": -83.05190332271631,
                            "check_ins": 1543
                        },
                        {
                            "latitude": 42.3289187,
                            "name": "Detroit MiWorks - South",
                            "longitude": -83.0521326,
                            "check_ins": 1
                        },
                        {
                            "latitude": 42.322697,
                            "name": "Wintex",
                            "longitude": -83.055678,
                            "check_ins": 3
                        },
                        {
                            "latitude": 42.32865322310704,
                            "name": "Avanti Press-Detroit",
                            "longitude": -83.05025692315124,
                            "check_ins": 553
                        },
                        {
                            "latitude": 42.3291086337718,
                            "name": "Michigan Forward",
                            "longitude": -83.0550596805361,
                            "check_ins": 48
                        },
                        {
                            "latitude": 42.3295737388381,
                            "name": "Gurewitz & Raben",
                            "longitude": -83.0500087668903,
                            "check_ins": 0
                        },
                        {
                            "latitude": 42.328681842826825,
                            "name": "Howard Parking Lot",
                            "longitude": -83.05990402806933,
                            "check_ins": 311
                        },
                        {
                            "latitude": 42.32994978664618,
                            "name": "World Asset Management",
                            "longitude": -83.05036703396195,
                            "check_ins": 10
                        },
                        {
                            "latitude": 42.3302277471528,
                            "name": "Legal Aid and Defenders Association",
                            "longitude": -83.05552106234492,
                            "check_ins": 329
                        },
                        {
                            "latitude": 42.32761323451996,
                            "name": "Fort Street Presbyterian Church",
                            "longitude": -83.053759932518,
                            "check_ins": 268
                        },
                        {
                            "latitude": 42.32942559134141,
                            "name": "Fort Washington Plaza",
                            "longitude": -83.0502778966532,
                            "check_ins": 330
                        },
                        {
                            "latitude": 42.32729166666667,
                            "name": "Performax",
                            "longitude": -83.05659722222222,
                            "check_ins": 1
                        },
                        {
                            "latitude": 42.32908958396006,
                            "name": "US Department of State",
                            "longitude": -83.04959101098768,
                            "check_ins": 8
                        },
                        {
                            "latitude": 42.33015427214265,
                            "name": "MRJ Consulting",
                            "longitude": -83.05572029439803,
                            "check_ins": 25
                        },
                        {
                            "latitude": 42.32806681906185,
                            "name": "Foreman Bros. Inc.",
                            "longitude": -83.04842171584203,
                            "check_ins": 3226
                        },
                        {
                            "latitude": 42.33060769040349,
                            "name": "Crystal Ballroom",
                            "longitude": -83.05020973274736,
                            "check_ins": 6
                        },
                        {
                            "latitude": 42.329303142360125,
                            "name": "AFSCME LOCAL 25",
                            "longitude": -83.05505443754241,
                            "check_ins": 149
                        },
                        {
                            "latitude": 42.32620962824312,
                            "name": "Aisin Drive Green Experience",
                            "longitude": -83.04794455355714,
                            "check_ins": 13
                        },
                        {
                            "latitude": 42.32760848749417,
                            "name": "RR Donnelley",
                            "longitude": -83.05449343480122,
                            "check_ins": 43
                        },
                        {
                            "latitude": 42.33029297426193,
                            "name": "The Z",
                            "longitude": -83.0512007241202,
                            "check_ins": 15
                        },
                        {
                            "latitude": 42.32722,
                            "name": "MACUL11",
                            "longitude": -83.04829863333333,
                            "check_ins": 20
                        },
                        {
                            "latitude": 42.3284374,
                            "name": "BEI Associates, Inc.",
                            "longitude": -83.0528815,
                            "check_ins": 6
                        },
                        {
                            "latitude": 42.32917333545208,
                            "name": "DoubleTree Suites by Hilton Hotel Detroit Downtown - Fort Shelby",
                            "longitude": -83.05292040109634,
                            "check_ins": 6983
                        },
                        {
                            "latitude": 42.328586575523026,
                            "name": "Detroit Free Press",
                            "longitude": -83.05415263640695,
                            "check_ins": 3207
                        },
                        {
                            "latitude": 42.32959643929145,
                            "name": "WDIV Local 4 News",
                            "longitude": -83.0535024930339,
                            "check_ins": 1249
                        },
                        {
                            "latitude": 42.33002904329738,
                            "name": "Comerica Bank",
                            "longitude": -83.05170407910059,
                            "check_ins": 1435
                        },
                        {
                            "latitude": 42.329469083830794,
                            "name": "West Fort Street Building",
                            "longitude": -83.04960149784564,
                            "check_ins": 1453
                        }
                    ],
                    "nightlife": [
                        {
                            "latitude": 42.32826161170011,
                            "name": "Cobo Joe's",
                            "longitude": -83.05088612530166,
                            "check_ins": 1474
                        },
                        {
                            "latitude": 42.32720121329311,
                            "name": "Tommy's Detroit Bar & Grill",
                            "longitude": -83.05376989148958,
                            "check_ins": 1477
                        },
                        {
                            "latitude": 42.325197,
                            "name": "Miller Lite Party Deck at The Joe",
                            "longitude": -83.051419,
                            "check_ins": 75
                        },
                        {
                            "latitude": 42.327421,
                            "name": "Max On Third",
                            "longitude": -83.053931,
                            "check_ins": 171
                        },
                        {
                            "latitude": 42.325252168361025,
                            "name": "Comerica Bank Legends Club",
                            "longitude": -83.05141045583011,
                            "check_ins": 142
                        },
                        {
                            "latitude": 42.328036,
                            "name": "U.S. Social Forum",
                            "longitude": -83.048644,
                            "check_ins": 45
                        },
                        {
                            "latitude": 42.329689683333335,
                            "name": "Mikes Mary Jane",
                            "longitude": -83.05321653333333,
                            "check_ins": 3
                        },
                        {
                            "latitude": 42.32812468949382,
                            "name": "Delta Sky360 Lounge",
                            "longitude": -83.0494337079177,
                            "check_ins": 10
                        },
                        {
                            "latitude": 42.329318,
                            "name": "The Detroit Club712 Cass Avenue",
                            "longitude": -83.050744,
                            "check_ins": 0
                        },
                        {
                            "latitude": 42.326099,
                            "name": "The Vu",
                            "longitude": -83.047708,
                            "check_ins": 91
                        },
                        {
                            "latitude": 42.330623626708984,
                            "name": "Southwoods Pub And Grill",
                            "longitude": -83.05054473876953,
                            "check_ins": 0
                        },
                        {
                            "latitude": 42.326277,
                            "name": "Bakari Anwar Lounge",
                            "longitude": -83.059858,
                            "check_ins": 105
                        },
                        {
                            "latitude": 42.328344973193516,
                            "name": "Cellar D Cafe & Lounge",
                            "longitude": -83.05061871512301,
                            "check_ins": 48
                        },
                        {
                            "latitude": 42.32838268859445,
                            "name": "Ciccarelli's Sports Bar",
                            "longitude": -83.05026216652735,
                            "check_ins": 222
                        },
                        {
                            "latitude": 42.32538821283585,
                            "name": "Olympia Club",
                            "longitude": -83.0522096157074,
                            "check_ins": 1002
                        },
                        {
                            "latitude": 42.329284,
                            "name": "The Anchor Bar",
                            "longitude": -83.05155848333334,
                            "check_ins": 5638
                        },
                        {
                            "latitude": 42.32396682124744,
                            "name": "Signature Grille Bar",
                            "longitude": -83.05523794207325,
                            "check_ins": 638
                        },
                        {
                            "latitude": 42.329428016671784,
                            "name": "Round Bar",
                            "longitude": -83.05296244970077,
                            "check_ins": 1048
                        },
                        {
                            "latitude": 42.32887034368453,
                            "name": "Finn & Porter Restaurant",
                            "longitude": -83.05245637893677,
                            "check_ins": 831
                        }
                    ],
                    "food": [
                        {
                            "latitude": 42.32924,
                            "name": "Prism",
                            "longitude": -83.05331,
                            "check_ins": 112
                        },
                        {
                            "latitude": 42.32669831048064,
                            "name": "SUBWAY",
                            "longitude": -83.05550533347291,
                            "check_ins": 17
                        },
                        {
                            "latitude": 42.329958,
                            "name": "Starbucks @ The Doubletree",
                            "longitude": -83.05478,
                            "check_ins": 1
                        },
                        {
                            "latitude": 42.328344973193516,
                            "name": "Cellar D Cafe & Lounge",
                            "longitude": -83.05061871512301,
                            "check_ins": 48
                        },
                        {
                            "latitude": 42.325121260693514,
                            "name": "Haz Subs & Salads",
                            "longitude": -83.0602710095498,
                            "check_ins": 86
                        },
                        {
                            "latitude": 42.32865322310704,
                            "name": "Avanti Press-Detroit",
                            "longitude": -83.05025692315124,
                            "check_ins": 553
                        },
                        {
                            "latitude": 42.32940219512221,
                            "name": "Salubres",
                            "longitude": -83.05739801405873,
                            "check_ins": 2
                        },
                        {
                            "latitude": 42.32947,
                            "name": "Bearclaw Coffee Co",
                            "longitude": -83.053103,
                            "check_ins": 341
                        },
                        {
                            "latitude": 42.32939618788168,
                            "name": "Sterling Services Comerica 411",
                            "longitude": -83.05090709860303,
                            "check_ins": 517
                        },
                        {
                            "latitude": 42.32776810434997,
                            "name": "Cork & Grind",
                            "longitude": -83.04868389144872,
                            "check_ins": 4
                        },
                        {
                            "latitude": 42.326099,
                            "name": "The Vu",
                            "longitude": -83.047708,
                            "check_ins": 91
                        },
                        {
                            "latitude": 42.330078,
                            "name": "Sodexho",
                            "longitude": -83.051567,
                            "check_ins": 0
                        },
                        {
                            "latitude": 42.32523715966513,
                            "name": "Buffalo Wild Wings",
                            "longitude": -83.05164640320446,
                            "check_ins": 34
                        },
                        {
                            "latitude": 42.326045885214576,
                            "name": "Reggie's Soul Food Cafe",
                            "longitude": -83.06006654869199,
                            "check_ins": 52
                        },
                        {
                            "latitude": 42.32924493307363,
                            "name": "Motor City Kitchen",
                            "longitude": -83.05252726592461,
                            "check_ins": 36
                        },
                        {
                            "latitude": 42.327990502629014,
                            "name": "Eatsville USA",
                            "longitude": -83.0485632907994,
                            "check_ins": 9
                        },
                        {
                            "latitude": 42.32640923705075,
                            "name": "The Pickle Shack",
                            "longitude": -83.05884501288243,
                            "check_ins": 12
                        },
                        {
                            "latitude": 42.32573437794764,
                            "name": "Rybas Fudge",
                            "longitude": -83.04892509208429,
                            "check_ins": 11
                        },
                        {
                            "latitude": 42.329767228804165,
                            "name": "Gateway Deli",
                            "longitude": -83.0501835158417,
                            "check_ins": 476
                        },
                        {
                            "latitude": 42.32541437,
                            "name": "Coney King",
                            "longitude": -83.06027,
                            "check_ins": 419
                        },
                        {
                            "latitude": 42.32887034368453,
                            "name": "Finn & Porter Restaurant",
                            "longitude": -83.05245637893677,
                            "check_ins": 831
                        },
                        {
                            "latitude": 42.32870530686395,
                            "name": "The Bean Bar",
                            "longitude": -83.04918726568529,
                            "check_ins": 383
                        },
                        {
                            "latitude": 42.329428016671784,
                            "name": "Round Bar",
                            "longitude": -83.05296244970077,
                            "check_ins": 1048
                        },
                        {
                            "latitude": 42.32555823095665,
                            "name": "Burger King",
                            "longitude": -83.06154338097065,
                            "check_ins": 506
                        }
                    ]
                }
            }
        }
    }
    return json.dumps(json_data["results"][request.args.get('id')])


@app.route('/api/map')
def api_map():
    output_data = {
        "response": "ok",
        "message": "data is valid"
    }

    return json.dumps(output_data)


if __name__ == "__main__":
    app.debug = True
    app.run()
