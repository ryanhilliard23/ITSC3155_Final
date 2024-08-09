from . import customers, resources, menu_items, order_details, orders, promotion, review, recipes, payment, resource_management

def load_routes(app):
    app.include_router(customers.router)
    app.include_router(menu_items.router)
    app.include_router(order_details.router)
    app.include_router(orders.router)
    app.include_router(promotion.router)
    app.include_router(review.router)
    app.include_router(payment.router)
    app.include_router(recipes.router)
    app.include_router(resources.router)
    app.include_router(resource_management.router)