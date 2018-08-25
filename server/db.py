import sqlite3
db = sqlite3.connect('API.sqlite')

db.execute('DROP TABLE IF EXISTS places')

db.execute('''CREATE TABLE places(
	id integer PRIMARY KEY,	
	state text NOT NULL,
	location text NOT NULL,
	name text NOT NULL,
	address text NOT NULL,
	description text NOT NULL
)''')

cursor = db.cursor()

cursor.execute('''
	INSERT INTO places(state, location, name, address, description)
	VALUES("01", "Georgetown", "UNESCO World Heritage Site", "Georgetown, 10200 George Town, Penang", "Georgetown is a UNESCO World Heritage site, officially recognised for its unique architecture and cultural townscape. A socially diverse and culturally-rich town, there is much to see and do here in the many ethnic enclaves present here such as Little India, Chinatown and Kampong Siam. For the more progressive lovers of culture and art, you may find pleasure in hunting for the various street arts that line the walls of buildings all over Georgetown.")
''')
cursor.execute('''
	INSERT INTO places(state, location, name, address, description)
	VALUES("01", "Ayer Itam", "Batu Ferringhi Beach", "45, Jalan Batu Ferringhi, Kampung Batu Feringgi, 11100 Ayer Itam, Pulau Pinang", "Batu Ferringhi, situated along the coastal road north-west of Georgetown and lined with a string of international- standard resorts, is the most popular beach in Penang.")
''')
cursor.execute('''
	INSERT INTO places(state, location, name, address, description)
	VALUES("01", "Teluk Bahang", "Entopia Penang", "No.830, Jalan Teluk Bahang, 11050 Teluk Bahang, Pulau Pinang", "Entopia is a centre for nature learning where it brings the best of the insect and plant worlds together for everyone to experience the harmony in nature. Within Entopia lies two new worlds; The Natureland and The Cocoon. The Natureland, which is a living garden vivarium, is a shared ecological space for a variety of animals from invertebrates and reptiles living in their re-created natural habitat.")
''')
cursor.execute('''
	INSERT INTO places(state, location, name, address, description)
	VALUES("01", "Teluk Bahang", "Escape Waterplay", "828, Teluk Bahang, 11050 Tanjung Bungah, Pulau Pinang", "ESCAPE WATERPLAY is the newest fun destination with exciting water activities. It features 20 attractions; namely Atan's Jump, Banan Flip, Family Twister, Mega Drop and more.")
''')

cursor.execute('''
	INSERT INTO places(state, location, name, address, description)
	VALUES("02", "Ampang", "National Zoo of Malaysia", "Jalan Ulu Kelang, Kemensah Heights, 68000 Ampang, Selangor", " Zoo Negara is home to 5137 animals of 476 different species. Over the years, the zoo has transformed itself to an open concept zoo with over 90% of its animals kept in spacious exhibits with landscape befitting its nature.")
''')
cursor.execute('''
	INSERT INTO places(state, location, name, address, description)
	VALUES("02", "Subang Jaya", "Sewing World Gallery", "One City, 47630 Subang Jaya, Selangor", "As a gallery of handmade products, it displays hundreds of toys, fashionable apparel, artworks made of thread and fabric, and decorations suitable to adorn furniture. Expect to see colourful creations turned into teddy bears, bedsheet covers, handbags and more.")
''')
cursor.execute('''
	INSERT INTO places(state, location, name, address, description)
	VALUES("02", "Gombak", "Batu Cave Murugan Temple", "Gombak, 68100 Batu Caves, Selangor", "Batu Caves is a an iconic and popular tourist attraction in Selangor. Site of a Hindu temple and shrine, Batu Caves attracts thousands of worshippers and tourists, especially during the annual Hindu festival, Thaipusam. A limestone outcrop located just north of Kuala Lumpur, Batu Caves has three main caves featuring temples and Hindu shrines.")
''')
cursor.execute('''
	INSERT INTO places(state, location, name, address, description)
	VALUES("02", "Serdang", "The Malay Heritage Museum", "Fakulti Bahasa Moden dan Komunikasi, Jalan Upm, Putra Square, 43400 Serdang, Selangor", "The museum promises visitors many more interesting finds about the history and heritage of the Malays, and is a great way to spend an afternoon back in time! Tours in English by the curator can be arranged upon request. Tickets are RM2/person and the museum opens daily from 9 am to 5 pm, and is closed on Sundays.")
''')

cursor.execute('''
	INSERT INTO places(state, location, name, address, description)
	VALUES("03", "Nusajaya", "Legoland", "7, Jalan Legoland, Medini, 79250 Nusajaya, Johor", "LEGOLAND is built with over 40 interactive rides, shows and attractions. One of the main attractions here is Miniland. More than 30 million LEGO bricks were used in the building of the various monuments here including the Petronas Twin Towers, The Merlion Statue, Taj Mahal and others. These well-known buildings were built to a scale of 1:20 where people, trains and airplanes come to life at the touch of a button.")
''')
cursor.execute('''
	INSERT INTO places(state, location, name, address, description)
	VALUES("03", "Mersing", "Endau Rompin National Park", "Taman Negara Endau Rompin, Mersing, Johor", "The park is home to a vast species of birds, mammals, frogs, insects and exotic varieties of orchids, herbs, medicinal plants and trees. It seems that every time a scientific expedition returns from Endau Rompin, they discover a new species")
''')
cursor.execute('''
	INSERT INTO places(state, location, name, address, description)
	VALUES("03", "Mersing", "Pulau Rawa", "Pulau Rawa, Mersing, Johor, Malaysia", "Sixteen kilometres off the coast of Mersing is Pulau Rawa. The island is famed for its white coral sand, tall palm trees and coral reefs with neon-coloured fish and other exotic marine life. This quiet island only has two choices of accommodation on it. The wooden chalets nestled amongst coconut groves complement the island's reputation as a quaint hideaway, perfect for those wanting to escape the hustle and bustle of the city.")
''')

cursor.execute('''
	INSERT INTO places(state, location, name, address, description)
	VALUES("04", "Sandakan", "Sepilok Orang Utan Rehabilitation Centre", "Sabah Wildlife Department, W.D.T. 200, Sandakan, Jalan Sepilok, Sepilok, 90000 Sandakan, Sabah", "The best times to visit the 'Wild Men of Borneo' are at 10am and again, at 2.30pm when the primates emerge from the forest for their daily ration of bananas and milk. Watch as the orang utans are fed from a platform in the centre and then returned to roam freely in the forest where they can fend for themselves.")
''')
cursor.execute('''
	INSERT INTO places(state, location, name, address, description)
	VALUES("04", "Tuaran", "Borneo Ant House", "Highway Tuaran- Tenghilan, 89207 Kg Kindu, Tuaran, SABAH Kg.Kindu , Tuaran, 89207 Tuaran, Sabah", "Borneo Ant House is so named because its underground walkways and tunnels simulate an ant nest. There are four main galleries here namely the Ant Replica gallery, the Traditional and Culture gallery, the Sword gallery and the Fishing & Paddy Farming gallery. The walls in the Ant Replica gallery are filled with a total of 463 replicas of crawling ants, and each and every ant replica is not moulded but are actual handmade sculptures.")
''')
cursor.execute('''
	INSERT INTO places(state, location, name, address, description)
	VALUES("04", "Kota Kinabalu", "North Borneo Cruises", "The Marina Clubhouse Sutera Harbour, 88000 Kota Kinabalu, Sabah", "North Borneo Cruises aim to dazzle you with breathtakingly Scenic Cruises like no other, complete with lavish dinners and buffet meals. Pass by water Villages and tropical island paradises, view a world class sunset while been wined and dined. After dinner, the perfect evening aswe cruise by kota kinabalu waterfront to see the beautiful city lights.")
''')
cursor.execute('''
	INSERT INTO places(state, location, name, address, description)
	VALUES("04", "Lahad Datu", "Danum Valley", "Lahad Datu, Sabah", ": The Danum Valley Conservation Area, 83km south-west of Lahad Datu, is blessed with a startling diversity of tropical flora and fauna. This vast Eden-like basin is home to the rare Sumatran Rhinoceros, orang utans, gibbons, mousedeer and the beautiful clouded leopard. Some 270 species of birds have been recorded in the area. The Danum Field Research Centre is located within the confines of the 440sq km forest reserve.")
''')

cursor.execute('''
	INSERT INTO places(state, location, name, address, description)
	VALUES("05", "Kuching", "Saradise Gallery", "Level 1, Titanium Tower, Lot 1, Brighton Square, Jalan Song, Kuching, Sarawak.", "This gallery is a platform for creating awareness among the public to promote local art and culture. Gallery Paradise is not only a place to showcase the art and culture of Sarawak, but also as a comfortable place in which both the public and the artists and designers can interact with each other, share ideas and knowledge with regard to the identity of the state, art and culture.")
''')
cursor.execute('''
	INSERT INTO places(state, location, name, address, description)
	VALUES("05", "Kuching", "Bako National Park", "Jalan Bako, Kuching 93050, Malaysia", "Sarawak's oldest national park was established in 1957, covers a modest 27 sq. km., and is about 37km from Kuching. It's known for its extraordinary natural scenery, habitats, plants and wild life. Its most significant features are secluded coves and rugged rocky headlands with magnificent steep cliffs that overlook the South China Sea. The sea spray, wave action and the wind have also carved out magnificent sea arches and sea stacks at the base of the cliffs, some rearing above the waves like a mighty serpent's head.")
''')
cursor.execute('''
	INSERT INTO places(state, location, name, address, description)
	VALUES("05", "Miri", "Lambir Hills National Park", "Lambir Hills National Park,98200 Miri, Sarawak.", "The famed Lambir Hills National Park is located along the Miri-Bintulu road, 36 km south-west of Miri town in Sarawak, East Malaysia. It was gazetted as a park in 1975, and covers an area of 6,952 hectares. There are around 1,173 tree species in the park alone, with 286 genera and 81 tree families making Lambir one of the more diversified forests in Malaysia. Wild animals can also be found in the deeper parts of the park, especially monkeys, sun bear, pangolin and bats.")
''')
cursor.execute('''
	INSERT INTO places(state, location, name, address, description)
	VALUES("05", "Miri", "Niah National Park", "Niah National Park, 98200 Miri, Sarawak.", "Over 400km up the coast from Kuching, hidden in the forests of Miri, are the Niah Caves. The park covers a vast swathe of 3,140 hectares of peat swamp, dipterocarp forests, as well as the massive limestone outcroppings within which the giant Niah caves are concealed. The caves consist of one big cave (The Great Cave) and some smaller caves.")
''')

cursor.execute('''
	INSERT INTO places(state, location, name, address, description)
	VALUES("06", "Melaka City", "Baba Nyonya Heritage Museum", "48-50, Jalan Tun Tan Cheng Lock, 75200 Melaka", "The 'Straits Chinese', also called the Baba and Nyonya, are Chinese of noble descent who have adopted much of the Malay culture into theirs. This has been a gradual process lasting over 400 years since the great Chinese explorer Admiral Cheng Ho first brought Chinese settlers to Melaka. Over the centuries, the Baba Nyonya have developed a distinct and highly interesting culture that is unique to Malaysia's west coast, particularly Melaka.")
''')
cursor.execute('''
	INSERT INTO places(state, location, name, address, description)
	VALUES("06", "Alor Gajah", "A Famosa Resort", "A Famosa Resort Jalan Kemus, Simpang Empat,78000 Alor Gajah, Melaka, Malaysia", "A Famosa was named after the 16th century Portuguese fort of the same name which was once stood near the harbor of Malacca city. The logo of the resort also incorporates a stylized silhouette of the forts gateway in the background.")
''')

cursor.execute('''
	INSERT INTO places(state, location, name, address, description)
	VALUES("07", "Ipoh", "Lost World of Tambun", "1, Persiaran Lagun Sunway, Sunway City, 31150 Ipoh, Negeri Perak", "Lost World Of Tambun is an action packed, wholesome family adventure destination. This self contained wonderland is cocooned by lush tropical jungle, natural hot springs, breathtaking limestone features of 400 million years of age and seven amazing attraction parks making it the ultimate day and night destination for a unique eco adventure excursion for visitors of all ages. Just a stones throw away is the Lost World Hotel, a perfect snooze chamber after a long day of adventure.")
''')
cursor.execute('''
	INSERT INTO places(state, location, name, address, description)
	VALUES("07", "Ipoh", "Movie Animation Park Studios", "3, Persiaran Meru Raya, 31200 Ipoh, Negeri Perak", "Movie Animation Park Studios will be the home to some of the worlds biggest animation attractions including the much loved BoBoiBoy, The Smurfs and DreamWorks characters such as Mr. Peabody and Sherman, Megamind, The Croods and Casper the Friendly Ghost.")
''')

cursor.execute('''
	INSERT INTO places(state, location, name, address, description)
	VALUES("08", "Jitra", "Darulaman Hills", "Gate 2, Darulaman Trails, Bandar Darulaman,06000, Jitra, Kedah.", "Darulaman hills are upgraded to a bicycle park with tracks connected to a particular track to create a complete pathway for cycling, trial running, hiking and walking activities. There is an uplift of 365 meters from the bottom (GATE 2) to the Dataran which is an open space on a hill.")
''')
cursor.execute('''
	INSERT INTO places(state, location, name, address, description)
	VALUES("08", "Langkawi", "Upsidow Langkawi", "Jalan Padang Matsirat,Langkawi,07000, Kedah", "A weird and wonderful interaction gallery featuring an urban open air food court and viewing platform.Upsidow is an upcycled art installation for the young and old. It is an upside down house full of fun, that was fully built from recycled materials. Upsidow is the first and only Eco-friendly upside down house in the world, offering a food court with European standards and a viewing platform.")
''')

cursor.execute('''
	INSERT INTO places(state, location, name, address, description)
	VALUES("09", " Kuantan", "Kuantan City Mall", "Address: Level 5, Kuantan City Mall, Jalan Putra Square 6/1, Putra Square 25300, Kuantan Pahang Darul Makmur", "Kuantan City Mall is a brand new shopping centre strategically located in the new commercial hub of Kuantan, comprising all the shopping, dining, play and entertainment experience that you can spend quality time with family.")
''')
cursor.execute('''
	INSERT INTO places(state, location, name, address, description)
	VALUES("09", "Kuantan", "Serambi Teruntum", "Jalan Tanjung Lumpur, 26060 Kuantan, Pahang", "Serambi Teruntum, located in Tanjung Lumpur Kuantan, Pahang, is a newly established marketplace for local products that is gaining much popularity among both domestic and international tourists alike. This one stop centre gathers and sells traditional products such as food and handicrafts made by Pahang small and medium sized enterprises. Serambi Teruntum provides a marketplace for local sellers to introduce and sell their products directly to customers without the use of intermediaries.")
''')

cursor.execute('''
	INSERT INTO places(state, location, name, address, description)
	VALUES("10", "Kuala Terengganu", "Taman Tamadun Islam", "Pulau Wan Man, Losong Panglima Perang, 21000 Kuala Terengganu, Terengganu", "Taman Tamadun Islam or The Islamic Civilization Park is an outdoor edutainment park featuring the glory of the Islamic civilization as its theme. Located in Terengganu, it prides itself in giving visitors a chance to visit and learn about historic monuments from around the world. The main attractions are the scaled monuments like Malaysia National Mosque, India Taj Mahal, Saudi Arabia Masjidil Haram and many more made with great detail displayed around the park. All of the monuments have information accompanying them while a few even have interactive videos, games, photos and artefacts for visitors to engage with.")
''')
cursor.execute('''
	INSERT INTO places(state, location, name, address, description)
	VALUES("10", "Kuala Terengganu", "Tengku Tengah Zaharah Mosque", "Tengku Tengah Zaharah Mosque,20400 Kuala Terengganu, Terengganu", "Tengku Tengah Zaharah Mosque is built on a floating platform, giving it a unique perspective from all facets.  It sits snuggly on the estuary of Terengganu River and its modern architecture is due to the ingenuity of one of the princes in Terengganu. The glistening white mosque combines modern and Moorish architecture, symbolizing a new modernisation in the state, making it an Islamic icon in the country.  The design of the mosque reflects a subtle Islamic influence combined with local features, incorporating the use of marble, ceramics, mosaic works and bomanite paving.")
''')
cursor.execute('''
	INSERT INTO places(state, location, name, address, description)
	VALUES("11", "Dabong", "Gunung Stong State Park", "Dabong Forest Reserve, Kelantan, 18200, Dabong, Kelantan", "Gunung Stong State Park (GSSP) is a forested area, totaling 21,950ha with several prominent mountain peaks. The area is of outstanding beauty and is home to one of the highest waterfalls in Malaysia, the seven-tiered Jelawang Waterfall.")
''')
cursor.execute('''
	INSERT INTO places(state, location, name, address, description)
	VALUES("12", "Rembau", "Rembau Crystal ", "Kampung Senama, 71300 Rembau, Negeri Sembilan", "You can shop for a wide variety of hand-crafted crystal products such as vases, bowls, candy dishes and decorative items at Rembau Crystal. This one-stop centre houses a sales gallery as well as a production and training centre. After your visit, you can drop by at nearby attractions like the Pedas Hotspring, Gunung Datuk Recreational Forest or the Sungai Timun Fireflies")
''')

cursor.execute('''
	INSERT INTO places(state, location, name, address, description)
	VALUES("13", "Kangar", "Snake and Reptile Farm", "Sungai Batu Pahat, Perlis, 01000, Kangar, Perlis", "The Snake and Reptile Farm in Perlis is the only Snake Farm ever built in Malaysia. The farm is the major tourist attraction not only in Perlis, but the entire country, Malaysia. The main objective of the establishment of the Snake and Reptile Farm is to aid in the research in the production of anti - venom for local consumption by the Institute of Medical Research in Malaysia. It was established with a showcase of about 200 snakes of 34 different species from Malaysia and also the other parts of the world including King Cobra and python. Out of the 34 species, there are a total of 10 species that is poisonous.")
''')

db.commit()
db.close()
