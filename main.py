import pandas as pd
from utils import Functions as f


def run_all(df):
    # level 1
    df = f.converting_types(df)
    # level 2
    df = f.removing_html(df)
    #level 3
    df = f.no_coupon(df)
    # level 4
    df = f.adding_month_column(df)
    #level 5
    df = f.adding_high_value_order_column(df)
    #level 6
    df = f.adding_avg_rating(df)
    #level 7
    df = f.sorting_columns(df)
    #level 8
    df = f.creatin_delivery_status(df)


if __name__ == "__main__":
    df = f.read_json('orders_simple.json')
    df = run_all(df)
    #level 9
    df.to_csv('clean_orders_[209643808].csv', index = False)
    print('csv file create succefully')