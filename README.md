# Pandas Publisher

Pandas Publisher allows you to generate HTML and PDF reports using Jinja2 templates and Pandas dataframes. The generated reports can be saved as HTML, PDF, or returned as an HTML string.

## Dependencies

- pandas
- Jinja2
- WeasyPrint

To install the latest release run:

```bash
pip install pandaspublisher
```

To install from source run the following after cloning this repo:

```bash
pip install -e .
```

## Usage

```python
import pandas as pd
from pandaspublisher import generate

# Create some sample DataFrames
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'C': [5, 6], 'D': [7, 8]})

# Use a dictionary to pass the DataFrames and their variable names
dataframes = {'dataframe1': df1, 'dataframe2': df2}

# Use the full path to the template file
template_path = "/Users/jasonflittner/code/PandasPublisher/examples/templates/modern_template.html"
output_file = 'output.html'
output_format = 'html'  # The desired output format for the report, either 'html', 'pdf', or 'html_string'.
context = {
    "title": "Sample Report",
    "content": "This is a sample report generated using Pandas Publisher."
}

generate.report(template_path=template_path, dataframes=dataframes, output_format=output_format, output_filename=output_file, context=context)

```

The output_format parameter accepts the following values:

- "html": Save the report as an HTML file.
- "pdf": Save the report as a PDF file.
- "html_string": Return the rendered HTML content as a string.


## Template Creation
Create your Jinja2 templates using standard HTML and Jinja2 syntax. Use the keys from your dataframes dictionary to reference the respective dataframes in the template. For example:

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        table {
            border-collapse: collapse;
            width: 100%;
        }
        th, td {
            border: 1px solid black;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>
    <h1>{{ title }}</h1>
    <p>{{ content }}</p>

    <h2>DataFrame 1</h2>
    <table>
        <thead>
            <tr>
                {% for column in dataframe1.columns %}
                    <th>{{ column }}</th>
                {% endfor %}
            </tr>
        </thead>
        <tbody>
            {% for _, row in dataframe1.iterrows() %}
                <tr>
                    {% for cell in row %}
                        <td>{{ cell }}</td>
                    {% endfor %}
                </tr>
            {% endfor %}
        </tbody>
    </table>

    <h2>DataFrame 2</h2>
    <table>
        <thead>
            <tr>
                {% for column in dataframe2.columns %}
                    <th>{{ column }}</th>
                {% endfor %}
            </tr>
        </thead>
        <tbody>
            {% for _, row in dataframe2.iterrows() %}
                <tr>
                    {% for cell in row %}
                        <td>{{ cell }}</td>
                    {% endfor %}
                </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>
```
