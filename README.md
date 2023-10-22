# Open Seattle Donation Inventory Management Software (IMS)

Django web application project developed for Open Seattle's asynchronous technical challenge. The application is a light IMS used for tracking donation inventory (add, update, delete) with data visualizations for reporting, using SQLite database.

## Open Seattle Prompt






YouTube source: https://youtu.be/QUsExxncodk?si=TSnLGimYaUun5IYt

Uses an SQLITE database. Each donation/inventory uses the following attributes:




## Installation

Use the pip package manager [pip](https://pip.pypa.io/en/stable/) to install all of the Python modules and packages listed in the requirements.txt file:

```bash
pip install -r requirements.txt 
```

## Usage

After installation, run the following command to create a local Django development server instance of the IMS:

```bash
python3 manage.py runserver
```
donor_name (string): name of donor



item_type (string):

amount (decimal): when adding to a new location this will be positive, when removing from a location this will be negative

location (string): 

date (date): date recorded when item is received, removed, or moved

When transferring inventory from one location to another, requires two entries, one to remove from the current location and another to add to a new location. 

login is capital sensitive

Example

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)