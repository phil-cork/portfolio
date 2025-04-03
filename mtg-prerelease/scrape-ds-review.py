import marimo

__generated_with = "0.12.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import requests
    import pandas as pd
    import bs4 as bs
    return bs, mo, pd, requests


@app.cell
def _(bs, requests):
    ds_url = "https://draftsim.com/mtg-tdm-limited-set-review"
    request = requests.get(ds_url)
    main_soup = bs.BeautifulSoup(request.text, 'html.parser')
    return ds_url, main_soup, request


@app.cell
def _(main_soup):
    titles = []
    ratings = []
    texts = []
    colors = []

    # Find all the h2 tags (each marking a new section)
    h2_tags = main_soup.find_all('h2', class_='wp-block-heading')
    # List of color names that we want to keep
    color_list = ['White', 'Blue', 'Black', 'Red', 'Green', "Multicolor", "Artifacts/Colorless"]
    # Filter the h2 elements based on match
    color_tags = [h2 for h2 in h2_tags if h2.get_text(strip=True) in color_list]

    for i, h2_tag in enumerate(color_tags):
        # Find the next h2 tag to mark the end of the current section
            next_h2 = h2_tag.find_next('h2', class_='wp-block-heading')

            # Create a list of all the h3s (cards) between each h2 (color category)
            h3s_in_section = []
            # look through every subsequent tag - at the next h2, break the loop
            # if it is an h3, store it,
            for tag in h2_tag.find_all_next(True):
                if tag == next_h2:
                    break
                if tag.name == 'h3':
                    h3s_in_section.append(tag)

            # with the list of color-specific cards, extract data
            for h3_tag in h3s_in_section:

                # h3 title is card name
                titles.append(h3_tag.get_text())

                # the first p tag that's bolded after h3 is the rating
                rating_tag = h3_tag.find_next('p').find('strong')
                rating = rating_tag.get_text(strip=True) if rating_tag else None
                ratings.append(rating)

                # the next p tag after rating is text/description
                p_tag = rating_tag.find_next('p')
                text = p_tag.get_text(strip=True) if p_tag else None
                texts.append(text)

                # for each card, store the color category
                colors.append(h2_tag.get_text())
    return (
        color_list,
        color_tags,
        colors,
        h2_tag,
        h2_tags,
        h3_tag,
        h3s_in_section,
        i,
        next_h2,
        p_tag,
        rating,
        rating_tag,
        ratings,
        tag,
        text,
        texts,
        titles,
    )


@app.cell
def _(colors, pd, ratings, texts, titles):
    data = {
        'name': titles,
        'ds_rating': ratings,
        'ds_commentary': texts,
        'ds_category': colors
    }

    df = pd.DataFrame(data)
    df['ds_rating'] = df['ds_rating'].str.removeprefix("Rating: ")
    df['ds_rating'] = df['ds_rating'].str.removesuffix("/10")
    # handle the one-off 'range' rating
    df['ds_rating'] = df['ds_rating'].str.removesuffix("-4")
    df['ds_rating'] = df['ds_rating'].astype('int')

    df
    return data, df


@app.cell
def _(df):
    df.to_csv("data/tdm-draftsim-set-review.csv", index=False)
    return


if __name__ == "__main__":
    app.run()
