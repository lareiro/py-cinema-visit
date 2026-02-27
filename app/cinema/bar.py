class CinemaBar:

    @staticmethod
    def sell_product(product: str, customer: object) -> None:
        customer_name = customer.name if hasattr(customer, "name")\
            else customer
        print(f"Cinema bar sold {product} to {customer_name}.")
