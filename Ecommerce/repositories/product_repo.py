class productRepository:

    products = []
    curr_id = 0

    @classmethod
    def create_product(cls, product):
        product_data = {
            "id": cls.curr_id,
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "brand": product.brand,
            "stock_quantity": product.stock_quantity,
            "image_url": product.image_url
        }
        cls.products.append(product_data)
        cls.curr_id += 1
        return product_data

    @classmethod
    def list_products(cls, offset: int = 0, limit: int = 10):
        return cls.products[offset: offset + limit]
    
    @classmethod
    def get_product(cls, product_id: int):
        for product in cls.products:
            if product["id"] == product_id:
                return product
        return None