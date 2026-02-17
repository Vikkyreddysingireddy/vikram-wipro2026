from flask import Flask
from restaurant import restaurant_bp
from dish import dish_bp
from admin import admin_bp
from user import user_bp
from order import order_bp

app = Flask(__name__)

app.register_blueprint(restaurant_bp)
app.register_blueprint(dish_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(user_bp)
app.register_blueprint(order_bp)

if __name__ == "__main__":
    app.run(debug=True, port=2700)