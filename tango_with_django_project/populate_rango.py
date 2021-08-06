import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django

django.setup()
from rango.models import Category, Page


def populate():
    phonelaptop = [{'title': 'Apple iPhone 7, GSM Unlocked, 32GB - Rose Gold',
                    'url': 'https://www.amazon.com/Apple-iPhone-32GB-Rose-Renewed/dp/B0731HBTZ7/ref=sr_1_1?currency=GBP&dchild=1&keywords=iphone&qid=1628199618&sr=8-1/',
                    'content': 'UPDATE: so I was just notified I got 100 helpful thumbs up on this review and thought I should update it.... yeah, no. The phone lasted two months. It shut completely off one day, wouldn’t turn back on, nothing. Went to get it checked, and was told it was fried. I lost so many photos and notes because apparently it never uploaded to icloud. The only reason I’m giving it two stars was because I got the refund.ORIGINAL: I was extremely skeptical, as I have always bought contracted new phones from att, but I wanted to get off their plan and I was just done with my old iPhone 5s which had completely given up on me. However, as a college student, I couldn’t afford to buy straight from Apple so I checked OfferUp and letgo, and when those seemed wayyy to sketchy I came to amazon and found this.It took me a week to finally come to terms on buying a refurbished phone off the internet, but I am so glad I did! First off, the battery life is ridiculous; I charge my phone about every TWO days. Also, unlocked made it really easy to switch to metro pcs. I love the Live Photo’s! I love the size (I have small hands, but with a pop socket, it’s perfect)! I also love being able to take it out on the boat and not worry about it getting wet!Love love love that I took the chance to buy it!',
                    'user_id': 1,
                    'image': 'page_images/1.jpg',
                    'is_show': True},
                   {'title': 'Apple iPhone 11 Pro Max, US Version, 256GB, Space Gray',
                    'url': 'https://www.amazon.com/Apple-iPhone-256GB-Space-Gray/dp/B07ZQSSKY4/ref=sr_1_1?dchild=1&keywords=iphone12&qid=1628201030&sr=8-1',
                    'content': 'Initially, the phone (iPhone 11 Pro Max) looked fine when I took it out of the box. '
                               'The outer stainless steel band did have some minor scuffs, but nothing that bothered '
                               'me. What was peculiar was that the phone came with a preinstalled screen protector, '
                               'albeit misaligned. I decided to take it off and put my own. And immediately I could '
                               'notice so many scratches on the screen. It was horrible and well hidden by the screen '
                               'protector. More than anything, I just want to give this warning: these '
                               '“renewed”/refurbished phones are not at the same standard like the ones at the Apple '
                               'Store. They will be scuffed up. In addition, the battery health was at 98% capacity. '
                               'From personal experience with my XS Max, it took an entire year for it to drop to '
                               'that point from 100%. I can’t say how all these phones they sell will turn it, '
                               'since YMMV, but a word of warning',
                    'user_id': 1,
                    'image': 'page_images/2.jpg',
                    'is_show': True},
                   {'title': '2020 Apple MacBook Air Laptop: Apple M1 Chip',
                    'url': 'https://www.amazon.com/Apple-MacBook-13-inch-256GB-Storage/dp/B08N5M7S6K/ref=sr_1_3?dchild=1&keywords=Macbook&qid=1628201130&sr=8-3',
                    'content': 'I\'m a fan of apple products and I like almost everything about this new MBA. But it '
                               'has one huge flaw that nobody talks about. It\'s the camera hardware and it hasn\'t '
                               'been updated in ages. My zoom calls are so grainy and bad even with decent light. A '
                               '$1000 laptop with 10 year old front camera is unacceptable. Camera is very important '
                               'to me. Especially now that we all are quarantined at home and making zoom calls all '
                               'the time.',
                    'user_id': 1,
                    'image': 'page_images/3.jpg',
                    'is_show': True}, ]
    toys = [{'title': 'Funko Pop! Star Wars: Across The Galaxy - Rey (Jakku), Amazon Funkon Exclusive',
             'url': 'https://www.amazon.com/POP-Star-Wars-ATG-Rey/dp/B08QXR2KD8/ref=sr_1_1?dchild=1&fst=as%3Aoff&pf_rd_i=16225015011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=da121563-253a-4b83-b6ab-b694e4e456ac&pf_rd_r=03MC9CB4FHCPQ2HNGAH0&pf_rd_s=merchandised-search-4&pf_rd_t=101&qid=1628208640&refinements=p_n_shipping_option-bin%3A3242350011&rnid=165795011&s=toys-and-games&sr=1-1',
             'content': 'From Star Wars: Clone Wars, Bo Katan gets the Pop! Vinyl treatment! This figure '
                        'measures about 3 3/4-Inch tall and comes in a window display box. Collect the entire '
                        'line of Clone Wars Funko Pop Vinyl\'s: Anakin Skywalker, Ahsoka Tano, General Obi-Wan '
                        'Kenobi, Yoda, Captain Rex, Clone Trooper, Bo Katan, Bad Batch Hunter, Crosshair, '
                        'Tech, Wrecker, Gar Saxon, Cad Bane, Asajj Ventress, General Grievous & Darth Maul. '
                        'Collect the entire line of The Mandalorian Funko Pop Vinyl\'s: The Mandalorian, '
                        'Baby Yoda "The Child", Kuiil, IG-11, Cara Dune, Greef Karga, Q9-Zero, Heavy Infantry '
                        'Mandalorian, Incinerator Stormtrooper, Offworld Jawa. Collect the entire line of Star '
                        'Wars Rebels Funko Pop Vinyl\'s: Ezra, Kanan, Sabine, Hera, Zeb, Chopper, Ahsoka, '
                        'Captain Rex, Grand Admiral Thrawn, Fifth Brother, Seventh Sister, The Inquisitor, '
                        'Jedi Fallen Order Cal Kestis, BD-1 & Second Sister, Rogue One Scarif Shoretrooper & '
                        'Imperial Death Trooper! Collect the entire line of Star Wars Funko Pops: Darth Vader, '
                        'Darth Maul, Stormtrooper, Boba Fett, Han Solo, Tatooine Luke Skywalker, '
                        'Princess Leia, Chewbacca, C-3PO, R2-D2, Dagobah Yoda, Jabba the Hutt, Wicket, '
                        'Clone Trooper, Jedi Luke, Bespin Luke, Lando, Jawa, X-Wing Pilot, Obi-Wan Kenobi, '
                        'Slave Leia, Bib Fortuna, Biker Scout, Bossk, Emperor, Gamorrean Guard, Greedo, '
                        'Tie Fighter Pilot & Tusken Raider! (Each Sold Separately) Includes a Pop box '
                        'protector fit for any collectors investment.',
             'user_id': 1,
             'image': 'page_images/4.jpg',
             'is_show': True},
            {'title': 'Fisher-Price Little People Collector Lord of The Rings Figure Set',
             'url': 'https://www.amazon.com/Fisher-Price-Little-People-Collector-Rings/dp/B084P4K1CQ/ref=sr_1_1?dchild=1&fst=as%3Aoff&pf_rd_i=16225015011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=da121563-253a-4b83-b6ab-b694e4e456ac&pf_rd_r=03MC9CB4FHCPQ2HNGAH0&pf_rd_s=merchandised-search-4&pf_rd_t=101&qid=1628208789&refinements=p_n_shipping_option-bin%3A3242350011&rnid=165795011&s=toys-and-games&sr=1-1',
             'content': 'My toddler has never seen the movies or heard the books, but it brings my husband and '
                        'I much joy when Gandalf goes flying off the table to the appropriately red carpet, '
                        'or Frodo is set on the back of our massive rocking horse in wonderful hobbit scale. '
                        'At our house, Gimli is currently guarding the cable box with Aragorn while Arwen and '
                        'Legolas are hanging out at a farm with a t-rex and a rubber duck.',
             'user_id': 1,
             'image': 'page_images/5.jpg',
             'is_show': True,
             'category_id': 1},
            {
                'title': 'Star Wars The Bounty Collection Series 3 The Child Collectible Figures 2.25-Inch-Scale Curious Child',
                'url': 'https://www.amazon.com/Star-Wars-Collection-Collectible-2-25-Inch-Scale/dp/B08MVVSNKG/ref=sr_1_2?dchild=1&fst=as%3Aoff&pf_rd_i=16225015011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=da121563-253a-4b83-b6ab-b694e4e456ac&pf_rd_r=03MC9CB4FHCPQ2HNGAH0&pf_rd_s=merchandised-search-4&pf_rd_t=101&qid=1628208789&refinements=p_n_shipping_option-bin%3A3242350011&rnid=165795011&s=toys-and-games&sr=1-2',
                'content': 'High quality cute little figure that sits on my desk. Love the craftsmanship of the '
                           'floating eggs and The Child\'s expression. Reminds me that we\'re all imperfect, '
                           'mischievous, and craving stuff at times, and it\'s okay. The second figure is also '
                           'nice.',
                'user_id': 1,
                'image': 'page_images/6.jpg',
                'is_show': True,
                'category_id': 1}, ]
    books = [{'title': 'American Marxism Hardcover – July 13, 2021',
              'url': 'https://www.amazon.com/American-Marxism-Mark-R-Levin/dp/150113597X/ref=zg_1/142-5830387-0388111?pd_rd_w=kvtXo&pf_rd_p=59b4e7e4-1051-4d19-8861-9d7936c4c9b7&pf_rd_r=CKWKGENF26R6BA3300V2&pd_rd_r=90785ec5-bab6-4f03-beda-f435b4cbf3d5&pd_rd_wg=GwKq5&pd_rd_i=150113597X&psc=1',
              'content': 'Levine gives more than most authors. His perspective is well documented and supported as are his suggestions for how to take up the cause to restore democracy to our country and his plan is very specific:BOYCOTT - DIVESTMENT - SANCTIONS - a plan that has been used on the nation of Israel can be applied to various factions within our own country’s business, finance, education and government in order to bring them to heel, to return to sanity.',
              'user_id': 1,
              'image': 'page_images/7.jpg',
              'is_show': True},
             {'title': 'Billy Summers',
              'url': 'https://www.amazon.com/Billy-Summers/dp/B08V9HZGJP/ref=zg_2/142-5830387-0388111?pd_rd_w=kvtXo&pf_rd_p=59b4e7e4-1051-4d19-8861-9d7936c4c9b7&pf_rd_r=CKWKGENF26R6BA3300V2&pd_rd_r=90785ec5-bab6-4f03-beda-f435b4cbf3d5&pd_rd_wg=GwKq5&pd_rd_i=B08V9HZGJP&psc=1',
              'content': 'Halfway through the book, we meet Alice, another troubled character that has suffered through her own brutal traumas. From the point that Billy meets Alice, the book morphs into more of a revenge quest; hunting down the bad guys to make them pay for their crimes. This shift in pace and motivation almost makes it seem like a different story, and I wonder if this part was written after the pandemic? There are also a few cool easter eggs, or references to places from other King books, that I\'m sure Constant Readers will appreciate.',
              'user_id': 1,
              'image': 'page_images/8.jpg',
              'is_show': True,
              'category_id': 1},
             {
                 'title': 'Greenlights',
                 'url': 'https://www.amazon.com/Greenlights/dp/B08HLW2JXD/ref=zg_3/142-5830387-0388111?pd_rd_w=kvtXo&pf_rd_p=59b4e7e4-1051-4d19-8861-9d7936c4c9b7&pf_rd_r=CKWKGENF26R6BA3300V2&pd_rd_r=90785ec5-bab6-4f03-beda-f435b4cbf3d5&pd_rd_wg=GwKq5&pd_rd_i=B08HLW2JXD&psc=1',
                 'content': 'Greenlights is a remarkable first book from an already renowned artist. Kind of a mashup of Anthony Bourdain with Ernest Hemingway, McConaughey tells stories with the aplomb of accomplished raconteur. Part memoir, part life guide and part ethic Greenlights is worth reading for many beyond McConaughey’s fan base; basically anyone who likes a good man’s man adventure story.',
                 'user_id': 1,
                 'image': 'page_images/9.jpg',
                 'is_show': True,
                 'category_id': 1}, ]

    cats = {'PhoneAndLaptop': {'pages': phonelaptop, 'views': 0, 'likes': 0},
            'Toys': {'pages': toys, 'views': 0, 'likes': 0},
            'Books': {'pages': books, 'views': 0, 'likes': 0},
            }



    for cat, cat_data in cats.items():
        c = add_cat(cat, views=cat_data['views'], likes=cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], p['content'], p['is_show'], p['image'], p['user_id'])

    # Print out the categories we have added.
    for c in Category.objects.all():

        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')


def add_page(cat, title, url, content, is_show, image, user_id):
    p = Page.objects.get_or_create(category=cat, title=title, url=url, content=content, is_show=is_show, image=image,
                                   user_id=user_id)[0]
    p.save()
    return p


def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name, likes=likes, views=views)[0]
    c.save()
    return c


if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
