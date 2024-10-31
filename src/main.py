from data_loader import DataLoader
from data_cleaner import DataCleaner
from analysis import Analysis
from reporting import Reporting

def main():
    vendas_df = DataLoader.load_csv('data/vendas_globais.csv')
    vendas_df = DataCleaner.clean_data(vendas_df)

    analysis = Analysis(
        'data/vendas_globais.csv', 
        'data/transportadoras.csv',
        'data/fornecedores.csv',
        'data/vendedores.csv'
    )
    
    # 1. Quem são os meus 10 maiores clientes, em termos de vendas ($)?
    top_customers = analysis.top_customers()
    Reporting.generate_report(top_customers, "Top 10 Clientes (em $)")

    # 2. Quais os três maiores países, em termos de vendas ($)?
    top_countries = analysis.top_countries()
    Reporting.generate_report(top_countries, "Top 3 Países em Vendas (em $)")

    # 3. Quais as categorias de produtos que geram maior faturamento (vendas $) no Brasil?
    country_to_filter_top_categories = 'Brazil'
    top_categories_from_country = analysis.top_categories_by_country(country_to_filter_top_categories)
    Reporting.generate_report(top_categories_from_country, f"Categorias mais Vendidas no {country_to_filter_top_categories} (em $)")

    # 4. Qual a despesa com frete envolvendo cada transportadora?
    freight_per_carrier = analysis.freight_per_carrier()
    Reporting.generate_report(freight_per_carrier, "Despesa com Frete por Transportadora (em $)")

    # 5. Quais são os principais clientes (vendas $) do segmento “Calçados Masculinos” na Alemanha?
    country_to_filter_footwear_customers = 'Germany'
    top_mens_footwear_customers_from_country = analysis.top_mens_footwear_customers(country_to_filter_footwear_customers)
    Reporting.generate_report(top_mens_footwear_customers_from_country, f"Principais Clientes de Calçados Masculinos na {country_to_filter_footwear_customers} (em $)")

    # 6. Quais os vendedores que mais dão descontos nos Estados Unidos?
    country_to_filter_top_discounts = 'USA'
    top_discount_sellers_from_country = analysis.top_discount_sellers_by_country(country_to_filter_top_discounts)
    Reporting.generate_report(top_discount_sellers_from_country, f"Vendedores que Mais Dão Descontos no {country_to_filter_top_discounts} (em $)")

    # 7. Quais os fornecedores que dão a maior margem de lucro ($) no segmento de “Vestuário Feminino”?
    top_profit_suppliers_womens_wear = analysis.top_profit_suppliers_womens_wear()
    Reporting.generate_report(top_profit_suppliers_womens_wear, "Fornecedores com Maior Margem de Lucro em Vestuário Feminino")

    # 8. Quanto que foi vendido ($) no ano de 2009? O faturamento entre 2009 e 2012 está crescendo, estável ou decaindo?
    year_beginning, year_end = 2009, 2012
    sales_over_years = analysis.sales_over_years(year_beginning, year_end)
    Reporting.generate_report(sales_over_years, f"Vendas de {year_beginning} a {year_end} (em $)")

    # 10. Quais os países nos quais mais se tiram pedidos (qtde total de pedidos)?
    top_countries_by_order = analysis.top_countries_by_orders()
    Reporting.generate_report(top_countries_by_order, "Países que mais tiram pedidos")


if __name__ == "__main__":
    main()

