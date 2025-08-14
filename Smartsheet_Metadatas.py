'''This Code List out the Sheet Name(Client Name) with the Sheet ID'''
import smartsheet

# Replace with your API token
TOKEN = 'VJMHRFRfjH3IaO3dUJKPp5sf0I8WqkzamUw**'

# Create Smartsheet client
smartsheet_client = smartsheet.Smartsheet(TOKEN)

# List your sheets
response = smartsheet_client.Sheets.list_sheets()
for sheet in response.data:
    print(f"{sheet.name} — {sheet.id}")

# THE END
