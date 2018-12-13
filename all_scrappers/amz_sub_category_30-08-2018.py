# -*- coding: utf-8 -*-
import scrapy
import urllib
from pymongo import MongoClient
import os
import time
import re
import json
from scrapy.conf import settings
class AmazonItem(scrapy.Item):
    url = scrapy.Field()
    category = scrapy.Field()


class amazonSpider(scrapy.Spider):
    imgcount = 1
    name = "amz_sub_category_30-08-2018"
    allowed_domains = []

    start_urls = ["http://www.flipkart.com/search?q=9780005996218"]  

    def parse(self,response):
        urls_done = [
]
        urls=[
["2","Sofas & Couches","https://www.amazon.com/Sofas-and-Couches/b?ie=UTF8&node=3733551"],
["3","Home Office Desk Chairs","https://www.amazon.com/Home-Office-Desk-Chairs/b?ie=UTF8&node=3733721"],
["4","Beds","https://www.amazon.com/Beds/b?ie=UTF8&node=3248804011"],
["5","Table & Chair Sets","https://www.amazon.com/Table-and-Chair-Sets/b?ie=UTF8&node=8566630011"],
["6","Mattresses","https://www.amazon.com/Mattresses/b?ie=UTF8&node=3732981"],
["7","Area Rugs, Runners & Pads","https://www.amazon.com/area-rugs-runners-pads/b?ie=UTF8&node=1063298"],
["8","Living Room Tables","https://www.amazon.com/Living-Room-Tables/b?ie=UTF8&node=680098011"],
["9","Nightstands","https://www.amazon.com/Nightstands/b?ie=UTF8&node=3733251"],
["10","Coastal Vibes: Kids' Room","https://www.amazon.com/b?ie=UTF8&node=17733374011"],
["11","Patio Furniture Sets","https://www.amazon.com/Patio-Furniture-Sets/b?ie=UTF8&node=3742441"],
["12","Casual accent chairs","https://www.amazon.com/b?ie=UTF8&node=17732894011"],
["13","TV & Media Furniture","https://www.amazon.com/TV-and-Media-Furniture/b?ie=UTF8&node=1063310"],
["14","Coastal Vibes: Living Room","https://www.amazon.com/b?ie=UTF8&node=17733371011"],
["15","Home Office Desks","https://www.amazon.com/Home-Office-Desks/b?ie=UTF8&node=3733671"],
["16","Living Room Chairs","https://www.amazon.com/Living-Room-Chairs/b?ie=UTF8&node=3733491"],
["17","Desert Modern Outdoor Living","https://www.amazon.com/b?ie=UTF8&node=17701288011"],
["18","Desert Modern Living Room","https://www.amazon.com/b?ie=UTF8&node=17701284011"],
["19","Desert Modern Entertaining","https://www.amazon.com/b?ie=UTF8&node=17701285011"],
["20","Coastal Vibes: Design Recipe","https://www.amazon.com/b?ie=UTF8&node=17739089011"],
["21","Candles","https://www.amazon.com/candles/b?ie=UTF8&node=3734391"],
["22","Coastal Vibes: Natural Woven Rugs","https://www.amazon.com/b?ie=UTF8&node=17736594011"],
["23","Coastal Vibes: Indigo Accents","https://www.amazon.com/b?ie=UTF8&node=17732879011"],
["24","Home Fragrance","https://www.amazon.com/home-fragrance/b?ie=UTF8&node=3734741"],
["25","Vases","https://www.amazon.com/vases/b?ie=UTF8&node=3745451"],
["26","Throw Blankets","https://www.amazon.com/throws/b?ie=UTF8&node=14058581"],
["27","Clocks","https://www.amazon.com/clocks/b?ie=UTF8&node=542938"],
["28","Floating Shelves","https://www.amazon.com/floating-shelves/b?ie=UTF8&node=3743991"],
["29","Curtains","https://www.amazon.com/draperies-curtains/b?ie=UTF8&node=3736141"],
["30","Lighting & Ceiling Fans","https://www.amazon.com/Lighting-26-Ceiling-Fans/b?ie=UTF8&node=495224"],
["31","Decorative Pillows, Inserts & Covers","https://www.amazon.com/decorative-pillows-inserts-covers/b?ie=UTF8&node=1063262"],
["32","Kitchen Sink Faucets","https://www.amazon.com/faucets-Kitchen-Sink/s?ie=UTF8&page=1&rh=n%3A3754311%2Ck%3Afaucets"],
["33","Medicine Balls","https://www.amazon.com/medicine-ball/b?ie=UTF8&node=3408001"],
["34","Island lights","https://www.amazon.com/Island-Lights/b?ie=UTF8&node=5486418011"],
["35","Pulls","https://www.amazon.com/pulls-Cabinet-Hardware/s?ie=UTF8&page=1&rh=n%3A511260%2Ck%3Apulls"],
["36","Vacuums","https://www.amazon.com/vacuums/b?ie=UTF8&node=3743521"],
["37","Area Rugs","https://www.amazon.com/area-rugs/b?ie=UTF8&node=684541011"],
["38","Drying Rack","https://www.amazon.com/laundry-drying-racks/b?ie=UTF8&node=695488011"],
["39","Door Hardware & Locks","https://www.amazon.com/door-knob-levers-Hardware-Locks/s?ie=UTF8&page=1&rh=n%3A511276%2Ck%3Adoor%20knob%20and%20levers"],
["40","Ceiling Fans","https://www.amazon.com/Ceiling-Fans/b?ie=UTF8&node=404433011"],
["41","Kids' Blankets","https://www.amazon.com/kids-blankets/b?ie=UTF8&node=362533011"],
["42","Baby","https://www.amazon.com/crib-sheets-Baby-Brand-4-selected/s?ie=UTF8&page=1&rh=n%3A165796011%2Ck%3Acrib%20sheets%2Cp_6%3AATVPDKIKX0DER%2Cp_89%3AAmazonBasics%7CBedtime%20Originals%7CBurt%27s%20Bees%20Baby%7CPinzon%20by%20Amazon"],
["43","Kids' Sheets & Pillowcases","https://www.amazon.com/kids-sheets-pillowcases/b?ie=UTF8&node=13750161"],
["44","Kids' Comforter Sets","https://www.amazon.com/kids-comforter-sets/b?ie=UTF8&node=10671054011"],
["45","Mattresses","https://www.amazon.com/Nursery-Bed-Mattresses/b?ie=UTF8&node=166817011"],
["46","The Baby Store","https://www.amazon.com/baby-car-seats-strollers-bedding/b?ie=UTF8&node=165796011"],
["47","Nursery","https://www.amazon.com/baby-nursery-bedding-cribs-furniture/b?ie=UTF8&node=695338011"],
["48","Cribs & Nursery Beds","https://www.amazon.com/Cribs-Furniture/b?ie=UTF8&node=166812011"],
["49","Melissa & Doug","https://www.amazon.com/Melissa-Doug-Toys-Games/b?ie=UTF8&node=11095706011"],
["50","Cabinet & Drawer Organization","https://www.amazon.com/kitchen-cabinet-drawer-organization/b?ie=UTF8&node=3743971"],
["51","Toys & Games","https://www.amazon.com/magformers-Toys-Games/s?ie=UTF8&page=1&rh=n%3A165793011%2Ck%3Amagformers"],
["52","Small Appliances","https://www.amazon.com/kitchen-small-appliances/b?ie=UTF8&node=289913"],
["53","Leapfrog- Encourage a Love of Learning","https://www.amazon.com/b?ie=UTF8&node=11153921011"],
["54","Disney Favorites","https://www.amazon.com/b?ie=UTF8&node=17386931011"],
["55","Toys & Games","https://www.amazon.com/play-doh-Toys-Games/s?ie=UTF8&page=1&rh=n%3A165793011%2Ck%3Aplay%20doh"],
["56","Video Games","https://www.amazon.com/Kids-Family-Video-Games/b?ie=UTF8&node=8794716011"],
["57","Stuffed Animals & Plush Toys","https://www.amazon.com/kids-stuffed-animals-toys/b?ie=UTF8&node=166461011"],
["58","STEM Toys","https://www.amazon.com/b?ie=UTF8&node=14725559011"],
["59","Sports & Outdoor Play","https://www.amazon.com/outdoor-toys-kids-play/b?ie=UTF8&node=166420011"],
["60","Tricycles, Scooters & Wagons","https://www.amazon.com/kids-bikes-skates-rideons-scooter-skateboard/b?ie=UTF8&node=256994011"],
["61","Toy Remote Control & Play Vehicles","https://www.amazon.com/kids-play-vehicles-die-cast/b?ie=UTF8&node=166508011"],
["62","Grown-Up Toys","https://www.amazon.com/Grown-Up-Toys/b?ie=UTF8&node=3226142011"],
["63","Hobbies","https://www.amazon.com/kids-hobbies-coins-models/b?ie=UTF8&node=276729011"],
["64","Games","https://www.amazon.com/kids-games-board-classic-dvd-travel/b?ie=UTF8&node=166220011"],
["65","Dress Up & Pretend Play","https://www.amazon.com/Costumes-Pretend-Play/b?ie=UTF8&node=166316011"],
["66","Building Toys","https://www.amazon.com/kids-construction-blocks-models-building-sets/b?ie=UTF8&node=166092011"],
["67","Dolls & Accessories","https://www.amazon.com/kids-toys-dolls-accessories/b?ie=UTF8&node=166118011"],
["68","Choose your champion, WWE Summer Slam is around the corner","https://www.amazon.com/b?ie=UTF8&node=17923675011"],
["69","Amazon Exclusive Movie and TV Toys","https://www.amazon.com/b?ie=UTF8&node=17728828011"],
["70","Prime Exclusive Phones","https://www.amazon.com/Prime-Exclusive-Phones/b?ie=UTF8&node=14613304011"],
["71","Amazon Devices","https://www.amazon.com/Amazon-Devices/b?ie=UTF8&node=2102313011"],
["72","K-12 Store","https://www.amazon.com/b?ie=UTF8&node=17608673011"],
["73","Girls' Back-to-School Essentials","https://www.amazon.com/b?ie=UTF8&node=17862645011"],
["74","Boys' Back-to-School Essentials","https://www.amazon.com/b?ie=UTF8&node=17862646011"],
["75","Home Gift Guide: Featured Brita, Clorox, & GLAD Products","https://www.amazon.com/b?ie=UTF8&node=17874140011"],
["76","Home Gift Guide: Featured Bath & Personal Care Products","https://www.amazon.com/b?ie=UTF8&node=17874139011"],
["77","Home Gift Guide: Featured Clorox Products","https://www.amazon.com/b?ie=UTF8&node=17874141011"],
["78","Home Gift Guide: Featured Black+Decker Products","https://www.amazon.com/b?ie=UTF8&node=17324658011"],
["79","Home Gift Guide: Featured Ninja Products","https://www.amazon.com/b?ie=UTF8&node=16786441011"],
["80","Home Gift Guide: Featured DYMO Products","https://www.amazon.com/b?ie=UTF8&node=17874192011"],
["81","Home Gift Guide: Featured Newell Products","https://www.amazon.com/b?ie=UTF8&node=17874191011"],
["82","Home Gift Guide: Featured ACCO Products","https://www.amazon.com/b?ie=UTF8&node=17874142011"],
["83","Home Gift Guide: Featured HP Products","https://www.amazon.com/b?ie=UTF8&node=17716255011"],
["84","Home Gift Guide: Featured Instant Pot Products","https://www.amazon.com/b?ie=UTF8&node=17324664011"],
["85","Home Gift Guide: Featured products by Rivet","https://www.amazon.com/b?ie=UTF8&node=17719895011"],
["86","Home Gift Guide: Featured Zinus Products","https://www.amazon.com/b?ie=UTF8&node=15578318011"],
["87","Home Gift Guide: Featured Dyson Products","https://www.amazon.com/b?ie=UTF8&node=16786440011"],
["88","Home Gift Guide: Featured Bissell Products","https://www.amazon.com/b?ie=UTF8&node=10161523011"],
["89","Home Gift Guide: Featured iRobot Products","https://www.amazon.com/b?ie=UTF8&node=17716241011"],
["90","Women's Off-to-College Essentials","https://www.amazon.com/b?ie=UTF8&node=17862647011"],
["91","Men's Off-to-College Essentials","https://www.amazon.com/b?ie=UTF8&node=17862648011"],
["92","Home Gift Guide: Featured Shark Products","https://www.amazon.com/b?ie=UTF8&node=17324659011"],
["93","Home Gift Guide: Featured Black & Decker Vacuums","https://www.amazon.com/b?ie=UTF8&node=17886609011"],
["94","Home Gift Guide: Featured Rowenta Products","https://www.amazon.com/b?ie=UTF8&node=16977389011"],
["95","Toys & Games","https://www.amazon.com/justice-league-Toys-Games-Amazon-com/s?ie=UTF8&field-enc-merchantbin=ATVPDKIKX0DER&page=1&rh=n%3A165793011%2Ck%3Ajustice%20league"],
["96","Toys & Games","https://www.amazon.com/harry-potter-Toys-Games-Amazon-com/s?ie=UTF8&field-enc-merchantbin=ATVPDKIKX0DER&page=1&rh=n%3A165793011%2Ck%3Aharry%20potter"],
["97","Test Prep & Study Guides","https://www.amazon.com/Test-Prep-Study-Guides/b?ie=UTF8&node=684300011"],
["98","Social Sciences","https://www.amazon.com/Social-Sciences-Books/b?ie=UTF8&node=468214"],
["99","Medicine & Health Sciences","https://www.amazon.com/Medicine-New-Used-Textbooks-Books/b?ie=UTF8&node=468228"],
["100","Science & Mathematics","https://www.amazon.com/Sciences-New-Used-Textbooks-Books/b?ie=UTF8&node=468216"],
["101","Reference","https://www.amazon.com/Reference/b?ie=UTF8&node=684283011"],
["102","Humanities","https://www.amazon.com/Humanities-New-Used-Textbooks-Books/b?ie=UTF8&node=468206"],
["103","Education","https://www.amazon.com/Education-New-Used-Textbooks-Books/b?ie=UTF8&node=468224"],
["104","Law","https://www.amazon.com/Law-New-Used-Textbooks-Books/b?ie=UTF8&node=468222"],
["105","Engineering","https://www.amazon.com/Engineering-New-Used-Textbooks-Books/b?ie=UTF8&node=468212"],
["106","Communication & Journalism","https://www.amazon.com/Communications-Humanities-Books/b?ie=UTF8&node=468226"],
["107","Computer Science","https://www.amazon.com/Computer-Science-Information-Systems-Books/b?ie=UTF8&node=468204"],
["108","Business & Finance","https://www.amazon.com/Business-Finance-Books/b?ie=UTF8&node=468220"],
["109","Books Back to School Promotion*","https://www.amazon.com/b?ie=UTF8&node=13431611011"],
["110","Arts & Crafts","https://www.amazon.com/kids-arts-crafts-easel-paper-marker-stamp/b?ie=UTF8&node=166057011"],
["111","New Fall Toys from Fisher-Price","https://www.amazon.com/b?ie=UTF8&node=17924401011"],
["112","Preschool Amazon Exclusives","https://www.amazon.com/b?ie=UTF8&node=17506220011"],
["113","Action Figures & Statues","https://www.amazon.com/kids-toys-action-figures-accessories/b?ie=UTF8&node=165993011"],
["114","14 Years & Up","https://www.amazon.com/Toys-Games-14-Years-Up/s?ie=UTF8&page=1&rh=n%3A165793011%2Cp_n_age_range%3A5442388011"],
["115","5 to 7 Years","https://www.amazon.com/Toys-Games-5-7-Years/s?ie=UTF8&page=1&rh=n%3A165793011%2Cp_n_age_range%3A165936011"],
["116","8 to 13 Years","https://www.amazon.com/Toys-Games-8-13-Years/s?ie=UTF8&page=1&rh=n%3A165793011%2Cp_n_age_range%3A5442387011"],
["117","2 to 4 Years","https://www.amazon.com/Toys-Games-2-4-Years/s?ie=UTF8&page=1&rh=n%3A165793011%2Cp_n_age_range%3A165890011"],
["118","Birth to 24 Months","https://www.amazon.com/Toys-Games-Birth-24-Months/s?ie=UTF8&page=1&rh=n%3A165793011%2Cp_n_age_range%3A165813011"],
["119","Polly is back!  New Dolls from Polly Pocket","https://www.amazon.com/b?ie=UTF8&node=17923674011"],
["120","Coffee Makers","https://www.amazon.com/Coffee-Makers/b?ie=UTF8&node=7740213011"],
["121","Blenders","https://www.amazon.com/blenders/b?ie=UTF8&node=289914"],
["122","Mixing Bowls","https://www.amazon.com/Mixing-Bowls/b?ie=UTF8&node=289696"],
["123","Household Stand Mixers","https://www.amazon.com/Stand-Mixers-Small-Appliances-Kitchen/b?ie=UTF8&node=289932"],
["124","Cake Pans","https://www.amazon.com/cake-pans/b?ie=UTF8&node=289679"],
["125","Baking & Cookie Sheets","https://www.amazon.com/baking-cookie-sheets/b?ie=UTF8&node=289674"],
["126","Saucepans","https://www.amazon.com/Saucepans-Cookware-Baking-Kitchen/b?ie=UTF8&node=289827"],
["127","Dutch Ovens","https://www.amazon.com/dutch-ovens/b?ie=UTF8&node=289818"],
["128","Kitchen Cookware Sets","https://www.amazon.com/cookware-sets/b?ie=UTF8&node=289816"],
["129","Bakeware Sets","https://www.amazon.com/bakeware-sets/b?ie=UTF8&node=289669"],
["130","Skillets","https://www.amazon.com/Skillets-Cookware-Baking-Kitchen-Dining/b?ie=UTF8&node=289829"],
["131","Flatware Sets","https://www.amazon.com/Flatware-Sets-Tableware-Kitchen-Dining/b?ie=UTF8&node=367232011"],
["132","Glassware & Drinkware","https://www.amazon.com/glassware/b?ie=UTF8&node=13217501"],
["133","Bowls","https://www.amazon.com/Bowls/b?ie=UTF8&node=367107011"],
["134","Dinnerware Sets","https://www.amazon.com/dinnerware-sets/b?ie=UTF8&node=367146011"],
["135","living room ceiling lights","https://www.amazon.com/living-room-ceiling-lights/s?ie=UTF8&page=1&rh=i%3Aaps%2Ck%3Aliving%20room%20ceiling%20lights"],
["136","Storage Containers","https://www.amazon.com/baskets-bins-containers/b?ie=UTF8&node=2422430011"],
["137","Blankets & Throws","https://www.amazon.com/blankets-throws/b?ie=UTF8&node=1063280"],
["138","Wall Art","https://www.amazon.com/artwork/b?ie=UTF8&node=3736081"],
["139","TV Stands","https://www.amazon.com/TV-Stands/b?ie=UTF8&node=14109851"],
["140","Coffee Tables","https://www.amazon.com/Coffee-Tables/b?ie=UTF8&node=3733631"],
["141","Throw Pillows","https://www.amazon.com/throw-pillows/b?ie=UTF8&node=3732321"],
["142","Ceiling Lights","https://www.amazon.com/entryway-Ceiling-Lights-Lighting-Fans/s?ie=UTF8&hidden-keywords=entryway&page=1&rh=n%3A5486428011%2Ck%3Aentryway"],
["143","Storage & Organization","https://www.amazon.com/coat-racks-Storage-Organization-Home-Kitchen/s?ie=UTF8&page=1&rh=n%3A3610841%2Ck%3Acoat%20racks%2Cp_89%3ACoaster%20Home%20Furnishings%7CHeadbourne%7CInterDesign%7CLiberty%7CMonarch%20Specialties%7CPrepac%7CUmbra"],
["144","Laundry Hamper","https://www.amazon.com/laundry-laundry-hampers/b?ie=UTF8&node=695489011"],
["145","Handle sets","https://www.amazon.com/handlesets/b?node=573758011"],
["146","Wall-Mounted Mirrors","https://www.amazon.com/wall-mounted-mirrors/b?ie=UTF8&node=3736411"],
["147","Storage Benches","https://www.amazon.com/Storage-Benches/b?ie=UTF8&node=3734121"],
["148","Sofa & Console Tables","https://www.amazon.com/Sofa-and-Console-Tables/b?ie=UTF8&node=3733651"],
["149","Sports & Outdoors","https://www.amazon.com/plyo-box-Sports-Outdoors-Amazon-com/s?ie=UTF8&page=1&rh=n%3A3375251%2Ck%3Aplyo%20box%2Cp_6%3AATVPDKIKX0DER"],
["150","Kettlebells","https://www.amazon.com/kettlebell/b?ie=UTF8&node=16385851"],
["151","Jump Ropes","https://www.amazon.com/Juming-Ropes-Jump-Rope/b?ie=UTF8&node=3407981"],
["152","Lawn Mowers & Tractors","https://www.amazon.com/Lawn-Mowers-Tractors-Amazon-com/s?ie=UTF8&page=1&rh=n%3A128066011%2Cp_6%3AATVPDKIKX0DER"],
["153","Yoga Towels","https://www.amazon.com/yoga-towels-hot-yoga-towels/b?ie=UTF8&node=7261122011"],
["154","Exercise Balls & Accessories","https://www.amazon.com/exercise-ball-stability-ball/b?ie=UTF8&node=3407921"],
["155","Leaf Blowers & Vacuums","https://www.amazon.com/Leaf-Blowers-Vacuums/b?ie=UTF8&node=553910"],
["156","Pressure Washers","https://www.amazon.com/Pressure-Washers/b?ie=UTF8&node=552856"],
["157","Power Hedge Trimmers","https://www.amazon.com/Power-Hedge-Trimmers/b?ie=UTF8&node=553938"],
["158","Patio Umbrellas","https://www.amazon.com/Patio-Umbrellas/b?ie=UTF8&node=13819001"],
["159","Outdoor Hot Tubs","https://www.amazon.com/Outdoor-Hot-Tubs/b?ie=UTF8&node=2475557011"],
["160","Outdoor Fryers & Smokers","https://www.amazon.com/Outdoor-Fryers-Smokers/b?ie=UTF8&node=9001144011"],
["161","Grills","https://www.amazon.com/Outdoor-Grills/b?ie=UTF8&node=328983011"],
["162","Washers & Dryers","https://www.amazon.com/washers-dryers/b?node=2383576011"],
["163","Fire Pits","https://www.amazon.com/Outdoor-Fire-Pits/b?ie=UTF8&node=14107621"],
["164","Outdoor Rugs","https://www.amazon.com/Outdoor-Rugs/b?ie=UTF8&node=16509767011"],
["165","Outdoor Pillows","https://www.amazon.com/Patio-Furniture-Pillows/b?ie=UTF8&node=3480725011"],
["166","Hammocks","https://www.amazon.com/Hammocks/b?ie=UTF8&node=13881881"],
["167","Outdoor Storage","https://www.amazon.com/Outdoor-Storage/b?ie=UTF8&node=13400641"],
["168","Yoga Blocks","https://www.amazon.com/yoga-block/b?ie=UTF8&node=3422271"],
["169","Yoga Mats","https://www.amazon.com/yoga-mat/b?ie=UTF8&node=3422301"],
["170","Home Gyms","https://www.amazon.com/home-gym-equipment/b?ie=UTF8&node=3408411"],
["171","Weight Benches","https://www.amazon.com/workout-bench-weight-bench/b?ie=UTF8&node=3408341"],
["172","Weight Plates","https://www.amazon.com/Weight-Plates/b?ie=UTF8&node=3408441"],
["173","Dumbbells","https://www.amazon.com/dumbbells-dumbbell-set/b?ie=UTF8&node=3408401"],
["174","Exercise Bikes","https://www.amazon.com/stationary-bike-exercise-bikes/b?ie=UTF8&node=3407781"],
["175","Rowers","https://www.amazon.com/rowing-machine/b?ie=UTF8&node=3407791"],
["176","Treadmills","https://www.amazon.com/treadmill-home-treadmill/b?ie=UTF8&node=3407831"],
["177","Elliptical Trainers","https://www.amazon.com/elliptical-machine-elliptical-trainers/b?ie=UTF8&node=3407771"],
["178","Wine & Champagne Glasses","https://www.amazon.com/b?ie=UTF8&node=16861787011"],
["179","Place Mats","https://www.amazon.com/Place-Mats-Kitchen-Table-Linens/b?ie=UTF8&node=3742001"],
["180","Tablecloths","https://www.amazon.com/Tablecloths-Kitchen-Table-Linens/b?ie=UTF8&node=3742031"],
["181","Chandeliers","https://www.amazon.com/Chandeliers/b?ie=UTF8&node=3736671"],
["182","Cloth Napkins","https://www.amazon.com/Cloth-Napkins/b?ie=UTF8&node=3741981"],
["183","Table Runners","https://www.amazon.com/Table-Runners/b?ie=UTF8&node=3742021"],
["184","Serving Dishes, Trays & Platters","https://www.amazon.com/Serving-Dishes-Trays-Platters/b?ie=UTF8&node=367201011"],
["185","Bathroom Hardware","https://www.amazon.com/hardware-sets-Bathroom/s?ie=UTF8&page=1&rh=n%3A3755001%2Ck%3Ahardware%20sets"],
["186","Touch On Bathroom Sink Faucets","https://www.amazon.com/Bathroom-Touch-On-Faucets/b?ie=UTF8&node=6808092011"],
["187","Buffets and Sideboards","https://www.amazon.com/Buffets-and-Sideboards/b?ie=UTF8&node=3733831"],
["188","Kitchen & Dining Room Chairs","https://www.amazon.com/Kitchen-and-Dining-Room-Chairs/b?ie=UTF8&node=3733821"],
["189","Kitchen & Dining Room Tables","https://www.amazon.com/Kitchen-and-Dining-Room-Tables/b?ie=UTF8&node=3733811"],
["190","Makeup Organizers","https://www.amazon.com/Makeup-Organizers-Amazon-com-Bathroom-Accessories/s?ie=UTF8&page=1&rh=n%3A3743871%2Cp_6%3AATVPDKIKX0DER"],
["191","Bathroom Storage & Organization","https://www.amazon.com/Bathroom-Storage-Organization/b?ie=UTF8&node=2422451011"],
["192","Bathroom Mirrors","https://www.amazon.com/Bathroom-Mirrors/b?ie=UTF8&node=13749901"],
["193","Shower Caddies","https://www.amazon.com/bathroom-shower-caddies/b?ie=UTF8&node=85969011"],
["194","Bathroom Accessory Sets","https://www.amazon.com/bathroom-accessory-sets/b?ie=UTF8&node=3731911"],
["195","Bath Rugs","https://www.amazon.com/bath-rugs/b?ie=UTF8&node=1063242"],
["196","Shower Curtains","https://www.amazon.com/shower-curtains/b?ie=UTF8&node=13749881"],
["197","Pens, Pencils & Writing","https://www.amazon.com/Pens-Pencils-Writing-Amazon-com/s?ie=UTF8&page=1&rh=n%3A3002949011%2Cp_6%3AATVPDKIKX0DER%2Cp_89%3ABIC%7CDixon%20Ticonderoga%7CExpo%7CFisher%7CPaper%20Mate%7CPentel%7CPilot%7CPrismacolor%7CUni-ball"],
["198","Printers","https://www.amazon.com/Printers/b?ie=UTF8&node=172635"],
["199","Paper","https://www.amazon.com/paper/b?ie=UTF8&node=1069664"],
["200","Bulletin Boards","https://www.amazon.com/Bulletin-Boards/b?ie=UTF8&node=1069306"],
["201","Picture Frames","https://www.amazon.com/picture-frames/b?ie=UTF8&node=1063286"],
["202","Desk Accessories & Workspace Organizers","https://www.amazon.com/Desk-Accessories-Workspace-Organizers/b?ie=UTF8&node=1069514"],
["203","File Cabinets","https://www.amazon.com/File-Storage-Cabinets-Racks-Shelves/b?ie=UTF8&node=1069166"],
["204","Bookcases","https://www.amazon.com/Bookcases/b?ie=UTF8&node=10824421"],
["205","Mirrors","https://www.amazon.com/mirrors/b?ie=UTF8&node=3736371"],
["206","Artificial Plants","https://www.amazon.com/artificial-plants/b?ie=UTF8&node=14087351"],
["207","Decorative Accessories","https://www.amazon.com/Home-Decorative-Accessories/b?ie=UTF8&node=3295676011"],
["208","Grilling","https://www.amazon.com/b?ie=UTF8&node=17795807011"],
["209","Coastal Vibes: Outdoor Living","https://www.amazon.com/b?ie=UTF8&node=17733381011"],
["210","Coastal Vibes: Rattan Accents","https://www.amazon.com/b?ie=UTF8&node=17732877011"],
["211","Coastal Vibes: Hanging Outdoor Seating","https://www.amazon.com/b?ie=UTF8&node=17732878011"],
["212","Arts, Crafts & Sewing","https://www.amazon.com/Arts-Crafts-Sewing/b?ie=UTF8&node=2617941011"],
["213","Pet Supplies","https://www.amazon.com/pet-shops-dogs-cats-hamsters-kittens/b?ie=UTF8&node=2619533011"],
["214","Party Supplies","https://www.amazon.com/Event-Party-Supplies/b?ie=UTF8&node=901590"],
["215","Kids' Home Store","https://www.amazon.com/kids-home-store/b?ie=UTF8&node=3206325011"],
["216","Heating, Cooling & Air Quality","https://www.amazon.com/Heating-Cooling-Air-Quality/b?ie=UTF8&node=3206324011"],
["217","Vacuums & Floor Care","https://www.amazon.com/vacuums-floor-care/b?ie=UTF8&node=510106"],
["218","Storage & Organization","https://www.amazon.com/storage-organization/b?ie=UTF8&node=3610841"],
["219","Bath Towels","https://www.amazon.com/bath-towels/b?ie=UTF8&node=10789941"],
["220","Pie Pans","https://www.amazon.com/Pie-Pans/b?ie=UTF8&node=14067421"],
["221","Seasonal DÃ©cor","https://www.amazon.com/Seasonal-D%C3%A9cor-Home/s?ie=UTF8&hidden-keywords=Autumn%7Cfall&page=1&rh=n%3A11434603011"],
["222","Two-tone ceramics","https://www.amazon.com/b?ie=UTF8&node=17922270011"],
["223","Handmade Gift Shop","https://www.amazon.com/b?ie=UTF8&node=17296384011"],
["224","Storage & Organization","https://www.amazon.com/kitchen-storage-organization/b?ie=UTF8&node=510136"],
["225","Kitchen & Table Linens","https://www.amazon.com/Kitchen-Table-Linens-Dining/b?ie=UTF8&node=1063916"],
["226","Dining & Entertaining","https://www.amazon.com/dining-entertaining/b?ie=UTF8&node=13162311"],
["227","Kitchen Knives & Cutlery Accessories","https://www.amazon.com/cutlery/b?ie=UTF8&node=289851"],
["228","Coffee, Tea & Espresso","https://www.amazon.com/coffee-tea-espresso/b?ie=UTF8&node=915194"],
["229","Kitchen Utensils & Gadgets","https://www.amazon.com/tools-gadgets/b?ie=UTF8&node=289754"],
["230","Bakeware","https://www.amazon.com/bakeware/b?ie=UTF8&node=289668"],
["231","Coastal Vibes: Bedroom","https://www.amazon.com/b?ie=UTF8&node=17733373011"],
["232","Luxurious bath linens","https://www.amazon.com/b?ie=UTF8&node=17696595011"],
["233","Mixed metal lighting","https://www.amazon.com/b?ie=UTF8&node=17695193011"],
["234","Kitchen & Bath Fixtures","https://www.amazon.com/Kitchen-26-Bath-Fixtures/b?ie=UTF8&node=3754161"],
["235","Ladders","https://www.amazon.com/ladders/b?node=553470"],
["236","Safety & Security","https://www.amazon.com/Safety-26-Security/b?ie=UTF8&node=3180231"],
["237","Light Bulbs","https://www.amazon.com/light-bulbs/b?node=322525011"],
["238","Electrical","https://www.amazon.com/electrical/b?node=495266"],
["239","Southern Champion Tray","https://www.amazon.com/b?ie=UTF8&node=16907768011"],
["240","Mercer Culinary","https://www.amazon.com/b?ie=UTF8&node=16907769011"],
["241","Bunn","https://www.amazon.com/b?ie=UTF8&node=16907766011"],
["242","American Metalcraft","https://www.amazon.com/b?ie=UTF8&node=16907765011"],
["243","National Public Seating","https://www.amazon.com/b?ie=UTF8&node=16907767011"],
["244","Hoffmaster","https://www.amazon.com/b?ie=UTF8&node=16907764011"],
["245","Carlisle","https://www.amazon.com/b?ie=UTF8&node=16907762011"],
["246","John Boos","https://www.amazon.com/b?ie=UTF8&node=16907763011"],
["247","Dixie","https://www.amazon.com/b?ie=UTF8&node=16907760011"],
["248","Hamilton Beach Commercial","https://www.amazon.com/b?ie=UTF8&node=16907759011"],
["249","Rubbermaid Commercial","https://www.amazon.com/b?ie=UTF8&node=16907761011"],
["250","TRUE","https://www.amazon.com/b?ie=UTF8&node=16907758011"],
["251","Food Service Supplies & Equipment - Deals and markdowns","https://www.amazon.com/b?ie=UTF8&node=15645192011"],
["252","Hardware","https://www.amazon.com/hardware/b?node=511228"],
["253","Woodworking Shop","https://www.amazon.com/Woodworking-Shop-Tools-Hardware/b?ie=UTF8&node=541016"],
["254","Tool Organizers","https://www.amazon.com/Tool-Organizers/b?ie=UTF8&node=13400691"],
["255","Cozy throws","https://www.amazon.com/b?ie=UTF8&node=17732895011"],
["256","Cookware","https://www.amazon.com/cookware/b?ie=UTF8&node=289814"],
["257","Kenmore Labor Day","https://www.amazon.com/b?ie=UTF8&node=17932490011"],
["258","Measuring & Layout Tools","https://www.amazon.com/Measuring-26-Layout-Tools/b?ie=UTF8&node=553244"],
["259","Air Tools","https://www.amazon.com/Air-Tools-Power-Hand/b?ie=UTF8&node=552684"],
["260","Power Concrete Tools","https://www.amazon.com/Concrete-Tools/b?ie=UTF8&node=552992"],
["261","Power Tool Parts & Accessories","https://www.amazon.com/Power-Tool-Parts-26-Accessories/b?ie=UTF8&node=552262"],
["262","Hand Tools","https://www.amazon.com/Hand-Tools/b?ie=UTF8&node=551238"],
["263","Floor Mirrors","https://www.amazon.com/floor-mirrors/b?ie=UTF8&node=3736381"],
["264","Power Tools","https://www.amazon.com/Power-Tools/b?ie=UTF8&node=551236"],
["265","Save Money and Energy with Smart Home","https://www.amazon.com/b?ie=UTF8&node=17304249011"],
["266","Duvets & Down Comforters","https://www.amazon.com/duvets-down-comforters/b?ie=UTF8&node=10671048011"],
["267","Pillows","https://www.amazon.com/bed-pillows/b?ie=UTF8&node=10671043011"],
["268","Smart Home: 6 easy ways to get started","https://www.amazon.com/b?ie=UTF8&node=17165932011"],
["269","Mattress Pads","https://www.amazon.com/mattress-pads/b?ie=UTF8&node=10671044011"],
["270","Comforter Sets","https://www.amazon.com/comforter-sets/b?ie=UTF8&node=14053321"],
["271","Ceramic planters","https://www.amazon.com/b?ie=UTF8&node=17732888011"],
["272","Dressers","https://www.amazon.com/Dressers/b?ie=UTF8&node=3733261"],
["273","Patio Furniture","https://www.amazon.com/b?ie=UTF8&node=17871122011"],
["274","Sheet & Pillowcase Sets","https://www.amazon.com/sheet-pillowcase-sets/b?ie=UTF8&node=3732781"],
["275","tuya","https://www.amazon.com/tuya/s?ie=UTF8&page=1&rh=i%3Aaps%2Ck%3Atuya%2Cp_n_amazon_certified%3A16741513011"],
["276","Works with Alexa: Vacuums","https://www.amazon.com/b?ie=UTF8&node=17934444011"],
["277","Other smart solutions | Works with Alexa","https://www.amazon.com/smart-othersolutions/b?ie=UTF8&node=16334613011"],
["278","Garden Sculptures & Statues","https://www.amazon.com/Garden-Sculptures-Statues/b?ie=UTF8&node=553802"],
["279","Pots, Planters & Container Accessories","https://www.amazon.com/Gardening-Pots-Planters-Accessories/b?ie=UTF8&node=3480694011"],
["280","Amazon Echo & Alexa Devices","https://www.amazon.com/Amazon-Device-Accessories-Echo-Alexa-Devices/s?ie=UTF8&page=1&rh=n%3A370783011%2Cp_n_feature_browse-bin%3A16926006011"],
["281","Alexa Built-in Devices","https://www.amazon.com/b?ie=UTF8&node=15443147011"],
["282","Plants, Seeds & Bulbs","https://www.amazon.com/Plants-Seeds-Bulbs/b?ie=UTF8&node=3480662011"],
["283","Gardening Tools","https://www.amazon.com/gardening-tools/b?node=128061011"],
["284","Pools, Hot Tubs & Supplies","https://www.amazon.com/Pools-Hot-Tubs-Supplies/b?ie=UTF8&node=1272941011"],
["285","Outdoor Power Tools","https://www.amazon.com/Outdoor-Power-Lawn-Equipment/b?ie=UTF8&node=551242"],
["286","Canopies, Gazebos and Pergolas","https://www.amazon.com/Canopies-Gazebos-Pergolas/b?ie=UTF8&node=14135021011"],
["287","Lawn Mowers & Tractors","https://www.amazon.com/Lawn-Mowers-Tractors/b?ie=UTF8&node=128066011"],
["288","Patio Seating","https://www.amazon.com/Patio-Seating/b?ie=UTF8&node=9001152011"],
["289","Outdoor lighting","https://www.amazon.com/outdoor-lighting/b?node=495236"],
]

        for url in urls:
            try:
                #req = scrapy.Request(url[3] , headers={ 'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.8' , 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36' , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'Cache-Control': 'max-age=0' },callback=self.parse6)
                #req = scrapy.Request(url[3] , headers= {'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.9' , 'Upgrade-Insecure-Requests': '1' , 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36' , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'Cache-Control': 'max-age=0' , 'Connection': 'keep-alive'}, callback=self.parse6)
                #req = scrapy.Request(url[2] , callback=self.parse6)
                #req = scrapy.Request(url[2] , headers={'Accept-Encoding': 'gzip, deflate, br' , 'Accept-Language': 'en-US,en;q=0.9' , 'Upgrade-Insecure-Requests': '1' , 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36' , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 'Cache-Control': 'max-age=0', 'Connection': 'keep-alive' }, callback=self.parse6)
                req = scrapy.Request(url[2] , callback=self.parse6)
                req.meta['page_id']=url[0]
                req.meta['category']=url[1]
                #req.cookies = {'lc-main':'en_US', 's_nr':'1503816974090-New', 's_vnum':'1935816974090%26vn%3D1', 's_dslv':'1503816974091', 'x-main':'pHlb3N0WUwENeYPsqI@jzfF7PXLCCMcJSFiGwcdKfrlzzhc8yQR4kOovInsAXJRe', 'at-main':'Atza|IwEBIF45RJQgsZLrUGO7JaJnp1uVC-RDIfDCqwjV0PeKEDcSIP7e0Pvcm_n-R4iCtwyo7zXH7KLDakbXVsW-9UevBLsZEeSIH2YZJFCjQqDsNAySplN1BcQ1tUj5kmj24vddIVYyi7vx3S0B-tkr9EISA5O5_d5Tr--5JO2qiruKCKawd1MLIyk8KFGS2KdQJGW9wwb9fJf6C7Fk4_7UiW5C3D1DLeuP3VXdar3-_S3yvGXRindK-xRNl3O_YFLRo-a_yn9_Z1V8vNj6kvWgzui_fOIRGrsI9qCHAJpcpt5Nh4Ta5n6-ALqNPkS-zbWlmMkZMgWsZb5EwLk8qr5O_FUA9Be8bqkneub7AuYy2QcvE01rYqkAKgAm4QKR5MSCXDQg8Fquyibqt_a3TRBYXTOzPnoedkm7JdBsUtVGYs4TBNssF4KGFefA1cQRLvxAhHfZe58', 'x-wl-uid':'1QBgT0TBwoj9RQ+QP7eh8ocBTABgs1739+rzq1e3s1iwjoSRYnMpbAczaaknzT2id2ww9iSyiyXd3OQeaJ9Nm9xZrZOKqXNWIDJihS4V7CV+xlp+PQA7T/ILJyNBZ15so9XvNPTzCBQA=', 'x-amz-captcha-1':'1511784189246059', 'x-amz-captcha-2':'e+dIUFBcjimZCAzt1M7ENg==', 'skin':'noskin', 'session-token':'iLbxbiSqExhaR4LPazKup8FEME8wVof1IaYWHpuSZwkY9Pk99Za2t1nVKi07sKUQrt7vqJ1e8hVd+j+XnNR0sr/z1MFubVFga4Gs7V0Ex2bhH+zFs7fU23+xahjvRAHWjVywkXsJyB8REkaRCDWd5GhE6loyew2Ibyol3vtiEyuebDuB1Y1hwVGYY+DGF8ujzqDQvV0psuzZg3JwtZCgfaymOM9XSIYP8OlojdlhdY8g6texOGn+IwTndrN3g5zYg4TsvZU7oWYXp6bVS8QP+A==', 'csm-hit':'s-YCC0NCGB2CHZFXZA740S|1513777168018', 'ubid-main':'151-8001146-5395566', 'session-id-time':'2082787201l', 'session-id':'151-4943311-4733238' }
                #req.cookies = { 'x-wl-uid':'1y8ltVLwKU/L4uHVRT4wcyu32QxGmsLap3PS10lHQ8I4lHwvcV3mdItRxlTQQbVCy6hcltYxKLMM=', 's_nr':'1498670542228-New', 's_vnum':'1930670542228%26vn%3D1', 's_dslv':'1498670542232','amznacsleftnav-ac35e287-d67e-4607-a950-5d9ffd0c2ca9':'1', 'x-amz-captcha-1':'1499054178128406', 'x-amz-captcha-2':'f44Jo5PiWFZO/J2o05Otig==', 'session-token':'jmS4MZ+87cNOfytK07tpUCEGti+GXuHdZ0oZyPtYqY7t0jdykH+Ub7kXBm+uyaqfsw9okzU8c7KFuF577LQSOEOVzXGU6Ky1xqdZjaFUDfW6H5HbFByM0YxhwaB/i3TdgWzWRV7hvGo3qygmjkrIJ3ESRIOOM6YB4EJWL65CQUTq+Cp4ORjO1XQaGvfPERmPKJ8tKI4p77AQ0pKocXEOtyFku2Vp9HJzTUI9LN4bZVnXVtkV/ra/ElaVLqz1HqDJ', 'csm-hit':'s-GZBERSD0R10VXC0HBQZ6|1500714195597', 'session-id-time':'2082754801l', 'session-id':'261-2325209-6209161', 'ubid-acbde':'259-4651163-1859124' }
                #req.cookies = {'lc-main':'en_US', 's_nr':'1503816974090-New', 's_vnum':'1935816974090%26vn%3D1', 's_dslv':'1503816974091', 'x-main':'pHlb3N0WUwENeYPsqI@jzfF7PXLCCMcJSFiGwcdKfrlzzhc8yQR4kOovInsAXJRe', 'at-main':'Atza|IwEBIF45RJQgsZLrUGO7JaJnp1uVC-RDIfDCqwjV0PeKEDcSIP7e0Pvcm_n-R4iCtwyo7zXH7KLDakbXVsW-9UevBLsZEeSIH2YZJFCjQqDsNAySplN1BcQ1tUj5kmj24vddIVYyi7vx3S0B-tkr9EISA5O5_d5Tr--5JO2qiruKCKawd1MLIyk8KFGS2KdQJGW9wwb9fJf6C7Fk4_7UiW5C3D1DLeuP3VXdar3-_S3yvGXRindK-xRNl3O_YFLRo-a_yn9_Z1V8vNj6kvWgzui_fOIRGrsI9qCHAJpcpt5Nh4Ta5n6-ALqNPkS-zbWlmMkZMgWsZb5EwLk8qr5O_FUA9Be8bqkneub7AuYy2QcvE01rYqkAKgAm4QKR5MSCXDQg8Fquyibqt_a3TRBYXTOzPnoedkm7JdBsUtVGYs4TBNssF4KGFefA1cQRLvxAhHfZe58', 'x-wl-uid':'1QBgT0TBwoj9RQ+QP7eh8ocBTABgs1739+rzq1e3s1iwjoSRYnMpbAczaaknzT2id2ww9iSyiyXd3OQeaJ9Nm9xZrZOKqXNWIDJihS4V7CV+xlp+PQA7T/ILJyNBZ15so9XvNPTzCBQA=', 'session-token':'qLl3vjnjOse5+Cy5cC+3OlMT95d5wVC4bWvaoAbqyhOetjeYqWP24HhMNHJI9Ni3Y7rljL1VdkRzXeolkaGJX8cPCh2P8OzRCIL3t4dynzdXlADAwNZxyWK1BFxTvyUzw4CXSHIeNdq1l95h3SbsLhG4gOhSf5JLHUzfx9dKziC4SpGUaTP+/8VbIE886Ipz6wOjM1J1YwP4lwLQABPJPh/qNzYZWgWTmLW2sk2bkN1nGCJk9XWAoIA2ClwvqPRRIFg8mbX73GFXkSCPmdboKQ==', 'csm-hit':'HCCNKDAR5Q931G1FR5S1+s-HCCNKDAR5Q931G1FR5S1|1504589304054', 'ubid-main':'151-8001146-5395566', 'session-id-time':'2082787201l', 'session-id':'151-4943311-4733238'}
                #req.cookies = {'s_nr':'1514464459649-Repeat', 's_vnum':'1935816974090%26vn%3D2', 's_dslv':'1514464459650', 'amznacsleftnav-74393fbe-66a6-3a52-840b-37b54d8c76ce':'1', 'ubid-main':'151-8001146-5395566', 'session-id':'143-2570392-1761151', 'session-id-time':'2082787201l', 'x-amz-captcha-1':'1518087751656922', 'x-amz-captcha-2':'TAtOiFxNP39/4JXr1HRtRQ==', 'sst-main':'Sst1|PQEIWOSKQkmRJNiLdAIpYuxvCAgSf8fU0zrPqIDU7VYVKFCOVnWBgJtiBpdxZRVT3-poc3ti0PuawPx6vNYyBVldZhbnizavxNe9Bk4hO_sfGatBlE4qbUfAffoSGZ6yY5qCSewJxENQdMoYJdd2iGeltGkf31I7IedHWFkRNqIMeLvDhOTN6hqKpQTN9hDBPQMu5cmGO5GyahsVZgdQHW7nBs2FLMophIEpjxCVzavMHwn4aHwIdloCWgkG6TfVmKcDiLUXWWoEXfBKp1QLdH2Mrg', 'x-wl-uid':'1yxWFE65rJfR+kOyS6k2hEnyGw4GjqsLYgzk8HpBprCTXNRb3M/MHB8cr9TuingY8KMY1MTFD/DRDFDi8l+aNIzcMf1WnUCGQpyuxT03VbXPERI+scQGnJsJeQnc9o4RlV2Ma6WJrdc4=', 'session-token':'rxLcGYC0NRCcoO4VkktmBsPxOQ9ijb7A7y+U04K11tUdm56q5+IfofrwXNkASd2VRmrzzjMAZYXSYCfNpYtun/TVNDL2W9szbccnXIwNl1WCwn0nSmKS252Ny1WqkdB0gWJem0QYwk9DIcz/Rm27nFidGDvO0QUKDRuqDXoXvxNDciWc86l/HX+vFS9RNG55PPuLoxeSz4isAn6TjnB+DLpNoO/6XZbi4IcZUvEonMZ6fnsL1Ut/RDk/6sxP5vOa', 'csm-hit':'1EK1B8SRZQ7J0XNH96X2+s-1EK1B8SRZQ7J0XNH96X2|1522756475463' }
                if url[0] not in urls_done: 
                    yield req
                    #time.sleep(.1)
            except: raise
        #print "URLS_DONE : ",urls_done


    def parse6(self,response):
        categorylist=response.xpath('//*[@id="leftNav"]/ul[1]/ul/div/li/span/a')
        categorylist1=response.xpath('//*[@id="leftNavContainer"]/ul[1]/ul/div/li/span/a')
        if len(categorylist)>0:
            for categories in categorylist:
                #item=LowesItem()
                #categoryurl="https://www.amazon.com" + categories.xpath('span/a/@href').extract()[0]
                #categoryname= categories.xpath('span/a/span/text()').extract()[0]
                categoryurl=categories.xpath('@href').extract()[0]
                categoryname=categories.xpath('span/text()').extract()[0]
                req=scrapy.Request(categoryurl,callback=self.parse6, meta={'categoryname':categoryname})
                #item['url']=categoryurl
                #item['category'] =categoryname
                #yield item
                yield req
        elif len(categorylist1)>0:
            for categories in categorylist1:
                #item=LowesItem()
                #categoryurl="https://www.amazon.com" + categories.xpath('span/a/@href').extract()[0]
                #categoryname= categories.xpath('span/a/span/text()').extract()[0]
                categoryurl=categories.xpath('@href').extract()[0]
                categoryname=categories.xpath('span/text()').extract()[0]
                req=scrapy.Request(categoryurl,callback=self.parse6, meta={'categoryname':categoryname})
                #item['url']=categoryurl
                #item['category'] =categoryname
                #yield item
                yield req
        else:
            item=AmazonItem()
            #categoryname=response.xpath('//*[@id="mainContent"]/div[3]/h1/text()').extract()[0]
            categoryname="".join(response.xpath('//*[@id="fst-hybrid-dynamic-h1"]/div/h1//text()').extract())
            if not categoryname: categoryname="".join(response.xpath('//*[@id="leftNavContainer"]/ul[1]/li/span/h4//text()').extract())
            if not categoryname: categoryname="".join(response.xpath('//*[@id="leftNav"]/ul[1]/li/span/h4//text()').extract())
            if not categoryname: categoryname="".join(response.xpath('//*[@id="s-result-count"]/span/span/text()').extract())
            categoryurl=response.url
            item['url']=categoryurl
            item['category'] =categoryname
            yield item