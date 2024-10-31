import pandas as pd

from data_loader import DataLoader
from data_cleaner import DataCleaner

class Analysis:
    def __init__(self, vendas_globais: str, transportadoras: str, fornecedores: str, vendedores: str):
        self.vendas_globais = DataLoader.load_csv(rf'{vendas_globais}')
        self.transportadoras = DataLoader.load_csv(rf'{transportadoras}')
        self.fornecedores = DataLoader.load_csv(rf'{fornecedores}')
        self.vendedores = DataLoader.load_csv(rf'{vendedores}')

        self.clean_data()

        self.vendas_globais = self.vendas_globais.merge(
            self.vendedores[['VendedorID', 'VendedorNome']], on='VendedorID', how='left'
        ).merge(
            self.fornecedores[['FornecedorID', 'FornecedorNome']], on='FornecedorID', how='left'
        )


    def clean_data(self):
        self.vendas_globais = DataCleaner.clean_data(self.vendas_globais)
        self.transportadoras = DataCleaner.clean_data(self.transportadoras)
        self.fornecedores = DataCleaner.clean_data(self.fornecedores)
        self.vendedores = DataCleaner.clean_data(self.vendedores)

    
    def top_customers(self, n: int = 10) -> pd.DataFrame:
        return self.vendas_globais.groupby('ClienteNome')['Vendas'].sum().nlargest(n)

    def top_countries(self, n: int = 3) -> pd.DataFrame:
        return self.vendas_globais.groupby('ClientePaís')['Vendas'].sum().nlargest(n)
        
    def top_categories_by_country(self, country: str) -> pd.DataFrame:
        df_country = self.vendas_globais[self.vendas_globais['ClientePaís'] == country]
        return df_country.groupby('CategoriaNome')['Vendas'].sum().nlargest(3)

    def freight_per_carrier(self) -> pd.DataFrame:
        df_with_names = self.vendas_globais.merge(
            self.transportadoras[['TransportadoraID', 'TransportadoraNome']],
            on='TransportadoraID',
            how='left'
        )
        return df_with_names.groupby('TransportadoraNome')['Frete'].sum()

    def top_mens_footwear_customers(self, country: str) -> pd.DataFrame:
        df_segment = self.vendas_globais[
            (self.vendas_globais['CategoriaNome'].str.contains("Men")) & 
            (self.vendas_globais['ClientePaís'] == country)
        ]
        
        if df_segment.empty:
            return pd.DataFrame({'ClienteNome': [], 'Vendas': []})  
        
        return df_segment.groupby('ClienteNome')['Vendas'].sum().nlargest(5)


    def top_discount_sellers_by_country(self, country: str) -> pd.DataFrame:
        df_country = self.vendas_globais[self.vendas_globais['ClientePaís'] == country]
        if df_country.empty:
            return pd.DataFrame({'VendedorNome': [], 'Desconto': []})

        df_with_names = df_country.merge(
            self.vendedores[['VendedorID', 'VendedorNome']],
            on='VendedorID',
            how='left'
        )

        df_with_names.rename(columns={'VendedorNome_y': 'VendedorNome'}, inplace=True)

        if 'VendedorNome' not in df_with_names.columns:
            raise ValueError("A coluna 'VendedorNome' não foi encontrada após o merge. Verifique os nomes das colunas.")

        return df_with_names.groupby('VendedorNome')['Desconto'].sum().nlargest(5)

    def top_profit_suppliers_womens_wear(self) -> pd.DataFrame:
        df_segment = self.vendas_globais[self.vendas_globais['CategoriaNome'] == "Womens wear"]
        profit_per_supplier = df_segment.groupby('FornecedorID')['Margem Bruta'].sum().nlargest(5).reset_index()

        profit_per_supplier = profit_per_supplier.merge(
            self.fornecedores[['FornecedorID', 'FornecedorNome']], on='FornecedorID', how='left'
        )

        profit_per_supplier = profit_per_supplier[['FornecedorNome', 'Margem Bruta']]
        
        return profit_per_supplier.set_index('FornecedorNome')




    def sales_over_years(self, start_year: int, end_year: int) -> pd.DataFrame:
        self.vendas_globais['Data'] = pd.to_datetime(self.vendas_globais['Data'], format='%d/%m/%Y')
        self.vendas_globais['Ano'] = self.vendas_globais['Data'].dt.year
        sales_per_year = self.vendas_globais.groupby('Ano')['Vendas'].sum()
        return sales_per_year[(sales_per_year.index >= start_year) & (sales_per_year.index <= end_year)]

    
    def top_countries_by_orders(self) -> pd.DataFrame:
        return self.vendas_globais.groupby('ClientePaís')['PedidoID'].count().nlargest(5)
