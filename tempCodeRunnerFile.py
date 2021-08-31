for index, row in df.iterrows():
    short = taa.EMA(df["Volume"], 5)
    long = taa.EMA(df["Volume"], 20)
    df['osc']= 100*(short-long)/long
color = []
for index, row in df.iterrows():
    if(df['Close'][index]<df['Open'][index]):
        color.append('r')
    if(df['Close'][index]>=df['Open'][index]):
        color.append('g')
    
df['color'] = color