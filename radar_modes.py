
radar = {}

# Kodiak
#             Common: uafscan --stid kod --xcf 1 --fast --df 10400 --nf 10400 -c 4
#      Discretionary: uafscan --stid kod --di --xcf 1 --fast --df 10400 --nf 10400 -c 4
# Special:THEMISSCAN: uafscan --stid kod --xcf 1 --fast --df 10400 --nf 10400 -c 4
#   Special:RBSPSCAN: uafscan --stid kod --xcf 1 --fast --df 10400 --nf 10400 -c 4
radar.update({"kod": {"Control Program": "uafscan",
                      "Control Program Path": "/home/radar/rst/usr/bin",
                      "Control Program Arguments": "--xcf 1 --fast",
                      "Day Frequency": 10400,
                      "Night Frequency": 10400,
                      "Mode": {'Common': '',
                               'Discretionary': '--di',
                               'Special:THEMISSCAN': '',
                               'Special:RBSPSCAN': ''}

                      }})

# McMurdo
#             Common: uafscan --stid mcm --xcf 1 --fast --df 10250 --nf 10250 -c 1
#      Discretionary: uafscan --stid mcm --di --xcf 1 --fast --df 10250 --nf 10250 -c 1
# Special:THEMISSCAN: uafscan --stid mcm --xcf 1 --fast --df 10250 --nf 10250 -c 1
#   Special:RBSPSCAN: uafscan --stid mcm --xcf 1 --fast --df 10250 --nf 10250 -c 1
radar.update({"mcm": {"Control Program": "uafscan",
                      "Control Program Path": "/home/radar/rst/usr/bin",
                      "Control Program Arguments": "--xcf 1 --fast",
                      "Day Frequency": 10250,
                      "Night Frequency": 10250,
                      "Mode": {'Common': '',
                               'Discretionary': '--di',
                               'Special:THEMISSCAN': '',
                               'Special:RBSPSCAN': ''}

                      }})

# South Pole
#             Common: uafscan --stid sps --xcf 1 --fast --df 12550 --nf 12550 -c 1
#      Discretionary: uafscan --stid sps --di --xcf 1 --fast --df 12550 --nf 12550 -c 1
# Special:THEMISSCAN: uafscan --stid sps --xcf 1 --fast --df 12550 --nf 12550 -c 1
#   Special:RBSPSCAN: uafscan --stid sps --xcf 1 --fast --df 12550 --nf 12550 -c 1
radar.update({"sps": {"Control Program": "uafscan",
                      "Control Program Path": "/home/radar/rst/usr/bin",
                      "Control Program Arguments": "--xcf 1 --fast",
                      "Day Frequency": 10200,
                      "Night Frequency": 10200,
                      "Mode": {'Common': '',
                               'Discretionary': '--di',
                               'Special:THEMISSCAN': '',
                               'Special:RBSPSCAN': ''}

                      }})
