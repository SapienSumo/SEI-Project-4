from pony.orm import db_session
from app import db
from models.Book import Book
from models.Genre import Genre
from models.User import User, UserSchema
from models.Author import Author

db.drop_all_tables(with_all_data=True)
db.create_tables()

with db_session():

    Sci_fi = Genre(name='Sci fi')
    Fantasy = Genre(name='Fantasy')
    Non_Fiction = Genre(name='Non Fiction')
    Fiction = Genre(name='Fiction')
    Memoir = Genre(name='Memoir')
    Novel = Genre(name='Novel')
    Crime_Fiction = Genre(name='Crime Fiction')
    Literary_fiction = Genre(name='Literary fiction')
    Autobiography = Genre(name='Autobiography')
    Mystery_fiction = Genre(name='Mystery fiction')
    Anthology = Genre(name='Anthology')
    Magical_Realism = Genre(name='Magical Realism')
    Gothic_fiction = Genre(name='Gothic fiction')
    Alternate_history = Genre(name='Alternate history')
    History = Genre(name='History')
    Graphic_novel = Genre(name='Graphic novel')
    Hard_science_fiction = Genre(name='Hard science fiction')
    Self_help_book = Genre(name='Self help book')
    Mystery = Genre(name='Mystery')


    Karen_Travis = Author(name='Karen Travis')
    Madeline_Miller = Author(name='Madeline Miller')
    JRR_Tolkien = Author(name='JRR Tolkien')
    Yuval_Noah_Harari = Author(name='Yuval Noah Harari')
    George_Orwell = Author(name='George Orwell')
    Stefan_Zweig = Author(name='Stefan Zweig')
    Charlotte_Brontë = Author(name='Charlotte Brontë')
    Michelle_Obama = Author(name='Michelle Obama')
    Truman_Capote = Author(name='Truman Capote')
    Sally_Rooney = Author(name='Sally Rooney')
    Benjamin_Franklin = Author(name='Benjamin Franklin')
    Louise_Penny = Author(name='Louise Penny')
    Al_Sarrantonio = Author(name='Al Sarrantonio')
    Percy_Makhuba = Author(name='Percy Makhuba')
    Philip_K_Dick = Author(name='Philip K. Dick')
    Peter_Frankopan = Author(name='Peter Frankopan')
    Bungie = Author(name='Bungie')
    Martha_Wells = Author(name='Martha Wells')
    DK = Author(name='DK')
    Robert_Crais = Author(name='Robert Crais')
    James_Clear = Author(name='James Clear')
    Herodotus = Author(name='Herodotus')
    Bram_Stoker = Author(name='Bram Stoker')


    schema = UserSchema()
    user = User(
    username='User',
    email='user@user.com',
    password_hash=schema.generate_hash('pass')
    )

    Book(
        name='Mortal Dictata',
        image='./images/mortal-dictata.jpg',
        blurb='With the Covenant War over, the Office of Naval Intelligence faces old grievances rising again to threaten Earth. The angry, bitter colonies, still with scores to settle from the insurrection put on hold for thirty years, now want justice -- and so does a man whose life was torn apart by ONI when his daughter was abducted for the SPARTAN-II program. Black ops squad Kilo-Five find their loyalties tested beyond breaking point when the father of their Spartan comrade, still searching for the truth about her disappearance, prepares to glass Earth\'s cities to get an answer. How far will Kilo-Five go to stop him? And will he be able to live with the truth when he finds it? The painful answer lies with a man long dead, and a conscience that still survives in the most unlikely, undiscovered place.',
        author=Karen_Travis,
        genres=[Sci_fi],
        user=user
    )

    Book(
        name='Sapiens',
        image='./images/sapiens.jpg',
        blurb='100,000 years ago, at least six human species inhabited the earth. Today there is just one. Us. Homo sapiens. How did our species succeed in the battle for dominance? Why did our foraging ancestors come together to create cities and kingdoms? How did we come to believe in gods, nations and human rights; to trust money, books and laws; and to be enslaved by bureaucracy, timetables and consumerism? And what will our world be like in the millennia to come? In Sapiens, Dr Yuval Noah Harari spans the whole of human history, from the very first humans to walk the earth to the radical – and sometimes devastating – breakthroughs of the Cognitive, Agricultural and Scientific Revolutions. Drawing on insights from biology, anthropology, palaeontology and economics, he explores how the currents of history have shaped our human societies, the animals and plants around us, and even our personalities. Have we become happier as history has unfolded? Can we ever free our behaviour from the heritage of our ancestors? And what, if anything, can we do to influence the course of the centuries to come? ',
        author=Yuval_Noah_Harari,
        genres=[Non_Fiction],
        user=user
    )

    Book(
        name='Homo Deus',
        image='./images/homo-deus.jpg',
        blurb='Yuval Noah Harari, author of the bestselling Sapiens: A Brief History of Humankind, envisions a not-too-distant world in which we face a new set of challenges. In Homo Deus, he examines our future with his trademark blend of science, history, philosophy and every discipline in between. Homo Deus explores the projects, dreams and nightmares that will shape the twenty-first century – from overcoming death to creating artificial life. It asks the fundamental questions: Where do we go from here? And how will we protect this fragile world from our own destructive powers? This is the next stage of evolution. This is Homo Deus.',
        author=Yuval_Noah_Harari,
        genres=[Non_Fiction],
        user=user
    )

    Book(
        name='1984',
        image='./images/1984.jpg',
        blurb='Nineteen Eighty-Four, often published as 1984, is a dystopian novel by English writer George Orwell published in June 1949, whose themes center on the risks of government overreach, totalitarianism and repressive regimentation of all persons and behaviors within society.',
        author=George_Orwell,
        genres=[Sci_fi],
        user=user
    )

    Book(
        name='21 Lessons for the 21st Century',
        image='./images/21-lessons.jpg',
        blurb='How can we protect ourselves from nuclear war, ecological cataclysms and technological disruptions? What can we do about the epidemic of fake news or the threat of terrorism? What should we teach our children? Yuval Noah Harari takes us on a thrilling journey through today’s most urgent issues. The golden thread running through his exhilarating new book is the challenge of maintaining our collective and individual focus in the face of constant and disorienting change. Are we still capable of understanding the world we have created?',
        author=Yuval_Noah_Harari,
        genres=[Non_Fiction],
        user=user
    )

    Book(
        name='Fantastic Night',
        image='./images/fantastic.jpg',
        blurb='‘I alone know that I am only just beginning to live.’ He is distinguished, rich, a member of fashionable society-utterlybored. But, over the course of one fantastic night, a young Baron becomes a thief, unashamed, and awakes to life for the first time. This collection is full of tales of infinite passions, of intense encounters that transform lives, a knock on a door that forces a whole community to take flight, a doomed attempt to save a soul poisoned by addiction, a love soured into awful cruelty, of longing and liberation. They are the gripping work of a master storyteller, unmatched and completely unforgettable.',
        author=Stefan_Zweig,
        genres=[Fiction],
        user=user
    )

    Book(
        name='The Thursday War',
        image='./images/Thursday-war.jpg',
        blurb='Welcome to humanity\'s new war: silent, high stakes, and unseen. This is a life-or-death mission for ONI\'s black-ops team, Kilo-Five, which is tasked with preventing the ruthless Elites, once the military leaders of the Covenant, from regrouping and threatening humankind again. What began as a routine dirty-tricks operation?keeping the Elites busy with their own insurrection? turns into a desperate bid to extract one member of Kilo-Five from the seething heart of an alien civil war. But troubles never come singly for Kilo-Five. Colonial terrorism is once again surfacing on one of the worlds that survived the war against the Covenant, and the man behind it is much more than just a name to Spartan-010. Meanwhile, the treasure trove of Forerunner technology recovered from the shield world of Onyx is being put to work while a kidnapped Elite plots vengeance on the humans he fears will bring his people to the brink of destruction.',
        author=Karen_Travis,
        genres=[Sci_fi],
        user=user
    )

    Book(
        name='Charlotte Brontë',
        image='./images/jane_eyre.jpg',
        blurb='Jane Eyre is the story of a young, orphaned girl (shockingly, she’s named Jane Eyre) who lives with her aunt and cousins, the Reeds, at Gateshead Hall. Like all nineteenth-century orphans, her situation pretty much sucks.',
        author=Charlotte_Brontë,
        genres=[Novel],
        user=user
    )

    Book(
        name='Becoming',
        image='./images/Michelle_Obama.jpg',
        blurb='Becoming is the memoir of former United States First Lady Michelle Obama published in 2018. Described by the author as a deeply personal experience, the book talks about her roots and how she found her voice, as well as her time in the White House, her public health campaign, and her role as a mother.',
        author=Michelle_Obama,
        genres=Memoir,
        user=user
    )

    Book(
        name='In Cold Blood',
        image='./images/cold_blood.jpg',
        blurb='The chilling true crime non-fiction novel that made Truman Capote\'s name, In Cold Blood is a seminal work of modern prose, a remarkable synthesis of journalistic skill and powerfully evocative narrative published in Penguin Modern Classics. Controversial and compelling, In Cold Blood reconstructs the murder in 1959 of a Kansas farmer, his wife and both their children. Truman Capote\'s comprehensive study of the killings and subsequent investigation explores the circumstances surrounding this terrible crime and the effect it had on those involved.',
        author=Truman_Capote,
        genres=Crime_Fiction,
        user=user
    )

    Book(
        name='Normal People',
        image='./images/normal_people.jpg',
        blurb='Connell and Marianne grow up in the same small town in rural Ireland. The similarities end there; they are from very different worlds. When they both earn places at Trinity College in Dublin, a connection that has grown between them lasts long into the following years. This is an exquisite love story about how a person can change another person\'s life - a simple yet profound realisation that unfolds beautifully over the course of the novel. It tells us how difficult it is to talk about how we feel and it tells us - blazingly - about cycles of domination, legitimacy and privilege. Alternating menace with overwhelming tenderness, Sally Rooney\'s second novel breathes fiction with new life.',
        author=Sally_Rooney,
        genres=Literary_fiction,
        user=user
    )

    Book(
        name='Benjamin Franklin',
        image='./images/ben.jpg',
        blurb='Book review: "The Autobiography of Benjamin Franklin" by Benjamin Franklin. (audiobook) Benjamin Franklin was a well known scientist and public servant that lived in the 18th century. He was also a successful diplomat and one of USA\'s founding fathers. ... The book is variably entertaining, but always educational.',
        author=Benjamin_Franklin,
        genres=Autobiography,
        user=user
    )

    Book(
        name='Kingdom of the Blind',
        image='./images/blind.jpg',
        blurb='When Armand Gamache receives a letter inviting him to an abandoned farmhouse outside of Three Pines, the former head of the Sûreté du Québec discovers that a complete stranger has named him as an executor of her will.Armand never knew the elderly woman, and the bequests are so wildly unlikely that he suspects the woman must have been delusional - until a body is found, and the terms of the bizarre document suddenly seem far more menacing.',
        author=Louise_Penny,
        genres=Mystery,
        user=user
    )

    Book(
        name='999',
        image='./images/999.jpg',
        blurb='A ward-winning writer and editor Al Sarrantonio gathers together twenty-nine original stories from masters of the macabre. From dark fantasy and pure suspense to classic horror tales of vampires and zombies, 999 showcases the extraordinary scope of fantastical fright fiction. The stories in this anthology are a relentless tour de force of fear, which will haunt you, terrify you, and keep the adrenaline rushing all through the night.',
        author=Al_Sarrantonio,
        genres=Anthology,
        user=user
    )

    Book(
        name='Cries of the Forgotten',
        image='./images/cries.jpg',
        blurb='Can the wish of one man’s heart truly change an entire nation? One day, Tshepo Nonyane, a mild-mannered government statistician walks into the Johannesburg Metro Police Department and confesses to the brutal rapes and murders of several women. He describes his crimes in grisly detail, even as his clean-cut, sincere appearance completely belies the violent man he claims to be. As Detective Eloff Mueller and her police partner, Joseph Langa, investigate Nonyane’s horrifying confessions, they find themselves pulled into a world where appearance and reality are blurred beyond recognition.',
        author=Percy_Makhuba,
        genres=Magical_Realism,
        user=user
    )

    Book(
        name='Dracula',
        image='./images/dracula.jpg',
        blurb='Dracula is an 1897 Gothic horror novel by Irish author Bram Stoker. ... The novel tells the story of Dracula\'s attempt to move from Transylvania to England so that he may find new blood and spread the undead curse, and of the battle between Dracula and a small group of men and a woman led by Professor Abraham Van Helsing.',
        author=Bram_Stoker,
        genres=Gothic_fiction,
        user=user
    )

    Book(
        name='The Man in the High Castle',
        image='./images/high-castle.jpg',
        blurb='Main. Alexa Davalos as Juliana Crain, a young woman from San Francisco who is outwardly happy living under Japanese control. She is an expert in aikido and is friendly with the Japanese people who live in San Francisco. As Juliana learns of The Man in the High Castle and his films, she begins to rebel.',
        author=Philip_K_Dick,
        genres=Alternate_history,
        user=user
    )

    Book(
        name='The Silk Roads',
        image='./images/slik.jpg',
        blurb='The Silk Roads are rising again. A major reassessment of world history, The Silk Roads is an important account of the forces that have shaped the global economy and the political renaissance in the re-emerging east. For centuries, fame and fortune was to be found in the west - in the New World of the Americas.',
        author=Peter_Frankopan,
        genres=History,
        user=user
    )

    Book(
        name='The Halo Graphic Novel',
        image='./images/halo-graphic.jpg',
        blurb='The Halo Graphic Novel is the first graphic novel adaptation of the military science fiction video game Halo, published by Marvel Comics in partnership with Bungie. ... Each story focuses on different aspects of the Halo universe, revealing stories that are tangential to the main plot of the game.',
        author=Bungie,
        genres=Graphic_novel,
        user=user
    )

    Book(
        name='All Systems Red',
        image='./images/all-systems-red.jpg',
        blurb='A murderous android discovers itself in All Systems Red, a tense science fiction adventure by Martha Wells that interrogates the roots of consciousness through Artificial Intelligence. "As a heartless killing machine, I was a complete failure."',
        author=Martha_Wells,
        genres=Hard_science_fiction,
        user=user
    )

    Book(
        name='Artificial Condition',
        image='./images/ai-condition.jpg',
        blurb='Artificial Condition (Murderbot Diaries) Paperback – 30 Jan 2018. It has a dark past - one in which a number of humans were killed. ... Teaming up with a Research Transport vessel named ART (you don\'t want to know what the "A" stands for), Murderbot heads to the mining facility where it went rogue.',
        author=Martha_Wells,
        genres=Hard_science_fiction,
        user=user
    )

    Book(
        name='Rogue Protocol',
        image='./images/rouge-p.jpg',
        blurb='Martha Wells\' Rogue Protocol is the third in the Murderbot Diaries series, starring a human-like android who keeps getting sucked back into adventure after adventure, though it just wants to be left alone, away from humanity and small talk.',
        author=Martha_Wells,
        genres=Hard_science_fiction,
        user=user
    )

    Book(
        name='Exit Strategy',
        image='./images/Exit-Strategy.jpg',
        blurb='Exit Strategy. An innovative debut thriller about the secretive organization that the rich and infamous call when they need to start over with a new name, new face and new life—and what happens when one client tries to go home. Sometimes you just need to escape.',
        author=Martha_Wells,
        genres=Hard_science_fiction,
        user=user
    )

    Book(
        name='Dinosaurs',
        image='./images/dinos.jpg',
        blurb='Packed full of engaging photography and easy-to-follow text, First Dinosaur Encyclopedia brings history to life. ... A delightful first reference book about dinosaurs for young paleontologists, this updated edition of First Dinosaur Encyclopedia takes readers on a journey to the prehistoric world of dinosaurs.',
        author=DK,
        genres=Non_Fiction,
        user=user
    )

    Book(
        name='Atomic Habits',
        image='./images/atomic.jpg',
        blurb='“Atomic Habits is a great book for anyone who is frustrated with the way they can\'t seem to kick that one (or two dozen) bad habit(s) and wants to finally achieve health, fitness, financial freedom, great relationships, and a good life.”',
        author=James_Clear,
        genres=Self_help_book,
        user=user
    )

    Book(
        name='The two minute rule',
        image='./images/two-min.jpg',
        blurb='Robert Crais: The Two Minute Rule. Ask anyone on the wrong side of the law about the two minute rule and they\'ll tell you that\'s as long as you can hope for at a robbery before the cops show up. ... The only thing on his mind is reconciliation with his estranged son, who is, ironically, a cop.',
        author=Robert_Crais,
        genres=Fiction,
        user=user
    )

    Book(
        name='Histories',
        image='./images/histories.jpg',
        blurb='The Histories (Greek: Ἱστορίαι; Ancient Greek: [historíai̯]; also known as The Histories) of Herodotus is considered the founding work of history in Western literature. ... The Histories was at some point divided into the nine books that appear in modern editions, conventionally named after the nine Muses.',
        author=Herodotus,
        genres=History,
        user=user
    )

    Book(
        name='The Lord of the Rings',
        image='./images/lotr.jpg',
        blurb='All three parts of epic masterpiece ‘The Lord of the Rings’ in one paperback. Features brand new packaging, the definitive edition of the text, fold-out flaps with the original two-colour maps, and a revised and expanded index. Sauron, the Dark Lord, has gathered to him all the Rings of Power – the means by which he intends to rule Middle-earth. All he lacks in his plans for dominion is the One Ring – the ring that rules them all – which has fallen into the hands of the hobbit, Bilbo Baggins. In a sleepy village in the Shire, young Frodo Baggins finds himself faced with an immense task, as the Ring is entrusted to his care. He must leave his home and make a perilous journey across the realms of Middle-earth to the Crack of Doom, deep inside the territories of the Dark Lord. There he must destroy the Ring forever and foil the Dark Lord in his evil purpose. Since it was first published in 1954, ‘The Lord of the Rings’ has been a book people have treasured. Steeped in unrivalled magic and otherworldliness, its sweeping fantasy has touched the hearts of young and old alike. Now, to coincide with the publication of J.R.R. Tolkien’s The Children of Hurin, the definitive 50th Anniversary text, fully restored with almost 400 corrections – with the full co-operation of Christopher Tolkien – is reissued with a striking new cover.',
        author=JRR_Tolkien,
        genres=Fantasy,
        user=user
    )

    db.commit()
