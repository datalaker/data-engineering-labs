import time
from datetime import datetime
from airflow.models.dag import DAG
from airflow.decorators import task
from airflow.utils.task_group import TaskGroup
from airflow.hooks.base_hook import BaseHook
from airflow.providers.postgres.operators.postgres import PostgresOperator
import pandas as pd
from sqlalchemy import create_engine

#extract tasks
@task()
def get_src_tables(file_path):
    df = pd.read_excel(file_path)
    print("Summary of src data table:\n", df.info())
    return df

@task()
def load_src_data(df: pd.DataFrame):
    conn = BaseHook.get_connection('postgres')
    engine = create_engine(f'postgresql://{conn.login}:{conn.password}@{conn.host}:{conn.port}/{conn.schema}')
    df.to_sql(f'src_AdvWorks', engine, if_exists='replace', index=False)
    print("Data imported successful")

#transform tasks
@task()
def transform_srcProduct():
    conn = BaseHook.get_connection('postgres')
    engine = create_engine(f'postgresql://{conn.login}:{conn.password}@{conn.host}:{conn.port}/{conn.schema}')
    pdf = pd.read_sql_query('SELECT * FROM public."src_DimProduct" ', engine)
    #drop columns
    revised = pdf[['ProductKey', 'ProductAlternateKey', 'ProductSubcategoryKey','WeightUnitMeasureCode', 'SizeUnitMeasureCode', 'EnglishProductName',
                   'StandardCost','FinishedGoodsFlag', 'Color', 'SafetyStockLevel', 'ReorderPoint','ListPrice', 'Size', 'SizeRange', 'Weight',
                   'DaysToManufacture','ProductLine', 'DealerPrice', 'Class', 'Style', 'ModelName', 'EnglishDescription', 'StartDate','EndDate', 'Status']]
    #replace nulls
    revised['WeightUnitMeasureCode'].fillna('0', inplace=True)
    revised['ProductSubcategoryKey'].fillna('0', inplace=True)
    revised['SizeUnitMeasureCode'].fillna('0', inplace=True)
    revised['StandardCost'].fillna('0', inplace=True)
    revised['ListPrice'].fillna('0', inplace=True)
    revised['ProductLine'].fillna('NA', inplace=True)
    revised['Class'].fillna('NA', inplace=True)
    revised['Style'].fillna('NA', inplace=True)
    revised['Size'].fillna('NA', inplace=True)
    revised['ModelName'].fillna('NA', inplace=True)
    revised['EnglishDescription'].fillna('NA', inplace=True)
    revised['DealerPrice'].fillna('0', inplace=True)
    revised['Weight'].fillna('0', inplace=True)
    # Rename columns with rename function
    revised = revised.rename(columns={"EnglishDescription": "Description", "EnglishProductName":"ProductName"})
    revised.to_sql(f'stg_DimProduct', engine, if_exists='replace', index=False)
    return {"table(s) processed ": "Data imported successful"}

#
@task()
def transform_srcProductSubcategory():
    conn = BaseHook.get_connection('postgres')
    engine = create_engine(f'postgresql://{conn.login}:{conn.password}@{conn.host}:{conn.port}/{conn.schema}')
    pdf = pd.read_sql_query('SELECT * FROM public."src_DimProductSubcategory" ', engine)
    #drop columns
    revised = pdf[['ProductSubcategoryKey','EnglishProductSubcategoryName', 'ProductSubcategoryAlternateKey','EnglishProductSubcategoryName', 'ProductCategoryKey']]
    # Rename columns with rename function
    revised = revised.rename(columns={"EnglishProductSubcategoryName": "ProductSubcategoryName"})
    revised.to_sql(f'stg_DimProductSubcategory', engine, if_exists='replace', index=False)
    return {"table(s) processed ": "Data imported successful"}

@task()
def transform_srcProductCategory():
    conn = BaseHook.get_connection('postgres')
    engine = create_engine(f'postgresql://{conn.login}:{conn.password}@{conn.host}:{conn.port}/{conn.schema}')
    pdf = pd.read_sql_query('SELECT * FROM public."src_DimProductCategory" ', engine)
    #drop columns
    revised = pdf[['ProductCategoryKey', 'ProductCategoryAlternateKey','EnglishProductCategoryName']]
    # Rename columns with rename function
    revised = revised.rename(columns={"EnglishProductCategoryName": "ProductCategoryName"})
    revised.to_sql(f'stg_DimProductCategory', engine, if_exists='replace', index=False)
    return {"table(s) processed ": "Data imported successful"}

#load
@task()
def prdProduct_model():
    conn = BaseHook.get_connection('postgres')
    engine = create_engine(f'postgresql://{conn.login}:{conn.password}@{conn.host}:{conn.port}/{conn.schema}')
    pc = pd.read_sql_query('SELECT * FROM public."stg_DimProductCategory" ', engine)
    p = pd.read_sql_query('SELECT * FROM public."stg_DimProduct" ', engine)
    p['ProductSubcategoryKey'] = p.ProductSubcategoryKey.astype(float)
    p['ProductSubcategoryKey'] = p.ProductSubcategoryKey.astype(int)
    ps = pd.read_sql_query('SELECT * FROM public."stg_DimProductSubcategory" ', engine)
    #join all three
    merged = p.merge(ps, on='ProductSubcategoryKey').merge(pc, on='ProductCategoryKey')
    merged.to_sql(f'prd_DimProductCategory', engine, if_exists='replace', index=False)
    return {"table(s) processed ": "Data imported successful"}


# [START how_to_task_group]
with DAG(dag_id="product_etl_dag",schedule_interval="0 9 * * *", start_date=datetime(2022, 3, 5),catchup=False,  tags=["product_model"]) as dag:

    with TaskGroup("extract_dimProudcts_load", tooltip="Extract and load source data") as extract_load_src:
        src_product_tbls = get_src_tables()
        load_dimProducts = load_src_data(src_product_tbls)
        #define order
        src_product_tbls >> load_dimProducts

    # [START howto_task_group_section_2]
    with TaskGroup("transform_src_product", tooltip="Transform and stage data") as transform_src_product:
        transform_srcProduct = transform_srcProduct()
        transform_srcProductSubcategory = transform_srcProductSubcategory()
        transform_srcProductCategory = transform_srcProductCategory()
        #define task order
        [transform_srcProduct, transform_srcProductSubcategory, transform_srcProductCategory]

    with TaskGroup("load_product_model", tooltip="Final Product model") as load_product_model:
        prd_Product_model = prdProduct_model()
        #define order
        prd_Product_model

    extract_load_src >> transform_src_product >> load_product_model