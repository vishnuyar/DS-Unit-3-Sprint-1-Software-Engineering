from random import randint, sample, uniform,choice

from acme import Product

#List of available adjectives for the product name
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
#List of available nouns for the product name
NOUNS = ['Anvil', 'Catapult', 'Disguise' ,'Mousetrap', '???']

def generate_products(num_products=30):
    """ 
    Generates and returns the given quantity of products
    If quantity of products is not given 30 products are generated
    
    """
    #creating a empty list for storing products    
    products = []
    
    #Generating a product for the given quantity
    names = [(choice(ADJECTIVES) + " " + choice(NOUNS)) for number in range(num_products)]
    prices = [randint(0,100) for number in range(num_products)]
    weights = [randint(0,100) for number in range(num_products)]
    flammbs = [uniform(0,2.5) for number in range(num_products)]
    
    #Generating the products by calling the product class
    for num in range(num_products):
        product = Product(names[num],prices[num],weights[num],flammbs[num])
        #Adding product to the Products list
        products.append(product)

    return products



def inventory_report(products):
    """ 
    Generating a report based on products
    The report will have 
    Number of unique product names in the product list
    Average (mean) price, weight, and flammability of listed products

    """
    #Getting the value of Number of products
    product_quanity = len(products)

    #Getting the values of each of  the products
    product_names = [products[num].name for num in range(product_quanity)]
    prices = [products[num].price for num in range(product_quanity)]
    weights = [products[num].weight for num in range(product_quanity)]
    flammbs = [products[num].flammability for num in range(product_quanity)]
    
    #Getting the set of unique names and number of items in the set
    unique_names = len(set(product_names))
    #Getting the average values of the product attributes
    avg_price = sum(prices)/product_quanity
    avg_weight = sum(weights)/product_quanity
    avg_flamability = sum(flammbs)/product_quanity

    #Creating a Report
    report = "ACME CORPORATION OFFICIAL INVENTORY REPORT\n"
    report = report + "Unique product names:"+str(unique_names)+"\n"
    report = report + "Average price:"+str(avg_price)+"\n"
    report = report + "Average weight:"+str(avg_weight)+"\n"
    report = report + "Average flammability:"+str(avg_flamability)+"\n"

    #Sending the report
    print(report)

if __name__ == '__main__':
    inventory_report(generate_products())