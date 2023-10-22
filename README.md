# Open Seattle Donation Inventory Management Software (IMS)

Django web application project developed for Open Seattle's asynchronous technical challenge. The application is a light IMS used for tracking donation inventory (add, update, delete) with data visualizations for reporting, using SQLite database.

### Open Seattle Prompt

Imagine you're tasked with creating a practical solution for a local shelter to manage their donation inventory. This shelter is in need of a user-friendly tool to accurately record and track the inflow and outflow of donations, and to generate insightful reports about their donation management.

Here are the core functionalities your solution should address:

1. Donation Registration: A feature that allows the shelter staff to record details of the donations, such as the donor's name, type of donation (money, food, clothing, etc.), quantity or amount donated, and the date of the donation.
2. Donation Distribution: A feature to log when and how much of the donations are distributed, capturing the type of donation, quantity or amount distributed, and the date of distribution.
3. Donation Reports: Your solution should have the capacity to generate two types of reports: (1) An inventory report displaying the current status of donations, grouped by type. (2) A donator report, summarizing the total contributions received from each donor.

## Getting Started

### Installation

Use the pip package manager [pip](https://pip.pypa.io/en/stable/) to install all of the Python modules and packages listed in the requirements.txt file:

```bash
pip install -r requirements.txt 
```

### Executing Program

After installation, run the following command to create a local Django development server instance of the IMS:

```bash
python3 manage.py runserver
```

## Authors
Michael Ho (https://github.com/Bearded-Gecko/)

## License
Code released under the [MIT License](https://github.com/Bearded-Gecko/open-seattle-ims/blob/master/LICENSE.txt)

## Acknowledgements
* [README_template](https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc)
* [YouTube_tutorial](https://youtu.be/QUsExxncodk?si=TSnLGimYaUun5IYt)
