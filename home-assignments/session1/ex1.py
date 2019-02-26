import json
import yaml


# Open and load JSON file
with open('my_list.json', 'r') as f:
    data = json.load(f)

    # Put the data from the JSON file into dictionary and a list
    ppl_ages = data['ppl_ages']
    ages_list = sorted(data['buckets'])

    # Find the maximum value in the dictionary in order to use it in the last age group
    oldest_age = max(ppl_ages.values())
    youngest_age = min(ppl_ages.values())

    # Build the list of the age groups
    age_groups = []
    for i, age in enumerate(ages_list[:-1]):
        next_age = ages_list[i+1]
        age_groups.append((age, next_age))

    # Add the last age group to age groups list
    age_groups.append((ages_list[-1], oldest_age))

    # Fill the buckets with names
    output = {}
    for i in range(len(age_groups)):
        place = "{0}-{1}".format(age_groups[i][0], age_groups[i][1])
        names = []
        for name, age in ppl_ages.items():
            if age_groups[i][0] <= age < age_groups[i][1]:
                names.append(":" + name)
        output[place] = names

    # One more extra bucket for the ones who don't have a relevant bucket
    names = []
    for name, age in ppl_ages.items():
        if age < ages_list[0]:
            max_age_in_first_bucket = age
    place = "{0}-{1}".format(youngest_age, max_age_in_first_bucket)
    for name, age in ppl_ages.items():
        if youngest_age <= age <= max_age_in_first_bucket:
            names.append(":" + name)
    output[place] = names


with open('output.yml', 'w') as d:
    yaml.dump(output, d, default_flow_style=False, allow_unicode=True)
