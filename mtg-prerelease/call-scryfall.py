import marimo

__generated_with = "0.12.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import requests
    import pandas as pd
    return mo, pd, requests


@app.cell
def _(requests):
    def fetch_all_cards(params):
        # Define the base URL for the Scryfall API
        url = "https://api.scryfall.com/cards/search"

        # Start with the initial request with the provided parameters
        all_cards = []

        while url:
            response = requests.get(url, params=params)

            # Check if the request was successful
            if response.status_code == 200:
                data = response.json()

                # Add cards from the current page to the all_cards list
                all_cards.extend(data['data'])

                # Update the URL for the next page (if exists)
                url = data.get('next_page', None)

                # Status Check
                print(f"Fetched {len(data['data'])} cards, total: {len(all_cards)}")
            else:
                print("Error fetching data:", response.status_code)
                break

        return all_cards
    return (fetch_all_cards,)


@app.cell
def _(fetch_all_cards):
    params = {
        'q': 'set:tarkir_dragonstorm',
        'unique': 'prints',
        'order': 'name'
    }

    set_cards = fetch_all_cards(params)
    return params, set_cards


@app.cell
def _(set_cards):
    names = []
    cmcs = []
    card_colors = []
    mana_costs = []
    keywords = []
    type_lines = []
    rarities = []
    oracle_texts = []

    for card in set_cards:
        # keep only the standard printings 
        #TODO: move this to function parameter
        if int(card['collector_number']) < 287:
            if card['layout'] in ['normal', 'saga']:
                names.append(card['name'])
                cmcs.append(card['cmc'])
                card_colors.append(card['colors'])
                mana_costs.append(card['mana_cost'])
                keywords.append(card['keywords'])
                type_lines.append(card['type_line'])
                rarities.append(card['rarity'])
                oracle_texts.append(card['oracle_text'])

            elif card['layout'] == 'adventure':
                names.append(card['name'])
                cmcs.append(card['cmc'])
                card_colors.append(card['colors'])
                mana_costs.append(card['mana_cost'])
                keywords.append(card['keywords'])
                type_lines.append(card['type_line'])
                rarities.append(card['rarity'])
                oracle_texts.append(f"{card['card_faces'][0]['oracle_text']} // {card['card_faces'][1]['oracle_text']}")

            else:
                # control for card layouts not handled for future examples
                print(f"Name: {card['name']}")
                print(f"Layout: {card['layout']}")
                print("--------")
    return (
        card,
        card_colors,
        cmcs,
        keywords,
        mana_costs,
        names,
        oracle_texts,
        rarities,
        type_lines,
    )


@app.cell
def _(
    card_colors,
    cmcs,
    keywords,
    mana_costs,
    names,
    oracle_texts,
    pd,
    rarities,
    type_lines,
):
    data = {'name': names,
            'cmc': cmcs,
            'card_colors': card_colors,
            'mana_cost': mana_costs,
            'keywords': keywords,
            'type_line': type_lines,
            'rarity': rarities,
            'oracle_text' : oracle_texts
           }
    df = pd.DataFrame(data)
    return data, df


@app.cell
def _(df):
    df['card_colors'] = [', '.join(map(str, l)) for l in df['card_colors']]
    df['keywords'] = [', '.join(map(str, l)) for l in df['keywords']]
    df
    return


@app.cell
def _(df):
    df.to_csv("data/tdm-scryfall-data.csv", index=False)
    return


if __name__ == "__main__":
    app.run()
