import re
text = ''' MAR, STE, BAR, offshore
 Galveston (Texas)
 FIFI: Honduras
 Dominican Republic
 FLORA: Haiti, Cuba
 Pointe-a-Pitre Bay (GUA)
 Newfoundland Banks
 Puerto Rico, Carolinas
 FL, GUA, PR, TUR, MAR
 Cuba, CI, Jamaica
 Central Atlantic
 Martinique
 El Salvador, Honduras
 Western Cuba
 Barbados
 Belize
 HAI, HON, offshore JAM
 DAVID: DR, Dominica, US
 Offshore Florida (?)
 South Carolina, Georgia
 Eastern Gulf of Mexico
 Cuba
 Louisiana
 Guadeloupe, Martinique
 Martinique
 Mexico
 W Cuba, Straits of FL
 Guadeloupe, Puerto Rico
 Offshore Nicaragua
 GORDON: HAI, FL, CR, DR
 Jamaica, Cuba
 Straits of Florida
 Gulf of Mexico
 Offshore Barbados
 S Bahamas, Straits of FL
 Havana (Cuba)
 Veracruz (Mexico)
 HAZEL: HAI, US, GRE, CAN
 INEZ: Caribbean, Mexico
 Cuba, PR, Turks Islands
 St  Thomas, Puerto Rico
 Texas, Cuba
 Cuba, offshore Bermuda
 Martinique, TUR, PR
 Georgia, South Carolina
 Florida west coast
 Florida
 New England
 JANET: Mexico, BEL, BAR
 FL Keys, S Texas, Cuba
 MAR, DOM, New Eng, BAH
 Offshore Martinique
 W Atlantic, Nova Scotia
 FOX: Cuba
 Southwest Caribbean Sea 
 AUDREY: SW LA, N Texas
 Atlantic
 Offshore DR
 Offshore western FL
 Offshore Puerto Rico
 Georgia, SC, NC
 Florida east coast
 Dominica
 Martinique
 North Carolina
 Florida Keys
 SE TX, Gulf MX, CU, JAM
 Jamaica
 Jamaica, Cayman Islands
 Louisiana
 US  east coast, W ATL
 Offshore SC, BAH, TUR
 St  Vincent, Barbados
 DONNA: Florida, PR, BAH
 Louisiana, Mississippi
 FL, N Gulf States, BAH
 GILBERT: MX, JAM, HAI
 Cuba, offshore Florida
 HILDA: Mexico, Cuba
 Gulf of Mexico
 South Carolina
 Bahamas, PR, DR, FL
 Near Cape Canaveral (FL)
 Hispaniola, PR, Jamaica
 Mississippi, LA, Jamaica
 HATTIE: Belize
 CHARLIE: Jamaica, Mexico
 ALLEN: Haiti, US
 CAMILLE: MS, LA, WV, VA
 Puerto Rico
 St  Lucia, Dominica, BAR
 Cuba
 CLEO: Lesser Antilles
 MX, offshore GRE, JAM
 JOAN: NIC, CR, COL, VEN
 Mexico
 Barbados
 Guadeloupe, NE US coast
 Dominica, DR
 Upper Texas coast
 Barbados
 St  Kitts
 Cuba
 Jamaica
 DIANE: US NE states
 Southeast Florida, Cuba
 Cayman Islands, JAM, MAR
 NW Atlantic, S NF coast
 Tampico (Mexico)
 BRET: VEN, NIC, COL
 Jamaica
 Island near Nevis, Cuba
 Delaware coast
 Isabel: Puerto Rico
 Cuba, TUR, S Texas
 Georgia, SC, NC
 North coast of Colombia
 Dominica
 W Cuba, FL Keys, CI
 North Carolina, Virginia
 East Texas
 Massachusetts
 JAM, PR, Cuba, St  Croix
 Near STT, SW Atlan , PR
 Labrador coast, W Cuba
 Central Atlantic
 Mississippi, AL, NW FL
 Florida, Georgia, SC
 JAM, near HAI & DR, HAI
 AGNES: US NE states, CU
 Hispaniola
 Between JAM and England
 Atlantic (?)
 Roanoke Island (NC)
 BERYL: Cape Verde Is
 North Carolina, Bahamas
 Gulf coast, NC
 Offshore Mexico
 South Carolina, NC
 Cuba, Southwest Florida
 Cuba
 Jamaica
 Honduras
 Cuba
 Jamaica
 Puerto Rico
 Montserrat to VI
 FRANCELIA: Guatemala
 Belize
 Martinique
 Georgia
 Charleston (SC)
 Dominican Republic
 DIANA: Mexico
 ALMA: Honduras, Cuba, FL
 Cuba
 Curacao, PA, US E coast
 Windward Islands, BER
 New England
 Near NC Outer Banks
 Newfoundland Banks
 Dominican Republic
 CARRIE: SW of Azores
 ELOISE: PR, US, HAI, DR
 Jamaica, Cuba, Florida
 BETSY: SE Florida, SE LA
 GERT: Mexico, HON, NIC
 Cuba, Bimini
 Western Cuba
 US E coast waters, Cuba
 Rio Grande Valley
 Jamaica
 South Carolina
 EMMY: Azores
 Near St  Augustine (FL)
 Mexico
 Near Tortola, Montserrat
 Offshore Mexico
 Off US SE coast, FL
 Cuba
 CAROL: US NE states
 OPAL: Guatemala, MX, US SE states
 BEULAH: TX, N MX, MAR
 Martinique, SW Atlantic
 U S mid-Atlantic coast
 Cuba
 S BAH, FL, FL Straits
 HUGO: GUA, MON, SC
 ALICE: NE MX, TX
 Offshore central FL, VA
 Off Bermuda
 CESAR: NIC, HON, El Salvador
 South Texas
 SE Florida, LA, MS
 DOROTHY: Martinique, DOM
 Newfoundland Banks
 Bahamas
 Cape Cod (Massachusetts)
 Barbuda
 North Carolina
 Dominica
 Georgia, SC, NC
 Honduras
 Louisiana
 NC, coastal Virginia
 CARLA: Texas
 Louisiana
 North-central Atlantic
 Louisiana, MS, Alabama
 Offshore US E coast
 Velasco (Texas)
 Western Atlantic
 US mid-Atlantic coast
 Western Cuba
 St  Marks (Florida)
 Freeport (Texas)
 Puerto Rico
 Near Cape Florida (FL)
 HILDA: Louisiana
 Coastal NB, NY, ME
 ELLA: HAI, CU
 South Carolina
 Northeast Gulf of Mexico
 W Atlantic, US east coast
 Mississippi
 Trinidad, CU, VEN, JAM
 BETSY: GUA, PR
 Cuba, Florida Keys
 Gulf of MX and states
 Southwest Louisiana
 North Carolina, MA
 Western Cuba
 Near Maritime Provinces
 Southeastern Bahamas
 FRAN: Cape Verde Islands
 ALBERTO: Georgia, AL
 Offshore Yucatan
 Jamaica
 EDITH: Nicaragua, Aruba
 GILDA: Honduras
 Indianola (Texas), Cuba
 Virgin Islands
 South Carolina, Florida
 Tobago
 Virgin Islands
 Coastal New England
 Offshore Jamaica (?)
 Texas, Gulf of MX, JAM
 DORA: Mexico
 US mid-Atlantic coast
 NC, SC, offshore Bahamas
 Bahamas, Florida
 Cuba, Alabama
 SW Atlantic, CU
 ANDREW: FL, LA, Bahamas
 SC, offshore NC, GA
 Georgia, South Carolina
 Louisiana
 CONNIE: North Carolina
'''
dict = {'BAH':'Bahamas',
'BAR':'Barbados',
'BEL':'Belize',
'BER':'Bermuda',
'CAN':'Canada',
'CI':'Cayman Islands',
'COL':'Colombia',
'CR':'Costa Rica',
'CU':'Cuba',
'DOM':'Dominica',
'DR':'Dominican Republic',
'GRE':'Grenada',
'GUA':'Guadeloupe',
'HAI':'Haiti',
'HON':'Honduras',
'JAM':'Jamaica',
'MAR':'Martinique',
'MON':'Montserrat',
'MX':'Mexico',
'NIC':'Nicaragua',
'PR':'Puerto Rico',
'STB':'St. Bartholemy',
'STE':'St. Eustatius',
'STK':'St. Kitts',
'STT':'ST. Thomas',
'STV':'St. Vincent',
'TUR':'Turks Islands',
'US':'United States',
'VEN':'Venezuela',
'VI':'Virgin Islands',
    'AL':'Alabama',
'AK':'Alaska',
'AZ':'Arizona',
'AR':'Arkansas',
'CA':'California',
'CO':'Colorado',
'CT':'Connecticut',
'DE':'Delaware',
'FL':'Florida',
'GA':'Georgia',
'HI':'Hawaii',
'ID':'Idaho',
'IL':'Illinois',
'IN':'Indiana',
'IA':'Iowa',
'KS':'Kansas',
'KY':'Kentucky',
'LA':'Louisiana',
'ME':'Maine',
'MD':'Maryland',
'MA':'Massachusetts',
'MI':'Michigan',
'MN':'Minnesota',
'MS':'Mississippi',
'MO':'Missouri',
'MT':'Montana',
'NE':'Nebraska',
'NV':'Nevada',
'NH':'New Hampshire',
'NJ':'New Jersey',
'NM':'New Mexico',
'NY':'New York',
'NC':'North Carolina',
'ND':'North Dakota',
'OH':'Ohio',
'OK':'Oklahoma',
'OR':'Oregon',
'PA':'Pennsylvania',
'RI':'Rhode Island',
'SC':'South Carolina',
'SD':'South Dakota',
'TN':'Tennessee',
'TX':'Texas',
'UT':'Utah',
'VT':'Vermont',
'VA':'Virginia',
'WA':'Washington',
'WV':'West Virginia',
'WI':'Wisconsin',
'WY':'Wyoming'}

text = re.sub('[A-Z].+:','',text)

for key in dict.keys():
    text = re.sub(key,dict[key],text)
print text
