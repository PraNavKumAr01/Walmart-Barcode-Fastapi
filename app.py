from fastapi import FastAPI
import pandas as pd

app = FastAPI()

# Load Walmart data from CSV file
walmart_data = pd.read_csv('walmart_data.csv')

@app.get('/product/{barcode}')
def get_product(barcode: int):
    product = walmart_data[walmart_data['Gtin'] == barcode]
    if not product.empty:
        product_info = {
            "name": product.iloc[0]['Product Name'],
            "sale_price": float(product.iloc[0]['Sale Price'])
        }
        return product_info
    else:
        return {"error": "Product not found"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
