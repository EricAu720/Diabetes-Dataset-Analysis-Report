import pickle

# Load the plots_with_base64 list
with open('/Users/ericccccc/python_vscode/Self_Analysis/plots_with_base64.pkl', 'rb') as f:
    plots_with_base64 = pickle.load(f)

# Load the HTML template
with open('/Users/ericccccc/python_vscode/Self_Analysis/diabetes_report.html', 'r') as f:
    html_template = f.read()

# Replace placeholders with plot data
html_content = html_template
for i, (content, desc, plot_type) in enumerate(plots_with_base64):
    html_content = html_content.replace(f'{{{{plots[{i}][0]}}}}', content)
    html_content = html_content.replace(f'{{{{plots[{i}][1]}}}}', desc)

# Save the final HTML report
with open('diabetes_analysis_report.html', 'w') as f:
    f.write(html_content)

print("HTML report generated: diabetes_analysis_report.html")