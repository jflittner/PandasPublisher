import os
import pandas as pd
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

def render_template(template_path, context):
    env = Environment(loader=FileSystemLoader(os.path.dirname(template_path)))
    template = env.get_template(os.path.basename(template_path))
    return template.render(context)

def save_html(html_content, output_filename):
    with open(output_filename, "w") as f:
        f.write(html_content)

def convert_html_to_pdf(html_content, output_filename):
    HTML(string=html_content).write_pdf(output_filename)

def report(template_path, dataframes, output_format, output_filename, context=None):
    """
    Generates a report using the specified Jinja2 template and Pandas dataframes.
    
    Args:
        template_path (str): The full path of the HTML + Jinja2 template file.
        dataframes (dict): A dictionary containing Pandas dataframes as values.
        output_format (str): The desired output format for the report, either 'html', 'pdf', or 'html_string'.
        output_filename (str): The output file name for the generated report (only used when saving to 'html' or 'pdf').
        context (dict, optional): An optional dictionary for any additional context to be passed to the template.

    Returns:
        str: The rendered HTML content if output_format is set to 'html_string', otherwise None.

    Raises:
        ValueError: If an invalid output format is specified.
    """
    
    for key, df in dataframes.items():
        context[key] = df

    html_content = render_template(template_path, context)

    if output_format == "html":
        save_html(html_content, output_filename)
    elif output_format == "html_string":
        return html_content
    elif output_format == "pdf":
        convert_html_to_pdf(html_content, output_filename)
    else:
        raise ValueError("Invalid output format specified. Please specify 'html', 'pdf', or 'html_string'.")

    print(f"File saved as {output_filename}")
    
