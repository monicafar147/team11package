#import relevant modules
import numpy as np
import pandas as pd

def dictionary_of_metrics(items):
    """Return a dictionary of statistical measures: mean, median, variance, standard deviation, minimum and maximum of a list of items.
    All values in the returned dict will be rounded to 2 decimal places.

    Args:
        items (array): list containing numerical values.

    Returns:
        returns: dict type with keys 'mean', 'median', 'std', 'var', 'min', and 'max'

    Examples:
        dictionary_of_metrics(list) == {'mean': 26244.42,
                                   'median': 24403.50,
                                   'variance': 108160153.17,
                                   'standard deviation': 10400.01,
                                   'min': 8842.00,
                                   'max': 39660.00}
    """
    # Create and return dictionary: Mikael
    dict = {}

    # Use numpy to find the metrics: Courtney
    dict['mean'] = round(np.mean(items), 2)
    dict['median'] = round(np.median(items),2)
    dict['variance'] = round(np.var(items), 2)
    dict['standard variance'] = round(np.std(items),2)
    dict['min'] = round(np.min(items),2)
    dict['max'] = round(np.max(items),2)

    return dict

def five_num_summary(items):
    """Return a dictionary of the five number summary: maximum, median, minimum, first quartile and third quartile.
    All values in the returned dict will be rounded to 2 decimal places.

    Args:
        items (array): list containing numerical values.

    Returns:
        returns:dict type with keys 'max', 'median', 'min', 'q1', and 'q3'

    Examples:
        five_num_summary(list) == {
    'max': 39660.00,
    'median': 24403.50,
    'min': 8842.00,
    'q1': 18576.00,
    'q3': 36720.00}

    """
    # Calculate five number summary: Courtney
    maximum = np.max(items)
    median = np.median(items)
    minimum = np.min(items)
    q1 = np.percentile(items, 25)
    q3 = np.percentile(items, 75)

    # Create and return dictionary: Mikael
    dict = {}

    dict['max'] = maximum
    dict['median'] = median
    dict['min'] = minimum
    dict['q1'] = q1
    dict['q3'] = q3

    return dict

def date_parser(dates):
    """Takes as input a list of datetime strings and returns only the date in 'yyyy-mm-dd' format.


    Args:
        items (array): list containing dates represented as strings. Each string in the input list is formatted as 'yyyy-mm-dd hh:mm:ss'

    Returns:
        returns: list of strings where each element in the returned list contains only the date in the 'yyyy-mm-dd' format.

    Examples:
    date_parser(list) == ['2019-11-29', '2019-11-29', '2019-11-29']

    """
    # extract the date only from dates: Olwethu
    # append each date to a new list: Olwethu
    # return new list with dates only: Mikael

    date_list = []
    for i in dates:
        i = i.split(' ')
        date_list.append(i[0])
        
    return date_list

def extract_municipality_hashtags(df):
    """Takes in a pandas dataframe and returns a modified dataframe that includes two new columns that contain information about the municipality and hashtag of the tweet.

    Args:
        df (pandas dataframe)

    Returns:
        returns: pandas dataframe

    Expected output should be same dataframe but with new column headings municipality and hashtags
    """

    # dictionary mapping official municipality twitter handles to the municipality name
    mun_dict = {
    '@CityofCTAlerts' : 'Cape Town',
    '@CityPowerJhb' : 'Johannesburg',
    '@eThekwiniM' : 'eThekwini' ,
    '@EMMInfo' : 'Ekurhuleni',
    '@centlecutility' : 'Mangaung',
    '@NMBmunicipality' : 'Nelson Mandela Bay',
    '@CityTshwane' : 'Tshwane'
    }


    # Create 'municipality' column: Monica
    df['municipality'] = df['Tweets']

    # Extract municipality from Tweets: Mikael
    l = 0

    for tweet in df['Tweets']:
        tweet = tweet.split(' ')
        for key in mun_dict.keys():
            if key in tweet:
                df.loc[l, 'municipality'] = mun_dict[key]
            #else: Fill empty values in 'hashtags' and 'municipality' columns with np.nan: Courtney

        l += 1

    # Create 'hashtags' column: Mikael
    df['hashtags'] = df['Tweets'].str.lower().str.split()

    # Extract hashtags from Tweets: Monica
    i = 0

    for tweet in df['hashtags']:
      hashtags = []
      for word in tweet:
        if word.startswith('#'):
          hashtags.append(word)
      df.loc[i, 'hashtags'] = hashtags
      # Fill empty values in 'hashtags' and 'municipality' columns with np.nan: Courtney
      i += 1

    return df

def number_of_tweets_per_day(df):
    """Takes in a pandas dataframe and returns the number of tweets that were posted per day.
    The index of the new dataframe will be named Date, and the column of the new dataframe will be 'Tweets', corresponding to the date and number of tweets, respectively.
    The date should be formated as yyyy-mm-dd, and will be a datetime object

    Args:
        df (pandas dataframe)

    Returns:
        returns: pandas dataframe grouped by day, with the number of tweets for that day

    Expected output should be same dataframe but with new column headings Date and Tweets
    """
    # Create new dataframe: Monica
    new_df = pd.DataFrame() 

    # Create and complete 'Date' and 'Tweets' column in new dataframe: Mikael
    df['Date'] = df['Date'].str.split(' ')

    dates = []
    index = 0
    for date in df['Date']:
        if date[0] not in dates:
            dates.append(date[0])
        df.loc[index, 'Date'] = date[0]
        index += 1

    new_df['Date'] = sorted(dates)
    new_df['Date'] = pd.to_datetime(new_df['Date'], format='%Y-%m-%d')
    new_df = new_df.set_index('Date')
    new_df['Tweets'] = df['Date'].value_counts().sort_index()

    return new_df

def word_splitter(df):
    """Splits the sentences in a dataframe's column into a list of the separate words.
    The created lists will be placed in a column named 'Split Tweets' in the original dataframe.

    Args:
        df (pandas dataframe) should contain a column, named 'Tweets'.

    Returns:
        returns: pandas dataframe where the sentences are split in the 'Tweets' into a list of seperate words, and placed into a new column named 'Split Tweets'.
        The resulting words are all be lowercase.

    Expected output should be same dataframe but with new column headings Date and Split Tweets
    """
    # Create 'Split Tweets' column, with each tweet split into a list: Olwethu

    pass

def stop_words_remover(df):
    """Removes english stop words from a tweet.
    Tokenise the sentences according to the definition in word_splitter.
    Note that word_spliiter cannot be called within this function.
    The stopwords are defined in the stopwords_dict variable defined as:
    stop_words_dict = {
    'stopwords':[
        'where', 'done', 'if', 'before', 'll', 'very', 'keep', 'something', 'nothing', 'thereupon',
        'may', 'why', 'â€™s', 'therefore', 'you', 'with', 'towards', 'make', 'really', 'few', 'former',
        'during', 'mine', 'do', 'would', 'of', 'off', 'six', 'yourself', 'becoming', 'through',
        'seeming', 'hence', 'us', 'anywhere', 'regarding', 'whole', 'down', 'seem', 'whereas', 'to',
        'their', 'various', 'thereafter', 'â€˜d', 'above', 'put', 'sometime', 'moreover', 'whoever', 'although',
        'at', 'four', 'each', 'among', 'whatever', 'any', 'anyhow', 'herein', 'become', 'last', 'between', 'still',
        'was', 'almost', 'twelve', 'used', 'who', 'go', 'not', 'enough', 'well', 'â€™ve', 'might', 'see', 'whose',
        'everywhere', 'yourselves', 'across', 'myself', 'further', 'did', 'then', 'is', 'except', 'up', 'take',
        'became', 'however', 'many', 'thence', 'onto', 'â€˜m', 'my', 'own', 'must', 'wherein', 'elsewhere', 'behind',
        'becomes', 'alone', 'due', 'being', 'neither', 'a', 'over', 'beside', 'fifteen', 'meanwhile', 'upon', 'next',
        'forty', 'what', 'less', 'and', 'please', 'toward', 'about', 'below', 'hereafter', 'whether', 'yet', 'nor',
        'against', 'whereupon', 'top', 'first', 'three', 'show', 'per', 'five', 'two', 'ourselves', 'whenever',
        'get', 'thereby', 'noone', 'had', 'now', 'everyone', 'everything', 'nowhere', 'ca', 'though', 'least',
        'so', 'both', 'otherwise', 'whereby', 'unless', 'somewhere', 'give', 'formerly', 'â€™d', 'under',
        'while', 'empty', 'doing', 'besides', 'thus', 'this', 'anyone', 'its', 'after', 'bottom', 'call',
        'nâ€™t', 'name', 'even', 'eleven', 'by', 'from', 'when', 'or', 'anyway', 'how', 'the', 'all',
        'much', 'another', 'since', 'hundred', 'serious', 'â€˜ve', 'ever', 'out', 'full', 'themselves',
        'been', 'in', "'d", 'wherever', 'part', 'someone', 'therein', 'can', 'seemed', 'hereby', 'others',
        "'s", "'re", 'most', 'one', "n't", 'into', 'some', 'will', 'these', 'twenty', 'here', 'as', 'nobody',
        'also', 'along', 'than', 'anything', 'he', 'there', 'does', 'we', 'â€™ll', 'latterly', 'are', 'ten',
        'hers', 'should', 'they', 'â€˜s', 'either', 'am', 'be', 'perhaps', 'â€™re', 'only', 'namely', 'sixty',
        'made', "'m", 'always', 'those', 'have', 'again', 'her', 'once', 'ours', 'herself', 'else', 'has', 'nine',
        'more', 'sometimes', 'your', 'yours', 'that', 'around', 'his', 'indeed', 'mostly', 'cannot', 'â€˜ll', 'too',
        'seems', 'â€™m', 'himself', 'latter', 'whither', 'amount', 'other', 'nevertheless', 'whom', 'for', 'somehow',
        'beforehand', 'just', 'an', 'beyond', 'amongst', 'none', "'ve", 'say', 'via', 'but', 'often', 're', 'our',
        'because', 'rather', 'using', 'without', 'throughout', 'on', 'she', 'never', 'eight', 'no', 'hereupon',
        'them', 'whereafter', 'quite', 'which', 'move', 'thru', 'until', 'afterwards', 'fifty', 'i', 'itself', 'nâ€˜t',
        'him', 'could', 'front', 'within', 'â€˜re', 'back', 'such', 'already', 'several', 'side', 'whence', 'me',
        'same', 'were', 'it', 'every', 'third', 'together']

    Args:
        df (pandas dataframe) should contain a column.

    Returns:
        returns: pandas dataframe with a column named "Without Stop Words".

    Expected output should be same dataframe but with new column heading Without Stop Words
    """
    #create stop words dictionary
    # dictionary of english stopwords
    stop_words_dict = {
    'stopwords':[
        'where', 'done', 'if', 'before', 'll', 'very', 'keep', 'something', 'nothing', 'thereupon', 
        'may', 'why', 'â€™s', 'therefore', 'you', 'with', 'towards', 'make', 'really', 'few', 'former', 
        'during', 'mine', 'do', 'would', 'of', 'off', 'six', 'yourself', 'becoming', 'through', 
        'seeming', 'hence', 'us', 'anywhere', 'regarding', 'whole', 'down', 'seem', 'whereas', 'to', 
        'their', 'various', 'thereafter', 'â€˜d', 'above', 'put', 'sometime', 'moreover', 'whoever', 'although', 
        'at', 'four', 'each', 'among', 'whatever', 'any', 'anyhow', 'herein', 'become', 'last', 'between', 'still', 
        'was', 'almost', 'twelve', 'used', 'who', 'go', 'not', 'enough', 'well', 'â€™ve', 'might', 'see', 'whose', 
        'everywhere', 'yourselves', 'across', 'myself', 'further', 'did', 'then', 'is', 'except', 'up', 'take', 
        'became', 'however', 'many', 'thence', 'onto', 'â€˜m', 'my', 'own', 'must', 'wherein', 'elsewhere', 'behind', 
        'becomes', 'alone', 'due', 'being', 'neither', 'a', 'over', 'beside', 'fifteen', 'meanwhile', 'upon', 'next', 
        'forty', 'what', 'less', 'and', 'please', 'toward', 'about', 'below', 'hereafter', 'whether', 'yet', 'nor', 
        'against', 'whereupon', 'top', 'first', 'three', 'show', 'per', 'five', 'two', 'ourselves', 'whenever', 
        'get', 'thereby', 'noone', 'had', 'now', 'everyone', 'everything', 'nowhere', 'ca', 'though', 'least', 
        'so', 'both', 'otherwise', 'whereby', 'unless', 'somewhere', 'give', 'formerly', 'â€™d', 'under', 
        'while', 'empty', 'doing', 'besides', 'thus', 'this', 'anyone', 'its', 'after', 'bottom', 'call', 
        'nâ€™t', 'name', 'even', 'eleven', 'by', 'from', 'when', 'or', 'anyway', 'how', 'the', 'all', 
        'much', 'another', 'since', 'hundred', 'serious', 'â€˜ve', 'ever', 'out', 'full', 'themselves', 
        'been', 'in', "'d", 'wherever', 'part', 'someone', 'therein', 'can', 'seemed', 'hereby', 'others', 
        "'s", "'re", 'most', 'one', "n't", 'into', 'some', 'will', 'these', 'twenty', 'here', 'as', 'nobody', 
        'also', 'along', 'than', 'anything', 'he', 'there', 'does', 'we', 'â€™ll', 'latterly', 'are', 'ten', 
        'hers', 'should', 'they', 'â€˜s', 'either', 'am', 'be', 'perhaps', 'â€™re', 'only', 'namely', 'sixty', 
        'made', "'m", 'always', 'those', 'have', 'again', 'her', 'once', 'ours', 'herself', 'else', 'has', 'nine', 
        'more', 'sometimes', 'your', 'yours', 'that', 'around', 'his', 'indeed', 'mostly', 'cannot', 'â€˜ll', 'too', 
        'seems', 'â€™m', 'himself', 'latter', 'whither', 'amount', 'other', 'nevertheless', 'whom', 'for', 'somehow', 
        'beforehand', 'just', 'an', 'beyond', 'amongst', 'none', "'ve", 'say', 'via', 'but', 'often', 're', 'our', 
        'because', 'rather', 'using', 'without', 'throughout', 'on', 'she', 'never', 'eight', 'no', 'hereupon', 
        'them', 'whereafter', 'quite', 'which', 'move', 'thru', 'until', 'afterwards', 'fifty', 'i', 'itself', 'nâ€˜t',
        'him', 'could', 'front', 'within', 'â€˜re', 'back', 'such', 'already', 'several', 'side', 'whence', 'me', 
        'same', 'were', 'it', 'every', 'third', 'together'
    ]
    }

    # Create 'Without Stop Words' column: Mikael
    df['Without Stop Words'] = df['Tweets'].str.lower().str.split()

    # Extract stop words from 'Without Stop Words' column: Monica
    for row in df['Without Stop Words']:
        for word in row:
        #find stop word in stop word dictionary
            for stop_word in stop_words_dict['stopwords']:
                if word == stop_word:
                    #remove stop word from current row
                    row.remove(word)
    return df
