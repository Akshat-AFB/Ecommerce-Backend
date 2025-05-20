from repositories.product_repo import productRepository

class ProductService:
    @staticmethod
    def list_products(offset: int = 0, limit: int = 10):
        return productRepository.list_products(offset, limit)

    @staticmethod
    def get_product(product_id: int):
        return productRepository.get_product(product_id)

    @staticmethod
    def create_product(product):
        return productRepository.create_product(product)