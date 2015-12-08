import json
from urllib2 import urlopen

# copy/past the ip list here:
ip_address = ['1.119.19.254',
'252.219.62.163',
'207.13.124.193',
'196.98.159.84',
'90.108.111.28',
'205.65.212.127',
'238.13.72.159',
'204.90.64.154',
'42.110.237.223',
'112.32.12.35',
            ]

ISO2country = {'AD': 'Andorra',
              'AE': 'United Arab Emirates',
              'AF': 'Afghanistan',
              'AG': 'Antigua and Barbuda',
              'AI': 'Anguilla',
              'AL': 'Albania',
              'AM': 'Armenia',
              'AN': 'Netherlands Antilles',
              'AO': 'Angola',
              'AQ': 'Antarctica',
              'AR': 'Argentina',
              'AS': 'American Samoa',
              'AT': 'Austria',
              'AU': 'Australia',
              'AW': 'Aruba',
              'AX': 'Aland Islands',
              'AZ': 'Azerbaijan',
              'BA': 'Bosnia and Herzegovina',
              'BB': 'Barbados',
              'BD': 'Bangladesh',
              'BE': 'Belgium',
              'BF': 'Burkina Faso',
              'BG': 'Bulgaria',
              'BH': 'Bahrain',
              'BI': 'Burundi',
              'BJ': 'Benin',
              'BL': 'Saint-Barth\xc3\xa9lemy',
              'BM': 'Bermuda',
              'BN': 'Brunei Darussalam',
              'BO': 'Bolivia',
              'BR': 'Brazil',
              'BS': 'Bahamas',
              'BT': 'Bhutan',
              'BV': 'Bouvet Island',
              'BW': 'Botswana',
              'BY': 'Belarus',
              'BZ': 'Belize',
              'CA': 'Canada',
              'CC': 'Cocos (Keeling) Islands',
              'CD': 'Congo, Democratic Republic of the',
              'CF': 'Central African Republic',
              'CG': 'Congo (Brazzaville)',
              'CH': 'Switzerland',
              'CI': 'C\xc3\xb4te Ivoire',
              'CK': 'Cook Islands',
              'CL': 'Chile',
              'CM': 'Cameroon',
              'CN': 'China',
              'CO': 'Colombia',
              'CR': 'Costa Rica',
              'CU': 'Cuba',
              'CV': 'Cape Verde',
              'CX': 'Christmas Island',
              'CY': 'Cyprus',
              'CZ': 'Czech Republic',
              'DE': 'Germany',
              'DJ': 'Djibouti',
              'DK': 'Denmark',
              'DM': 'Dominica',
              'DO': 'Dominican Republic',
              'DZ': 'Algeria',
              'EC': 'Ecuador',
              'EE': 'Estonia',
              'EG': 'Egypt',
              'EH': 'Western Sahara',
              'ER': 'Eritrea',
              'ES': 'Spain',
              'ET': 'Ethiopia',
              'FI': 'Finland',
              'FJ': 'Fiji',
              'FK': 'Falkland Islands (Malvinas)',
              'FM': 'Micronesia, Federated States of',
              'FO': 'Faroe Islands',
              'FR': 'France',
              'GA': 'Gabon',
              'GB': 'United Kingdom',
              'GD': 'Grenada',
              'GE': 'Georgia',
              'GF': 'French Guiana',
              'GG': 'Guernsey',
              'GH': 'Ghana',
              'GI': 'Gibraltar',
              'GL': 'Greenland',
              'GM': 'Gambia',
              'GN': 'Guinea',
              'GP': 'Guadeloupe',
              'GQ': 'Equatorial Guinea',
              'GR': 'Greece',
              'GS': 'South Georgia and the South Sandwich Islands',
              'GT': 'Guatemala',
              'GU': 'Guam',
              'GW': 'Guinea-Bissau',
              'GY': 'Guyana',
              'HK': 'Hong Kong Special Administrative Region of China',
              'HM': 'Heard Island and Mcdonald Islands',
              'HN': 'Honduras',
              'HR': 'Croatia',
              'HT': 'Haiti',
              'HU': 'Hungary',
              'ID': 'Indonesia',
              'IE': 'Ireland',
              'IL': 'Israel',
              'IM': 'Isle of Man',
              'IN': 'India',
              'IO': 'British Indian Ocean Territory',
              'IQ': 'Iraq',
              'IR': 'Iran Islamic Republic of',
              'IS': 'Iceland',
              'IT': 'Italy',
              'JE': 'Jersey',
              'JM': 'Jamaica',
              'JO': 'Jordan',
              'JP': 'Japan',
              'KE': 'Kenya',
              'KG': 'Kyrgyzstan',
              'KH': 'Cambodia',
              'KI': 'Kiribati',
              'KM': 'Comoros',
              'KN': 'Saint Kitts and Nevis',
              'KP': 'Korea Democratic Republic of',
              'KR': 'Korea Republic of',
              'KW': 'Kuwait',
              'KY': 'Cayman Islands',
              'KZ': 'Kazakhstan',
              'LA': 'Lao PDR',
              'LB': 'Lebanon',
              'LC': 'Saint Lucia',
              'LI': 'Liechtenstein',
              'LK': 'Sri Lanka',
              'LR': 'Liberia',
              'LS': 'Lesotho',
              'LT': 'Lithuania',
              'LU': 'Luxembourg',
              'LV': 'Latvia',
              'LY': 'Libya',
              'MA': 'Morocco',
              'MC': 'Monaco',
              'MD': 'Moldova',
              'ME': 'Montenegro',
              'MF': 'Saint-Martin (French part)',
              'MG': 'Madagascar',
              'MH': 'Marshall Islands',
              'MK': 'Macedonia, Republic of',
              'ML': 'Mali',
              'MM': 'Myanmar',
              'MN': 'Mongolia',
              'MO': 'Macao Special Administrative Region of China',
              'MP': 'Northern Mariana Islands',
              'MQ': 'Martinique',
              'MR': 'Mauritania',
              'MS': 'Montserrat',
              'MT': 'Malta',
              'MU': 'Mauritius',
              'MV': 'Maldives',
              'MW': 'Malawi',
              'MX': 'Mexico',
              'MY': 'Malaysia',
              'MZ': 'Mozambique',
              'NA': 'Namibia',
              'NC': 'New Caledonia',
              'NE': 'Niger',
              'NF': 'Norfolk Island',
              'NG': 'Nigeria',
              'NI': 'Nicaragua',
              'NL': 'Netherlands',
              'NO': 'Norway',
              'NP': 'Nepal',
              'NR': 'Nauru',
              'NU': 'Niue',
              'NZ': 'New Zealand',
              'OM': 'Oman',
              'PA': 'Panama',
              'PE': 'Peru',
              'PF': 'French Polynesia',
              'PG': 'Papua New Guinea',
              'PH': 'Philippines',
              'PK': 'Pakistan',
              'PL': 'Poland',
              'PM': 'Saint Pierre and Miquelon',
              'PN': 'Pitcairn',
              'PR': 'Puerto Rico',
              'PS': 'Palestinian Territory',
              'PT': 'Portugal',
              'PW': 'Palau',
              'PY': 'Paraguay',
              'QA': 'Qatar',
              'RE': 'R\xc3\xa9union',
              'RO': 'Romania',
              'RS': 'Serbia',
              'RU': 'Russian Federation',
              'RW': 'Rwanda',
              'SA': 'Saudi Arabia',
              'SB': 'Solomon Islands',
              'SC': 'Seychelles',
              'SD': 'Sudan',
              'SE': 'Sweden',
              'SG': 'Singapore',
              'SH': 'Saint Helena',
              'SI': 'Slovenia',
              'SJ': 'Svalbard and Jan Mayen Islands',
              'SK': 'Slovakia',
              'SL': 'Sierra Leone',
              'SM': 'San Marino',
              'SN': 'Senegal',
              'SO': 'Somalia',
              'SR': 'Suriname',
              'SS': 'South Sudan',
              'ST': 'Sao Tome and Principe',
              'SV': 'El Salvador',
              'SY': 'Syrian Arab Republic (Syria)',
              'SZ': 'Swaziland',
              'TC': 'Turks and Caicos Islands',
              'TD': 'Chad',
              'TF': 'French Southern Territories',
              'TG': 'Togo',
              'TH': 'Thailand',
              'TJ': 'Tajikistan',
              'TK': 'Tokelau',
              'TL': 'Timor-Leste',
              'TM': 'Turkmenistan',
              'TN': 'Tunisia',
              'TO': 'Tonga',
              'TR': 'Turkey',
              'TT': 'Trinidad and Tobago',
              'TV': 'Tuvalu',
              'TW': 'Taiwan, Republic of China',
              'TZ': 'Tanzania United Republic of',
              'UA': 'Ukraine',
              'UG': 'Uganda',
              'UM': 'United States Minor Outlying Islands',
              'US': 'United States of America',
              'UY': 'Uruguay',
              'UZ': 'Uzbekistan',
              'VA': 'Holy See (Vatican City State)',
              'VC': 'Saint Vincent and Grenadines',
              'VE': 'Venezuela (Bolivarian Republic of)',
              'VG': 'British Virgin Islands',
              'VI': 'Virgin Islands, US',
              'VN': 'Viet Nam',
              'VU': 'Vanuatu',
              'WF': 'Wallis and Futuna Islands',
              'WS': 'Samoa',
              'YE': 'Yemen',
              'YT': 'Mayotte',
              'ZA': 'South Africa',
              'ZM': 'Zambia',
              'ZW': 'Zimbabwe'
            }
ISO2CONTINENTS = {'AD': 'Europe',
                'AE': 'Asia',
                'AF': 'Asia',
                'AG': 'North-America',
                'AI': 'North-America',
                'AL': 'Europe',
                'AM': 'Asia',
                'AN': 'North-America',
                'AO': 'Africa',
                'AP': 'Asia',
                'AQ': 'AN',
                'AR': 'South-America',
                'AS': 'Oceania',
                'AT': 'Europe',
                'AU': 'Oceania',
                'AW': 'North-America',
                'AX': 'Europe',
                'AZ': 'Asia',
                'BA': 'Europe',
                'BB': 'North-America',
                'BD': 'Asia',
                'BE': 'Europe',
                'BF': 'Africa',
                'BG': 'Europe',
                'BH': 'Asia',
                'BI': 'Africa',
                'BJ': 'Africa',
                'BL': 'North-America',
                'BM': 'North-America',
                'BN': 'Asia',
                'BO': 'South-America',
                'BR': 'South-America',
                'BS': 'North-America',
                'BT': 'Asia',
                'BV': 'AN',
                'BW': 'Africa',
                'BY': 'Europe',
                'BZ': 'North-America',
                'CA': 'North-America',
                'CC': 'Asia',
                'CD': 'Africa',
                'CF': 'Africa',
                'CG': 'Africa',
                'CH': 'Europe',
                'CI': 'Africa',
                'CK': 'Oceania',
                'CL': 'South-America',
                'CM': 'Africa',
                'CN': 'Asia',
                'CO': 'South-America',
                'CR': 'North-America',
                'CU': 'North-America',
                'CV': 'Africa',
                'CX': 'Asia',
                'CY': 'Asia',
                'CZ': 'Europe',
                'DE': 'Europe',
                'DJ': 'Africa',
                'DK': 'Europe',
                'DM': 'North-America',
                'DO': 'North-America',
                'DZ': 'Africa',
                'EC': 'South-America',
                'EE': 'Europe',
                'EG': 'Africa',
                'EH': 'Africa',
                'ER': 'Africa',
                'ES': 'Europe',
                'ET': 'Africa',
                'EU': 'Europe',
                'FI': 'Europe',
                'FJ': 'Oceania',
                'FK': 'South-America',
                'FM': 'Oceania',
                'FO': 'Europe',
                'FR': 'Europe',
                'FX': 'Europe',
                'GA': 'Africa',
                'GB': 'Europe',
                'GD': 'North-America',
                'GE': 'Asia',
                'GF': 'South-America',
                'GG': 'Europe',
                'GH': 'Africa',
                'GI': 'Europe',
                'GL': 'North-America',
                'GM': 'Africa',
                'GN': 'Africa',
                'GP': 'North-America',
                'GQ': 'Africa',
                'GR': 'Europe',
                'GS': 'AN',
                'GT': 'North-America',
                'GU': 'Oceania',
                'GW': 'Africa',
                'GY': 'South-America',
                'HK': 'Asia',
                'HM': 'AN',
                'HN': 'North-America',
                'HR': 'Europe',
                'HT': 'North-America',
                'HU': 'Europe',
                'ID': 'Asia',
                'IE': 'Europe',
                'IL': 'Asia',
                'IM': 'Europe',
                'IN': 'Asia',
                'IO': 'Asia',
                'IQ': 'Asia',
                'IR': 'Asia',
                'IS': 'Europe',
                'IT': 'Europe',
                'JE': 'Europe',
                'JM': 'North-America',
                'JO': 'Asia',
                'JP': 'Asia',
                'KE': 'Africa',
                'KG': 'Asia',
                'KH': 'Asia',
                'KI': 'Oceania',
                'KM': 'Africa',
                'KN': 'North-America',
                'KP': 'Asia',
                'KR': 'Asia',
                'KW': 'Asia',
                'KY': 'North-America',
                'KZ': 'Asia',
                'LA': 'Asia',
                'LB': 'Asia',
                'LC': 'North-America',
                'LI': 'Europe',
                'LK': 'Asia',
                'LR': 'Africa',
                'LS': 'Africa',
                'LT': 'Europe',
                'LU': 'Europe',
                'LV': 'Europe',
                'LY': 'Africa',
                'MA': 'Africa',
                'MC': 'Europe',
                'MD': 'Europe',
                'ME': 'Europe',
                'MF': 'North-America',
                'MG': 'Africa',
                'MH': 'Oceania',
                'MK': 'Europe',
                'ML': 'Africa',
                'MM': 'Asia',
                'MN': 'Asia',
                'MO': 'Asia',
                'MP': 'Oceania',
                'MQ': 'North-America',
                'MR': 'Africa',
                'MS': 'North-America',
                'MT': 'Europe',
                'MU': 'Africa',
                'MV': 'Asia',
                'MW': 'Africa',
                'MX': 'North-America',
                'MY': 'Asia',
                'MZ': 'Africa',
                'NA': 'Africa',
                'NC': 'Oceania',
                'NE': 'Africa',
                'NF': 'Oceania',
                'NG': 'Africa',
                'NI': 'North-America',
                'NL': 'Europe',
                'NO': 'Europe',
                'NP': 'Asia',
                'NR': 'Oceania',
                'NU': 'Oceania',
                'NZ': 'Oceania',
                'OM': 'Asia',
                'PA': 'North-America',
                'PE': 'South-America',
                'PF': 'Oceania',
                'PG': 'Oceania',
                'PH': 'Asia',
                'PK': 'Asia',
                'PL': 'Europe',
                'PM': 'North-America',
                'PN': 'Oceania',
                'PR': 'North-America',
                'PS': 'Asia',
                'PT': 'Europe',
                'PW': 'Oceania',
                'PY': 'South-America',
                'QA': 'Asia',
                'RE': 'Africa',
                'RO': 'Europe',
                'RS': 'Europe',
                'RU': 'Europe',
                'RW': 'Africa',
                'SA': 'Asia',
                'SB': 'Oceania',
                'SC': 'Africa',
                'SD': 'Africa',
                'SE': 'Europe',
                'SG': 'Asia',
                'SH': 'Africa',
                'SI': 'Europe',
                'SJ': 'Europe',
                'SK': 'Europe',
                'SL': 'Africa',
                'SM': 'Europe',
                'SN': 'Africa',
                'SO': 'Africa',
                'SR': 'South-America',
                'ST': 'Africa',
                'SV': 'North-America',
                'SY': 'Asia',
                'SZ': 'Africa',
                'TC': 'North-America',
                'TD': 'Africa',
                'TF': 'AN',
                'TG': 'Africa',
                'TH': 'Asia',
                'TJ': 'Asia',
                'TK': 'Oceania',
                'TL': 'Asia',
                'TM': 'Asia',
                'TN': 'Africa',
                'TO': 'Oceania',
                'TR': 'Europe',
                'TT': 'North-America',
                'TV': 'Oceania',
                'TW': 'Asia',
                'TZ': 'Africa',
                'UA': 'Europe',
                'UG': 'Africa',
                'UM': 'Oceania',
                'US': 'North-America',
                'UY': 'South-America',
                'UZ': 'Asia',
                'VA': 'Europe',
                'VC': 'North-America',
                'VE': 'South-America',
                'VG': 'North-America',
                'VI': 'North-America',
                'VN': 'Asia',
                'VU': 'Oceania',
                'WF': 'Oceania',
                'WS': 'Oceania',
                'YE': 'Asia',
                'YT': 'Africa',
                'ZA': 'Africa',
                'ZM': 'Africa',
                'ZW': 'Africa',}

country2ISO = {v: k for k, v in ISO2country.items()}
member_countries = {}

# Get number of IP in the same country
i = 0

for ip in ip_address:
    i += 1
    url = 'http://ipinfo.io/'+ ip +'/json'
    response = urlopen('http://ipinfo.io/'+ ip +'/json')
    data = json.load(response)

    if 'country' not in data:
        continue

    country = data['country']

    if country in member_countries:
        member_countries[country] += 1
    else:
         member_countries[country] = 1

    print 'Retrieiving location in progress:', (float(i)/len(ip_address))*100, '%'

print 'Cleaning data'
# remove unknown country
if '' in member_countries:
    del member_countries['']

# Retrieve country name from the ISO
for ISO in ISO2country:
    if ISO not in member_countries:
        continue
    country_name = ISO2country[ISO]
    member_countries[country_name] = member_countries.pop(ISO)

members_by_continent = {}

# Associate continent
for country in member_countries:
    iso = country2ISO[country]
    con = ISO2CONTINENTS[iso]

    if con in members_by_continent:
        members_by_continent[con] += member_countries[country]
    else:
         members_by_continent[con] = member_countries[country]


print 'Export results in members.csv file'
with open('members.csv', 'w') as f:
    f.write('Country, number of users\n')
    [f.write('{0},{1}\n'.format(key, value)) for key, value in member_countries.items()]
    f.write('\nContinent, number of users\n')
    [f.write('{0},{1}\n'.format(key, value)) for key, value in members_by_continent.items()]

print 'Done !'
