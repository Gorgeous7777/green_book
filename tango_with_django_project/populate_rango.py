import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django

django.setup()
from rango.models import Category, Page


def populate():
    phonelaptop = [{'title': 'Apple iPhone 7, GSM Unlocked, 32GB - Rose Gold',
                    'url': 'https://www.amazon.com/Apple-iPhone-32GB-Rose-Renewed/dp/B0731HBTZ7/ref=sr_1_1?currency=GBP&dchild=1&keywords=iphone&qid=1628199618&sr=8-1/',
                    'content':'UPDATE: so I was just notified I got 100 helpful thumbs up on this review and thought I should update it.... yeah, no. The phone lasted two months. It shut completely off one day, wouldn’t turn back on, nothing. Went to get it checked, and was told it was fried. I lost so many photos and notes because apparently it never uploaded to icloud. The only reason I’m giving it two stars was because I got the refund.ORIGINAL: I was extremely skeptical, as I have always bought contracted new phones from att, but I wanted to get off their plan and I was just done with my old iPhone 5s which had completely given up on me. However, as a college student, I couldn’t afford to buy straight from Apple so I checked OfferUp and letgo, and when those seemed wayyy to sketchy I came to amazon and found this.It took me a week to finally come to terms on buying a refurbished phone off the internet, but I am so glad I did! First off, the battery life is ridiculous; I charge my phone about every TWO days. Also, unlocked made it really easy to switch to metro pcs. I love the Live Photo’s! I love the size (I have small hands, but with a pop socket, it’s perfect)! I also love being able to take it out on the boat and not worry about it getting wet!Love love love that I took the chance to buy it!',
                    'user_id':1,
                    'image':'page_images/1.jpg',
                    'is_show':True,
                    'category_id':1},
                   {'title': 'Apple iPhone 11 Pro Max, US Version, 256GB, Space Gray',
                    'url': 'https://www.amazon.com/Apple-iPhone-256GB-Space-Gray/dp/B07ZQSSKY4/ref=sr_1_1?dchild=1&keywords=iphone12&qid=1628201030&sr=8-1',
                    'content': 'Initially, the phone (iPhone 11 Pro Max) looked fine when I took it out of the box. The outer stainless steel band did have some minor scuffs, but nothing that bothered me. What was peculiar was that the phone came with a preinstalled screen protector, albeit misaligned. I decided to take it off and put my own. And immediately I could notice so many scratches on the screen. It was horrible and well hidden by the screen protector. More than anything, I just want to give this warning: these “renewed”/refurbished phones are not at the same standard like the ones at the Apple Store. They will be scuffed up. In addition, the battery health was at 98% capacity. From personal experience with my XS Max, it took an entire year for it to drop to that point from 100%. I can’t say how all these phones they sell will turn it, since YMMV, but a word of warning',
                    'user_id': 1,
                    'image': 'page_images/2.jpg',
                    'is_show': True,
                    'category_id': 1},
                   {'title': '2020 Apple MacBook Air Laptop: Apple M1 Chip',
                    'url': 'https://www.amazon.com/Apple-MacBook-13-inch-256GB-Storage/dp/B08N5M7S6K/ref=sr_1_3?dchild=1&keywords=Macbook&qid=1628201130&sr=8-3',
                    'content': 'I\'m a fan of apple products and I like almost everything about this new MBA. But it has one huge flaw that nobody talks about. It\'s the camera hardware and it hasn\'t been updated in ages. My zoom calls are so grainy and bad even with decent light. A $1000 laptop with 10 year old front camera is unacceptable. Camera is very important to me. Especially now that we all are quarantined at home and making zoom calls all the time.',
                    'user_id': 1,
                    'image': 'page_images/3.jpg',
                    'is_show': True,
                    'category_id': 1},]

    cats = {'test2': {'pages': phonelaptop, 'views': 0, 'likes': 0},
            }

    # If you want to add more categories or pages,
    # add them to the dictionaries above.

    # The code below goes through the cats dictionary, then adds each category,
    # and then adds all the associated pages for that category.
    #for cat, cat_data in cats.items():
    #    c = add_cat(cat, cat_data["views"], cat_data["likes"])
    for cat, cat_data in cats.items():
        c = add_cat(cat, views=cat_data['views'], likes=cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c,p['title'], p['url'],p['content'],p['is_show'],p['image'],p['user_id'])

    # Print out the categories we have added.
    for c in Category.objects.all():

        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')


def add_page( cat,title, url,content,is_show,image,user_id):
    p = Page.objects.get_or_create(category=cat, title=title,url=url,content=content,is_show=is_show,image=image,user_id=user_id)[0]
    p.save()
    return p


def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name, likes=likes, views=views)[0]
    c.save()
    return c


if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
