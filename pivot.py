import pandas as pd 

#Constructing the dataframe with desired parameters
sales_data = pd.read_csv(
    "sales_data.csv",
    parse_dates = ["order_date"],
    dayfirst = True,
    ).convert_dtypes(dtype_backend ="pyarrow")

#Adding to format the currency in the dataframe 
pd.set_option("display.float_format", "${:,.2f}".format)

#Using pivot table method to the pandas dataFrame 
new_sales_data = sales_data.pivot_table(
    values= "sale_price", index ="sales_region", columns="order_type", 
    aggfunc ="sum", margins = True, margins_name= "Totals" )

#Using pivot method again to make a new dataframe with Sub Columns
new_new_sales_data = sales_data.pivot_table(
    values = "sale_price", index = "customer_state",
    columns=["customer_type", "order_type"], aggfunc= "mean"
    )

#Using pivot method to make a new dataframe with sub rows
new_new_new_sales_data = sales_data.pivot_table(
    values="sale_price", index=["customer_type", "order_type"], 
    columns = "product_category", aggfunc="sum" 
)

#Calculating multiple values in the pivot table by taking two columns as value 
new_new_new_new_sales_data = sales_data.pivot_table(
    index=["sales_region", "product_category"],
    values=["sale_price", "quantity"],
    aggfunc = "sum", fill_value=0
).loc[:, ["sale_price", "quantity"]] #the loc to define the rows and columns that I wish to see by their index label


#Apply multiple aggregation to the same data 
new_x5_sales_data = sales_data.pivot_table(
    values= ["sale_price", "quantity"], 
    index=["product_category"],
    columns = "customer_type",
    aggfunc={"sale_price": "mean", "quantity": "max"},
    )

# Custom aggregated function, takes a series as its argument
#and returns a single aggregated value 
def count_unique (values): #Accepting a pandas series named values
    return len(values.unique())

new_custom_sales_data = sales_data.pivot_table(
    values = "employee_id",
    index = ["sales_region"], 
    aggfunc = count_unique
    )

#named aggregation using .groupby 
(
 
     sales_data
     .groupby("product_category")
     .agg(
          low_price=("sale_price", "min"),
          average_price= ("sale_price", "mean"),
          high_price=("sale_price", "max"),
          standard_deviation = ("sale_price", "std"),
      )
 )

#

#pringting and saving it 
new_x5_sales_data.head(2)
print(sales_data)
new_x5_sales_data.to_csv (r'~/Desktop/test.csv')

