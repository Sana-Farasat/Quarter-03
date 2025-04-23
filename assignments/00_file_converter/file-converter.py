import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="File Converter", layout="wide")
st.title("File Converter and Cleaner")
st.write("Upload CSV and Excel files, clean data and convert formats.")

# Upload files
files = st.file_uploader("Upload CSV or Excel files.", type=['csv', 'xlsx'], accept_multiple_files=True)

if files:
    for file in files:
        ext = file.name.split(".")[-1]
        
        try:
            # Read the file based on its extension
            if ext == 'csv':
                df = pd.read_csv(file)
            else:
                df = pd.read_excel(file)

            # Check if the file is successfully read and df is not None
            if df is None or df.empty:
                st.error(f"Failed to read data from {file.name}. Please check the file format.")
                continue

            # Display file preview
            st.subheader(f"{file.name} - Preview")
            st.dataframe(df.head())

            # Remove duplicates
            if st.checkbox(f"Remove Duplicates - {file.name}"):
                df = df.drop_duplicates()
                st.success("Duplicates Removed")
                st.dataframe(df.head())

            # Fill missing values with the mean of numeric columns
            if st.checkbox(f"Fill Missing Values - {file.name}"):
                df = df.fillna(df.select_dtypes(include=["number"]).mean())
                st.success("Missing values filled with mean")
                st.dataframe(df.head())

            # Select columns to display
            select_columns = st.multiselect(f"Select Columns {file.name}", df.columns, default=df.columns)
            df = df[select_columns]
            st.dataframe(df.head())

            # Show chart
            if st.checkbox(f"Show Chart - {file.name}"):

                # Check if there are any numeric columns to plot
                numeric_columns = df.select_dtypes(include="number")
                
                if not numeric_columns.empty:
                    # Allow the user to select which columns to plot
                    chart_columns = st.multiselect(
                        f"Select Numeric Columns to Plot for {file.name}",
                        numeric_columns.columns.tolist(),
                        default=numeric_columns.columns.tolist()[:2]  # Default to the first 2 columns
                    )

                    if chart_columns:
                        # Plot the selected columns
                        st.bar_chart(df[chart_columns].head())  # Show first few rows for better performance
                    else:
                        st.warning("Please select at least one numeric column for the chart.")
                else:
                    st.warning(f"No numeric columns available in {file.name} for plotting.")

            # Convert file to different format
            format_choice = st.radio(f"Convert {file} to:", ['csv', 'Excel'], key=file.name)

            if st.button(f"Download {file.name} as {format_choice}"):
                output = BytesIO()
                if format_choice == 'csv':
                    df.to_csv(output, index=False)
                    mime_type = 'text/csv'
                    new_name = file.name.replace(ext, "csv")
                else:
                    df.to_excel(output, index=False, engine='openpyxl')
                    mime_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                    new_name = file.name.replace(ext, "xlsx")

                output.seek(0)
                st.download_button("Download Button", file_name=new_name, data=output, mime=mime_type)
                st.success('Processing Complete!')

        except Exception as e:
            st.error(f"Error reading {file.name}: {e}")
