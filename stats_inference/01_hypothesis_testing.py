import streamlit as st

from st_pages import add_page_title

from utils.other_utils import add_logo

def main():
    st.set_page_config(
        page_title='Hypothesis Testing',
        layout='wide'
    )

    # Add USF logo
    add_logo()

if __name__ == '__main__':
    main()