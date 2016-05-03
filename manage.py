import os

from flask.ext.script import Manager

from stamps import app, models
from stamps.database import session


manager = Manager(app)

@manager.command
def seed():
    """ seed DB with dummy entries """
    print('start seed')
    al_stamp = models.Stamp(stamp_url="/static/images/States/alabama-stamp.jpg",
                     stamp_name="alabama-stamp",
                     tags="state, alabama",
                     blurb="This is the Alabama state stamp."
                     )
    session.add(al_stamp)
    ak_stamp = models.Stamp(stamp_url="/static/images/States/alaska-stamp.jpg",
                     stamp_name="alaska-stamp",
                     tags="state, alaska",
                     blurb="This is the Alaska state stamp."
                     )
    session.add(ak_stamp)
    az_stamp = models.Stamp(stamp_url="/static/images/States/arizona-stamp.jpg",
                     stamp_name="arizona-stamp", 
                     tags="state, arizona",
                     blurb="This is the Arizona state stamp."
                     )
    session.add(az_stamp)
    ar_stamp = models.Stamp(stamp_url="/static/images/States/arkansas-stamp.jpg",
                     stamp_name="arkansas-stamp", 
                     tags="state, arkansas",
                     blurb="This is the Arkansas state stamp."
                     )
    session.add(ar_stamp)
    ca_stamp = models.Stamp(stamp_url="/static/images/States/california-stamp.jpg",
                     stamp_name="california-stamp", 
                     blurb="This is the California state stamp.",
                     tags="state, california"
                     )
    session.add(ca_stamp)
    co_stamp = models.Stamp(stamp_url="/static/images/States/colorado-stamp.jpg",
                     stamp_name="colorado-stamp", 
                     blurb="This is the Colorado state stamp.",
                     tags="state, colorado"
                     )
    session.add(co_stamp)
    ct_stamp = models.Stamp(stamp_url="/static/images/States/connecticut-stamp.jpg",
                     stamp_name="connecticut-stamp", 
                     blurb="This is the Connecticut state stamp.",
                     tags="state, connecticut")
    session.add(ct_stamp)
    de_stamp = models.Stamp(stamp_url="/static/images/States/delaware-stamp.jpg",
                     stamp_name="delaware-stamp", 
                     blurb="This is the Delaware state stamp.",
                     tags="state, delaware")
    session.add(de_stamp)
    fl_stamp = models.Stamp(stamp_url="/static/images/States/florida-stamp.jpg",
                     stamp_name="florida-stamp", 
                     blurb="This is the Florida state stamp.",
                     tags="state, florida")
    session.add(fl_stamp)
    ga_stamp = models.Stamp(stamp_url="/static/images/States/georgia-stamp.jpg",
                     stamp_name="georgia-stamp", 
                     blurb="This is the Georgia state stamp.",
                     tags="state, georgia")
    session.add(ga_stamp)
    hi_stamp = models.Stamp(stamp_url="/static/images/States/hawaii-stamp.jpg",
                     stamp_name="hawaii-stamp", 
                     blurb="This is the Hawaii state stamp.",
                     tags="state, hawaii")
    session.add(hi_stamp)
    id_stamp = models.Stamp(stamp_url="/static/images/States/idaho-stamp.jpg",
                     stamp_name="idaho-stamp", 
                     blurb="This is the Idaho state stamp.",
                     tags="state,idaho")
    session.add(id_stamp)
    il_stamp = models.Stamp(stamp_url="/static/images/States/illinois-stamp.jpg",
                    stamp_name="illinois-stamp",
                    blurb="This is the Illinois state stamp.",
                    tags="state, illinois"
                    )
    session.add(il_stamp)
    in_stamp = models.Stamp(stamp_url="/static/images/States/indiana-stamp.jpg",
                     stamp_name="indiana-stamp", 
                     blurb="This is the Indiana state stamp.",
                     tags="state, indiana")
    session.add(in_stamp)
    ia_stamp = models.Stamp(stamp_url="/static/images/States/iowa-stamp.jpg",
                     stamp_name="iowa-stamp", 
                     blurb="This is the Iowa state stamp.",
                     tags="state, iowa")
    session.add(ia_stamp)
    ks_stamp = models.Stamp(stamp_url="/static/images/States/kansas-stamp.jpg",
                     stamp_name="kansas-stamp", 
                     blurb="This is the Kansas state stamp.",
                     tags="state, kansas")
    session.add(ks_stamp)
    ky_stamp = models.Stamp(stamp_url="/static/images/States/kentucky-stamp.jpg",
                     stamp_name="kentucky-stamp",
                     blurb="This is the Kentucky state stamp.",
                     tags="state, kentucky")
    session.add(ky_stamp)
    la_stamp = models.Stamp(stamp_url="/static/images/States/louisiana-stamp.jpg",
                     stamp_name="louisiana-stamp", 
                     blurb="This is the Louisiana state stamp.",
                     tags="state, lousiana")
    session.add(la_stamp)
    me_stamp = models.Stamp(stamp_url="/static/images/States/maine-stamp.jpg",
                     stamp_name="maine-stamp", 
                     blurb="This is the Maine state stamp.",
                     tags="state, maine")
    session.add(me_stamp)
    md_stamp = models.Stamp(stamp_url="/static/images/States/maryland-stamp.jpg",
                     stamp_name="maryland-stamp", 
                     blurb="This is the Maryland state stamp.",
                     tags="state, maryland")
    session.add(md_stamp)
    ma_stamp = models.Stamp(stamp_url="/static/images/States/massachusetts-stamp.jpg",
                     stamp_name="massachusetts-stamp", 
                     blurb="This is the Massachusetts state stamp.",
                     tags="state, massachusetts")
    session.add(ma_stamp)
    mi_stamp = models.Stamp(stamp_url="/static/images/States/michigan-stamp.jpg",
                     stamp_name="michigan-stamp", 
                     blurb="This is the Michigan state stamp.",
                     tags="state, michigan")
    session.add(mi_stamp)
    mn_stamp = models.Stamp(stamp_url="/static/images/States/minnesota-stamp.jpg",
                     stamp_name="minnesota-stamp", 
                     blurb="This is the Minnesota state stamp.",
                     tags="state, minnesota")
    session.add(mn_stamp)
    ms_stamp = models.Stamp(stamp_url="/static/images/States/mississippi-stamp.jpg",
                     stamp_name="mississippi-stamp", 
                     blurb="This is the Mississippi state stamp.",
                     tags="state, mississippi")
    session.add(ms_stamp)
    mo_stamp = models.Stamp(stamp_url="/static/images/States/missouri-stamp.jpg",
                     stamp_name="missouri-stamp", 
                     blurb="This is the Missouri state stamp.",
                     tags="state, missouri")
    session.add(mo_stamp)
    mt_stamp = models.Stamp(stamp_url="/static/images/States/Montana-stamp.jpg".lower(),
                     stamp_name="Montana-stamp".lower(), 
                     blurb="This is the Montana state stamp.",
                     tags="state, montana")
    session.add(mt_stamp)
    ne_stamp = models.Stamp(stamp_url="/static/images/States/Nebraska-stamp.jpg".lower(),
                     stamp_name="Nebraska-stamp".lower(), 
                     blurb="This is the Nebraska state stamp.",
                     tags="state, nebraska")
    session.add(ne_stamp)
    nv_stamp = models.Stamp(stamp_url="/static/images/States/Nevada-stamp.jpg".lower(),
                     stamp_name="Nevada-stamp".lower(), 
                     blurb="This is the Nevada state stamp.",
                     tags="state, nevada")
    session.add(nv_stamp)
    nh_stamp = models.Stamp(stamp_url="/static/images/States/NewHampshire-stamp.jpg".lower(),
                     stamp_name="New Hampshire-stamp".lower(), 
                     blurb="This is the New Hampshire state stamp.",
                     tags="state, new hampshire")
    session.add(nh_stamp)
    nj_stamp = models.Stamp(stamp_url="/static/images/States/NewJersey-stamp.jpg".lower(),
                     stamp_name="New Jersey-stamp".lower(), 
                     blurb="This is the New Jersey state stamp.",
                     tags="state, new jersey")
    session.add(nj_stamp)
    nm_stamp = models.Stamp(stamp_url="/static/images/States/NewMexico-stamp.jpg".lower(),
                     stamp_name="New Mexico-stamp".lower(), 
                     blurb="This is the New Mexico state stamp.",
                     tags="state, new mexico")
    session.add(nm_stamp)
    ny_stamp = models.Stamp(stamp_url="/static/images/States/NewYork-stamp.jpg".lower(),
                     stamp_name="New York-stamp".lower(), 
                     blurb="This is the New York state stamp.",
                     tags="state, new york")
    session.add(ny_stamp)
    nc_stamp = models.Stamp(stamp_url="/static/images/States/NorthCarolina-stamp.jpg".lower(),
                     stamp_name="North Carolina-stamp".lower(), 
                     blurb="This is the North Carolina state stamp.",
                     tags="state, north carolina")
    session.add(nc_stamp)
    nd_stamp = models.Stamp(stamp_url="/static/images/States/NorthDakota-stamp.jpg".lower(),
                     stamp_name="North Dakota-stamp".lower(), 
                     blurb="This is the North Dakota state stamp.",
                     tags="state, north dakota")
    session.add(nd_stamp)
    oh_stamp = models.Stamp(stamp_url="/static/images/States/Ohio-stamp.jpg".lower(),
                     stamp_name="Ohio-stamp".lower(), 
                     blurb="This is the Ohio state stamp.",
                     tags="state, ohio")
    session.add(oh_stamp)
    ok_stamp = models.Stamp(stamp_url="/static/images/States/Oklahoma-stamp.jpg".lower(),
                     stamp_name="Oklahoma-stamp".lower(), 
                     blurb="This is the Oklahoma state stamp.",
                     tags="state, oklahoma")
    session.add(ok_stamp)
    or_stamp = models.Stamp(stamp_url="/static/images/States/Oregon-stamp.jpg".lower(),
                     stamp_name="Oregon-stamp".lower(), 
                     blurb="This is the Oregon state stamp.",
                     tags="state, oregon")
    session.add(or_stamp)
    pa_stamp = models.Stamp(stamp_url="/static/images/States/Pennsylvania-stamp.jpg".lower(),
                     stamp_name="Pennsylvania-stamp".lower(), 
                     blurb="This is the Pennsylvania state stamp.",
                     tags="state, pennsylvania")
    session.add(pa_stamp)
    ri_stamp = models.Stamp(stamp_url="/static/images/States/RhodeIsland-stamp.jpg".lower(),
                     stamp_name="Rhode Island-stamp".lower(), 
                     blurb="This is the Rhode Island state stamp.",
                     tags="state, rhode island")
    session.add(ri_stamp)
    sc_stamp = models.Stamp(stamp_url="/static/images/States/SouthCarolina-stamp.jpg".lower(),
                     stamp_name="South Carolina-stamp".lower(), 
                     blurb="This is the South Carolina state stamp.",
                     tags="state, south carolina")
    session.add(sc_stamp)
    sd_stamp = models.Stamp(stamp_url="/static/images/States/SouthDakota-stamp.jpg".lower(),
                     stamp_name="South Dakota-stamp".lower(), 
                     blurb="This is the South Dakota state stamp.",
                     tags="state, south dakota")
    session.add(sd_stamp)
    tn_stamp = models.Stamp(stamp_url="/static/images/States/Tennessee-stamp.jpg".lower(),
                     stamp_name="Tennessee-stamp".lower(), 
                     blurb="This is the Tennessee state stamp.",
                     tags="state, tennessee")
    session.add(tn_stamp)
    tx_stamp = models.Stamp(stamp_url="/static/images/States/Texas-stamp.jpg".lower(),
                     stamp_name="Texas-stamp".lower(), 
                     blurb="This is the Texas state stamp.",
                     tags="state, texas")
    session.add(tx_stamp)
    ut_stamp = models.Stamp(stamp_url="/static/images/States/Utah-stamp.jpg".lower(),
                     stamp_name="Utah-stamp".lower(), 
                     blurb="This is the Utah state stamp.",
                     tags="state, utah")
    session.add(ut_stamp)
    vt_stamp = models.Stamp(stamp_url="/static/images/States/Vermont-stamp.jpg".lower(),
                     stamp_name="Vermont-stamp".lower(), 
                     blurb="This is the Vermont state stamp.",
                     tags="state, vermont")
    session.add(vt_stamp)
    va_stamp = models.Stamp(stamp_url="/static/images/States/Virginia-stamp.jpg".lower(),
                     stamp_name="Virginia-stamp".lower(), 
                     blurb="This is the Virginia state stamp.",
                     tags="state, virginia")
    session.add(va_stamp)
    wa_stamp = models.Stamp(stamp_url="/static/images/States/Washington-stamp.jpg".lower(),
                     stamp_name="Washington-stamp".lower(), 
                     blurb="This is the Washington state stamp.",
                     tags="state, washington")
    session.add(wa_stamp)
    wv_stamp = models.Stamp(stamp_url="/static/images/States/WestVirginia-stamp.jpg".lower(),
                     stamp_name="West Virginia-stamp".lower(), 
                     blurb="This is the West Virginia state stamp.",
                     tags="state, west virginia")
    session.add(wv_stamp)
    wi_stamp = models.Stamp(stamp_url="/static/images/States/Wisconsin-stamp.jpg".lower(),
                     stamp_name="Wisconsin-stamp".lower(), 
                     blurb="This is the Wisconsin state stamp.",
                     tags="state, wisconsin")
    session.add(wi_stamp)
    wy_stamp = models.Stamp(stamp_url="/static/images/States/Wyoming-stamp.jpg".lower(),
                     stamp_name="Wyoming-stamp".lower(), 
                     blurb="This is the Wyoming state stamp.",
                     tags="state, wyoming")
    session.add(wy_stamp)
   
    q1 = models.Question(category="US Presidents", 
        image="/static/images/Presidents/1c6637a8f2e1f75e06ff9984894d6bd16a3a36a9.gif",
        body="Abraham Lincoln, the 16th U.S. President, is known for which famous speech that endorsed the principles of nationalism, equal rights, liberty, and democracy?",
        correct_answer="Gettysburg Address", 
        answers="Farewell Address,\"I Have A Dream\" Speech,\"We Shall Overcome\" Speech"
        )
    session.add(q1)
    q2 = models.Question(category="US Presidents", 
        image="/static/images/Presidents/fe2fb474076a872e237e4430d40cbed150d20033.gif",
        body="Grover Cleveland is the only U.S. president who\'s time in office included which of the following?",
        correct_answer="Non-Consecutive Terms", 
        answers="A 2-year Term,An Unappointed Cabinet,No Vice President"
        )
    session.add(q2)
    
    q3 = models.Question(category="US Presidents", 
        image="/static/images/Presidents/dad39ce1a0f516e191b0b515ea02e6cbc4ea76b6.gif",
        body="After his death,  President Warren G. Harding\'s popular regard was diminished by revelations of his affair with a mistress by what name?",
        correct_answer="Nan Britton", 
        answers="Dorothy Parker,Mary Schlesinger,Florence Smith"
        )
    session.add(q3)
					
    q4 = models.Question(category="US Presidents", 
        image="/static/images/Presidents/a1eb7ce1b3132d269f15acd9c978c481c9389506.gif",
        body="Thomas Jefferson was an American Founding Father and the third President of the United States. He is known for his involventment in all BUT which of the following?",
        correct_answer="Flying a kite in a storm", 
        answers="Louisiana Purchase,Lewis and Clark Expedition,Declaration of Independence"
        )
    session.add(q4)
    				
    q5 = models.Question(category="US Presidents", 
        image="/static/images/Presidents/8c12d571138fce48a15ab55d1234f359312ea78f.gif",
        body="John Fitzgerald Kennedy (JFK), served as the 35th President of the United States until his assassination in November, 1963, which was charged to what man?",
        correct_answer="Lee Harvey Oswald", 
        answers="James Michael Curley,Peter Bent Brigham,James Forrestal"
        )
    session.add(q5)
    q6 = models.Question(category="US Presidents", 
        image="/static/images/Presidents/91b92669ecf0fa9c6e550fd5fd76c31b5c969f57.gif",
        body="President Andrew Jackson is known for having signed the Indian Removal Act, which relocated a number of native tribes to 'Indian Territory' - which now the site of which U.S. state?",
        correct_answer="Oklahoma", 
        answers="Nebraska,Kansas,Arkansas"
        )
    session.add(q6)
    q7 = models.Question(category="US Presidents", 
        image="/static/images/Presidents/e6cfa8e4a054b888d7a80898d1a7092aa631a302.gif",
        body="President Lyndon B. Johnson acted on the Gulf of Tonkin Resolution, which allowed authorization, without a formal declaration of war by Congress, for the use of military force in Southeast Asia. This escalated what conflict?",
        correct_answer="Vietnam War", 
        answers="Korean War,Gulf War,Iraq War"
        )
    session.add(q7)
    q8 = models.Question(category="US Presidents", 
        image="/static/images/Presidents/9a6aa8b8b6919d3b97d0f40c9eda85f5523c7dd2.gif",
        body="The neoclassical memorial building pictured on this stamp resides on the of the Potomac River in Washington D.C and celebrates which president?",
        correct_answer="Thomas Jefferson", 
        answers="John Adams,George Washington,Theodore Roosevelt"
        )
    session.add(q8)
    					
    q9 = models.Question(category="US Presidents", 
        image="/static/images/Presidents/37585335691c5a6647266cf0d14de500031ffb07.gif",
        body="Harry S. Truman was president during the final months of World War II. He ultimately made the decision to to drop atomic bombs on which Japanese cities?",
        correct_answer="Hiroshima & Nagasaki", 
        answers="Toyohashi & Okazaki,Toyokawa & Nishio,Shinshiro & Takahama"
        )
    session.add(q9)
    					
    q10 = models.Question(category="US Presidents", 
        image="/static/images/Presidents/6cb25e858ae8ea2e3c48218c3c9cc0bd41fc282e.gif",
        body="William Howard Taft is the only person to have held the U.S. Presidency and which other position?",
        correct_answer="Chief Justice of the Supreme Court", 
        answers="Secretary of State,Secretary of the Treasury,U.S Ambassador"
        )
    session.add(q10)
    q11 = models.Question(category="US Presidents", 
        image="/static/images/Presidents/67f931e7075791871f56d3576c8dcb1f35125aef.gif",
        body="	President Theodore Roosevelt was an American statesman, author, explorer, soldier, naturalist, and reformer. He was known for his involvement in all BUT which of the following?",
        correct_answer="The New Deal", 
        answers="National Parks,Panama Canal,Progressive Era"
        )
    session.add(q11)
    q12 = models.Question(category="US Presidents", 
        image="/static/images/Presidents/896d2d7e498c779570c0af418a07ce12370afa22.gif",
        body="A leading force in the Progressive Movement, President Wilson, enacted which of the following bills which created a centralized banking system in the U.S.?",
        correct_answer="Federal Reserve Act", 
        answers="Clayton Antitrust Act,Adamson Act,Federal Farm Loan Act"
        )
    session.add(q12)
    q13 = models.Question(category="Movies", 
        image="/static/images/Movies/21188f1974ee9a6a79de64dee0fc849629de3181.gif",
        body="Which character in the 1939 Wizard of Oz movie is searching for a heart?",
        correct_answer="The Tin Man", 
        answers="The Scarecrow,The Cowardly Lion,The Wicked Witch of The West"
        )
    session.add(q13)
    			 		
    q14 = models.Question(category="Movies", 
        image="/static/images/Movies/4a6bfd1995bc16264467895891165bd2fc50fe95.gif",
        body="What is the name of Scarlett O'Hara's plantation home in the movie Gone with the Wind?",
        correct_answer="Tara", 
        answers="Willow Oaks,Twelve Oaks,Rosedale"
        )
    session.add(q14)		
    q15 = models.Question(category="Movies", 
        image="/static/images/Movies/c7b3f6f6411d271ebab2b3b0e90d317acc95d9a8.gif",
        body="Clara Bow became know as the \"It Girl\" for her portrayal of a wide-eyed, carefree flapper in the 1927 film called _______.",
        correct_answer="It", 
        answers="Some Like it Hot,Mantrap,Wings"
        )
    session.add(q15)

    q16 = models.Question(category="Movies", 
        image="/static/images/Movies/afbebe5f5afca9b5f2460bc54e431a84eb8fc797.gif",
        body="Which actor was the star of the 1939 classic film Stagecoach?",
        correct_answer="John Wayne", 
        answers="Clark Gable,Cary Grant,Gary Cooper"
        )
    session.add(q16)		
    q17 = models.Question(category="Movies", 
        image="/static/images/Movies/8304c52b0c2b67372d5dcbe998ee4e04271275d6.gif",
        body="How many actors were in the original Keystone Cops gang?",
        correct_answer="7", 
        answers="9,8,10"
        )
    session.add(q17)
		
    q18 = models.Question(category="Movies", 
        image="/static/images/Movies/887705229a4a68507120316cfc13273e1c3777e1.gif",
        body="What was Humphrey Bogart's character's name in the 1942 film Casablanca?",
        correct_answer="Rick Blaine", 
        answers="Victor Laszlo,Captain Louis Renault,Major Heinrich Strasser"
        )
    session.add(q18)

    q19 = models.Question(category="Movies", 
        image="/static/images/Movies/d5807d3d1a8ff7466ec43cdafce556cb79e048a7.gif",
        body="James Dean famously played the troubled high school rebel, Jim Stark, in which movie?",
        correct_answer="Rebel Without a Cause", 
        answers="East of Eden,Giant,A Place in the Sun"
        )
    session.add(q19)
    q20 = models.Question(category="Movies", 
        image="/static/images/Movies/b749475c2b2f437d28cf26bdf900e04569fed62c.gif",
        body="What was Marilyn Monroe's birth name?",
        correct_answer="Norma Jean Baker", 
        answers="Betty Sue,Mary Monroe,Mary Baker"
        )
    session.add(q20)
    q21 = models.Question(category="Movies", 
        image="/static/images/Movies/2145c3e7ce74ef291f7254708749ad33403111fc.gif",
        body="Who was the author of the novel Frankenstein, which later inspired the 1931 movie of the same name?",
        correct_answer="Mary Shelley", 
        answers="Elizabeth Frankenstien,Peggy Webling,Mae Clark"
        )
    session.add(q21)
    q22 = models.Question(category="Movies", 
        image="/static/images/Movies/fe85b11fb29ae3cf6ca9eaaa025972868e628b58.gif",
        body="Where is Count Dracula\'s castle in the 1931 classic movie, Dracula?",
        correct_answer="Transylvania", 
        answers="Moscow,Urkraine,Leverkusen"
        )
    session.add(q22)
		
    q23 = models.Question(category="Movies", 
        image="/static/images/Movies/a6dec37d42e59d8151f675151f0ace42ac4b62ab.gif",
        body="Which previously unknown dancer does the Phantom of the Opera fall in love with in the 1925 film?",
        correct_answer="Christine Daae", 
        answers="Carlotta,Florine Papillon,Martha Sorelli"
        )
    session.add(q23)

    q24 = models.Question(category="Movies", 
        image="/static/images/Movies/71dc6756f12fbd64df82b2f05f4bbe849955f4b6.gif",
        body="Which is NOT a name of one of the seven dwarfs from the 1937 movie, Snow White and the Seven Dwarfs?",
        correct_answer="Crabby", 
        answers="Grumpy,Doc,Happy "
        )
    session.add(q24)
    			 		
    q25 = models.Question(category="Movies", 
        image="/static/images/Movies/c681a9f6a3b9d51502cc3978298feaccfa9f500b.gif",
        body="The 'Master of Suspense', Alfred Hitchcock directed all BUT which of the following movies?",
        correct_answer="Seven", 
        answers="Psycho,The Birds,Vertigo"
        )
    session.add(q25)

    q26 = models.Question(category="Movies", 
        image="/static/images/Movies/d42aa23e70c6bfa11686bb84f806911254d7efe7.gif",
        body="Who directed 'Citizen Kane' - which many critics often consider the greatest movie of all time?",
        correct_answer="Orson Welles", 
        answers="Alfred Hitchcock,Steven Spielberg,Stanley Kubrick"
        )
    session.add(q26)
	
    q27 = models.Question(category="Movies", 
        image="/static/images/Movies/46fcf77e89e78e2542f731a169874088b1083df5.gif",
        body="Released in 1952, what was the first color, stereoscopic film which began the Golden Era of 3-D films that continued through 1955?",
        correct_answer="Bwana Devil", 
        answers="M.A.R.S.,Zowie,Luna-cy!"
        )
    session.add(q27)
    q28 = models.Question(category="Movies", 
        image="/static/images/Movies/1088946f2cf58dcd71526b2abf76d2c3e06c1540.jpg",
        body="Which Looney Tunes character had the signature catch phrase \"That's All Folks!\"?",
        correct_answer="Porkey Pig", 
        answers="Daffy Duck,Bugs Bunny,Taz"
        )
    session.add(q28)
    q29 = models.Question(category="Movies", 
        image="/static/images/Movies/6c93fba6b2c44ae4dddd4f9639bee1879c82b844.gif",
        body="Who was the director of the 1997 film \"Titanic\" starring Leonard DiCaprio and Kate Winslet?",
        correct_answer="James Cameron", 
        answers="Christopher Nolan,Steven Spielberg,Francis Ford Coppola"
        )
    session.add(q29)
    q30 = models.Question(category="Movies", 
        image="/static/images/Movies/5ad6e8090db37c5ac6442ec6020f137fa1cf488c.jpg",
        body="	What is the name of the ship piloted by Han Solo and Chewy in the Star Wars movie series?",
        correct_answer="Millenium Falcon", 
        answers="Death Star,AT-PT Transport,A-wing Fighter"
        )
    session.add(q30)
    q31 = models.Question(category="Movies", 
        image="/static/images/Movies/a5f8c3d3e27f636b039ada0aa8340c1a3c1c5192.jpg",
        body="What is Darth Vader's birth name, which is revealed in Star Wars: Episode VI - Return of the Jedi (1983)?",
        correct_answer="Anakin Skywalker", 
        answers="Han Solo,Luke Skywalker,R2D2"
        )
    session.add(q31)
    q32 = models.Question(category="Movies", 
        image="/static/images/Movies/825b0d4d0156775d1fb9855ffae9f3356a7b9e38.jpg",
        body="What is Buzz Lightyear's signature catch phrase from the 1995 movie Toy Story?",
        correct_answer="to infinity and beyond!\"", 
        answers="\"say hello to my little friend\",\"Good morning, Vietnam\",\"Welcome to Earth\""
        )
    session.add(q32)
    q33 = models.Question(category="Movies", 
        image="/static/images/Movies/35fce2922f24443bc0fddfdee94d6a9a68fe6e7e.jpg",
        body="Harry Potter and Ron Weasley are members of what house at Hogwarts School of Witchcraft and Wizardry?",
        correct_answer="Gryffindor", 
        answers="Ravenclaw,Hufflepuff,Slytherin"
        )
    session.add(q33)
    q34 = models.Question(category="Movies", 
        image="/static/images/Movies/60ed93e091c0c7cd056fa172586870ff0ca3327b.jpg",
        body="Which house elf, first appearing in Harry Potter and the Chamber of Secrets (2002), is pictured here?",
        correct_answer="Dobby", 
        answers="Kreacher,Winky,Albus"
        )
    session.add(q34)

    q35 = models.Question(category="Aviation", 
        image="/static/images/Aviation/ac2dd3c1c9c32527df42f41d3d7ec9de22ce25a0.gif",
        body="Born in 1898, Amelia Earhart was the first female aviator to fly solo across which body of water?",
        correct_answer="Atlantic Ocean", 
        answers="Pacific Ocean,Gulf of Mexico,English Channel "
        )
    session.add(q35)
    			 		
    q36 = models.Question(category="Aviation", 
        image="/static/images/Aviation/d2df16bee9d37212d9dc0a9709c3a8579fedcfff.gif",
        body="Charles Lindbergh, an American aviator, was the first person to make a solo flight across the Atlantic Ocean in 1927. What was the name of his plane?",
        correct_answer="Spirit of St. Louis", 
        answers="Piper Cub,The Tribute,Flying Jenny"
        )
    session.add(q36)		 		
    q37 = models.Question(category="Aviation", 
        image="/static/images/Aviation/74e41f208e021885e4023b11ffec786837599735.gif",
        body="Domestic U.S. Air Mail was formally established as a new class of service by the United States Post Office Department with the inauguration of the Washington-Philadelphia-New York route. This happened in what year?",
        correct_answer="1918", 
        answers="1924,1910,1906"
        )
    session.add(q37)
    q38 = models.Question(category="Aviation", 
        image="/static/images/Aviation/26a62281fb9dd58120e5e19c173915e47e040c7f.gif",
        body="Glenn Curtiss's most important contribution to aerodynamics is the movable control surface on the trailing edge of the airplane wing which permits a plane to roll. What is this surface called?",
        correct_answer="Aileron", 
        answers="Trunnion,Rotation Actuator,Downlock and Drag Brace"
        )
    session.add(q38)
    q39 = models.Question(category="Aviation", 
        image="/static/images/Aviation/6d4db6462de701a26efaad3bbc5f7207f2985405.gif",
        body="Alfred Victor Verville was an aviation pioneer and aircraft designer known for designing and developing nearly 20 aircraft. He specialized in which type of plane?",
        correct_answer="Flying Boats", 
        answers="Gliders,Rotarcraft,Unmanned Aerial Vehicles (UAEs)"
        )
    session.add(q39)
	 		
    q40 = models.Question(category="Aviation", 
        image="/static/images/Aviation/023965274d969e872243fe3cafbc9e7cc3d93768.gif",
        body="Blanche Stuart Scott, also known as 'Betty Scott', was an American woman aviator and became an the first offical, female test pilot during what year?",
        correct_answer="1910", 
        answers="1926,1900,1905"
        )
    session.add(q40)
			
    q41 = models.Question(category="Aviation", 
        image="/static/images/Aviation/df11c7b8a100ac08e2e13ec5a81f98e1a3e3fc6b.gif",
        body="Development of long-range,'flying-boat' aircraft cleared a major hurdle in the rapid transport of mail and passengers to parts of the world previously only accessible by ship. What is the name of one of the most famous types of these aircraft?",
        correct_answer="China Clipper", 
        answers="Paris Flyer,Rothko Runner,Frequent Flyer"
        )
    session.add(q41)
    q42 = models.Question(category="Aviation", 
        image="/static/images/Aviation/161b3433de41cf002e6ec4360a6393793ee80ff1.gif",
        body="On November 28, 1929, the first flight to the South Pole and back was launched by Richard E. Byrd and company. How many hours did the flight take?",
        correct_answer="19 hours", 
        answers="42 hours,30 hours,10 hours"
        )
    session.add(q42)

    q43 = models.Question(category="Aviation", 
        image="/static/images/Aviation/14cfbf1eb2d5520b647584e6214007da727c8995.gif",
        body="William T. Piper is known as \"the Henry Ford of Aviation\" for his design of which aircraft which is often compared to the first Model-T?",
        correct_answer="Piper J-3 Cub", 
        answers="MD-11,Twinengine DC-1,Heinkel HE 178"
        )
    session.add(q43)
		
    q44 = models.Question(category="Aviation", 
        image="/static/images/Aviation/074fe681c9742d991dc00dc287aba5094ff8c678.gif",
        body="Seaplanes were used in World War I for sea patrol and anti-submarine work. Instead of conventional wheeled landing gears, they are equipped with which landing device(s)?",
        correct_answer="Floats", 
        answers="Bogie,Rudder,Ailerons"
        )
    session.add(q44)
    	 		
    q45 = models.Question(category="Aviation", 
        image="/static/images/Aviation/dc92e340487067efda0c3e744ef03ad4bd590b96.gif",
        body="The P-51 Mustang was a World War II-era, long-range, single-seat fighter. It went on to be the principle fighter plane in which American conflict?",
        correct_answer="Korean War", 
        answers="Vietnam War,Gulf War,Bay of Pigs Invasion"
        )
    session.add(q45)
    q46 = models.Question(category="Aviation", 
        image="/static/images/Aviation/53dcadf721562d906250eff7346805b5a9414a5e.gif",
        body="Which famous pair of brothers were the first to design and build the early Model B in 1910? ",
        correct_answer="The Wright brothers", 
        answers="The Cohen brothers,The Kennedy brothers,The Klitschko brothers"
        )
    session.add(q46)
    q47 = models.Question(category="Aviation", 
        image="/static/images/Aviation/31343c4e5030fc96818376c598d111381a26bb17.jpg",
        body="Wilbur and Orville Wright were the inventors of the first successfully piloted, heavier-than-air airplane to achieve controlled, sustained flight. During this flight, the plane traveled 36 ft and flew for how many seconds?",
        correct_answer="12 seconds", 
        answers="121 seconds,83 seconds,6 seconds"
        )
    session.add(q47)
    q48 = models.Question(category="Science", 
        image="/static/images/Science/d4e1aca5dd0e4965a2a66e1256e5b25a346a759b.gif",
        body="Albert Einstein was a German-born theoretical physicist who developed the general theory of relativity, which is one of the two pillars of modern physics. What is the second pillar?",
        correct_answer="Quantum Mechanics", 
        answers="Newton's Method,Pauli Exclusion Principle,Natural Philosophy"
        )
    session.add(q48)
    		 			
    q49 = models.Question(category="Science", 
        image="/static/images/Science/0012e4f1dc0e5920644dc5eed874ce6baa7e25d7.gif",
        body="The Viking 1 was the first spacecraft to successfully land on Mars. It held the record for the longest Mars surface mission until it was broken by what spacecraft on May 19, 2010?",
        correct_answer="Opportunity Rover", 
        answers="Spirit,Mars Pathfinder,Viking 2"
        )
    session.add(q49)

    q50 = models.Question(category="Science", 
        image="/static/images/Science/8a03b737c40c35350adf1161eb6f2918439fec70.gif",
        body="In conventional photography, what is the name of the additive color model in which red, green, and blue light are added together in various ways to reproduce a broad array of colors?",
        correct_answer="RGB Model", 
        answers="CMYK Color Model,Visible Spectrum,Perception Model "
        )
    session.add(q50)
    q51 = models.Question(category="Science", 
        image="/static/images/Science/0f8eabfc55ec13950d6abb0e03e8f539eb8d0629.gif",
        body="Benjamin Banneker, born to a free black family in Maryland in 1731, was known for publishing painstakinly made tables of the positions of celestial bodies. These tables are called _______.",
        correct_answer="Ephemeris", 
        answers="Pivot tables,Sky maps,Parsecs"
        )
    session.add(q51)
    q52 = models.Question(category="Science", 
        image="/static/images/Science/1938b79762f018cf11cc7d1011b8157840d37e60.gif",
        body="What is the name of the method for converting solar energy into electricity by using semiconducting materials?",
        correct_answer="Photovoltaics", 
        answers="Hydropower,Fission,Incandescence"
        )
    session.add(q52)
    q53 = models.Question(category="Science", 
        image="/static/images/Science/7d96c64fe787fd03b289ac6f792269648348fab1.gif",
        body="Lillian Moller Gilbreth and her husband were efficiency experts who contributed to what scientific field which deals with motion studies, human factors and the optimization of complex systems?",
        correct_answer="Industrial Engineering", 
        answers="Astrology,Ergonomics,Biomechanics"
        )
    session.add(q53)
	 			
    q54 = models.Question(category="Science", 
        image="/static/images/Science/77047adb220c3c791f5ff69ed584ed3dbd78dbc4.gif",
        body="Nikola Tesla was a Serbian American inventor, electrical engineer, physicist, and futurist, best known for his contributions in designing what modern electricity supply system?",
        correct_answer="Alternating Current (AC)", 
        answers="Direct Current (DC),Thermodynamics,Thrombosis"
        )
    session.add(q54)
    q55 = models.Question(category="Science", 
        image="/static/images/Science/d8c61d3ce833b5e48b7d18a0dca5af34174f3f50.gif",
        body="The Egg Nebula is a bipolar protoplanetary nebula approximately how many light-years away from Earth?",
        correct_answer="3,000", 
        answers="50000,10 Bazillion,2"
        )
    session.add(q55)
				
    q56 = models.Question(category="Science", 
        image="/static/images/Science/82128953f6ed3ae729dd80bb3b748e4bd34b8816.gif",
        body="Alfred Nobel, the inventor of dynamite, was a renown chemist who bequeathed his fortune to institute the Nobel Prizes. What is his country of origin?",
        correct_answer="Sweden", 
        answers="Norway,Finland,Denmark"
        )
    session.add(q56)
    q57 = models.Question(category="Science", 
        image="/static/images/Science/d19ff2c8b8a40765e316fb33cd99d968c79ece1f.jpg",
        body="Barbara McClintock was an American geneticist who was awarded the Nobel Prize for her studies of child genetic traits that differ from those found in their parents. This area of study is called _______.",
        correct_answer="Genetic recombination", 
        answers="Statistical Mechanics,Thermodynamic Equilibrium,Fluid Dynamics"
        )
    session.add(q57)
    q58 = models.Question(category="Science", 
        image="/static/images/Science/95ad137911a723d1df6118522ab29da20e4cbfb4.gif",
        body="Enrico Fermi was an Italian physicist involved in the Manhattan Project and was the creator of the Chicago Pile-1, the world's first _______.",
        correct_answer="	Nuclear Reactor", 
        answers="Piston Engine,Printed Circuit Board,Microwave Oven"
        )
    session.add(q58)
    q59 = models.Question(category="Science", 
        image="/static/images/Science/c1ece8a30d07e86687eeb87ebf56b82d6a26f8af.jpg",
        body="Melvin Calvin was a Nobel Prize winning biochemist who studied the process used by plants and other organisms to convert light into energy. What is this process called?",
        correct_answer="Photosynthesis", 
        answers="Bioreacting,Catalysis,Digestion"
        )
    session.add(q59)
    q60 = models.Question(category="Olympics", 
        image="/static/images/Olympics/8b4078f9f76081a0c3ce5db983aa4f340ecd7531.gif",
        body="A fast and dangerous sport, bobsledding involves two or four persons maneuvering a bobsled down a winding ice track around what top speed?",
        correct_answer="90 mph", 
        answers="45 mph,120 mph,200 mph"
        )
    session.add(q60)
    					
    q61 = models.Question(category="Olympics", 
        image="/static/images/Olympics/6e0312072ad7e48b470123802c90755c690b7644.gif",
        body="Which is the most recent cycling event to be adopted into the Olympics as of 2008?",
        correct_answer="BMX Racing", 
        answers="Track Cycling,Road Cycling,Mountain Biking"
        )
    session.add(q61)

    q62 = models.Question(category="Olympics", 
        image="/static/images/Olympics/4e09628da925a6d474f1700841b7fdba51d53090.gif",
        body="The Olympic Games were a originally series of athletic competitions held in Greece begining around 776 BC. They first included all BUT which of the following events?",
        correct_answer="Pentathlon", 
        answers="Running with Armor,Chariot Race,Discos"
        )
    session.add(q62)
    	 			
    q63 = models.Question(category="Olympics", 
        image="/static/images/Olympics/aeef1b612c266fdbbd09ef5c274e670df0718ad7.gif",
        body="The decathlon is a combination of 10 track and field events, including all BUT which of the following events?",
        correct_answer="50-meter hurdles", 
        answers="Discus Throw,Long Jump,1500 meter run"
        )
    session.add(q63)

    q64 = models.Question(category="Olympics", 
        image="/static/images/Olympics/e5c24fef2e7ac4ea6e51308c08fbdcf083e70c20.gif",
        body="Though figure skating has been an Olympic event since 1908, what related event was adopted in the 1976 Winter Games?",
        correct_answer="Ice Dancing", 
        answers="Men's Special Figures,Mixed Pair Skating,Rhythm Skating"
        )
    session.add(q64)
	     		
    q65 = models.Question(category="Olympics", 
        image="/static/images/Olympics/cf70b1cc3fb8c74f6faf74b0d1ca03130b179c90.gif",
        body="The Special Olympics is the world's largest sports organization for children and adults with intellectual disabilities. The most recent 2015 Summer Games were held in what city?",
        correct_answer="Los Angeles", 
        answers="Atlanta,Seattle,Houston"
        )
    session.add(q65)
	    			
    q66 = models.Question(category="Olympics", 
        image="/static/images/Olympics/7ab78e36254ba7e5442d54cba1acc581f9540a41.gif",
        body="There are five alpine skiing disciplines in the World Cup iwhich include all BUT which of the following events?",
        correct_answer="Fall Line", 
        answers="Down Hill,Super Giant Slalom (super-G),Slalom Skiing"
        )
    session.add(q66)

    q67 = models.Question(category="Olympics", 
        image="/static/images/Olympics/6126a7a3c93822ec8f598f7a9ea7b49d925c8305.gif",
        body="After the IOC voted to approve women's hockey as an Olympic event, it was first held at the 1998 Winter Olympics in which city?",
        correct_answer="Nagano Japan", 
        answers="Toronto Canada,Gothenburg Sweden,Sarajevo Yugoslavia"
        )
    session.add(q67)
				
    q68 = models.Question(category="Olympics", 
        image="/static/images/Olympics/ce4018d383e97bdadf36c3ee5a2be5c11e191cef.gif",
        body="At the 2012 Summer Olympics held in London, which country won gold in men's soccer?",
        correct_answer="Mexico", 
        answers="Brazil,Japan,France"
        )
    session.add(q68)
		
    q69 = models.Question(category="Olympics", 
        image="/static/images/Olympics/66193dbb27155eb36deac4efe09db25ec38cf539.gif",
        body="The men's Olympic pole vaulting record, set by Renaud Lavillenie in 2012, stands at what height?",
        correct_answer="19 ft 7 in", 
        answers="35 ft 2 in,11 ft 9in,26 ft 1in"
        )
    session.add(q69)

    q70 = models.Question(category="Olympics", 
        image="/static/images/Olympics/4a67984f8d0fca27af38e2f50cc8bc252e072f49.gif",
        body="Olympic wrestling competitions are are divided by weight class into two categories: freestyle and ___________.",
        correct_answer="Greco-Roman", 
        answers="WWE,Arm Wrestling,Old English"
        )
    session.add(q70)
			
    q71 = models.Question(category="Olympics", 
        image="/static/images/Olympics/cbbdcf3de9aaf4ee51e8783d816e7c00e2ccb00f.gif",
        body="Michael Phelps is an American competition swimmer and the most decorated Olympian of all time. He holds a total of how many medals?",
        correct_answer="22", 
        answers="18,32,20"
        )
    session.add(q71)
	    	
    q72 = models.Question(category="Music", 
        image="/static/images/Music/fcf67442d03ba2d8f29e0dbb745807f66cd3b82c.gif",
        body="Almost every modern piano has 52 white keys and 36 black keys for a total of 88 keys. The fourth C key on a standard 88-key piano keyboard is commonly known as ________?",
        correct_answer="Middle C", 
        answers="Soprano C,Tenor C,Low C"
        )
    session.add(q72)
    q73 = models.Question(category="Music", 
        image="/static/images/Music/d6385a5e54213bf645222ecd6b74244e0db3e995.gif",
        body="What is the name of Elvis Presley's mansion in Memphis, Tennessee?",
        correct_answer="Graceland", 
        answers="Carolands,Gamble House,Rosecliff"
        )
    session.add(q73)

    q74 = models.Question(category="Music", 
        image="/static/images/Music/fc339cfad6bffa85d804db823d8f387cdea57cb3.gif",
        body="Bill Haley & His Comets, an American rock and roll group, are credited with first popularizing Rock and Roll in the early 1950s. Their hits include all BUT which of the following?",
        correct_answer="Heartbreak Hotel", 
        answers="Rock Around the Clock,See You Later Alligator,Shake Rattle and Roll"
        )
    session.add(q74)
		
    q75 = models.Question(category="Music", 
        image="/static/images/Music/7240a8ae76d16e2890f58e7fe413eb6d7c55edc4.gif",
        body="Bessie Smith was the most popular American female blues singer of the 1920s and 1930s. What was her nickname?",
        correct_answer="The Empress of the Blues", 
        answers="Queen Bae,Her Royal Highness,The Dixeland Belle"
        )
    session.add(q75)

    q76 = models.Question(category="Music", 
        image="/static/images/Music/abd601ff6346dad326247e13778ec1f493b9d7e8.gif",
        body="Thelonious Monk, is considered one of the most important (and eccentric) jazz composers of the century. He is the second-most recorded jazz composer behind which artist?",
        correct_answer="Duke Ellington", 
        answers="Louis Armstrong,Wynton Marsalis,Charles Mingus"
        )
    session.add(q76)

    q77 = models.Question(category="Music", 
        image="/static/images/Music/705d14908f1731e360bdc3f9fef6401c9b3d3a65.gif",
        body="Glenn Miller was an American musician, arranger and composer in the swing era. He is best known for which jazz style?",
        correct_answer="Big Band", 
        answers="West Coast,Blues,Bebop"
        )
    session.add(q77)

    q78 = models.Question(category="Music", 
        image="/static/images/Music/22c7a0b4071487b66206b8d6bd025e6b0a69d515.gif",
        body="Who was the drummer in The Beatles - the English rock band formed in Liverpool in 1960, often regarded as the most influential act of the rock era?",
        correct_answer="Ringo Starr", 
        answers="John Lennon,Paul McCartney,George Harrison"
        )
    session.add(q78)
    q79 = models.Question(category="Music", 
        image="/static/images/Music/54ac5431897a8f8c5e067bfeb0f9e68b89bd8321.gif",
        body="The Woodstock Festival was a music festival held in 1969 which attracted an audience of 400,000 people and was held on a dairy farm in what state?",
        correct_answer="New York", 
        answers="California,Wisconsin,Illinois"
        )
    session.add(q79)

    q80 = models.Question(category="Music", 
        image="/static/images/Music/3f8952111ed8ec4e0cdbc1df7a72c48451f38dbd.jpg",
        body="Johnny Cash was an American singer-songwriter, guitarist, and actor known for his country and gospel songs and signature color of clothing:_______.",
        correct_answer="Black", 
        answers="Red,White,Blue"
        )
    session.add(q80)

    q81 = models.Question(category="Music", 
        image="/static/images/Music/fca5bb93c833ad71742675dcdc2af79bd3169ce0.jpg",
        body="Ray Charles, was an American singer-songwriter, composer and pioneer of soul music. His famous songs include all BUT which of the following?",
        correct_answer="Back Door Man", 
        answers="Hit the Road Jack,Georgia,I Got a Woman"
        )
    session.add(q81)
	    
    q82 = models.Question(category="Music", 
        image="/static/images/Music/a4fa3848a31e32e44414477d76f77453c8e00a23.jpg",
        body="Jimi Hendrix was one of the most influential guitarists of the 1960s despite his untimely death at what young age?",
        correct_answer="27", 
        answers="18,35,20"
        )
    session.add(q82)
	
    q83 = models.Question(category="Music", 
        image="/static/images/Music/f933be252dfed9664ffdf6d6a9b4c5e9d3abe76e.jpg",
        body="Janis Joplin was an an American singer-songwriter famous in what genre of music?",
        correct_answer="Psychedelic/Acid rock", 
        answers="R & B,Bluegrass,Classical "
        )
    session.add(q83)
    print('commit')
    session.commit()

if __name__ == "__main__":
    manager.run()
    