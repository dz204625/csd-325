def city_country(city, country, population = "", language = ""):
    formatted_city_country = f"{city}, {country}".title()
    if population and not language:
        print(f"{formatted_city_country} - population {population}")
        return f"{formatted_city_country} - population {population}"
    elif population and language:
        print(f"{formatted_city_country} - population {population}, {language}")
        return f"{formatted_city_country} - population {population}, {language}"
    else:
        print(formatted_city_country)
        return formatted_city_country


city_country("shenyang", "china")
city_country("Sydney", "Australia", 5231147)
city_country("chicago", "United states", 2746388, "English")
