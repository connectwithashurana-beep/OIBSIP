from django.core.management.base import BaseCommand
from inventory.models import Pizza, PizzaBase, Sauce, Cheese, Vegetable


def unsplash(photo_id):
    return (
        f"https://images.unsplash.com/{photo_id}"
        "?auto=format&fit=crop&w=900&q=80"
    )


# Image URLs are pre-verified (HTTP 200) Unsplash food photos. They mirror the
# pools used by the frontend fallback so every product has a real image.
PIZZA_IMGS = [
    unsplash("photo-1513104890138-7c749659a591"),
    unsplash("photo-1574071318508-1cdbab80d002"),
    unsplash("photo-1534308983496-4fabb1a015ee"),
    unsplash("photo-1579751626657-72bc17010498"),
    unsplash("photo-1552539618-7eec9b4d1796"),
    unsplash("photo-1528137871618-79d2761e3fd5"),
]
BURGER_IMGS = [
    unsplash("photo-1568901346375-23c9450c58cd"),
    unsplash("photo-1550547660-d9450f859349"),
    unsplash("photo-1561758033-d89a9ad46330"),
    unsplash("photo-1606755962773-d324e0a13086"),
]
SIDES_IMGS = [
    unsplash("photo-1573080496219-bb080dd4f877"),
    unsplash("photo-1541592106381-b31e9677c0e5"),
    unsplash("photo-1576107232684-1279f390859f"),
    unsplash("photo-1631452180519-c014fe946bc7"),
    unsplash("photo-1497034825429-c343d7c6a68f"),
]
DRINKS_IMGS = [
    unsplash("photo-1544145945-f90425340c7e"),
    unsplash("photo-1546173159-315724a31696"),
    unsplash("photo-1513558161293-cdaf765ed2fd"),
    unsplash("photo-1554866585-cd94860890b7"),
    unsplash("photo-1504674900247-0877df9cc836"),
]
DESSERTS_IMGS = [
    unsplash("photo-1551024601-bec78aea704b"),
    unsplash("photo-1578985545062-69928b1d9587"),
    unsplash("photo-1509440159596-0249088772ff"),
    unsplash("photo-1565958011703-44f9829ba187"),
    unsplash("photo-1550507992-eb63ffee0847"),
]

PIZZAS = [
    {
        "name": "Margherita Magic",
        "category": "pizza",
        "description": "Classic pizza with fresh tomatoes, mozzarella, basil, and oregano",
        "ingredients_text": "Tomato, Mozzarella, Basil",
        "base_price": 299.00,
        "rating": 4.8,
        "review_count": 245,
        "is_featured": True,
        "discount": 10,
        "delivery_time": "20-25 min",
        "image_url": PIZZA_IMGS[0],
    },
    {
        "name": "Pepperoni Passion",
        "category": "pizza",
        "description": "Loaded with spicy pepperoni and extra cheese",
        "ingredients_text": "Pepperoni, Mozzarella, Tomato",
        "base_price": 349.00,
        "rating": 4.7,
        "review_count": 312,
        "is_featured": True,
        "discount": 15,
        "delivery_time": "25-30 min",
        "image_url": PIZZA_IMGS[4],
    },
    {
        "name": "Veggie Paradise",
        "category": "pizza",
        "description": "Packed with fresh vegetables and herbs",
        "ingredients_text": "Bell Peppers, Onions, Mushrooms, Olives, Spinach",
        "base_price": 329.00,
        "rating": 4.6,
        "review_count": 187,
        "is_featured": True,
        "discount": 10,
        "delivery_time": "22-28 min",
        "image_url": PIZZA_IMGS[1],
    },
    {
        "name": "BBQ Chicken Bonanza",
        "category": "pizza",
        "description": "Grilled chicken with BBQ sauce and caramelized onions",
        "ingredients_text": "Chicken, BBQ Sauce, Onions, Cheddar",
        "base_price": 379.00,
        "rating": 4.9,
        "review_count": 428,
        "is_featured": False,
        "discount": 12,
        "delivery_time": "25-32 min",
        "image_url": PIZZA_IMGS[5],
    },
    {
        "name": "Seafood Supreme",
        "category": "pizza",
        "description": "Premium pizza with shrimp, calamari, and garlic",
        "ingredients_text": "Shrimp, Calamari, Garlic, Mushrooms",
        "base_price": 449.00,
        "rating": 4.5,
        "review_count": 156,
        "is_featured": False,
        "discount": 8,
        "delivery_time": "28-35 min",
        "image_url": PIZZA_IMGS[3],
    },
    {
        "name": "Four Cheese Delight",
        "category": "pizza",
        "description": "Combination of mozzarella, cheddar, parmesan, and feta",
        "ingredients_text": "Mozzarella, Cheddar, Parmesan, Feta",
        "base_price": 389.00,
        "rating": 4.7,
        "review_count": 289,
        "is_featured": False,
        "discount": 10,
        "delivery_time": "23-30 min",
        "image_url": PIZZA_IMGS[2],
    },
    {
        "name": "Meat Lovers",
        "category": "pizza",
        "description": "Pepperoni, sausage, bacon, and ham on thick crust",
        "ingredients_text": "Pepperoni, Sausage, Bacon, Ham",
        "base_price": 399.00,
        "rating": 4.8,
        "review_count": 356,
        "is_featured": False,
        "discount": 14,
        "delivery_time": "26-32 min",
        "image_url": PIZZA_IMGS[5],
    },
    {
        "name": "Spicy Buffalo",
        "category": "pizza",
        "description": "Chicken with hot buffalo sauce and ranch drizzle",
        "ingredients_text": "Chicken, Buffalo Sauce, Ranch, Cheddar",
        "base_price": 359.00,
        "rating": 4.6,
        "review_count": 198,
        "is_featured": False,
        "discount": 11,
        "delivery_time": "24-30 min",
        "image_url": PIZZA_IMGS[1],
    },
]

BURGERS = [
    {
        "name": "Classic Cheeseburger",
        "category": "burger",
        "description": "Juicy beef patty with melted cheddar and fresh lettuce",
        "ingredients_text": "Beef, Cheddar, Lettuce, Tomato, Pickles",
        "base_price": 199.00,
        "rating": 4.5,
        "review_count": 234,
        "is_featured": False,
        "discount": 10,
        "delivery_time": "15-20 min",
        "image_url": BURGER_IMGS[0],
    },
    {
        "name": "Double Bacon Burger",
        "category": "burger",
        "description": "Double patty with crispy bacon and onion rings",
        "ingredients_text": "Double Beef, Bacon, Cheddar, Onion Rings",
        "base_price": 279.00,
        "rating": 4.7,
        "review_count": 312,
        "is_featured": True,
        "discount": 12,
        "delivery_time": "18-23 min",
        "image_url": BURGER_IMGS[1],
    },
    {
        "name": "Spicy Jalapeno Burger",
        "category": "burger",
        "description": "Beef burger with jalapenos, pepper jack cheese, and chipotle mayo",
        "ingredients_text": "Beef, Jalapenos, Pepper Jack, Chipotle Mayo",
        "base_price": 239.00,
        "rating": 4.6,
        "review_count": 167,
        "is_featured": False,
        "discount": 8,
        "delivery_time": "16-21 min",
        "image_url": BURGER_IMGS[2],
    },
    {
        "name": "Mushroom Swiss Burger",
        "category": "burger",
        "description": "Beef with sautéed mushrooms and swiss cheese",
        "ingredients_text": "Beef, Mushrooms, Swiss Cheese, Caramelized Onions",
        "base_price": 249.00,
        "rating": 4.4,
        "review_count": 143,
        "is_featured": False,
        "discount": 10,
        "delivery_time": "17-22 min",
        "image_url": BURGER_IMGS[3],
    },
]

SIDES = [
    {
        "name": "Crispy French Fries",
        "category": "sides",
        "description": "Golden crispy fries with sea salt",
        "ingredients_text": "Potatoes, Sea Salt",
        "base_price": 99.00,
        "rating": 4.3,
        "review_count": 567,
        "is_featured": False,
        "discount": 5,
        "delivery_time": "8-12 min",
        "image_url": SIDES_IMGS[0],
    },
    {
        "name": "Cheesy Garlic Bread",
        "category": "sides",
        "description": "Toasted bread with garlic butter and melted cheese",
        "ingredients_text": "Bread, Garlic, Butter, Mozzarella",
        "base_price": 129.00,
        "rating": 4.6,
        "review_count": 423,
        "is_featured": True,
        "discount": 10,
        "delivery_time": "10-15 min",
        "image_url": SIDES_IMGS[1],
    },
    {
        "name": "Loaded Nachos",
        "category": "sides",
        "description": "Nachos with cheese, jalapeños, and sour cream",
        "ingredients_text": "Tortilla Chips, Cheddar, Jalapenos, Sour Cream",
        "base_price": 159.00,
        "rating": 4.5,
        "review_count": 289,
        "is_featured": False,
        "discount": 8,
        "delivery_time": "12-17 min",
        "image_url": SIDES_IMGS[2],
    },
    {
        "name": "Mozzarella Sticks",
        "category": "sides",
        "description": "Crispy mozzarella sticks with marinara sauce",
        "ingredients_text": "Mozzarella, Breadcrumbs, Marinara",
        "base_price": 149.00,
        "rating": 4.7,
        "review_count": 356,
        "is_featured": False,
        "discount": 12,
        "delivery_time": "10-15 min",
        "image_url": SIDES_IMGS[3],
    },
    {
        "name": "Buffalo Wings",
        "category": "sides",
        "description": "Spicy buffalo wings with blue cheese dip",
        "ingredients_text": "Chicken Wings, Buffalo Sauce, Blue Cheese",
        "base_price": 199.00,
        "rating": 4.8,
        "review_count": 445,
        "is_featured": False,
        "discount": 10,
        "delivery_time": "15-20 min",
        "image_url": SIDES_IMGS[4],
    },
]

DRINKS = [
    {
        "name": "Coca Cola",
        "category": "drinks",
        "description": "Ice-cold cola drink (500ml)",
        "ingredients_text": "Carbonated Water, Sugar, Caramel Color",
        "base_price": 49.00,
        "rating": 4.0,
        "review_count": 234,
        "is_featured": False,
        "discount": 0,
        "delivery_time": "2-5 min",
        "image_url": DRINKS_IMGS[0],
    },
    {
        "name": "Sprite Lemonade",
        "category": "drinks",
        "description": "Refreshing lemon-lime soda (500ml)",
        "ingredients_text": "Carbonated Water, Lemon, Lime",
        "base_price": 49.00,
        "rating": 4.1,
        "review_count": 178,
        "is_featured": False,
        "discount": 0,
        "delivery_time": "2-5 min",
        "image_url": DRINKS_IMGS[1],
    },
    {
        "name": "Fresh Mango Shake",
        "category": "drinks",
        "description": "Creamy mango shake with ice cream",
        "ingredients_text": "Mango, Milk, Ice Cream",
        "base_price": 129.00,
        "rating": 4.6,
        "review_count": 289,
        "is_featured": True,
        "discount": 8,
        "delivery_time": "5-10 min",
        "image_url": DRINKS_IMGS[2],
    },
    {
        "name": "Strawberry Smoothie",
        "category": "drinks",
        "description": "Fresh strawberry smoothie with yogurt",
        "ingredients_text": "Strawberry, Yogurt, Honey",
        "base_price": 119.00,
        "rating": 4.5,
        "review_count": 212,
        "is_featured": False,
        "discount": 7,
        "delivery_time": "5-10 min",
        "image_url": DRINKS_IMGS[3],
    },
    {
        "name": "Iced Coffee",
        "category": "drinks",
        "description": "Strong iced coffee with cream and sugar",
        "ingredients_text": "Coffee, Milk, Ice, Sugar",
        "base_price": 99.00,
        "rating": 4.7,
        "review_count": 334,
        "is_featured": False,
        "discount": 10,
        "delivery_time": "5-8 min",
        "image_url": DRINKS_IMGS[4],
    },
]

DESSERTS = [
    {
        "name": "Chocolate Lava Cake",
        "category": "desserts",
        "description": "Warm chocolate cake with melting center",
        "ingredients_text": "Chocolate, Flour, Butter, Eggs",
        "base_price": 149.00,
        "rating": 4.9,
        "review_count": 423,
        "is_featured": True,
        "discount": 12,
        "delivery_time": "8-12 min",
        "image_url": DESSERTS_IMGS[0],
    },
    {
        "name": "Cheesecake Delight",
        "category": "desserts",
        "description": "Creamy New York style cheesecake",
        "ingredients_text": "Cream Cheese, Eggs, Sugar, Graham Crackers",
        "base_price": 179.00,
        "rating": 4.8,
        "review_count": 356,
        "is_featured": False,
        "discount": 10,
        "delivery_time": "10-15 min",
        "image_url": DESSERTS_IMGS[1],
    },
    {
        "name": "Brownie Sundae",
        "category": "desserts",
        "description": "Warm brownie with vanilla ice cream and chocolate sauce",
        "ingredients_text": "Brownie, Ice Cream, Chocolate Sauce",
        "base_price": 159.00,
        "rating": 4.7,
        "review_count": 267,
        "is_featured": False,
        "discount": 8,
        "delivery_time": "8-12 min",
        "image_url": DESSERTS_IMGS[2],
    },
    {
        "name": "Tiramisu Cup",
        "category": "desserts",
        "description": "Traditional tiramisu with mascarpone and cocoa",
        "ingredients_text": "Mascarpone, Ladyfinger, Cocoa, Coffee",
        "base_price": 169.00,
        "rating": 4.6,
        "review_count": 198,
        "is_featured": False,
        "discount": 10,
        "delivery_time": "5-8 min",
        "image_url": DESSERTS_IMGS[3],
    },
    {
        "name": "Gulab Jamun Dessert",
        "category": "desserts",
        "description": "Soft gulab jamun balls in warm sugar syrup",
        "ingredients_text": "Milk Powder, Sugar Syrup, Cardamom",
        "base_price": 129.00,
        "rating": 4.5,
        "review_count": 312,
        "is_featured": False,
        "discount": 7,
        "delivery_time": "5-8 min",
        "image_url": DESSERTS_IMGS[4],
    },
]

# Existing products in the DB that only lack an image reference. Only the empty
# image_url is repaired; every other field is left untouched.
EXISTING_IMAGE_REPAIRS = {
    "Margherita": PIZZA_IMGS[0],
    "Pepperoni": PIZZA_IMGS[2],
    "Veggie Blast": PIZZA_IMGS[1],
}

ALL_PRODUCTS = PIZZAS + BURGERS + SIDES + DRINKS + DESSERTS

# Builder ingredients consumed by the Pizza Builder API
# (/inventory/bases|sauces|cheeses|vegetables). These MUST exist or the
# builder has nothing to select and the custom-pizza checkout fails because
# base/sauce/cheese ids are null. Seed them idempotently alongside the menu.
INGREDIENTS = {
    "bases": PizzaBase,
    "sauces": Sauce,
    "cheeses": Cheese,
    "vegetables": Vegetable,
}

INGREDIENT_DATA = {
    "bases": [
        ("Thin Crust", 180.00),
        ("Hand Tossed", 220.00),
        ("Stuffed Crust", 260.00),
        ("Cheese Burst", 280.00),
        ("Whole Wheat", 240.00),
    ],
    "sauces": [
        ("Marinara", 40.00),
        ("BBQ", 50.00),
        ("Pesto", 60.00),
        ("Arrabbiata", 55.00),
        ("Creamy Garlic", 65.00),
    ],
    "cheeses": [
        ("Mozzarella", 55.00),
        ("Cheddar", 65.00),
        ("Paneer", 70.00),
    ],
    "vegetables": [
        ("Onion", 20.00),
        ("Capsicum", 25.00),
        ("Olives", 30.00),
        ("Mushroom", 35.00),
    ],
}


class Command(BaseCommand):
    help = ("Seed the full food catalog (pizza/burger/sides/drinks/desserts) and "
            "the pizza-builder ingredients (bases/sauces/cheeses/vegetables) "
            "without deleting anything. Existing rows are kept as-is; only empty "
            "image_url fields are repaired.")

    def handle(self, *args, **options):
        created = 0
        repaired = 0

        # 1) Pizza-builder ingredients first — the builder (and custom-pizza
        #    checkout validation) depend on these existing.
        for group, model_cls in INGREDIENTS.items():
            for name, price in INGREDIENT_DATA[group]:
                obj, was_created = model_cls.objects.get_or_create(
                    name=name,
                    defaults={"price": price, "is_available": True},
                )
                if was_created:
                    created += 1
                    self.stdout.write(f"  + Created {group[:-1]}: {name}")

        # 2) Menu products.
        for product_data in ALL_PRODUCTS:
            defaults = {k: v for k, v in product_data.items() if k != "name"}
            obj, was_created = Pizza.objects.get_or_create(
                name=product_data["name"], defaults={**defaults, "is_available": True}
            )
            if was_created:
                created += 1
                self.stdout.write(f"  + Created {product_data['name']} ({product_data['category']})")
            elif not obj.image_url and not obj.image and product_data.get("image_url"):
                obj.image_url = product_data["image_url"]
                obj.save(update_fields=["image_url"])
                repaired += 1
                self.stdout.write(f"  + Repaired image for {product_data['name']}")

        for name, image_url in EXISTING_IMAGE_REPAIRS.items():
            obj = Pizza.objects.filter(name=name).first()
            if obj and not obj.image_url and not obj.image:
                obj.image_url = image_url
                obj.save(update_fields=["image_url"])
                repaired += 1
                self.stdout.write(f"  + Repaired image for {name}")

        counts = {c: Pizza.objects.filter(category=c).count()
                  for c in ("pizza", "burger", "sides", "drinks", "desserts")}
        ingredient_counts = {
            "bases": PizzaBase.objects.count(),
            "sauces": Sauce.objects.count(),
            "cheeses": Cheese.objects.count(),
            "vegetables": Vegetable.objects.count(),
        }
        self.stdout.write(self.style.SUCCESS(
            f"Done. Created {created}, repaired {repaired} image refs. "
            f"Menu totals: {counts}. Ingredients: {ingredient_counts}"
        ))