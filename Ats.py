import os
import streamlit as st
import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
import subprocess
import openpyxl
from PIL import Image
import random


data = pd.read_excel("C:/Users/syed/OneDrive/Desktop/Final Project/TestAnalysis/DPSD- Comprehensive vaiva Quiz details.xlsx")
# 
# data = pd.read_excel("DPSD- Comprehensive vaiva Quiz details.xlsx")
# data[:]

ques=[]
students=len(data["First name"].value_counts())
percent = (30/100)
to_calculate = int(students*percent)
regex = "Q\. ([1-9]|[1-9][0-9]{1,2}|1000)(.+)\.00$"
v=data.columns.ravel()
for i in v:
    match = re.match(regex, i)
    if match:
        ques.append(i)
# print(ques)

dict_questions = {}

for ques_val in ques:
        lst=[]
        s=data.loc[:students, ques_val]
        s=np.array(s.values)

        for filter_none in s:
            filter_none = str(filter_none)
            if filter_none.isdigit():
                lst.append(int(filter_none))
            else:
                lst.append(0)
        dict_questions[ques_val]=lst

# print(dict_questions)

Fascilation_index = []
Descrimination_index = []

for ques_no in ques:
    sum_first = sum(dict_questions[ques_no][:to_calculate])
    sum_last = sum(dict_questions[ques_no][-to_calculate:])

    fac = ((sum_first+sum_last)/(2*to_calculate*max(dict_questions[ques_no])))
    Fascilation_index.append(fac)

    Des = ((sum_first-sum_last)/to_calculate*max(dict_questions[ques_no]))
    Descrimination_index.append(Des)


total_indices = [sum(pair) for pair in zip(Fascilation_index, Descrimination_index)]

output_data = pd.DataFrame({
    "Questions": ques,
    "Fascilitation_index": Fascilation_index,
    "Discrimination_index": Descrimination_index,
    "total_indices": total_indices
})

# Limit Total Indices to two decimal places
output_data['total_indices'] = output_data['total_indices'].round(2)

# Display the table
# print(tabulate(output_data, headers="keys", tablefmt='fancy_grid', numalign='center', stralign='left', colalign=('center', 'center', 'center')))

# Save plots to a file (optional)
for i, lst in enumerate([Fascilation_index, Descrimination_index, total_indices]):
    fig, ax = plt.subplots()
    ax.plot(lst)
    ax.set_title(f"Index graph {i + 1}")
    ax.set_ylabel("Question")
    ax.set_xlabel("Index")
    # plt.savefig(f"C:\\Users\\syed\\OneDrive\\Desktop\\Final Project\\index_graph_{i + 1}.png")
    # Show the plots
    # plt.show()
  
data = None

def main():
    st.title("Excel Data Analyzer")

    uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx", "xls"])

    if uploaded_file is not None:
        data = pd.read_excel(uploaded_file)
        st.success("Data loaded successfully!")
        analyze_data(data)
    st.markdown("Thank you for using my app! 👋")
try:
    img = Image.open("C:\\Users\\syed\\OneDrive\\Desktop\\Final Project\\TestAnalysis\\4.jpg")
    # Proceed with processing the image
except FileNotFoundError:
    print("Error: Image file not found.")
except Exception as e:
    print("An error occurred:", e)
st.image(img,caption="Welcome to Ats app!",width=700,channels="RGB")
st.header("Test Item Analaysis")



# List of quotes
quotes = [
    "The only way to do great work is to love what you do. – Steve Jobs",
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "Don’t watch the clock; do what it does. Keep going. – Sam Levenson",
    "Everything you can imagine is real. – Pablo Picasso",
    "Success usually comes to those who are too busy to be looking for it. – Henry David Thoreau",
    "If life were predictable, it would cease to be life, and be without flavor. – Eleanor Roosevelt",
    "Life is 10% what happens to us and 90% how we react to it. – Charles R. Swindoll",
    "The best way to predict the future is to invent it. – Alan Kay",
    "The pessimist sees difficulty in every opportunity. The optimist sees the opportunity in every difficulty. – Winston Churchill",
    "You miss 100% of the shots you don’t take. Wayne Gretzky",
    "Strive not to be a success, but rather to be of value. – Albert Einstein",
    "Do not wait to strike till the iron is hot; but make it hot by striking. – William Butler Yeats",
    "A champion is defined not by their wins but by how they can recover when they fall. – Serena Williams",
    "What lies behind us and what lies before us are tiny matters compared to what lies within us. – Ralph Waldo Emerson",
    "I cannot give you the formula for success, but I can give you the formula for failure: Try to please everybody. – Herbert Bayard Swope",
    "Innovation distinguishes between a leader and a follower. – Steve Jobs",
    "There are no shortcuts to any place worth going. – Beverly Sills",
    "We become what we think about most of the time, and that's the strangest secret. – Earl Nightingale",
    "Your positive action combined with positive thinking results in success. – Shiv Khera",
    "An unexamined life is not worth living. – Socrates",
    "Either write something worth reading or do something worth writing. – Benjamin Franklin",
    "You must expect great things of yourself before you can do them. – Michael Jordan",
    "Talent is cheaper than table salt. What separates the talented individual from the successful one is a lot of hard work. – Stephen King",
    "Genius is one percent inspiration and ninety-nine percent perspiration. – Thomas A. Edison",
    "Great minds discuss ideas. Average minds discuss events. Small minds discuss people. – Eleanor Roosevelt",
    "When everything seems to be going against you, remember that the airplane takes off against the wind, not with it. – Henry Ford",
    "Only put off until tomorrow what you are willing to die having left undone. – Pablo Picasso",
    "Be patient and calm—for no one can catch fish in anger. – Heraclitus",
    "Imagination was given to man to compensate him for what he isn't. A sense of humor was provided to console him for what he is. – Oscar Wilde",
    "Human beings are works in progress that mistakenly think they're finished. – Dan Gilbert",
    "People rarely succeed unless they have fun in what they are doing. – Dale Carnegie",
    "Logic will get you from A to B. Imagination will take you everywhere. – Albert Einstein",
    "Keep away from those who try to belittle your ambitions. Small people always do that, but the really great make you believe that you too can become great. – Mark Twain",
    "Twenty years from now you will be more disappointed by the things that you didn't do than by the ones you did do. So throw off the bowlines. Sail away from the safe harbor. Catch the trade winds in your sails. Explore. Dream. Discover. – Mark Twain",
    "Winning doesn't always mean being first. Winning means you're doing better than yesterday. – Haruki Murakami",
    "Opportunity is missed by most people because it is dressed in overalls and looks like work. – Thomas Alva Edison",
    "It's kind of fun to do the impossible. – Walt Disney",
    "The ultimate measure of a person is not where they stand in moments of comfort, but where they sit at times of challenge and controversy. – Martin Luther King Jr.",
    "Two roads diverged in a wood, and I took the one less traveled by, And that has made all the difference. – Robert Frost",
    "Always bear in mind that your own resolution to succeed is more important than any one thing. – Abraham Lincoln",
    "What counts can't always be counted; what can be counted doesn't always count. – Albert Einstein",
    "Far and away the best prize that life has to offer is the chance to work hard at work worth doing. – Theodore Roosevelt",
    "No matter how many mistakes you make or how slow you progress, you are still way ahead of everyone who isn't trying. – Tony Robbins",
    "Limitations live only in our minds. But if we use our imaginations, our possibilities become limitless. – Jamie Paolinetti",
    "Try not to become a person of success, but rather try to become a person of value. – Albert Einstein",
    "Develop success from failures. Discouragement and failure are two of the surest stepping stones to success. – Dale Carnegie",
    "Things do not happen. Things are made to happen. – John F. Kennedy",
    "Creativity is intelligence having fun. – Albert Einstein",
    "The power of imagination makes us infinite. – John Muir",
]

def generate_quote():
    random_index = random.randint(0, len(quotes) - 1)
    chosen_quote = quotes[random_index]
    return chosen_quote


if st.button('Generate New Quote'):
    new_quote = generate_quote()
    st.write(new_quote)


def get_unique_terms(data):
    unique_terms = []

    for column in data.columns:
        unique_values = data[column].unique()
        if len(unique_values) > 1:
            unique_terms.append(column)

    return unique_terms

def analyze_data(data):
    unique_terms = get_unique_terms(data)

    if not unique_terms:
        st.warning("No unique terms found in the data.")
        return

    selected_term = st.selectbox("Select a term for analysis:", unique_terms)
    selected_value = st.selectbox(f"Select {selected_term}:", data[selected_term].unique())

    result_data = data[data[selected_term] == selected_value]
    st.subheader(f"{selected_term} - {selected_value} Analysis")

     # Print Fascilation_index, Descrimination_index, and total_indices
    # st.write("Fascilation Index:", Fascilation_index)
    # st.write("Discrimination Index:", Descrimination_index)
    # st.write("Total Indices:", total_indices)
    st.write(output_data.style.format({'Total Indices': "{:.2f}"}))
    st.dataframe(result_data)

if __name__ == "__main__":
    main()
