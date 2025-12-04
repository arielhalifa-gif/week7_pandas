import pandas as pd

class Functions:
    @staticmethod
    def read_json(json_file):
        df = pd.read_json(json_file)
        return df
    

    @staticmethod
    def removing_dollar_sign(values):
        values = values.str.replace('$', '')
        return values
    

    @staticmethod
    def converting_types(df):
        # removing $
        df['total_amount'] = Functions.removing_dollar_sign(df['total_amount'])
        df['total_amount'] = df['total_amount'].astype(float)
        df['shipping_days'] = pd.to_numeric(df['shipping_days']) #already int but for practice i convert again beased on the teacher
        df['customer_age'] = pd.to_numeric(df['customer_age']) #already int but for practice i convert again based on the teacher
        df['order_date'] = pd.to_datetime(df['order_date'])


    @staticmethod
    def removing_html(df):
        df['items_html'] = df['items_html'].str.replace(r'<[^<>]*>', '', regex = True)
        return df
    
    @staticmethod
    def no_coupon(df):
        df['coupon_used'] = df['coupon_used'].str.replace('""', 'no coupon')
        return df
    

    @staticmethod
    def adding_month_column(df):
        df['order_month'] = df['order_date'].dt.month()
        return df
    
    @staticmethod
    def adding_high_value_order_column(df):
        df = df.assign(high_value_order = lambda x: x['total_amount'] > x['total_amount'].mean() True else: False)
        return df