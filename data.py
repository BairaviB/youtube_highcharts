import pandas as pd 

def get_data():
    
    df = pd.read_csv('youtubedata.csv')

    
    channel_var = df['channelname'].tolist()
    subscriber_var= df['subscribers'].tolist()

    
      
    list_of_tuples = [tuple(row) for row in df.values]
  
    print(list_of_tuples)

    # print(df['quebec'].tolist())

    result_dict = {
        'channel': channel_var,
        'subcriber': subscriber_var,
        'data_list': list_of_tuples,
    }

    # print(result_dict)

    return result_dict

def add_row(channel,subscriber):

    df = pd.read_csv('youtubedata.csv') 

    new_row = {
    
        'channelname'       : channel, 
        'subscribers'    : subscriber, 
        
    }

    print(df)

    df = df.append(new_row, ignore_index=True)

    print(df)

    df.to_csv('youtubedata.csv')

if __name__ == "__main__":
    get_data()