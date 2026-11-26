# Gera os arquivos lang/*.json do site. Para mudar um texto: editar aqui e rodar de novo
# (python ferramentas/gerar_idiomas.py), ou editar direto o lang/<idioma>.json.
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

K = ["nav_games", "nav_about", "nav_contact", "hero_sub", "hero_cta", "pub_title", "dev_title",
     "partner_title", "partner_note", "trailer",
     "milim_tag", "milim_text", "milim_cta", "sarrafo_tag", "sarrafo_text", "sordim_tag", "sordim_text",
     "crav_tag", "crav_text", "overspray_tag", "overspray_text", "overspray_cta", "poo_tag", "poo_text",
     "about_title", "about_p1", "about_p2", "contact_title", "contact_text", "privacy", "by_fazay", "lang_label"]

L = {}
L["en"] = ["Games", "About", "Contact", "Independent games, made to be played together.", "See our games",
 "Published", "In development", "Partner games", "Games from our friends at Fazay Games.", "Watch the trailer",
 "Available now · Android", "Guess the secret 5-letter word in 6 tries, guided by colors. Play on your own and compete for points with your friends. In Portuguese, English and Spanish.", "Get it on Google Play",
 "Closed testing · Android", "A battle arena for up to 20 fighters. Grab runes, use special moves and grow bigger and stronger to be the last one standing.",
 "In development · PC (Steam)", "A survival RPG in a big world of floating islands. Team up with friends, level up your skills and face the creatures of every region.",
 "In development · Android", "A survival action game for your phone. Dodge with your finger, hold your ground wave after wave and take on the boss at the end of each map.",
 "Free demo · PC (Steam)", "A tactical 4v4 first-person paintball shooter. Try the free demo on Steam.", "Play the free demo",
 "Closed testing · PC (Steam)", "A tycoon game full of chaos. It is in closed testing for now.",
 "About us", "Lippe Studios is an independent game studio. We make games for phones and for PC, and we like games that are better with friends.",
 "Our games share names from Hebrew: Milim means “words”, Crav means “battle” and Sordim means “the survivors”. They all live in the same world of floating islands.",
 "Contact", "Questions, press or partnerships? Write to us.", "Privacy policy", "by Fazay Games", "Language"]

L["pt"] = ["Jogos", "Sobre", "Contato", "Jogos independentes, feitos para jogar juntos.", "Ver os jogos",
 "Publicados", "Em desenvolvimento", "Jogos de parceiros", "Jogos dos nossos amigos da Fazay Games.", "Ver o trailer",
 "Disponível · Android", "Descubra a palavra secreta de 5 letras em 6 tentativas, guiado pelas cores. Jogue sozinho e dispute pontos com os amigos. Em português, inglês e espanhol.", "Baixar na Google Play",
 "Teste fechado · Android", "Uma arena de batalha para até 20 lutadores. Pegue runas, use golpes especiais e fique maior e mais forte para ser o último de pé.",
 "Em desenvolvimento · PC (Steam)", "Um RPG de sobrevivência num mundo grande de ilhas flutuantes. Junte os amigos, evolua suas habilidades e enfrente as criaturas de cada região.",
 "Em desenvolvimento · Android", "Um jogo de ação e sobrevivência para o celular. Desvie com o dedo, aguente onda após onda e enfrente o chefe no fim de cada mapa.",
 "Demo grátis · PC (Steam)", "Um jogo de paintball tático 4v4 em primeira pessoa. Experimente a demo grátis na Steam.", "Jogar a demo grátis",
 "Teste fechado · PC (Steam)", "Um tycoon cheio de caos. Por enquanto está em teste fechado.",
 "Sobre nós", "A Lippe Studios é um estúdio independente de jogos. Fazemos jogos para celular e para PC, e gostamos de jogos que ficam melhores com os amigos.",
 "Nossos jogos têm nomes em hebraico: Milim quer dizer “palavras”, Crav quer dizer “batalha” e Sordim quer dizer “os sobreviventes”. Todos vivem no mesmo mundo de ilhas flutuantes.",
 "Contato", "Dúvidas, imprensa ou parcerias? Escreva para nós.", "Política de privacidade", "da Fazay Games", "Idioma"]

L["es"] = ["Juegos", "Acerca de", "Contacto", "Juegos independientes, hechos para jugar juntos.", "Ver los juegos",
 "Publicados", "En desarrollo", "Juegos de socios", "Juegos de nuestros amigos de Fazay Games.", "Ver el tráiler",
 "Disponible ahora · Android", "Adivina la palabra secreta de 5 letras en 6 intentos, guiado por colores. Juega solo y compite por puntos con tus amigos. En portugués, inglés y español.", "Consíguelo en Google Play",
 "Prueba cerrada · Android", "Una arena de batalla para hasta 20 luchadores. Recoge runas, usa golpes especiales y hazte más grande y fuerte para ser el último en pie.",
 "En desarrollo · PC (Steam)", "Un RPG de supervivencia en un gran mundo de islas flotantes. Únete a tus amigos, mejora tus habilidades y enfréntate a las criaturas de cada región.",
 "En desarrollo · Android", "Un juego de acción y supervivencia para tu móvil. Esquiva con el dedo, resiste oleada tras oleada y enfréntate al jefe al final de cada mapa.",
 "Demo gratis · PC (Steam)", "Un shooter táctico de paintball 4v4 en primera persona. Prueba la demo gratis en Steam.", "Jugar la demo gratis",
 "Prueba cerrada · PC (Steam)", "Un juego de tycoon lleno de caos. Por ahora está en prueba cerrada.",
 "Sobre nosotros", "Lippe Studios es un estudio independiente de videojuegos. Hacemos juegos para móvil y para PC, y nos gustan los juegos que son mejores con amigos.",
 "Nuestros juegos tienen nombres en hebreo: Milim significa “palabras”, Crav significa “batalla” y Sordim significa “los supervivientes”. Todos viven en el mismo mundo de islas flotantes.",
 "Contacto", "¿Preguntas, prensa o colaboraciones? Escríbenos.", "Política de privacidad", "de Fazay Games", "Idioma"]

L["fr"] = ["Jeux", "À propos", "Contact", "Des jeux indépendants, faits pour jouer ensemble.", "Voir nos jeux",
 "Publiés", "En développement", "Jeux de partenaires", "Des jeux de nos amis de Fazay Games.", "Voir la bande-annonce",
 "Disponible · Android", "Devinez le mot secret de 5 lettres en 6 essais, guidé par les couleurs. Jouez seul et affrontez vos amis pour des points. En portugais, anglais et espagnol.", "Disponible sur Google Play",
 "Test fermé · Android", "Une arène de combat pour jusqu'à 20 combattants. Ramassez des runes, utilisez des coups spéciaux et devenez plus grand et plus fort pour rester le dernier debout.",
 "En développement · PC (Steam)", "Un RPG de survie dans un vaste monde d'îles flottantes. Faites équipe avec vos amis, améliorez vos compétences et affrontez les créatures de chaque région.",
 "En développement · Android", "Un jeu d'action et de survie pour votre téléphone. Esquivez du doigt, tenez bon vague après vague et affrontez le boss à la fin de chaque carte.",
 "Démo gratuite · PC (Steam)", "Un jeu de paintball tactique 4 contre 4 à la première personne. Essayez la démo gratuite sur Steam.", "Jouer à la démo gratuite",
 "Test fermé · PC (Steam)", "Un jeu de gestion plein de chaos. Pour l'instant, il est en test fermé.",
 "À propos de nous", "Lippe Studios est un studio de jeux indépendant. Nous faisons des jeux pour mobile et pour PC, et nous aimons les jeux qui sont meilleurs entre amis.",
 "Nos jeux portent des noms hébreux : Milim signifie « mots », Crav signifie « bataille » et Sordim signifie « les survivants ». Tous vivent dans le même monde d'îles flottantes.",
 "Contact", "Questions, presse ou partenariats ? Écrivez-nous.", "Politique de confidentialité", "par Fazay Games", "Langue"]

L["de"] = ["Spiele", "Über uns", "Kontakt", "Unabhängige Spiele, gemacht zum gemeinsamen Spielen.", "Unsere Spiele ansehen",
 "Veröffentlicht", "In Entwicklung", "Spiele von Partnern", "Spiele unserer Freunde von Fazay Games.", "Trailer ansehen",
 "Jetzt verfügbar · Android", "Errate das geheime Wort mit 5 Buchstaben in 6 Versuchen, geführt von Farben. Spiele allein und kämpfe mit deinen Freunden um Punkte. Auf Portugiesisch, Englisch und Spanisch.", "Bei Google Play laden",
 "Geschlossener Test · Android", "Eine Kampfarena für bis zu 20 Kämpfer. Sammle Runen, nutze Spezialangriffe und werde größer und stärker, um als Letzter zu stehen.",
 "In Entwicklung · PC (Steam)", "Ein Survival-Rollenspiel in einer großen Welt aus schwebenden Inseln. Tu dich mit Freunden zusammen, verbessere deine Fähigkeiten und stelle dich den Kreaturen jeder Region.",
 "In Entwicklung · Android", "Ein Survival-Actionspiel für dein Handy. Weiche mit dem Finger aus, halte Welle um Welle durch und besiege am Ende jeder Karte den Boss.",
 "Kostenlose Demo · PC (Steam)", "Ein taktischer 4-gegen-4-Paintball-Shooter aus der Ego-Perspektive. Probiere die kostenlose Demo auf Steam aus.", "Kostenlose Demo spielen",
 "Geschlossener Test · PC (Steam)", "Ein Tycoon-Spiel voller Chaos. Vorerst befindet es sich im geschlossenen Test.",
 "Über uns", "Lippe Studios ist ein unabhängiges Spielestudio. Wir machen Spiele für Handy und PC und mögen Spiele, die mit Freunden besser sind.",
 "Unsere Spiele tragen hebräische Namen: Milim bedeutet „Wörter“, Crav bedeutet „Schlacht“ und Sordim bedeutet „die Überlebenden“. Alle leben in derselben Welt aus schwebenden Inseln.",
 "Kontakt", "Fragen, Presse oder Partnerschaften? Schreib uns.", "Datenschutzerklärung", "von Fazay Games", "Sprache"]

L["ru"] = ["Игры", "О нас", "Контакты", "Независимые игры, созданные для совместной игры.", "Смотреть игры",
 "Выпущенные", "В разработке", "Игры партнёров", "Игры наших друзей из Fazay Games.", "Смотреть трейлер",
 "Уже доступна · Android", "Угадайте загаданное слово из 5 букв за 6 попыток, ориентируясь на цвета. Играйте один и соревнуйтесь с друзьями за очки. На португальском, английском и испанском.", "Скачать в Google Play",
 "Закрытое тестирование · Android", "Боевая арена на 20 бойцов. Собирайте руны, применяйте особые приёмы и становитесь больше и сильнее, чтобы остаться последним.",
 "В разработке · ПК (Steam)", "Ролевая игра на выживание в огромном мире парящих островов. Играйте с друзьями, прокачивайте навыки и сражайтесь с существами каждого региона.",
 "В разработке · Android", "Экшен на выживание для телефона. Уворачивайтесь пальцем, держитесь волну за волной и победите босса в конце каждой карты.",
 "Бесплатная демо · ПК (Steam)", "Тактический пейнтбол 4 на 4 от первого лица. Попробуйте бесплатную демо-версию в Steam.", "Играть в бесплатную демо",
 "Закрытое тестирование · ПК (Steam)", "Игра-тайкун, полная хаоса. Пока она проходит закрытое тестирование.",
 "О нас", "Lippe Studios — независимая студия игр. Мы делаем игры для телефонов и ПК и любим игры, которые лучше с друзьями.",
 "Названия наших игр — на иврите: Milim значит «слова», Crav — «битва», Sordim — «выжившие». Все они живут в одном мире парящих островов.",
 "Контакты", "Вопросы, пресса или сотрудничество? Напишите нам.", "Политика конфиденциальности", "от Fazay Games", "Язык"]

L["tr"] = ["Oyunlar", "Hakkında", "İletişim", "Birlikte oynamak için yapılmış bağımsız oyunlar.", "Oyunlarımızı gör",
 "Yayınlananlar", "Geliştirilenler", "Ortak oyunlar", "Fazay Games'teki arkadaşlarımızın oyunları.", "Fragmanı izle",
 "Şimdi mevcut · Android", "Renklerin yol gösterdiği 6 denemede 5 harfli gizli kelimeyi bul. Tek başına oyna, arkadaşlarınla puan için yarış. Portekizce, İngilizce ve İspanyolca.", "Google Play'den indir",
 "Kapalı test · Android", "20 savaşçıya kadar bir savaş arenası. Rünleri topla, özel hareketler kullan, büyü ve güçlen; ayakta kalan son kişi ol.",
 "Geliştiriliyor · PC (Steam)", "Süzülen adalardan oluşan büyük bir dünyada hayatta kalma RPG'si. Arkadaşlarınla birleş, yeteneklerini geliştir ve her bölgenin yaratıklarıyla yüzleş.",
 "Geliştiriliyor · Android", "Telefonun için hayatta kalma aksiyon oyunu. Parmağınla kaç, dalga dalga dayan ve her haritanın sonunda patronla savaş.",
 "Ücretsiz demo · PC (Steam)", "Birinci şahıs bakış açısıyla taktik 4'e 4 paintball nişancı oyunu. Ücretsiz demoyu Steam'de dene.", "Ücretsiz demoyu oyna",
 "Kapalı test · PC (Steam)", "Kaos dolu bir tycoon oyunu. Şimdilik kapalı testte.",
 "Hakkımızda", "Lippe Studios bağımsız bir oyun stüdyosudur. Telefon ve PC için oyunlar yapıyoruz ve arkadaşlarla daha eğlenceli olan oyunları seviyoruz.",
 "Oyunlarımızın adları İbranicedir: Milim “kelimeler”, Crav “savaş”, Sordim “hayatta kalanlar” demektir. Hepsi aynı süzülen adalar dünyasında yaşar.",
 "İletişim", "Sorular, basın veya ortaklıklar için bize yazın.", "Gizlilik politikası", "Fazay Games'ten", "Dil"]

L["id"] = ["Game", "Tentang", "Kontak", "Game independen, dibuat untuk dimainkan bersama.", "Lihat game kami",
 "Sudah rilis", "Dalam pengembangan", "Game mitra", "Game dari teman-teman kami di Fazay Games.", "Tonton trailer",
 "Sudah tersedia · Android", "Tebak kata rahasia 5 huruf dalam 6 kesempatan, dipandu warna. Main sendiri dan bersaing poin dengan teman. Dalam bahasa Portugis, Inggris, dan Spanyol.", "Unduh di Google Play",
 "Uji coba tertutup · Android", "Arena pertarungan untuk hingga 20 petarung. Kumpulkan rune, gunakan jurus spesial, dan jadi makin besar dan kuat agar menjadi yang terakhir bertahan.",
 "Dalam pengembangan · PC (Steam)", "RPG bertahan hidup di dunia luas berisi pulau-pulau melayang. Bergabung dengan teman, tingkatkan kemampuan, dan hadapi makhluk di setiap wilayah.",
 "Dalam pengembangan · Android", "Game aksi bertahan hidup untuk ponselmu. Menghindar dengan jari, bertahan gelombang demi gelombang, dan kalahkan bos di akhir setiap peta.",
 "Demo gratis · PC (Steam)", "Game tembak paintball taktis 4 lawan 4 dari sudut pandang orang pertama. Coba demo gratisnya di Steam.", "Mainkan demo gratis",
 "Uji coba tertutup · PC (Steam)", "Game tycoon penuh kekacauan. Saat ini masih dalam uji coba tertutup.",
 "Tentang kami", "Lippe Studios adalah studio game independen. Kami membuat game untuk ponsel dan PC, dan kami suka game yang lebih seru bersama teman.",
 "Nama game kami berasal dari bahasa Ibrani: Milim berarti “kata-kata”, Crav berarti “pertempuran”, dan Sordim berarti “para penyintas”. Semuanya hidup di dunia pulau melayang yang sama.",
 "Kontak", "Pertanyaan, pers, atau kerja sama? Tulis kepada kami.", "Kebijakan privasi", "dari Fazay Games", "Bahasa"]

L["vi"] = ["Trò chơi", "Giới thiệu", "Liên hệ", "Trò chơi độc lập, làm ra để chơi cùng nhau.", "Xem các trò chơi",
 "Đã phát hành", "Đang phát triển", "Trò chơi của đối tác", "Trò chơi của những người bạn ở Fazay Games.", "Xem trailer",
 "Đã có · Android", "Đoán từ bí mật 5 chữ cái trong 6 lượt, được dẫn đường bằng màu sắc. Chơi một mình và tranh điểm với bạn bè. Có tiếng Bồ Đào Nha, tiếng Anh và tiếng Tây Ban Nha.", "Tải trên Google Play",
 "Thử nghiệm kín · Android", "Đấu trường cho tối đa 20 chiến binh. Nhặt rune, dùng chiêu đặc biệt và lớn mạnh hơn để là người cuối cùng trụ lại.",
 "Đang phát triển · PC (Steam)", "Game nhập vai sinh tồn trong thế giới rộng lớn của những hòn đảo lơ lửng. Cùng bạn bè hợp sức, nâng cấp kỹ năng và đối đầu sinh vật ở mỗi vùng.",
 "Đang phát triển · Android", "Game hành động sinh tồn cho điện thoại. Né bằng ngón tay, trụ vững hết đợt này đến đợt khác và hạ boss ở cuối mỗi bản đồ.",
 "Bản demo miễn phí · PC (Steam)", "Game bắn súng paintball chiến thuật 4 đấu 4 góc nhìn thứ nhất. Hãy thử bản demo miễn phí trên Steam.", "Chơi bản demo miễn phí",
 "Thử nghiệm kín · PC (Steam)", "Một game tycoon đầy hỗn loạn. Hiện đang trong giai đoạn thử nghiệm kín.",
 "Về chúng tôi", "Lippe Studios là studio game độc lập. Chúng tôi làm game cho điện thoại và PC, và thích những game chơi cùng bạn bè thì vui hơn.",
 "Tên các game của chúng tôi đến từ tiếng Do Thái: Milim nghĩa là “những từ”, Crav nghĩa là “trận chiến” và Sordim nghĩa là “những người sống sót”. Tất cả cùng sống trong một thế giới đảo lơ lửng.",
 "Liên hệ", "Câu hỏi, báo chí hay hợp tác? Hãy viết cho chúng tôi.", "Chính sách quyền riêng tư", "của Fazay Games", "Ngôn ngữ"]

L["hi"] = ["गेम्स", "हमारे बारे में", "संपर्क", "स्वतंत्र गेम्स, जो साथ मिलकर खेलने के लिए बने हैं।", "हमारे गेम्स देखें",
 "रिलीज़ हो चुके", "विकास में", "साझेदारों के गेम्स", "Fazay Games में हमारे दोस्तों के गेम्स।", "ट्रेलर देखें",
 "अभी उपलब्ध · Android", "रंगों की मदद से 6 कोशिशों में 5 अक्षरों का गुप्त शब्द खोजें। अकेले खेलें और दोस्तों के साथ अंकों की होड़ करें। पुर्तगाली, अंग्रेज़ी और स्पेनिश में।", "Google Play पर पाएँ",
 "बंद परीक्षण · Android", "20 योद्धाओं तक का युद्ध-अखाड़ा। रूण इकट्ठा करें, खास चालें चलें और बड़े व ताकतवर बनकर आख़िरी तक टिके रहें।",
 "विकास में · PC (Steam)", "तैरते द्वीपों की बड़ी दुनिया में सर्वाइवल RPG। दोस्तों के साथ टीम बनाएँ, अपने हुनर बढ़ाएँ और हर इलाके के जीवों का सामना करें।",
 "विकास में · Android", "आपके फ़ोन के लिए सर्वाइवल एक्शन गेम। उँगली से बचें, लहर दर लहर डटे रहें और हर नक्शे के अंत में बॉस से लड़ें।",
 "मुफ़्त डेमो · PC (Steam)", "फ़र्स्ट-पर्सन में टैक्टिकल 4 बनाम 4 पेंटबॉल शूटर। Steam पर मुफ़्त डेमो आज़माएँ।", "मुफ़्त डेमो खेलें",
 "बंद परीक्षण · PC (Steam)", "अफ़रा-तफ़री से भरा टाइकून गेम। फ़िलहाल यह बंद परीक्षण में है।",
 "हमारे बारे में", "Lippe Studios एक स्वतंत्र गेम स्टूडियो है। हम फ़ोन और PC के लिए गेम बनाते हैं, और हमें वे गेम पसंद हैं जो दोस्तों के साथ और मज़ेदार होते हैं।",
 "हमारे गेम्स के नाम हिब्रू से हैं: Milim का मतलब “शब्द”, Crav का मतलब “युद्ध” और Sordim का मतलब “जीवित बचे लोग” है। सब एक ही तैरते द्वीपों की दुनिया में रहते हैं।",
 "संपर्क", "सवाल, प्रेस या साझेदारी? हमें लिखें।", "गोपनीयता नीति", "Fazay Games का", "भाषा"]

L["ar"] = ["الألعاب", "من نحن", "اتصل بنا", "ألعاب مستقلة، صُنعت لنلعب معًا.", "شاهد ألعابنا",
 "ألعاب منشورة", "قيد التطوير", "ألعاب الشركاء", "ألعاب من أصدقائنا في Fazay Games.", "شاهد العرض الدعائي",
 "متاحة الآن · Android", "خمّن الكلمة السرية من 5 أحرف في 6 محاولات بمساعدة الألوان. العب بمفردك وتنافس مع أصدقائك على النقاط. بالبرتغالية والإنجليزية والإسبانية.", "احصل عليها من Google Play",
 "اختبار مغلق · Android", "ساحة قتال تتسع لما يصل إلى 20 مقاتلًا. اجمع الرونات واستخدم الحركات الخاصة وازدد حجمًا وقوة لتكون آخر الصامدين.",
 "قيد التطوير · الحاسوب (Steam)", "لعبة تقمّص أدوار للبقاء في عالم واسع من الجزر العائمة. تعاون مع أصدقائك وطوّر مهاراتك وواجه مخلوقات كل منطقة.",
 "قيد التطوير · Android", "لعبة أكشن وبقاء لهاتفك. تفادَ بإصبعك وصمد موجة بعد موجة وواجه الزعيم في نهاية كل خريطة.",
 "عرض تجريبي مجاني · الحاسوب (Steam)", "لعبة رماية تكتيكية بالبينتبول 4 ضد 4 من منظور الشخص الأول. جرّب العرض التجريبي المجاني على Steam.", "العب العرض التجريبي المجاني",
 "اختبار مغلق · الحاسوب (Steam)", "لعبة تايكون مليئة بالفوضى. هي الآن في مرحلة الاختبار المغلق.",
 "من نحن", "Lippe Studios استوديو ألعاب مستقل. نصنع ألعابًا للهواتف والحاسوب، ونحب الألعاب التي تصبح أجمل مع الأصدقاء.",
 "أسماء ألعابنا عبرية: Milim تعني «كلمات» وCrav تعني «معركة» وSordim تعني «الناجون». كلها تعيش في عالم الجزر العائمة نفسه.",
 "اتصل بنا", "أسئلة أو صحافة أو شراكات؟ راسلنا.", "سياسة الخصوصية", "من Fazay Games", "اللغة"]

L["ja"] = ["ゲーム", "私たちについて", "お問い合わせ", "みんなで遊ぶためのインディーゲーム。", "ゲームを見る",
 "公開中", "開発中", "パートナーのゲーム", "Fazay Games の仲間たちのゲームです。", "トレーラーを見る",
 "配信中 · Android", "色をヒントに、5文字の秘密の単語を6回以内に当てよう。ひとりで遊んで、友だちとスコアを競えます。ポルトガル語・英語・スペイン語に対応。", "Google Play で入手",
 "クローズドテスト中 · Android", "最大20人が戦うバトルアリーナ。ルーンを集め、必殺技を使い、大きく強くなって最後の一人を目指そう。",
 "開発中 · PC (Steam)", "浮遊する島々が広がる大きな世界のサバイバルRPG。仲間と協力し、スキルを育て、各地域のクリーチャーに挑もう。",
 "開発中 · Android", "スマホ向けのサバイバルアクション。指で避け、ウェーブを耐え抜き、各マップの最後でボスに挑もう。",
 "無料体験版 · PC (Steam)", "一人称視点の戦術的な4対4ペイントボールシューター。Steamで無料体験版を試せます。", "無料体験版を遊ぶ",
 "クローズドテスト中 · PC (Steam)", "カオスだらけのタイクーンゲーム。現在はクローズドテスト中です。",
 "私たちについて", "Lippe Studios はインディーゲームスタジオです。スマホとPC向けのゲームを作っていて、友だちと遊ぶともっと楽しいゲームが好きです。",
 "ゲームの名前はヘブライ語から:Milim は「言葉」、Crav は「戦い」、Sordim は「生き残った者たち」という意味です。どれも同じ浮遊島の世界に住んでいます。",
 "お問い合わせ", "ご質問、取材、提携のご相談はこちらへ。", "プライバシーポリシー", "Fazay Games 制作", "言語"]

L["ko"] = ["게임", "소개", "문의", "함께 즐기려고 만든 인디 게임.", "게임 보기",
 "출시됨", "개발 중", "파트너 게임", "Fazay Games 친구들의 게임입니다.", "트레일러 보기",
 "지금 이용 가능 · Android", "색깔 힌트로 6번 안에 5글자 비밀 단어를 맞혀 보세요. 혼자 즐기고 친구와 점수를 겨뤄 보세요. 포르투갈어, 영어, 스페인어 지원.", "Google Play에서 받기",
 "비공개 테스트 · Android", "최대 20명이 싸우는 배틀 아레나. 룬을 모으고 특수 기술을 쓰며 더 크고 강해져 마지막까지 살아남으세요.",
 "개발 중 · PC (Steam)", "떠다니는 섬들로 이루어진 거대한 세계의 생존 RPG. 친구와 팀을 이루고 기술을 키우며 지역마다 다른 생물과 맞서세요.",
 "개발 중 · Android", "휴대폰용 생존 액션 게임. 손가락으로 피하고 웨이브를 버텨 각 맵의 마지막 보스와 맞서세요.",
 "무료 체험판 · PC (Steam)", "1인칭 시점의 전술적 4대4 페인트볼 슈터. Steam에서 무료 체험판을 해 보세요.", "무료 체험판 플레이",
 "비공개 테스트 · PC (Steam)", "혼돈으로 가득한 타이쿤 게임. 현재는 비공개 테스트 중입니다.",
 "소개", "Lippe Studios는 인디 게임 스튜디오입니다. 휴대폰과 PC용 게임을 만들며, 친구와 함께할 때 더 재미있는 게임을 좋아합니다.",
 "우리 게임의 이름은 히브리어에서 왔습니다. Milim은 “단어”, Crav는 “전투”, Sordim은 “생존자들”이라는 뜻입니다. 모두 같은 떠다니는 섬의 세계에 살고 있습니다.",
 "문의", "문의, 보도, 제휴는 메일로 보내 주세요.", "개인정보 처리방침", "Fazay Games 제작", "언어"]

L["zh"] = ["游戏", "关于我们", "联系我们", "为一起玩而做的独立游戏。", "查看我们的游戏",
 "已发布", "开发中", "合作伙伴的游戏", "来自我们 Fazay Games 朋友们的游戏。", "观看预告片",
 "现已上线 · Android", "在色彩提示下,6 次内猜出 5 个字母的秘密单词。可以单人游玩,也可以和好友比拼积分。支持葡萄牙语、英语和西班牙语。", "在 Google Play 获取",
 "封闭测试 · Android", "最多 20 名战士同场的战斗竞技场。收集符文,使用特殊招式,变得更大更强,成为最后站着的人。",
 "开发中 · PC (Steam)", "在漂浮岛屿组成的广阔世界里生存的 RPG。和好友组队,提升技能,迎战每个地区的生物。",
 "开发中 · Android", "一款手机生存动作游戏。用手指闪避,一波接一波坚持下去,并在每张地图结尾挑战首领。",
 "免费试玩版 · PC (Steam)", "第一人称的战术 4 对 4 彩弹射击游戏。欢迎在 Steam 上体验免费试玩版。", "玩免费试玩版",
 "封闭测试 · PC (Steam)", "一款充满混乱的经营模拟游戏。目前处于封闭测试阶段。",
 "关于我们", "Lippe Studios 是一家独立游戏工作室。我们为手机和电脑制作游戏,喜欢和朋友一起玩更有趣的游戏。",
 "我们的游戏名字来自希伯来语:Milim 意为“词语”,Crav 意为“战斗”,Sordim 意为“幸存者”。它们都生活在同一个漂浮岛屿的世界里。",
 "联系我们", "有问题、媒体或合作需求?请给我们写信。", "隐私政策", "Fazay Games 出品", "语言"]

NAMES = {"en": "English", "pt": "Português", "es": "Español", "fr": "Français", "de": "Deutsch", "ru": "Русский",
         "tr": "Türkçe", "id": "Bahasa Indonesia", "vi": "Tiếng Việt", "hi": "हिन्दी", "ar": "العربية",
         "ja": "日本語", "ko": "한국어", "zh": "中文"}

os.makedirs(os.path.join(ROOT, "lang"), exist_ok=True)
for code, vals in L.items():
    assert len(vals) == len(K), (code, len(vals), len(K))
    with open(os.path.join(ROOT, "lang", code + ".json"), "w", encoding="utf8") as f:
        json.dump(dict(zip(K, vals)), f, ensure_ascii=False, indent=1)
with open(os.path.join(ROOT, "lang", "index.json"), "w", encoding="utf8") as f:
    json.dump({"default": "en", "languages": [{"code": c, "name": NAMES[c]} for c in L]}, f, ensure_ascii=False, indent=1)
print(len(L), "idiomas gerados")
