# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv



def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

def save_csv(csvpath, qualifying_loans):
    """Saves the data to a csv file at the path provided
(
    Args:
        csvpath (Path): the csv file path
        qualifying_loans: the list of data to be stored in csv file

    Returns:
        A csv file containing a filtered list of banks that the user is approved for based on the questionary prompt answers.
    """
    
    with open(csvpath, "w") as csvfile:
        
        csvwriter = csv.writer(csvfile, delimiter=",")
        
        header = ["Lender", "Max Loan Amount", "Max LTV", "Max DTI", "Min Credit Score", "Interest Rate"]
        csvwriter.writerow(header)
        for item in qualifying_loans:
            csvwriter.writerow(item)

    print("Your file has been saved at the specified file location.  Thank you for using the Loan Qualifier Application.  Enjoy the rest of your day!")
