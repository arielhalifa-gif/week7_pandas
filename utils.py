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
        print(df.dtypes)

    @staticmethod
    def removing_html(df):
        df['items_html'] = df['items_html'].str.replace('<br>', ' ')
        df['items_html'] = df['items_html'].str.replace('<b>', '')
        df['items_html'] = df['items_html'].str.replace('</b>', '')
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
        avg_total = df['total_amount'].mean()
        mask = df['total_amount'] > avg_total
        df['high_value_order'] = mask
        return df.sort_values('total_amount', ascending = False)
    


    @staticmethod
    def adding_avg_rating(df):
        sorted_rating_by_country = df.groupby('country')['rating'].mean()
        df['avg_ratings'] = None
        for country in df['country']:
            for key, value in sorted_rating_by_country:
                if country == key:
                    df['avg_ratings'].loc[df['country'] == key] = value
        return df
    
    @staticmethod
    def sorting_columns(df):
        mask = df['total_amount'] < 1000 & df['avg_ratings'] < 4.5
        df = df.drop(mask)
        return df
    

    @staticmethod
    def creatin_delivery_status(df):
        df = df.assign(delivery_status = lambda x: 'delayed' if x['shipping_days'] > 7 else 'on time')
        return df