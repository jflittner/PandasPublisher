import pandas as pd
from pandaspublisher import generate

# Create some sample DataFrames
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'C': [5, 6], 'D': [7, 8]})

# Use a dictionary to pass the DataFrames and their variable names
dataframes = {'dataframe1': df1, 'dataframe2': df2}

# Use the full path to the template file
template_path = "/Users/jasonflittner/code/PandasPublisher/examples/templates/sample_template.html"
output_file = 'output.html'
output_format = 'html'  # The desired output format for the report, either 'html', 'pdf', or 'html_string'.
context = {
    "title": "Sample Report",
    "content": "This is a sample report generated using Pandas Publisher."
}

generate.report(template_path=template_path, dataframes=dataframes, output_format=output_format, output_filename=output_file, context=context)