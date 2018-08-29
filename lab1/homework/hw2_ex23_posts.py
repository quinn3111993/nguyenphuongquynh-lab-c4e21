from pymongo import MongoClient

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)
db = client.get_default_database()

posts = db["posts"]

my_post = {
    'title': 'Million years ago',
    'author': 'Quinn',
    'content': '''
    I know I'm not the only one
    Who regrets the things they've done
    Sometimes I just feel it's only me
    Who never became who they thought they'd be
    I wish I could live a little more
    Look up to the sky, not just the floor
    I feel like my life is flashing by
    And all I can do is watch and cry
    I miss the air, I miss my friends
    I miss my mother, I miss it when
    Life was a party to be thrown
    But that was a million years ago
    A million years ago''',
}

posts.insert_one(my_post)
