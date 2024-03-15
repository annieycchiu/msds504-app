import streamlit as st

from st_pages import Page, Section, show_pages

from utils.other_utils import add_logo

def main():

    st.set_page_config(
        page_title='MSDS504',
        layout='wide'
    )

    show_pages(
        [   
            Page('./app.py', 'MSDS 504', '🏠'),

            # Probability
            Section(name='Probability', icon='📊'),
            Page('./probability/01_binomial_distribution.py', '1-1. Binomial Distribution', in_section=True),

            # Statistical Inference
            Section(name='Statistical Inference', icon='🔍'),
            Page('./stats_inference/01_hypothesis_testing.py', '2-1. Hypothesis Testing', in_section=True),
            Page('./stats_inference/02_bootstrapping.py', '2-2. Bootstrapping', in_section=True),

            # Formula Cheatsheet
            Page('cheatsheet.py', 'Formula Cheatsheet', '📝', in_section=False),
        ]
    )

    st.title('USF MSDS504 Statistics & Probability')
    st.write('')
    st.write('')

    # Add USF logo
    add_logo()


if __name__ == '__main__':
    main()