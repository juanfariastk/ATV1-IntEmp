import pandas as pd

class Analysis:
    @staticmethod
    def top_customers(df: pd.DataFrame, n: int = 10) -> pd.DataFrame:
        return df.groupby('ClienteNome')['Vendas'].sum().nlargest(n)

    @staticmethod
    def top_countries(df: pd.DataFrame, n: int = 3) -> pd.DataFrame:
        return df.groupby('ClientePaís')['Vendas'].sum().nlargest(n)
        
    @staticmethod
    def top_categories_brazil(df: pd.DataFrame) -> pd.DataFrame:
        df_brazil = df[df['ClientePaís'] == 'Brazil']
        return df_brazil.groupby('CategoriaNome')['Vendas'].sum().nlargest(3)
    
    @staticmethod
    def freight_per_carrier(df: pd.DataFrame) -> pd.DataFrame:
        return df.groupby('TransportadoraID')['Frete'].sum()
    
    @staticmethod
    def top_mens_footwear_customers_germany(df: pd.DataFrame) -> pd.DataFrame:
        df_segment = df[(df['CategoriaNome'].str.contains("Men")) & (df['ClientePaís'] == 'Germany')]
        print(df_segment) 
        if df_segment.empty:
            return pd.DataFrame({'ClienteNome': [], 'Vendas': []})  
        return df_segment.groupby('ClienteNome')['Vendas'].sum().nlargest(5)


    @staticmethod
    def top_discount_sellers_usa(df: pd.DataFrame) -> pd.DataFrame:
        df_usa = df[df['ClientePaís'] == 'USA']
        if df_usa.empty:
            return pd.DataFrame({'VendedorID': [], 'Desconto': []})  
        return df_usa.groupby('VendedorID')['Desconto'].sum().nlargest(5)
    
    @staticmethod
    def top_profit_suppliers_womens_wear(df: pd.DataFrame) -> pd.DataFrame:
        df_segment = df[df['CategoriaNome'] == "Womens wear"]
        return df_segment.groupby('FornecedorID')['Margem Bruta'].sum().nlargest(5)

    @staticmethod
    def sales_over_years(df: pd.DataFrame) -> pd.DataFrame:
        df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y')
        df['Ano'] = df['Data'].dt.year
        sales_per_year = df.groupby('Ano')['Vendas'].sum()
        return sales_per_year[(sales_per_year.index >= 2009) & (sales_per_year.index <= 2012)]
    
    @staticmethod
    def top_countries_by_orders(df: pd.DataFrame) -> pd.DataFrame:
        return df.groupby('ClientePaís')['PedidoID'].count().nlargest(5)
