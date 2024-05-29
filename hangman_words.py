#Save file as hangman_words.py

random_words=[("candle","A block of wax which gives light."),
              ("magnet","A piece of iron or other material that can attract other iron materials."),
              ("satchel","A bag carried on the shoulder by a long strap and closed by a flap."),
              ("backpack","A piece of equipment carried on a person's back."),
              ("dice","A small cube with each side having a different number of spots on it,* ranging from one to six."),
              ("padlock","A detachable lock hanging by a pivoted hook on the object fastened."),
              ("letter","A written, typed, or printed communication, sent in an envelope by post* or messenger."),
              ("microscope","An optical instrument used for viewing very small objects."),
              ("balloon","A small coloured rubber bag which is inflated with air and then sealed* at the neck."),
              ("breifcase","A leather or plastic rectangular container with a handle for carrying* books and documents."),
              ("shopping","The action or activity of buying goods from shops."),
              ("globe","A spherical representation of the earth."),
              ("duffel","A sporting or camping equipment."),
              ("sword","A weapon with a long metal blade and a hilt."),
              ("luggage","Suitcases or other bags in which to pack personal belongings for* travelling.")]

eng_movies=[("gladiator","""Commodus takes over power and demotes Maximus,one of the preferred* generals of his father, Emperor Marcus Aurelius. As a result,Maximus* is relegated to fighting tilldeath as a gladiator."""),
        ("predator","""Dutch and his team are out on a mission to rescue a group of hostages* in Central America.There, they discover that they are being targeted by* an extraterrestrial warrior."""),
        ("frozen","""Anna sets out on a journey with an iceman, Kristoff, and his reindeer,* Sven,in order to find her sister, Elsa, who has the power to convert* any object or person into ice."""),
        ("avengers","Loki poses a threat to planet Earth. A squad of superheroes put their* minds together to accomplish the task."),
        ("dodgeball","""An average guy is out to save his gym by participatingin a dodgeball* championship. His debts along with his misfit friends prove to be quite* a headache."""),
        ("zoolander","""Derek, a model, loses hope when his rival wins a coveted title.* In abid to revive his career, a designer offers him a runway show but* ends up convincing him to kill the prime minister of Malaysia."""),
        ("ghostbusters","""Paranormal enthusiasts Abby, Erin, Jillian and Patty set outto capture* ghosts when they realise that someone is attempting to cause an* apocalypse by summoning ghosts in the City of New York."""),
        ("titanic","""Seventeen-year-old Rose hails from an aristocratic family and is set* to be married. When she boards the Titanic, she meets Jack Dawson,* an artist, and falls in love with him."""),
        ("ring","""After her niece, Katie's horrifying death, Rachel, a young journalist,* investigates a mysterious videotape that kills its viewers within a* week's time."""),
        ("divergent","""Tris, an adult resident of a futuristic world divided into five* factions, elects to join the Dauntless faction. But she actually* belongs to another faction, which she must hide, as a major war looms."""),
        ("scream","""A year after Sidney's mom is murdered, more murders start to occur.* She begins to suspect if these murders are related and tries to find* the killer as everyone seems to be a suspect."""),
        ("annabel","""John and Mia are attacked by a couple, who are worshippers of Satan.* However, before the cops kill them, the couple use a doll as a conduit* to make John and Mia's life miserable."""),
        ("conjuring","""The Perron family moves into a farmhouse where they experience* supernatural phenomena. However, they consult demonologists,Ed and* Lorraine, to help them get rid of the evil entity haunting them."""),
        ("joker","""Forever alone in a crowd, failed comedian Arthur Fleck seeks* connection as he walks the streets of Gotham City. Arthur wears two* masks -- the one he paints for his day job as a clown, and the guise* he projects in a futile attempt to feel like he's part of the world* around him. Isolated, bullied and disregarded by society, Fleck begins* a slow descent into madness as he transforms into the criminal* mastermind known as the Joker."""),
        ("chinatown","""Mrs Mulwray hires Detective Jake, who specializes in matrimonial* cases, to spy on her husband, the builder of the city's water system.* He finds himself in a web of deceit when Mr Mulwray dies.""")]

hindi_movies=[("dabbang","""Chulbul Pandey is a cop who has his own way of dealing with corruption.* His detractor Cheddi Singh manages to create a rift between Chulbul* and his step-brother and uses it to his advantage."""),
              ("zero","""Bauua, a person of short stature, falls in love with Aafia,a scientist* suffering from cerebral palsy, but soon breaks up with her. Later,* what he learns of Aafia changes his life forever."""),
              ("malang","""Advait visits Goa where he meets Sara, a free-spirited girl who lives* life unshackled. Opposites attract and all goes well until life turns* upside down. Years later, Advait is on a killing spree with cops* Aghase and Michael in his way."""),
              ("hero","""Sooraj, the son of gangster Suryakant Pasha, kidnaps Radha, the* daughter of the chief of police. They fall in love after spending some* time together but the police and Pasha's men try to catch them."""),
              ("race","""Two stepbrothers own a huge stud farm and a horse racing business.* When they learn that they have a common love interest, one of them* tries to kill the other and inherit the insurance money."""),
              ("dhoom","""A gang of bikers are on a robbing spree and infuse terror in the* city. In order to nab the perpetrators, ACP Jai teams up with Ali,* a mechanic."""),
              ("fanaa","""Against the advice of her friends, Zooni, a visually impaired Kashmiri* girl, falls in love with a tourist guide, Rehan. He helps her get her* eyesight back but she remains unaware of his true identity."""),
              ("raees","""Threat looms over bootlegger Raees Alam and his business after ACP* Majmudar decides to get the better of him. In order to survive and* keep his trade thriving, Raees must overcome Majumdar."""),
              ("golmaal","""A man falls in love with a beautiful woman, Purva, but he realises* that his room-mate also loves her. Things get stranger when two more* men fall in love with Purva and start competing with them."""),
              ("padmaavat","""Queen Padmavati is happily married to a Rajput ruler until a tyrant* Sultan, Alauddin Khilji, enters their life and calls a war on their* kingdom due to his obsession with the queen."""),
              ("kick","""Devi, a man who cannot stay put as he is addicted to going on new* adventures, breaks up with his girlfriend, Shaina, who is *a Warsaw-based psychiatrist, just to pursue his daredevil ambitions."""),
              ("hungama","""A millionaire businessman living in a village decides to move to the* city with his wife. They soon get into a case of mistaken identity* that results in comical situations."""),
              ("lagaan","""During the British Raj, a farmer named Bhuvan accepts the challenge* of Captain Andrew Russell to beat his team in a game of cricket and* enable his village to not pay taxes for the next three years."""),
              ("bahubali","""In the kingdom of Mahishmati, Shivudu falls in love with a fair maiden.* While trying to woo her, he learns about the conflict-ridden past of* his family and his true legacy."""),
              ("ready","""Prem believes Sanjana is the girl chosen by his dad and falls in love* with her. On learning the truth, he devises a plan to win her over from* her mafia uncles who intend to usurp her huge inheritance.""")]





