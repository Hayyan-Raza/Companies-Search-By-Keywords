# Apollo Companies Search By Keyword

This project automates the process of searching for company executives (e.g., CEO, Founder, Owner) using the Apollo API based on a list of keywords, and writes the results to separate tabs in a Google Sheet.

## Features

- Fetches people data from the Apollo API for each keyword.
- Reads keywords from the first column of a Google Sheet.
- Creates a new tab for each keyword and writes the results.
- Supports dummy data for testing without API calls.

## Project Structure

```
main.py
Readme.md
src/
    apollo.py
    gsheet.py
```

- **main.py**: Entry point for the automation.
- **src/gsheet.py**: Handles Google Sheets authentication and operations.
- **src/apollo.py**: Handles Apollo API requests and dummy data.

## Setup

1. **Clone the repository**

2. **Install dependencies**
   ```sh
   pip install gspread oauth2client
   ```

3. **Google Sheets API Credentials**
   - Place your `credentials.json` file in the project root (required for Google Sheets access).

4. **Apollo API Key**
   - Set your Apollo API key in `src/apollo.py` (replace the empty string in `api_key = ""`).

5. **Configure Google Sheet**
   - Create a Google Sheet named `ApolloAPIAutomation`.
   - Add your keywords in the first column of the first worksheet.

## Usage

Run the main script:

```sh
python main.py
```

- Enter `Y` to start the automation.
- The script will process each keyword, fetch data, and write results to the Google Sheet.

## Notes

- The Apollo API endpoint and API key must be set for live data fetching.
- Use the dummy data function for testing without API access.

## License

MIT License