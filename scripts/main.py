import pandas as pd
import numpy as np


def clean_cafe_data(input_path, output_path):
    """
    Realiza o pipeline completo de limpeza e normalização do dataset de café.
    """

  
    valores_invalidos = ["UNKNOWN", "ERROR", "nan", ""]
    df = pd.read_csv(input_path, na_values=valores_invalidos)

    df.columns = (df.columns
                    .str.lower()
                    .str.replace(' ', '_')
                    .str.replace(r'[^\w\s]', '', regex=True))

    
    df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce').astype('Int64')
    df['price_per_unit'] = pd.to_numeric(df['price_per_unit'], errors='coerce')
    df['total_spent'] = pd.to_numeric(df['total_spent'], errors='coerce')
    df['transaction_date'] = pd.to_datetime(df['transaction_date'], errors='coerce')

    price_map = {
        'Coffee': 2.0, 'Tea': 1.5, 'Juice': 3.0, 'Smoothie': 4.0,
        'Sandwich': 4.0, 'Cake': 3.0, 'Cookie': 1.0, 'Salad': 5.0
    }

 
    df['price_per_unit'] = df['price_per_unit'].fillna(df['item'].map(price_map))
    

    df['total_spent'] = df['quantity'] * df['price_per_unit']

    # Preenchimento de categorias nulas
    df['payment_method'] = df['payment_method'].fillna('Unknown')
    df['location'] = df['location'].fillna('Unknown')

 
    df.drop_duplicates(subset=['transaction_id'], keep='first', inplace=True)
    
  
    df.dropna(subset=['item'], inplace=True) 
    df.dropna(subset=['quantity', 'total_spent'], how='all', inplace=True)

   
    df.to_csv(output_path, index=False)

if __name__ == "__main__":

    ARQUIVO_ENTRADA = '../data/dirty_cafe_sales.csv'
    ARQUIVO_SAIDA = '../data/clean_cafe_sales.csv'
    
    clean_cafe_data(ARQUIVO_ENTRADA, ARQUIVO_SAIDA)