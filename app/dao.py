def get_categories():
    return [{
        "id": 1,
        "name": "Mobile"
    }, {
        "id":2,
        "name": "Tablet"
    }]


def get_products(kw):
    products = [{
        "id": 1,
        "name": "Iphone 15",
        "price": 25000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg",
        "category_id": 1
    }, {
        "id": 2,
        "name": "Iphone 15 Pro",
        "price": 30000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg",
        "category_id": 1
    }, {
        "id": 3,
        "name": "Oppo",
        "price": 20000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg",
        "category_id": 1
    }, {
        "id": 4,
        "name": "Samsung Galaxy S1",
        "price": 15000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg",
        "category_id": 1
    }, {
        "id": 5,
        "name": "Samsung Galaxy S5",
        "price": 23000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg",
        "category_id": 1
    }, {
        "id": 6,
        "name": "Realme",
        "price": 15000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg",
        "category_id": 1
    }, {
        "id": 7,
        "name": "Xiaomi 13 ",
        "price": 17000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg",
        "category_id": 1
    }, {
        "id": 8,
        "name": "Xiaomi 13 Pro",
        "price": 20000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg",
        "category_id": 1
    }, {
        "id": 9,
        "name": "OnePlus Ace",
        "price": 10000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg",
        "category_id": 1
    }]

    if kw:
        products = [p for p in products if p['name'].find(kw) >= 0]

    return products;