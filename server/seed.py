from faker import Faker
import random
from server import app

from models import db , User , Comment,Reward  , Lostitem

fake = Faker()

with app.app_context():

    items = [ 'laptop' , 'Earphone' , 'Airpod ', 'Charger' , 'Phone' , 'Mouse','Flashdisks']
    image_url =['https://www.lenovo.com/medias/lenovo-laptop-ideapad-3-14-intel-subseries-hero.png?context=bWFzdGVyfHJvb3R8MjY5MjEzfGltYWdlL3BuZ3xoODYvaDUzLzE0MTg2OTE5NTkxOTY2LnBuZ3w2ODgwOTdhZDhlODAwNTYzZmVlNDcwNzE5MGI3MzEzMWNiMTIxYmY5NWE3MzcxZDA1NzM2MzkwNWRlYzQ0MDU3'
                , 'https://rukminim2.flixcart.com/image/850/1000/l4a7pu80/battery-charger/c/j/a/33w-vooc-dart-flash-dh593-with-type-c-cable-charging-adapter-original-imagf7mgjty9z8sg.jpeg?q=90'
                , 'https://marvelafrica.co.ke/wp-content/uploads/2023/04/Apple-Airpods-Pro-2nd-gen-3.jpeg' ,
                'https://www.costco.co.uk/medias/sys_master/images/h37/hc3/119433914056734.jpg' ,
                'https://www.bigw.com.au/medias/sys_master/images/images/h05/h67/35171080798238.jpg' ,
                'https://oneplus.co.ke/wp-content/uploads/2022/09/OnePlus-Nord-Wired-Earphones.png' ,
                'https://www.techyshop.co.ke/wp-content/uploads/2015/11/8GB-TRANSCEND-HP-SANDISK-FLASH-DISK-1.jpg'
                ]
    print(len(image_url))

    User.query.delete()
    Lostitem.query.delete()
    Comment.query.delete()
    Reward.query.delete()

    print("🦸‍♀️ Seeding users...")
    users_ids = []
    users = []
    for i in range(20):
        userobject = User(
            username = fake.name() ,
            email = fake.email() ,
            role = fake.name()
        )
        users.append(userobject)
        db.session.add_all(users)
        db.session.commit()
        users_ids.append(userobject.id)

    print("🦸‍♀️ seeding lostitems...")
    
    lostitemids = []
    lostitems =[]
    for i in range(20):
        lostitemobject = Lostitem(
            item_name = random.choice(items) ,
            item_description = fake.sentence() ,
            user_reported_id = random.choice(users_ids) ,
            image_url = random.choice(image_url) ,
            isfound = False,
            isreturnedtoowner = False ,
        )

        lostitems.append(lostitemobject)
        db.session.add_all(lostitems)
        db.session.commit()
        lostitemids.append(lostitemobject.id)
    
    print ("🦸‍♀️ seeding comment..")

    comments = []
    for i in range(20):
        commentobject = Comment(
            comment = fake.paragraph() ,
            lostitem_id = random.choice(lostitemids)
            )
        comments.append(commentobject)
        db.session.add_all(comments)
        db.session.commit()

    print ("🦸‍♀️ seeding rewards..")
    rewards = []
    for i in range(20):
        rewardsobject = Reward(
            rewardamount = round(random.uniform(100.00, 100.00), 2) ,
            lostitem_id = random.choice(lostitemids)
        )
        rewards.append(rewardsobject)
        db.session.add_all(rewards)
        db.session.commit()