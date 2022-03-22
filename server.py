from flask import Flask, abort  # from file or mdule import X
import json
from mock_data import catalog  # fn or something...




app = Flask("Server")


@app.route("/")
def home():
  return "Hello from Flask"



@app.route("/me") # add /me to the URL
def about_me():
  return "Mark Omer"



#####################################
####  API ENDPOINTS  ################
####   RETURN JSON   ################
#####################################


# @app.route("/api/catalog")
@app.route("/api/catalog", methods=["get"])
def get_catalog():

  """ return "catalog data"
  return json.dumps(prod) # this is how parse..."""
  return json.dumps(catalog)

  """prod = {
    "title":"test",
    "price": 123.423
  }"""

@app.route("/api/catalog", methods=["post"])
def save_product():
  pass



# GET /api/catalog/count -> how many products exist in the catalog

@app.route("/api/catalog/count", methods=["get"])
def count_prods():
  count = len(catalog)
  return json.dumps(count)
  # or... return json.dumps(len(count))

# get /api/catalog/total => the sum of all porduct's prices
@app.route("/api/catalog/total")
def total_of_catalog():
  total = 0
  for prod in catalog: # into prods in catalog array
    total += prod["price"]

  return json.dumps(total)



@app.route("/api/product/<id>") # whatever is in <xx> is an id var
def get_by_id(id):
  # find the product with _id is equal to id
  for prod in catalog:
    if prod["_id"] == id:
      return json.dumps(prod)

  # not found, return an error 404
  return abort(404, "No product with such id")


# GET /api/product/cheapest
# should return the product with the lowest price


@app.route("/api/product/cheapest")
def cheapest_product():
  solution = catalog[0]
  for prod in catalog:
    if prod["price"] < solution["price"]:
      solution = prod

  return json.dumps(solution)



@app.route("/api/categories")
def unique_categories():
  categories = []
  for prod in catalog:
    category = prod["category"]
    if not category in categories:
      categories.append(category)

  return json.dumps(categories)

# 
# Ticket 2345
# Create and endpoint that allow the client to get all the products
# for an specified category 
# /api/catalog/Fruit where Fruit is the category in question

@app.route("/api/categories/<category>")
def get_by_category(category):
  result = []
  for prod in catalog:
    if prod["category"] == category:
      result.append(prod)

  return json.dumps(result)



app.run(debug=True)