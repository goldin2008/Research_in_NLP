import json
import csv
import os
import re
import sys
import pandas as pd


reload(sys)
sys.setdefaultencoding('utf-8')

def main():    
    with open('info/info_49446.json') as f:
        employee_parsed = json.loads(f.read())

    emp_data = employee_parsed
    # print emp_data['1']

    # open a file for writing
    employ_data = open('info_out.csv', 'w')

    # create the csv writer object
    csvwriter = csv.writer(employ_data)

    # Tillage Practice Terms
    ct = ["Conservation Tillage", "Conservation planting"]
    nt = ["No Tillage", "Direct Seeding", "Slot planting", "Zero till", "Row till", "Slot till", "No till"]
    rt = ["Ridge Tillage"]
    mt = ["Mulch Tillage"]
    st = ["Strip Tillage"]
    rt1 = ["Reduced Tillage", "Reduced till"]
    drt = ["Deep Ripping Tillage"]
    ct2 = ["Conventional Tillage", "Intensive Tillage"]
    ct3 = ["Chisel tillage"]

    # Soil Properties 
    at = ["Aggregate Stability", "Slaking Test", "Aggregation", "Soil water retention"]
    awc = ["Available Water Capacity", "Field Capacity", "Water Content", "Soil Water Content"]
    bd = ["Bulk Density"]
    sm = ["Soil Moisture"]
    c = ["Compaction", "Penetration Resistance", "Rooting Depth"]
    c1 = ["Crusting", "Soil surface crusting", "sealing"]
    shc = ["Saturated Hydraullic Conductivity"]
    p = ["Porosity", "Pore size", "Pore type"]
    ss = ["Soil Structure"]
    ssr = ["Soil Surface Roughness"]
    ir = ["Infiltration Rate"]

    cc = ["Carbon"] #


    tc = ["Total Carbon"]

    oc = ["Organic Carbon"] #
    om = ["Organic Matter"] #

    toc = ["Total Organic Carbon"]
    ec = ["Electrical Conductivity", "Salinity"]
    n = ["Nitrogen"]
    
    tn = ["Total Nitrogen"] #

    p1 = ["Phosphorus"]
    
    tp = ["Total Phosphorus"] #
    pap = ["Plant Available Phosphorus", "soil test P", "dissolved phosphorus"] #

    
    sar = ["Sodium Absorption Ratio"]
    ph = [" pH "]
    hm = ["Heavy Metals"]

    sb = ["Soil Bacteria", "Nitrogen fixing", "Rhizobia", "Bacteria"]
    se = ["Soil Enzymes", "Glues", "Enzyme"]
    e = ["Earthworms"]
    f = ["Fungi", "Arbuscular Mychorrhiza Fungi", "Fungal hyphae", "saprophytic fungi"]
    sm1 = ["Soil Microbes", "Soil microbial community structure", "Soil microbial community composition",
            "Soil biological activity", "Labile Soil Carbon", "Active Soil Carbon"]
    so = ["Soil Oranisms", "Protozoa", "nematodes", "anthropods"]
    mbc = ["Microbial Biomass Carbon", "Biomass C", "Microbial Biomass"]
    bg = ["Beta Glucosidase"]

    y = ["Yield", "Crop Yield", "Forage yield"] #


    # Land Use
    c2 = ["Cropland"]
    p2 = ["Pasture", "Silvopasture"]
    r = ["Rangeland", "Savannahs", "Shrub lands"]
    f1 = ["Forest", "Woodland", "Agroforestry"]
    w = ["Wetland"]

    crp = ["Conservation Reserve Program"] #

    # Crops/Management
    o = ["Organic"]
    r1 = ["Rangeland", "Range"]
    p3 = ["Prairie"]
    g = ["Grassland", "Grass"]
    f2 = ["Forest"]

    # Crops
    Alfalfa = ["Alfalfa"]
    Almonds = ["Almonds"]
    awr = ["Altal Wild Rye"]
    arg = ["Annual Rye Grass"]
    Apple_Trees = ["Apple Trees"]
    Artichokes = ["Artichokes"]
    Asparagus = ["Asparagus"]
    Bananas = ["Bananas"]
    Barley = ["Barley"]
    bbg = ["Big Bluestem Gr"]
    blt = ["Black Locust Trees"]
    Blueberries = ["Blueberries"]
    Broccoli = ["Broccoli"]
    Brome_Grass = ["Brome Grass"]
    Buffalo_Grass = ["Buffalo Grass"]
    Cabbage = ["Cabbage"]
    Camelina = ["Camelina"]
    Canadian_Barley = ["Canadian Barley"]
    Canadian_Oats = ["Canadian Oats"]
    csw = ["Canadian Spring Wheat"]
    Canadian_Sunflowers = ["Canadian Sunflowers"]
    cwp = ["Canadian Winter Pasture"]
    Canola_Argentine = ["Canola Argentine"]
    Canola_Polish = ["Canola Polish"]
    Cantaloupe = ["Cantaloupe"]
    Carrots = ["Carrots"]
    Cashews = ["Cashews"]
    Cauliflower = ["Cauliflower"]
    Celery = ["Celery"]
    Cheat_Grass = ["Cheat Grass"]
    Chickpeas = ["Chickpeas"]
    Citrus_trees = ["Citrus trees"]
    Clover_Alsike = ['Clover Alsike']
    Coastal_Bermuda = ['Coastal Bermuda']
    Cocklebur = ['Cocklebur']
    Coconut = ['Coconut']
    Coffee = ['Coffee']
    Collard_Greens = ['Collard Greens']
    Corn = ['Corn']
    Corn_Silage = ['Corn Silage']
    Cotton_Picker = ['Cotton Picker']
    Cotton_Stripper = ['Cotton Stripper']
    Cowpeas = ['Cowpeas']
    Crambe = ['Crambe']
    cwg = ['Crested Wheat Grass']
    Cucumbers = ['Cucumbers']
    Drybeans = ['Drybeans']
    Duram_Wheat = ['Duram Wheat']
    Eastern_Gamagrass = ['Eastern Gamagrass']
    Eggplant = ['Eggplant']
    Eragrostis_Teff = ['Eragrostis Teff']
    Faba_Beans = ['Faba Beans']
    Fallow = ['Fallow']
    Fescue = ['Fescue']
    Field_Peas = ['Field Peas']
    Flax = ['Flax']
    Forest_Deciduous = ['Forest-Deciduous']
    Forest_Evergreen = ['Forest-Evergreen']
    Forest_Mixed = ['Forest-Mixed']
    Garbanzo_beans = ['Garbanzo beans']
    Garlic = ['Garlic']
    Giant_Foxtail = ['Giant Foxtail']
    Ginseng = ['Ginseng']
    Gladiola = ['Gladiola']
    Grain_Sorghum = ['Grain Sorghum']
    Gramagrass = ['Gramagrass']
    Grape = ['Grape']
    Grarigue = ['Grarigue']
    Green_Beans = ['Green Beans']
    Green_Foxtail = ['Green Foxtail']
    Honey_Mesquite = ['Honey Mesquite']
    Honeydew_Melon = ['Honeydew Melon']
    Horseradish = ['Horseradish']
    Indian_grass = ['Indian grass']
    Johnson_grass = ['Johnson grass']
    Kale = ['Kale']
    Kentucky_Bluegrass = ['Kentucky Bluegrass']
    Lentils = ['Lentils']
    Lettuce = ['Lettuce']
    Lima_Beans = ['Lima Beans']
    lbg = ['Little Bluestem Grass']
    Mesquite_Trees = ['Mesquite Trees']
    Millet = ['Millet']
    Mint = ['Mint']
    Mung_Beans = ['Mung Beans']
    Mustard = ['Mustard']
    nwg = ['Northern Wheat Grass']
    Oak_Tree = ['Oak Tree']
    Oats = ['Oats']
    Oil_Palm = ['Oil Palm']
    Olives = ['Olives']
    Onions = ['Onions']
    octt = ['Orange citrus trees']
    Orchard = ['Orchard']
    Papayas = ['Papayas']
    Peanuts = ['Peanuts']
    Pearl_Millet = ['Pearl Millet']
    Peas = ['Peas']
    Pecans = ['Pecans']
    Peppers = ['Peppers']
    Pine_Trees = ['Pine Trees']
    Pineapple = ['Pineapple']
    Pinto_Beans = ['Pinto Beans']
    Pistachio = ['Pistachio']
    Plaintains = ['Plaintains']
    Poplar_Trees = ['Poplar Trees']
    Potatoes = ['Potatoes']
    Pumpkin = ['Pumpkin']
    Radish = ['Radish']
    Range = ['Range']
    Red_Beets = ['Red Beets']
    Red_Clover = ['Red Clover']
    Rice = ['Rice']
    Rubber_Trees = ['Rubber Trees']
    rwr = ['Russian Wild Rye']
    Rye = ['Rye']
    Ryegrass_Italian = ['Ryegrass Italian']
    Safflower = ['Safflower']
    Sea_Kale = ['Sea Kale']
    Sesbania = ['Sesbania']
    Sideoats = ['Sideoats']
    swg = ['Slender Wheat Grass']
    sbg = ['Smooth Brome Grass']
    Sorghum_Hay = ['Sorghum Hay']
    Soybeans = ['Soybeans']
    Spinach = ['Spinach']
    Spring_Wheat = ['Spring Wheat']
    Strawberries = ['Strawberries']
    Sugarbeets = ['Sugarbeets']
    Sugarcane = ['Sugarcane']
    Summer_Mung = ['Summer Mung']
    Summer_Pasture = ['Summer Pasture']
    Sunflowers = ['Sunflowers']
    Sweet_Clover = ['Sweet Clover']
    Sweet_Corn = ['Sweet Corn']
    Sweet_Potatoes = ['Sweet Potatoes']
    Switchgrass = ['Switchgrass']
    Switchgrass_Alamo = ['Switchgrass Alamo']
    Tall_Fescue = ['Tall Fescue']
    Teff_Grass = ['Teff Grass']
    Timothy = ['Timothy']
    Tobacco = ['Tobacco']
    Tomatillas = ['Tomatillas']
    Tomatoes = ['Tomatoes']
    Triticale = ['Triticale']
    Turnips = ['Turnips']
    Velvetleaf = ['Velvetleaf']
    Walnuts = ['Walnuts']
    Watermelon = ['Watermelon']
    Weeping_Lovegrass = ['Weeping Lovegrass']
    wwg = ['Western Wheat Grass']
    Willow = ['Willow']
    Winter_Pasture = ['Winter Pasture']
    Winter_Peas = ['Winter Peas']
    Winter_Wheat = ['Winter Wheat']
    Buckwheat = ['Buckwheat']
    Oilseed = ['Oilseed']
    ssg = ['Sorghum Sudan grass']
    Hairy_vetch = ['Hairy vetch']
    Crotalaria = ['Crotalaria']

    #Heavy
    Actinium = ["Actinium"]
    Americium = ["Americium"]
    Antimony = ["Antimony"]
    Arsenic = ["Arsenic"]
    Astatine = ["Astatine"]
    Berkelium = ["Berkelium"]
    Bismuth = ["Bismuth"]
    Bohrium	= ["Bohrium"]
    Cadmium	= ["Cadmium"]
    Californium	= ["Californium"]
    Cerium	= ["Cerium"]
    Chromium = ["Chromium"]
    Cobalt = ["Cobalt"]
    Copernicium	= ["Copernicium"]
    Copper	= ["Copper"]
    Curium	= ["Curium"]
    Darmstadtium = ["Darmstadtium"]
    Dubnium	= ["Dubnium"]
    Dysprosium	= ["Dysprosium"]
    Einsteinium	= ["Einsteinium"]
    Erbium	= ["Erbium"]

    Europium = ["Europium"]
    Fermium	= ["Fermium"]
    Flerovium = ["Flerovium"]
    Gadolinium = ["Gadolinium"]
    Gallium	= ["Gallium"]
    Germanium = ["Germanium"]
    Gold = ["Gold"]
    Hafnium	= ["Hafnium"]
    Hassium	= ["Hassium"]
    Holmium	= ["Holmium"]
    Indium	= ["Indium"]
    Iridium	= ["Iridium"]
    Iron = ["Iron"]
    Lanthanum = ["Lanthanum"]
    Lawrencium = ["Lawrencium"]
    Lead = ["Lead"]
    Livermorium	= ["Livermorium"]
    Lutetium = ["Lutetium"]
    Manganese = ["Manganese"]
    Meitnerium = ["Meitnerium"]
    Mendelevium	= ["Mendelevium"]

    Mercury	= ["Mercury"]
    Molybdenum = ["Molybdenum"]
    Moscovium = ["Moscovium"]
    Neodymium = ["Neodymium"]
    Neptunium = ["Neptunium"]
    Nickel = ["Nickel"]
    Nihonium = ["Nihonium"]
    Niobium	= ["Niobium"]
    Nobelium = ["Nobelium"]
    Osmium = ["Osmium"]
    Palladium = ["Palladium"]
    Platinum = ["Platinum"]
    Plutonium = ["Plutonium"]
    Polonium = ["Polonium"]
    Praseodymium = ["Praseodymium"]
    Promethium = ["Promethium"]
    Protactinium = ["Protactinium"]
    Radium = ["Radium"]
    Rhenium	= ["Rhenium"]
    Rhodium	= ["Rhodium"]
    Roentgenium	= ["Roentgenium"]

    Ruthenium = ["Ruthenium"]
    Rutherfordium = ["Rutherfordium"]
    Samarium = ["Samarium"]
    Seaborgium = ["Seaborgium"]
    Silver = ["Silver"]
    Tantalum = ["Tantalum"]
    Technetium = ["Technetium"]
    Tellurium = ["Tellurium"]
    Tennessine = ["Tennessine"]
    Terbium	= ["Terbium"]
    Thallium = ["Thallium"]
    Thorium	= ["Thorium"]
    Thulium	= ["Thulium"]
    Tin	= ["Tin"]
    Tungsten = ["Tungsten"]
    Uranium	= ["Uranium"]
    Vanadium = ["Vanadium"]
    Ytterbium = ["Ytterbium"]
    Zinc = ["Zinc"]
    Zirconium = ["Zirconium"]



    terms = ["ct", "nt", "rt", "mt", "st", "rt1", "drt", "ct2", "ct3", "at", "awc", "bd", "sm", "c", "c1", "shc", "p", 
    "ss", "ssr", "ir", 'cc',
    "tc", 'oc', 'om',
    "toc", "ec", "n", 'tn',
    "p1", 'tp', 'pap',
    "sar", "ph", "hm",
    "sb", "se", "e", "f", "sm1", "so", "mbc", "bg", "y", "c2", "p2", "r", "f1", "w", 'crp',
    "o", "r1", "p3", "g", "f2",
    
    'Alfalfa',
        'Almonds',
        'awr',
        'arg',
        'Apple_Trees',
        'Artichokes',
        'Asparagus',
        'Bananas',
        'Barley',
        'bbg',
        'blt',
        'Blueberries',
        'Broccoli',
        'Brome_Grass',
        'Buffalo_Grass',
        'Cabbage',
        'Camelina',
        'Canadian_Barley',
        'Canadian_Oats',
        'csw',
        'Canadian_Sunflowers',
        'cwp',
        'Canola_Argentine',
        'Canola_Polish',
        'Cantaloupe',
        'Carrots',
        'Cashews',
        'Cauliflower',
        'Celery',
        'Cheat_Grass',
        'Chickpeas',
        'Citrus_trees',
        'Clover_Alsike',
        'Coastal_Bermuda',
        'Cocklebur',
        'Coconut',
        'Coffee',
        'Collard_Greens',
        'Corn',
        'Corn_Silage',
        'Cotton_Picker',
        'Cotton_Stripper',
        'Cowpeas',
        'Crambe',
        'cwg',
        'Cucumbers',
        'Drybeans',
        'Duram_Wheat',
        'Eastern_Gamagrass',
        'Eggplant',
        'Eragrostis_Teff',
        'Faba_Beans',
        'Fallow',
        'Fescue',
        'Field_Peas',
        'Flax',
        'Forest_Deciduous',
        'Forest_Evergreen',
        'Forest_Mixed',
        'Garbanzo_beans',
        'Garlic',
        'Giant_Foxtail',
        'Ginseng',
        'Gladiola',
        'Grain_Sorghum',
        'Gramagrass',
        'Grape',
        'Grarigue',
        'Green_Beans',
        'Green_Foxtail',
        'Honey_Mesquite',
        'Honeydew_Melon',
        'Horseradish',
        'Indian_grass',
        'Johnson_grass',
        'Kale',
        'Kentucky_Bluegrass',
        'Lentils',
        'Lettuce',
        'Lima_Beans',
        'lbg',
        'Mesquite_Trees',
        'Millet',
        'Mint',
        'Mung_Beans',
        'Mustard',
        'nwg',
        'Oak_Tree',
        'Oats',
        'Oil_Palm',
        'Olives',
        'Onions',
        'octt',
        'Orchard',
        'Papayas',
        'Peanuts',
        'Pearl_Millet',
        'Peas',
        'Pecans',
        'Peppers',
        'Pine_Trees',
        'Pineapple',
        'Pinto_Beans',
        'Pistachio',
        'Plaintains',
        'Poplar_Trees',
        'Potatoes',
        'Pumpkin',
        'Radish',
        'Range',
        'Red_Beets',
        'Red_Clover',
        'Rice',
        'Rubber_Trees',
        'rwr',
        'Rye',
        'Ryegrass_Italian',
        'Safflower',
        'Sea_Kale',
        'Sesbania',
        'Sideoats',
        'swg',
        'sbg',
        'Sorghum_Hay',
        'Soybeans',
        'Spinach',
        'Spring_Wheat',
        'Strawberries',
        'Sugarbeets',
        'Sugarcane',
        'Summer_Mung',
        'Summer_Pasture',
        'Sunflowers',
        'Sweet_Clover',
        'Sweet_Corn',
        'Sweet_Potatoes',
        'Switchgrass',
        'Switchgrass_Alamo',
        'Tall_Fescue',
        'Teff_Grass',
        'Timothy',
        'Tobacco',
        'Tomatillas',
        'Tomatoes',
        'Triticale',
        'Turnips',
        'Velvetleaf',
        'Walnuts',
        'Watermelon',
        'Weeping_Lovegrass',
        'wwg',
        'Willow',
        'Winter_Pasture',
        'Winter_Peas',
        'Winter_Wheat',
        'Buckwheat',
        'Oilseed',
        'ssg',
        'Hairy_vetch',
        'Crotalaria',

        "Actinium",
"Americium",
"Antimony",
"Arsenic",
"Astatine",
"Berkelium",
"Bismuth",
"Bohrium",
"Cadmium",
"Californium",
"Cerium",
"Chromium",
"Cobalt",
"Copernicium",
"Copper",
"Curium",
"Darmstadtium",
"Dubnium",
"Dysprosium",
"Einsteinium",
"Erbium",

"Europium",
"Fermium",
"Flerovium",
"Gadolinium",
"Gallium",
"Germanium",
"Gold",
"Hafnium",
"Hassium",
"Holmium",
"Indium",
"Iridium",
"Iron",
"Lanthanum",
"Lawrencium",
"Lead",
"Livermorium",
"Lutetium",
"Manganese",
"Meitnerium",
"Mendelevium",

"Mercury",
"Molybdenum",
"Moscovium",
"Neodymium",
"Neptunium",
"Nickel",
"Nihonium",
"Niobium",
"Nobelium",
"Osmium",
"Palladium",
"Platinum",
"Plutonium",
"Polonium",
"Praseodymium",
"Promethium",
"Protactinium",
"Radium",
"Rhenium",
"Rhodium",
"Roentgenium",

"Ruthenium",
"Rutherfordium",
"Samarium",
"Seaborgium",
"Silver",
"Tantalum",
"Technetium",
"Tellurium",
"Tennessine",
"Terbium",
"Thallium",
"Thorium",
"Thulium",
"Tin",
"Tungsten",
"Uranium",
"Vanadium",
"Ytterbium",
"Zinc",
"Zirconium"
    
     ]

    # print 'ct: ', ct, type(ct)

    csvwriter.writerow(["ID", "Title", "Conservation Tillage", "No Tillage", "Ridge Tillage", "Mulch Tillage",
     "Strip Tillage", "Reduced Tillage", "Deep Ripping Tillage (break up pans)", "Conventional Tillage", "Chisel tillage", 
     "Aggregate Stability", "Available Water Capacity", "Bulk Density", "Soil Moisture", "Compaction", "Crusting", "Saturated Hydraullic Conductivity",
     "Porosity", "Soil Structure", "Soil Surface Roughness", "Infiltration Rate", "Carbon", 
     "Total Carbon", 'Organic Carbon', 'Organic Matter',
     "Total Organic Carbon", "Electrical Conductivity",
     "Nitrogen", 'Total Nitrogen', 
     "Phosphorus", 'Total Phosphorus', 'Plant Available Phosphorus',
     "Sodium Absorption Ratio", "pH", "Heavy Metals", "Soil Bacteria", "Soil Enzymes", "Earthworms", "Fungi", "Soil Microbes",
     "Soil Oranisms", "Microbial Biomass Carbon", "Beta Glucosidase", 'Yield', 
     "Cropland", "Pasture", "Rangeland", "Forest", "Wetland", 'Conservation Reserve Program',
     "Organic", "Rangeland", "Prairie", "Grassland", "Forest",

        'Alfalfa',
        'Almonds',
        'Altal Wild Rye',
        'Annual Rye Grass',
        'Apple Trees',
        'Artichokes',
        'Asparagus',
        'Bananas',
        'Barley',
        'Big Bluestem Gr',
        'Black Locust Trees',
        'Blueberries',
        'Broccoli',
        'Brome Grass',
        'Buffalo Grass',
        'Cabbage',
        'Camelina',
        'Canadian Barley',
        'Canadian Oats',
        'Canadian Spring Wheat',
        'Canadian Sunflowers',
        'Canadian Winter Pasture',
        'Canola Argentine',
        'Canola Polish',
        'Cantaloupe',
        'Carrots',
        'Cashews',
        'Cauliflower',
        'Celery',
        'Cheat Grass',
        'Chickpeas',
        'Citrus trees',
        'Clover Alsike',
        'Coastal Bermuda',
        'Cocklebur',
        'Coconut',
        'Coffee',
        'Collard Greens',
        'Corn',
        'Corn Silage',
        'Cotton Picker',
        'Cotton Stripper',
        'Cowpeas',
        'Crambe',
        'Crested Wheat Grass',
        'Cucumbers',
        'Drybeans',
        'Duram Wheat',
        'Eastern Gamagrass',
        'Eggplant',
        'Eragrostis Teff',
        'Faba Beans',
        'Fallow',
        'Fescue',
        'Field Peas',
        'Flax',
        'Forest-Deciduous',
        'Forest-Evergreen',
        'Forest-Mixed',
        'Garbanzo beans',
        'Garlic',
        'Giant Foxtail',
        'Ginseng',
        'Gladiola',
        'Grain Sorghum',
        'Gramagrass',
        'Grape',
        'Grarigue',
        'Green Beans',
        'Green Foxtail',
        'Honey Mesquite',
        'Honeydew Melon',
        'Horseradish',
        'Indian grass',
        'Johnson grass',
        'Kale',
        'Kentucky Bluegrass',
        'Lentils',
        'Lettuce',
        'Lima Beans',
        'Little Bluestem Grass',
        'Mesquite Trees',
        'Millet',
        'Mint',
        'Mung Beans',
        'Mustard',
        'Northern Wheat Grass',
        'Oak Tree',
        'Oats',
        'Oil Palm',
        'Olives',
        'Onions',
        'Orange citrus trees',
        'Orchard',
        'Papayas',
        'Peanuts',
        'Pearl Millet',
        'Peas',
        'Pecans',
        'Peppers',
        'Pine Trees',
        'Pineapple',
        'Pinto Beans',
        'Pistachio',
        'Plaintains',
        'Poplar Trees',
        'Potatoes',
        'Pumpkin',
        'Radish',
        'Range',
        'Red Beets',
        'Red Clover',
        'Rice',
        'Rubber Trees',
        'Russian Wild Rye',
        'Rye',
        'Ryegrass Italian',
        'Safflower',
        'Sea Kale',
        'Sesbania',
        'Sideoats',
        'Slender Wheat Grass',
        'Smooth Brome Grass',
        'Sorghum Hay',
        'Soybeans',
        'Spinach',
        'Spring Wheat',
        'Strawberries',
        'Sugarbeets',
        'Sugarcane',
        'Summer Mung',
        'Summer Pasture',
        'Sunflowers',
        'Sweet Clover',
        'Sweet Corn',
        'Sweet Potatoes',
        'Switchgrass',
        'Switchgrass Alamo',
        'Tall Fescue',
        'Teff Grass',
        'Timothy',
        'Tobacco',
        'Tomatillas',
        'Tomatoes',
        'Triticale',
        'Turnips',
        'Velvetleaf',
        'Walnuts',
        'Watermelon',
        'Weeping Lovegrass',
        'Western Wheat Grass',
        'Willow',
        'Winter Pasture',
        'Winter Peas',
        'Winter Wheat',
        'Buckwheat',
        'Oilseed',
        'Sorghum Sudan grass',
        'Hairy vetch',
        'Crotalaria',

                "Actinium",
"Americium",
"Antimony",
"Arsenic",
"Astatine",
"Berkelium",
"Bismuth",
"Bohrium",
"Cadmium",
"Californium",
"Cerium",
"Chromium",
"Cobalt",
"Copernicium",
"Copper",
"Curium",
"Darmstadtium",
"Dubnium",
"Dysprosium",
"Einsteinium",
"Erbium",

"Europium",
"Fermium",
"Flerovium",
"Gadolinium",
"Gallium",
"Germanium",
"Gold",
"Hafnium",
"Hassium",
"Holmium",
"Indium",
"Iridium",
"Iron",
"Lanthanum",
"Lawrencium",
"Lead",
"Livermorium",
"Lutetium",
"Manganese",
"Meitnerium",
"Mendelevium",

"Mercury",
"Molybdenum",
"Moscovium",
"Neodymium",
"Neptunium",
"Nickel",
"Nihonium",
"Niobium",
"Nobelium",
"Osmium",
"Palladium",
"Platinum",
"Plutonium",
"Polonium",
"Praseodymium",
"Promethium",
"Protactinium",
"Radium",
"Rhenium",
"Rhodium",
"Roentgenium",

"Ruthenium",
"Rutherfordium",
"Samarium",
"Seaborgium",
"Silver",
"Tantalum",
"Technetium",
"Tellurium",
"Tennessine",
"Terbium",
"Thallium",
"Thorium",
"Thulium",
"Tin",
"Tungsten",
"Uranium",
"Vanadium",
"Ytterbium",
"Zinc",
"Zirconium"
     
     
     
       ])

    # for emp in emp_data:
    #     print emp
    #     exit()

    for emp in emp_data.keys():        
        # title = emp_data[emp]["title"]
        title = emp
        id_ = emp_data[emp]["id"]
        # print emp
        # print type(emp)
        # print title


        ct_flag = 0
        nt_flag = 0
        rt_flag = 0
        mt_flag = 0
        st_flag = 0
        rt1_flag = 0
        drt_flag = 0
        ct2_flag = 0
        ct3_flag = 0

        # Soil Properties
        at_flag = 0
        awc_flag = 0
        bd_flag = 0
        sm_flag = 0
        c_flag = 0
        c1_flag = 0
        shc_flag = 0
        p_flag = 0
        ss_flag = 0
        ssr_flag = 0
        ir_flag = 0

        cc_flag = 0 #

        tc_flag = 0
        oc_flag = 0 #
        om_flag = 0 #


        toc_flag = 0
        ec_flag = 0
        n_flag = 0
        
        tn_flag = 0 #

        p1_flag = 0
        
        tp_flag = 0 #
        pap_flag = 0 #

        sar_flag = 0
        ph_flag = 0
        hm_flag = 0

        sb_flag = 0
        se_flag = 0
        e_flag = 0
        f_flag = 0
        sm1_flag = 0
        so_flag = 0
        mbc_flag = 0
        bg_flag = 0
        y_flag = 0 # 

        # Land Use
        c2_flag = 0
        p2_flag = 0
        r_flag = 0
        f1_flag = 0
        w_flag = 0

        crp_flag = 0 #

        # Crops/Management
        o_flag = 0
        r1_flag = 0
        p3_flag = 0
        g_flag = 0
        f2_flag = 0

        # Crops
        Alfalfa_flag = 0
        Almonds_flag = 0
        awr_flag = 0
        arg_flag = 0
        Apple_Trees_flag = 0
        Artichokes_flag = 0
        Asparagus_flag = 0
        Bananas_flag = 0
        Barley_flag = 0
        bbg_flag = 0
        blt_flag = 0
        Blueberries_flag = 0
        Broccoli_flag = 0
        Brome_Grass_flag = 0
        Buffalo_Grass_flag = 0
        Cabbage_flag = 0
        Camelina_flag = 0
        Canadian_Barley_flag = 0
        Canadian_Oats_flag = 0
        csw_flag = 0
        Canadian_Sunflowers_flag = 0
        cwp_flag = 0
        Canola_Argentine_flag = 0
        Canola_Polish_flag = 0
        Cantaloupe_flag = 0
        Carrots_flag = 0
        Cashews_flag = 0
        Cauliflower_flag = 0
        Celery_flag = 0
        Cheat_Grass_flag = 0
        Chickpeas_flag = 0
        Citrus_trees_flag = 0
        Clover_Alsike_flag = 0
        Coastal_Bermuda_flag = 0
        Cocklebur_flag = 0
        Coconut_flag = 0
        Coffee_flag = 0
        Collard_Greens_flag = 0
        Corn_flag = 0
        Corn_Silage_flag = 0
        Cotton_Picker_flag = 0
        Cotton_Stripper_flag = 0
        Cowpeas_flag = 0
        Crambe_flag = 0
        cwg_flag = 0
        Cucumbers_flag = 0
        Drybeans_flag = 0
        Duram_Wheat_flag = 0
        Eastern_Gamagrass_flag = 0
        Eggplant_flag = 0
        Eragrostis_Teff_flag = 0
        Faba_Beans_flag = 0
        Fallow_flag = 0
        Fescue_flag = 0
        Field_Peas_flag = 0
        Flax_flag = 0
        Forest_Deciduous_flag = 0
        Forest_Evergreen_flag = 0
        Forest_Mixed_flag = 0
        Garbanzo_beans_flag = 0
        Garlic_flag = 0
        Giant_Foxtail_flag = 0
        Ginseng_flag = 0
        Gladiola_flag = 0
        Grain_Sorghum_flag = 0
        Gramagrass_flag = 0
        Grape_flag = 0
        Grarigue_flag = 0
        Green_Beans_flag = 0
        Green_Foxtail_flag = 0
        Honey_Mesquite_flag = 0
        Honeydew_Melon_flag = 0
        Horseradish_flag = 0
        Indian_grass_flag = 0
        Johnson_grass_flag = 0
        Kale_flag = 0
        Kentucky_Bluegrass_flag = 0
        Lentils_flag = 0
        Lettuce_flag = 0
        Lima_Beans_flag = 0
        lbg_flag = 0
        Mesquite_Trees_flag = 0
        Millet_flag = 0
        Mint_flag = 0
        Mung_Beans_flag = 0
        Mustard_flag = 0
        nwg_flag = 0
        Oak_Tree_flag = 0
        Oats_flag = 0
        Oil_Palm_flag = 0
        Olives_flag = 0
        Onions_flag = 0
        octt_flag = 0
        Orchard_flag = 0
        Papayas_flag = 0
        Peanuts_flag = 0
        Pearl_Millet_flag = 0
        Peas_flag = 0
        Pecans_flag = 0
        Peppers_flag = 0
        Pine_Trees_flag = 0
        Pineapple_flag = 0
        Pinto_Beans_flag = 0
        Pistachio_flag = 0
        Plaintains_flag = 0
        Poplar_Trees_flag = 0
        Potatoes_flag = 0
        Pumpkin_flag = 0
        Radish_flag = 0
        Range_flag = 0
        Red_Beets_flag = 0
        Red_Clover_flag = 0
        Rice_flag = 0
        Rubber_Trees_flag = 0
        rwr_flag = 0
        Rye_flag = 0
        Ryegrass_Italian_flag = 0
        Safflower_flag = 0
        Sea_Kale_flag = 0
        Sesbania_flag = 0
        Sideoats_flag = 0
        swg_flag = 0
        sbg_flag = 0
        Sorghum_Hay_flag = 0
        Soybeans_flag = 0
        Spinach_flag = 0
        Spring_Wheat_flag = 0
        Strawberries_flag = 0
        Sugarbeets_flag = 0
        Sugarcane_flag = 0
        Summer_Mung_flag = 0
        Summer_Pasture_flag = 0
        Sunflowers_flag = 0
        Sweet_Clover_flag = 0
        Sweet_Corn_flag = 0
        Sweet_Potatoes_flag = 0
        Switchgrass_flag = 0
        Switchgrass_Alamo_flag = 0
        Tall_Fescue_flag = 0
        Teff_Grass_flag = 0
        Timothy_flag = 0
        Tobacco_flag = 0
        Tomatillas_flag = 0
        Tomatoes_flag = 0
        Triticale_flag = 0
        Turnips_flag = 0
        Velvetleaf_flag = 0
        Walnuts_flag = 0
        Watermelon_flag = 0
        Weeping_Lovegrass_flag = 0
        wwg_flag = 0
        Willow_flag = 0
        Winter_Pasture_flag = 0
        Winter_Peas_flag = 0
        Winter_Wheat_flag = 0
        Buckwheat_flag = 0
        Oilseed_flag = 0
        ssg_flag = 0
        Hairy_vetch_flag = 0
        Crotalaria_flag = 0
        #Heavy
        Actinium_flag = 0
        Americium_flag = 0
        Antimony_flag = 0
        Arsenic_flag = 0
        Astatine_flag = 0
        Berkelium_flag = 0
        Bismuth_flag = 0
        Bohrium_flag = 0
        Cadmium_flag = 0
        Californium_flag = 0
        Cerium_flag = 0
        Chromium_flag = 0
        Cobalt_flag = 0
        Copernicium_flag = 0
        Copper_flag = 0
        Curium_flag = 0
        Darmstadtium_flag = 0
        Dubnium_flag = 0
        Dysprosium_flag = 0
        Einsteinium_flag = 0
        Erbium_flag = 0

        Europium_flag = 0
        Fermium_flag = 0
        Flerovium_flag = 0
        Gadolinium_flag = 0
        Gallium_flag = 0
        Germanium_flag = 0
        Gold_flag = 0
        Hafnium_flag = 0
        Hassium_flag = 0
        Holmium_flag = 0
        Indium_flag = 0
        Iridium_flag = 0
        Iron_flag = 0
        Lanthanum_flag = 0
        Lawrencium_flag = 0
        Lead_flag = 0
        Livermorium_flag = 0
        Lutetium_flag = 0
        Manganese_flag = 0
        Meitnerium_flag = 0
        Mendelevium_flag = 0

        Mercury_flag = 0
        Molybdenum_flag = 0
        Moscovium_flag = 0
        Neodymium_flag = 0
        Neptunium_flag = 0
        Nickel_flag = 0
        Nihonium_flag = 0
        Niobium_flag = 0
        Nobelium_flag = 0
        Osmium_flag = 0
        Palladium_flag = 0
        Platinum_flag = 0
        Plutonium_flag = 0
        Polonium_flag = 0
        Praseodymium_flag = 0
        Promethium_flag = 0
        Protactinium_flag = 0
        Radium_flag = 0
        Rhenium_flag = 0
        Rhodium_flag = 0
        Roentgenium_flag = 0

        Ruthenium_flag = 0
        Rutherfordium_flag = 0
        Samarium_flag = 0
        Seaborgium_flag = 0
        Silver_flag = 0
        Tantalum_flag = 0
        Technetium_flag = 0
        Tellurium_flag = 0
        Tennessine_flag = 0
        Terbium_flag = 0
        Thallium_flag = 0
        Thorium_flag = 0
        Thulium_flag = 0
        Tin_flag = 0
        Tungsten_flag = 0
        Uranium_flag = 0
        Vanadium_flag = 0
        Ytterbium_flag = 0
        Zinc_flag = 0
        Zirconium_flag = 0

        flags = [ct_flag, nt_flag, rt_flag, mt_flag, st_flag, rt1_flag, drt_flag, ct2_flag, ct3_flag, at_flag, awc_flag, 
        bd_flag, sm_flag, c_flag, c1_flag, shc_flag, p_flag, ss_flag, ssr_flag, ir_flag, cc_flag,
        tc_flag, oc_flag, om_flag,
        toc_flag, ec_flag, 
        n_flag, tn_flag,
        p1_flag, tp_flag, pap_flag,
        sar_flag, ph_flag, hm_flag,
        sb_flag, se_flag, e_flag, f_flag, sm1_flag, so_flag, mbc_flag, bg_flag, y_flag, c2_flag, p2_flag, r_flag, f1_flag, w_flag, 
        crp_flag,
        o_flag, r1_flag, p3_flag, g_flag, f2_flag,
        
        
        Alfalfa_flag,
        Almonds_flag ,
        awr_flag ,
        arg_flag ,
        Apple_Trees_flag ,
        Artichokes_flag ,
        Asparagus_flag ,
        Bananas_flag ,
        Barley_flag ,
        bbg_flag ,
        blt_flag ,
        Blueberries_flag ,
        Broccoli_flag ,
        Brome_Grass_flag ,
        Buffalo_Grass_flag ,
        Cabbage_flag ,
        Camelina_flag ,
        Canadian_Barley_flag ,
        Canadian_Oats_flag ,
        csw_flag ,
        Canadian_Sunflowers_flag ,
        cwp_flag ,
        Canola_Argentine_flag ,
        Canola_Polish_flag ,
        Cantaloupe_flag ,
        Carrots_flag ,
        Cashews_flag ,
        Cauliflower_flag ,
        Celery_flag ,
        Cheat_Grass_flag ,
        Chickpeas_flag ,
        Citrus_trees_flag ,
        Clover_Alsike_flag ,
        Coastal_Bermuda_flag ,
        Cocklebur_flag ,
        Coconut_flag ,
        Coffee_flag ,
        Collard_Greens_flag ,
        Corn_flag ,
        Corn_Silage_flag ,
        Cotton_Picker_flag ,
        Cotton_Stripper_flag ,
        Cowpeas_flag ,
        Crambe_flag ,
        cwg_flag ,
        Cucumbers_flag ,
        Drybeans_flag ,
        Duram_Wheat_flag ,
        Eastern_Gamagrass_flag ,
        Eggplant_flag ,
        Eragrostis_Teff_flag ,
        Faba_Beans_flag ,
        Fallow_flag ,
        Fescue_flag ,
        Field_Peas_flag ,
        Flax_flag ,
        Forest_Deciduous_flag ,
        Forest_Evergreen_flag ,
        Forest_Mixed_flag ,
        Garbanzo_beans_flag ,
        Garlic_flag ,
        Giant_Foxtail_flag ,
        Ginseng_flag ,
        Gladiola_flag ,
        Grain_Sorghum_flag ,
        Gramagrass_flag ,
        Grape_flag ,
        Grarigue_flag ,
        Green_Beans_flag ,
        Green_Foxtail_flag ,
        Honey_Mesquite_flag ,
        Honeydew_Melon_flag ,
        Horseradish_flag ,
        Indian_grass_flag ,
        Johnson_grass_flag ,
        Kale_flag ,
        Kentucky_Bluegrass_flag ,
        Lentils_flag ,
        Lettuce_flag ,
        Lima_Beans_flag ,
        lbg_flag ,
        Mesquite_Trees_flag ,
        Millet_flag ,
        Mint_flag ,
        Mung_Beans_flag ,
        Mustard_flag ,
        nwg_flag ,
        Oak_Tree_flag ,
        Oats_flag ,
        Oil_Palm_flag ,
        Olives_flag ,
        Onions_flag ,
        octt_flag ,
        Orchard_flag ,
        Papayas_flag ,
        Peanuts_flag ,
        Pearl_Millet_flag ,
        Peas_flag ,
        Pecans_flag ,
        Peppers_flag ,
        Pine_Trees_flag ,
        Pineapple_flag ,
        Pinto_Beans_flag ,
        Pistachio_flag ,
        Plaintains_flag ,
        Poplar_Trees_flag ,
        Potatoes_flag ,
        Pumpkin_flag ,
        Radish_flag ,
        Range_flag ,
        Red_Beets_flag ,
        Red_Clover_flag ,
        Rice_flag ,
        Rubber_Trees_flag ,
        rwr_flag ,
        Rye_flag ,
        Ryegrass_Italian_flag ,
        Safflower_flag ,
        Sea_Kale_flag ,
        Sesbania_flag ,
        Sideoats_flag ,
        swg_flag ,
        sbg_flag ,
        Sorghum_Hay_flag ,
        Soybeans_flag ,
        Spinach_flag ,
        Spring_Wheat_flag ,
        Strawberries_flag ,
        Sugarbeets_flag ,
        Sugarcane_flag ,
        Summer_Mung_flag ,
        Summer_Pasture_flag ,
        Sunflowers_flag ,
        Sweet_Clover_flag ,
        Sweet_Corn_flag ,
        Sweet_Potatoes_flag ,
        Switchgrass_flag ,
        Switchgrass_Alamo_flag ,
        Tall_Fescue_flag ,
        Teff_Grass_flag ,
        Timothy_flag ,
        Tobacco_flag ,
        Tomatillas_flag ,
        Tomatoes_flag ,
        Triticale_flag ,
        Turnips_flag ,
        Velvetleaf_flag ,
        Walnuts_flag ,
        Watermelon_flag ,
        Weeping_Lovegrass_flag ,
        wwg_flag ,
        Willow_flag ,
        Winter_Pasture_flag,
        Winter_Peas_flag,
        Winter_Wheat_flag,
        Buckwheat_flag,
        Oilseed_flag,
        ssg_flag,
        Hairy_vetch_flag,
        Crotalaria_flag,

        Actinium_flag,
Americium_flag,
Antimony_flag,
Arsenic_flag,
Astatine_flag,
Berkelium_flag,
Bismuth_flag,
Bohrium_flag,
Cadmium_flag,
Californium_flag,
Cerium_flag,
Chromium_flag,
Cobalt_flag,
Copernicium_flag,
Copper_flag,
Curium_flag,
Darmstadtium_flag,
Dubnium_flag,
Dysprosium_flag,
Einsteinium_flag,
Erbium_flag,

Europium_flag,
Fermium_flag,
Flerovium_flag,
Gadolinium_flag,
Gallium_flag,
Germanium_flag,
Gold_flag,
Hafnium_flag,
Hassium_flag,
Holmium_flag,
Indium_flag,
Iridium_flag,
Iron_flag,
Lanthanum_flag,
Lawrencium_flag,
Lead_flag,
Livermorium_flag,
Lutetium_flag,
Manganese_flag,
Meitnerium_flag,
Mendelevium_flag,

Mercury_flag,
Molybdenum_flag,
Moscovium_flag,
Neodymium_flag,
Neptunium_flag,
Nickel_flag,
Nihonium_flag,
Niobium_flag,
Nobelium_flag,
Osmium_flag,
Palladium_flag,
Platinum_flag,
Plutonium_flag,
Polonium_flag,
Praseodymium_flag,
Promethium_flag,
Protactinium_flag,
Radium_flag,
Rhenium_flag,
Rhodium_flag,
Roentgenium_flag,

Ruthenium_flag,
Rutherfordium_flag,
Samarium_flag,
Seaborgium_flag,
Silver_flag,
Tantalum_flag,
Technetium_flag,
Tellurium_flag,
Tennessine_flag,
Terbium_flag,
Thallium_flag,
Thorium_flag,
Thulium_flag,
Tin_flag,
Tungsten_flag,
Uranium_flag,
Vanadium_flag,
Ytterbium_flag,
Zinc_flag,
Zirconium_flag

        
         ]

        title_r = title.replace(':', '-').rstrip()
        title_r = title_r.replace('"', '')
        file_name = os.path.join('corpus/', title_r + '.pdf.txt')
        # print file_name
        # print "ID : ", emp
        if os.path.exists(file_name):
            print "FOUND ", id_
            with open(file_name) as f:
                content = f.read()    
                for t in terms:
                    # print t, type(t)
                    # var = eval(t)
                    # print var
                    index = terms.index(t)
                    # print "index: ", index
                    name = t + '_flag'
                    # print name, type(name)
                    flag = eval(name)
                    # print flag, type(flag) 
                    for each in eval(t):
                        for m in re.finditer(each, content):
                            if m :
                                flags[index] = 1
                        for m in re.finditer(each.lower(), content.lower()):
                            if m :
                                flags[index] = 1
                                
                # print( 'flags: ', flags )
                csvwriter.writerow([id_, title.replace(',', '')] + flags)

        else:
            # print "NOT FOUND"
            pass

    employ_data.close()


if __name__ == "__main__":
    main()
