# Google Sheets Tools

This project provides a set of tools for Google Sheets, including fetching cryptocurrency spot prices from the CoinGecko API, pinning the price data to IPFS using the Pinata service, and importing the price data into a Google Sheet.

## Features

- Fetches cryptocurrency spot prices from the CoinGecko API
- Pins the price data to IPFS using the Pinata service
- Google Sheets script to import price data into a Google Sheet

## Installation

Follow these steps to set up the project on your local machine:

1. Clone the repository from GitHub:

   ```
   git clone <https://github.com/rossgalloway/google-sheets-tools.git>
   cd google-sheets-tools
   ```

2. Create and activate a Python virtual environment:

   ```
   python -m venv venv
   source venv/bin/activate  # On macOS and Linux
   .\venv\Scripts\activate    # On Windows
   ```

3. Install the required Python packages:

   ```
   pip install -r requirements.txt
   ```

4. Copy the `.env-example` file and rename it to `.env`. Replace the placeholder with your actual Pinata JWT token:

   ```
   PINATA_JWT=<Your_Pinata_JWT_Token>
   ```

   To obtain a Pinata JWT token, sign up for a free account at [Pinata](https://pinata.cloud/), go to the API Keys section, and generate a new API key. The JWT token will be displayed after the key is generated.

5. Make sure the `getPrices.sh` script is executable:

   ```
   chmod +x getPrices.sh
   ```

## Usage

1. Run the `getPrices.sh` script from the `google-sheets-tools` directory using the relative path to fetch the cryptocurrency prices and pin them to IPFS:

   ```
   ./getPrices.sh
   ```

   The script will output an IPFS hash for the pinned data and copy it to your clipboard.

2. Open your Google Sheet and go to `Tools > Script Editor`. Copy and paste the contents of the `google_sheets_script.js` file into the editor, then save and close the Script Editor.

3. In your Google Sheet, go to `Extensions > Apps Script`, and then click on the `importPrices` function.

4. When prompted, paste the IPFS hash that you copied earlier.

The script will import the cryptocurrency prices into your Google Sheet.

## Contributing

To contribute to this project, please submit issues and pull requests on the GitHub repository.

## License

This project is released under the MIT License.
