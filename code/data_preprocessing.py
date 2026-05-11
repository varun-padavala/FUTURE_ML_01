import pandas as pd

def load_and_prepare_data(path):
    print("Loading file...")

    df = pd.read_csv(path, encoding='latin1')
    print("Data shape:", df.shape)

    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df = df.sort_values('Order Date')


    df_monthly = df.resample('ME', on='Order Date')['Sales'].sum().reset_index()


    df_monthly = df_monthly.rename(columns={
        'Order Date': 'ds',
        'Sales': 'y'
    })

    return df_monthly