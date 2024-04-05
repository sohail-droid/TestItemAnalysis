# import os
# import streamlit as st
# import pandas as pd
# import re
# import numpy as np
# import matplotlib.pyplot as plt
# from tabulate import tabulate
# import subprocess
# import openpyxl
# from PIL import Image

# data = pd.read_excel("C:/Users/syed/OneDrive/Desktop/Final Project/TestAnalysis/DPSD- Comprehensive vaiva Quiz details.xlsx")

# ques = []
# students = len(data["First name"].value_counts())
# percent = (30 / 100)
# to_calculate = int(students * percent)
# regex = "Q\. ([1-9]|[1-9][0-9]{1,2}|1000)(.+)\.00$"
# v = data.columns.ravel()
# for i in v:
#     match = re.match(regex, i)
#     if match:
#         ques.append(i)

# dict_questions = {}

# for ques_val in ques:
#     lst = []
#     s = data.loc[:students, ques_val]
#     s = np.array(s.values)

#     for filter_none in s:
#         filter_none = str(filter_none)
#         if filter_none.isdigit():
#             lst.append(int(filter_none))
#         else:
#             lst.append(0)
#     dict_questions[ques_val] = lst

# Fascilation_index = []
# Descrimination_index = []

# for ques_no in ques:
#     sum_first = sum(dict_questions[ques_no][:to_calculate])
#     sum_last = sum(dict_questions[ques_no][-to_calculate:])

#     fac = ((sum_first + sum_last) / (2 * to_calculate * max(dict_questions[ques_no])))
#     Fascilation_index.append(fac)

#     Des = ((sum_first - sum_last) / to_calculate * max(dict_questions[ques_no]))
#     Descrimination_index.append(Des)

# distrac_eff = []
# for ques_no in ques:
#     incorrect_responses = sum(1 for val in dict_questions[ques_no] if val == 0)
#     total_responses = len(dict_questions[ques_no])
#     if total_responses != 0:
#         distrac_eff.append((incorrect_responses / total_responses) * 100)
#     else:
#         distrac_eff.append(0)

# output_data = pd.DataFrame({
#     "Questions": ques,
#     "Fascilitation_index": Fascilation_index,
#     "Discrimination_index": Descrimination_index,
#     "Distract_Effectiveness": distrac_eff
# })

# # Limit Distract_Effectiveness to two decimal places
# output_data['Distract_Effectiveness'] = output_data['Distract_Effectiveness'].round(2)

# data = None

# def main():
#     st.title("Excel Data Analyzer")

#     uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx", "xls"])

#     if uploaded_file is not None:
#         data = pd.read_excel(uploaded_file)
#         st.success("Data loaded successfully!")
#         analyze_data(data)
#     st.markdown("Thank you for using my app! 👋")

# st.header("Test Item Analysis")

# def get_unique_terms(data):
#     unique_terms = []

#     for column in data.columns:
#         unique_values = data[column].unique()
#         if len(unique_values) > 1:
#             unique_terms.append(column)

#     return unique_terms

# def analyze_data(data):
#     unique_terms = get_unique_terms(data)

#     if not unique_terms:
#         st.warning("No unique terms found in the data.")
#         return

#     selected_term = st.selectbox("Select a term for analysis:", unique_terms)
#     selected_value = st.selectbox(f"Select {selected_term}:", data[selected_term].unique())

#     result_data = data[data[selected_term] == selected_value]
#     st.subheader(f"{selected_term} - {selected_value} Analysis")

#     st.write(output_data.style.format({'Distract_Effectiveness': "{:.2f}"}))

#     st.dataframe(result_data)


# df = pd.read_excel("C:/Users/syed/OneDrive/Desktop/Final Project/TestAnalysis/DPSD- Comprehensive vaiva Quiz details.xlsx")
# top_30_percent = df['Grade/50.00'].quantile(0.7)
# bottom_30_percent = df['Grade/50.00'].quantile(0.3)

# # Filter the names based on the scores
# top_names = df[df['Grade/50.00'] >= top_30_percent]['First name']
# bottom_names = df[df['Grade/50.00'] <= bottom_30_percent]['First name']

# # Display top 30% names
# st.subheader("Top 30% Names:")
# st.write(top_names)

# # Display bottom 30% names
# st.subheader("Bottom 30% Names:")
# st.write(bottom_names)






# img = Image.open("C:\\Users\\syed\\OneDrive\\Desktop\\Final Project\\TestAnalysis\\4.jpg")

# st.image(img, caption="Welcome to Ats app!", width=700, channels="RGB")

# if __name__ == "_main_":
#     main()

#-------------------------------------------------------------------------
# import os
# import streamlit as st
# import pandas as pd
# import re
# import numpy as np
# import matplotlib.pyplot as plt
# import subprocess
# import openpyxl
# from PIL import Image

# def main():
#     st.title("Excel Data Analyzer")

#     # Add image at the top
#     img_top = Image.open("C:\\Users\\syed\\OneDrive\\Desktop\\Final Project\\TestAnalysis\\4.jpg")  # Replace "path_to_your_image.jpg" with the actual path to your image
#     st.image(img_top, caption="Welcome to Excel Data Analyzer!", use_column_width=True)

#     uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx", "xls"])

#     if uploaded_file is not None:
#         data = pd.read_excel(uploaded_file)
#         st.success("Data loaded successfully!")
#         analyze_data(data)
#     st.markdown("Thank you for using our app! 👋")

#------------------------------------------------------------------import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt
import subprocess
import openpyxl
from PIL import Image
import os
import streamlit as st
import pandas as pd

def main():
    st.title("Excel Data Analyzer")

    # Add image at the top
    img_top = Image.open("C:\\Users\\syed\\OneDrive\\Desktop\\Final Project\\TestAnalysis\\4.jpg")  # Replace "path_to_your_image.jpg" with the actual path to your image
    st.image(img_top, caption="Welcome to Excel Data Analyzer!", use_column_width=True)

    uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx", "xls"])

    if uploaded_file is not None:
        data = pd.read_excel(uploaded_file)
        st.success("Data loaded successfully!")
        analyze_data(data)
    st.markdown("Thank you for using our app! 👋")

def analyze_data(data):
    # Extracting question columns
    ques = [col for col in data.columns if re.match(r"Q\. ([1-9]|[1-9][0-9]{1,2}|1000)(.+)\.00$", col)]
    
    students = len(data["First name"].value_counts())
    percent = 0.3
    to_calculate = int(students * percent)
    
    dict_questions = {}
    Fascilation_index = []
    Descrimination_index = []
    distrac_eff = []
    
    for ques_val in ques:
        lst = []
        s = data[ques_val]
        s = np.array(s.values)

        for filter_none in s:
            filter_none = str(filter_none)
            if filter_none.isdigit():
                lst.append(int(filter_none))
            else:
                lst.append(0)
        dict_questions[ques_val] = lst
        
        sum_first = sum(lst[:to_calculate])
        sum_last = sum(lst[-to_calculate:])
        
        max_val = max(lst)
        fac = ((sum_first + sum_last) / (2 * to_calculate * max_val)) if max_val != 0 else 0
        Fascilation_index.append(fac)

        Des = ((sum_first - sum_last) / (to_calculate * max_val)) if max_val != 0 else 0
        Descrimination_index.append(Des)

        incorrect_responses = sum(1 for val in lst if val == 0)
        total_responses = len(lst)
        if total_responses != 0:
            distrac_eff.append((incorrect_responses / total_responses) * 100)
        else:
            distrac_eff.append(0)

    output_data = pd.DataFrame({
        "Question": range(1, len(ques) + 1),
        "Fascilitation_index": Fascilation_index,
        "Discrimination_index": Descrimination_index,
        "Distract_Effectiveness": distrac_eff
    })

    # Limit Distract_Effectiveness to two decimal places
    output_data['Distract_Effectiveness'] = output_data['Distract_Effectiveness'].round(2)

    # Display top and bottom 30% names side by side
    top_30_percent = data['Grade/50.00'].quantile(0.7)
    bottom_30_percent = data['Grade/50.00'].quantile(0.3)

    top_names = data[data['Grade/50.00'] >= top_30_percent][['First name', 'Grade/50.00']]
    bottom_names = data[data['Grade/50.00'] <= bottom_30_percent][['First name', 'Grade/50.00']]

    st.subheader("Top 30% & Bottom 30% Names:")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Top 30% Names:")
        st.write(top_names)
    with col2:
        st.subheader("Bottom 30% Names:")
        st.write(bottom_names)

    # Calculate various parameters based on Distract_Effectiveness values
    top_5 = output_data.nlargest(5, 'Distract_Effectiveness')
    bottom_5 = output_data.nsmallest(5, 'Distract_Effectiveness')
    topper = output_data.loc[output_data['Distract_Effectiveness'].idxmax()]

    # Get names based on their Distract Effectiveness
    top_5_names = data.iloc[top_5.index]['First name']
    bottom_5_names = data.iloc[bottom_5.index]['First name']
    topper_name = data.iloc[[topper.name]]['First name']

    # Display top 5, bottom 5, and topper side by side
    st.subheader("Analysis Based on Distract Effectiveness:")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Topper:")
        st.write("Name:", topper_name.values[0])
        st.write("Distract Effectiveness:", topper['Distract_Effectiveness'])
    with col2:
        st.subheader("Top 5 Distract Effectiveness:")
        st.write(top_5_names.reset_index(drop=True))
    with col3:
        st.subheader("Bottom 5 Distract Effectiveness:")
        st.write(bottom_5_names.reset_index(drop=True))

    # Display Fascilitation Index, Discrimination Index, and Distractive Effectiveness in a single table side by side
    st.subheader("Analysis Table:")
    st.write(output_data.set_index("Question"))  # Set the Question column as index to remove the index column

if __name__ == "__main__":
    main()
