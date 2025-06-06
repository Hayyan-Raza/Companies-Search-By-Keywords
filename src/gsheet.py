# gsheet file removed due to credentials 
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def setup_google_sheets(sheet_name):        
    """
    Set up Google Sheets connection and return the sheet object.

    Args:
        sheet_name (str): Name of the Google Sheet to connect to.

    Returns:
        gspread.models.Spreadsheet: The Google Sheet object.
    """

    # Define the scope for Google Sheets API
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

    # Load credentials from the JSON file
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

    # Authorize and create a client to interact with Google Sheets
    client = gspread.authorize(creds)

    # Open the specified Google Sheet
    sheet = client.open(sheet_name)

    return sheet

def get_keywords(sheet):
    """
    Retrieve keywords from the first column of the first worksheet in the Google Sheet.

    Args:
        sheet (gspread.models.Spreadsheet): The Google Sheet object.

    Returns:
        list: List of keywords.
    """
    try:
        worksheet = sheet.get_worksheet(0)  # Get the first worksheet
        keywords = worksheet.col_values(1)  # Get all values from the first column
        return [keyword.strip() for keyword in keywords if keyword.strip()]  # Return non-empty keywords
    except Exception as e:
        raise ValueError(f"Error retrieving keywords: {e}")
    
def create_tab(sheet, keyword):
    """
    Create a new tab in the Google Sheet for the specified keyword.

    Args:
        sheet (gspread.models.Spreadsheet): The Google Sheet object.
        keyword (str): The keyword for which to create a new tab.
    """
    try:
        # Create a new worksheet with the keyword as the title
        sheet.add_worksheet(title=keyword, rows="100", cols="20")
        print(f"Created tab for keyword: {keyword}")
    except Exception as e:
        raise ValueError(f"Error creating tab for keyword '{keyword}': {e}")

def write_data_to_tab(sheet, keyword, data):
    """
    Write data to the specified tab in the Google Sheet.

    Args:
        sheet (gspread.models.Spreadsheet): The Google Sheet object.
        keyword (str): The keyword corresponding to the tab.
        data (list): List of lists containing data to write to the tab.
    """
    try:
        worksheet = sheet.worksheet(keyword)  # Get the worksheet for the keyword
        worksheet.clear()  # Clear existing data
        worksheet.append_rows(data)  # Append new data
        print(f"Data written to tab for keyword: {keyword}")
    except Exception as e:
        raise ValueError(f"Error writing data to tab for keyword '{keyword}': {e}")