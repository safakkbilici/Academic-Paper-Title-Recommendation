import json
import pandas as pd

def getMetadata(path_to_json):
    with open(path_to_json, 'r') as f:
        for line in f:
            yield line

def json2list(path_to_json):
    metadata = getMetadata(path_to_json)
    generator_iter = next(metadata)
    keys = (json.loads(generator_iter))

    abstracts = []
    titles = []
    years = []
    categories = []
    authors = []
    authors_parsed = []

    for paper in metadata:
        paper_dict = json.loads(paper)
        try:
            a_year = int(paper_dict.get('journal-ref')[-4:])
            if(a_year > 1950 and a_year < 2020):
                years.append(a_year)
                titles.append(paper_dict.get('title'))
                abstracts.append(paper_dict.get('abstract'))
                categories.append(paper_dict.get('categories'))
                authors.append(paper_dict.get('authors'))
                authors_parsed.append(paper_dict.get('authors_parsed'))
            else:
                pass
        except:
            pass

    data = {'years': years, 'titles': titles, 'abstracts': abstracts,
            'categories': categories, 'authors': authors, 'authors_parsed': authors_parsed}
    print('Abstracts and titles are parsed...')
    return data

def json2csv(path_to_json):
    data = json2list(path_to_json)
    df_all = pd.DataFrame({
        'Title'            : data['titles'],
        'Abstract'         : data['abstracts'],
        'Parsed Authors'   : data['authors_parsed'],
        'Authors'          : data['authors'],
        'Year'             : data['years'],
        'Category'         : data['categories']
    })

    df.to_csv('../data/raw.csv',index=False)

    return df
