#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 09:15:39 2023

@author: ondrejsvoboda
"""

import streamlit as st
import streamlit.components.v1 as components

import hydralit_components as hc
import webbrowser
from st_click_detector import click_detector

class WorkflowProgress():
    theme_bad = {'bgcolor': '#FFF0F0','progress_color': 'red', 'title_color': 'red','content_color': 'red','icon_color': 'red', 'icon': 'fa fa-times-circle'}
    theme_inprogress = {'bgcolor': '#F8C471','progress_color': 'black', 'title_color': 'black','content_color': 'black','icon_color': 'black', 'icon': 'fa fa-cog'}
    theme_neutral = {'bgcolor': '#f9f9f9','progress_color': 'orange', 'title_color': 'orange','content_color': 'orange','icon_color': 'orange', 'icon': 'fa fa-question-circle'}
    theme_good = {'bgcolor': '#EFF8F7','progress_color': 'green', 'title_color': 'green','content_color': 'green','icon_color': 'green', 'icon': 'fa fa-check-circle'}
    
    def __init__(self, user):
        self.user = user
        self.columns = st.columns(2)
        self.authorization_sentiment = st.session_state.authorization_sentiment
        #self.data_sentiment = st.session_state.data_sentiment
        self.mapping_sentiment = st.session_state.mapping_sentiment
        #self._update_sentiments()
        self._prepare_progress_widget()
        
        
        
    def _prepare_progress_widget(self):
        
        with self.columns[0]:
            self.info_card = hc.info_card(content='Authorization step', theme_override=self.authorization_sentiment, bar_value=100, key='auth_card')
    #    with self.columns[1]:
    #        hc.info_card(content='Data extracted', theme_override=self.data_sentiment, bar_value=100, key='data_card')
        with self.columns[1]:
            hc.info_card(content='Mapping done', theme_override=self.mapping_sentiment, bar_value=100, key='map_card')    
    
        
def disable():
    st.session_state.disabled = True

def clicked():
    st.session_state.clicked = True

def open_url(url='www.google.com'):
    #webbrowser.open(url, 2)
    webbrowser.open_new_tab(url)
        
        #self.authorization_sentiment='good'
def submit_form():
    
        with st.form("submitform"):
            st.markdown("1. Please fill in your **Quickbooks Company ID** and if you are using a financial calendar, then select the checkbox below **Using Financial Calendar**")

            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("Quickbooks Company ID:")
                st.text_input(label="aaa", label_visibility="collapsed", key='company_id')
                
            with col2:
                st.markdown("Using Financial Calendar:")
                st.checkbox(label="", key='custom_calendar')
                
#            submitted = st.form_submit_button("Submit", on_click=disable, disabled=st.session_state.disabled)
            submitted = st.form_submit_button("Submit", on_click=clicked)

            ChangeButtonColour('Submit', 'black', '#F8C471') # button txt to find, colour to assign

            if submitted:
               st.info(f"You have entered: a company ID = {st.session_state.company_id} and Financial Calendar = {st.session_state.custom_calendar}")
            return submitted


            
# def submit_form2():
            
#     with st.form("submitform2"):
#         st.markdown("2. Now, please **authorize** the configuration by clicking at the button below")
            
#         submitted = st.form_submit_button("Authorize", on_click=nav_to)
#         ChangeButtonColour('Authorize', 'black', '#F8C471') # button txt to find, colour to assign


#         url = 'https://stackoverflow.com'
        
#         st.markdown(f'''
#         <a href={url}><button style="background-color:GreenYellow;">Stackoverflow</button></a>
#         ''',
#         unsafe_allow_html=True)

#         content = """
#                     <p>Check out <a href="https://www.freecodecamp.org/" id='Link code' target="_blank">freeCodeCamp</a>.</p>
#                     """
#         clicked = click_detector(content)


#         if submitted:
#             st.success("The configuration has been authorized. Now, data will be downloaded from Quickbooks.")
#             #components.iframe("www.google.com")
#             redirect('www.google.com')

#             nav_to()
            
def ChangeButtonColour(widget_label, font_color, background_color='transparent'):
    htmlstr = f"""
        <script>
            var elements = window.parent.document.querySelectorAll('button');
            for (var i = 0; i < elements.length; ++i) {{ 
                if (elements[i].innerText == '{widget_label}') {{ 
                    elements[i].style.color ='{font_color}';
                    elements[i].style.background = '{background_color}'
                }}
            }}
        </script>
        """
    components.html(f"{htmlstr}", height=0, width=0)

def render_clickable_link(url):
    content = f'''
                <p>2. Please authorize authorize to access <a href="{url}" id='Link code' target="_blank">QuickBooks</a>.</p>
                '''
    clicked = click_detector(content)
    
    if clicked:
        st.success("QuickBooks account has been authorized")
    else:
        st.warning("The link is yet to be clicked")
    
    #st.markdown(f"**{clicked} clicked**" if clicked != "" else "**No click**")
    

