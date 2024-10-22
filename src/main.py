from data_loader import DataLoader
from data_cleaner import DataCleaner
from analysis import Analysis
from reporting import Reporting

def main():

    vendas_df = DataLoader.load_csv('data/vendas_globais.csv')
    vendas_df = DataCleaner.clean_data(vendas_df)
    
    # 1. Quem são os meus 10 maiores clientes, em termos de vendas ($)?
    top_customers = Analysis.top_customers(vendas_df)
    Reporting.generate_report(top_customers, "Top 10 Clientes")

    # 2. Quais os três maiores países, em termos de vendas ($)?
    top_countries = Analysis.top_countries(vendas_df)
    Reporting.generate_report(top_countries, "Top 3 Países em Vendas")

    # 3. Quais as categorias de produtos que geram maior faturamento (vendas $) no Brasil?
    top_categories_brazil = Analysis.top_categories_brazil(vendas_df)
    Reporting.generate_report(top_categories_brazil, "Categorias mais Vendidas no Brasil")

    # 4. Qual a despesa com frete envolvendo cada transportadora?
    freight_per_carrier = Analysis.freight_per_carrier(vendas_df)
    Reporting.generate_report(freight_per_carrier, "Despesa com Frete por Transportadora")

    # 5. Quais são os principais clientes (vendas $) do segmento “Calçados Masculinos” na Alemanha?
    top_mens_footwear_customers_germany = Analysis.top_mens_footwear_customers_germany(vendas_df)
    Reporting.generate_report(top_mens_footwear_customers_germany, "Principais Clientes de Calçados Masculinos na Alemanha")

    # 6. Quais os vendedores que mais dão descontos nos Estados Unidos?
    top_discount_sellers_usa = Analysis.top_discount_sellers_usa(vendas_df)
    Reporting.generate_report(top_discount_sellers_usa, "Vendedores que Mais Dão Descontos nos EUA")

    # 7. Quais os fornecedores que dão a maior margem de lucro ($) no segmento de “Vestuário Feminino”?
    top_profit_suppliers_womens_wear = Analysis.top_profit_suppliers_womens_wear(vendas_df)
    Reporting.generate_report(top_profit_suppliers_womens_wear, "Fornecedores com Maior Margem de Lucro em Vestuário Feminino")

    # 8. Quanto que foi vendido ($) no ano de 2009? O faturamento entre 2009 e 2012 está crescendo, estável ou decaindo?
    sales_over_years = Analysis.sales_over_years(vendas_df)
    Reporting.generate_report(sales_over_years, "Vendas de 2009 a 2012")


if __name__ == "__main__":
    main()

