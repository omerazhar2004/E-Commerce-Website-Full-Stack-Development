'''Script to populate the database with some initial data.
   In reality you would probably create a separate editor or a tool for importing data from elsewhere,
   but for CM1102 we'll just use this script to populate the database.'''

from app import app, db, Technology
technologies = [
            { "name": "Stick Cooking Pan", "price": 28.99, "description": "Effortlessly cook and clean with our premium non-stick pan. Even heat distribution for perfect meals every time.", "img_loc": "/static/Stick cooking pan.jpeg"},
            { "name": "Ski Jacket", "price": 40.22, "description": "Stay warm and dry with our high-performance ski jacket. Advanced insulation and breathable waterproof design for ultimate comfort.", "img_loc": "/static/Ski Jacket.jpeg"},
            { "name": "Mountain Bike", "price": 699.99, "description": "Explore rugged terrains with our durable mountain bike. Lightweight frame, responsive suspension, and precision gearing for total control.", "img_loc": "/static/Mountain Bike.jpeg" },
        ]
# Bear in mind this script does NOT run the app
# instead we use app.app_context() which Flask provides to allow us to use the app's configuration and extensions
with app.app_context():
    db.create_all() # creates the empty tables
    
    for tech in technologies:
        newTech = Technology(name=tech["name"], price=tech["price"], description=tech["description"], img_loc = tech["img_loc"])
        db.session.add(newTech)
    
    db.session.commit()


