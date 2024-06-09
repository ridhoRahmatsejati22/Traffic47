import streamlit as st
from streamlit_option_menu import option_menu
import analisis
import prediksi
import About

def show_dashboard():
    class MultiApp:
        def __init__(self):
            self.apps = []

        def add_app(self, title, func):
            self.apps.append({
                "title": title,
                "function": func
            })

        def run(self):
            with st.sidebar:
                app = option_menu(
                    menu_title='Traffic47',
                    options=['About', 'Analisis', 'Prediksi', 'Logout'], 
                    icons=['info-square-fill', 'bar-chart-fill', 'arrow-up-circle-fill', 'door-open-fill'], 
                    menu_icon='shop-fill',
                    default_index=0,
                    styles={
                        "container": {"padding": "5px", "background-color": "#F8F9FA"},  # Background color: Light gray
                        "icon": {"color": "#007BFF", "font-size": "23px"},  # Icon color: Blue
                        "nav-link": {
                            "color": "#000000",
                            "font-size": "20px",
                            "text-align": "left",
                            "margin": "0px",
                            "--hover-color": "#007BFF"
                        },  # Link color: Black, Hover color: Blue
                        "nav-link-selected": {
                            "background-color": "#A9A9A9",  # Selected link background color: Dark Gray (Soft)
                            "color": "#FFFFFF"  # Text color: White
                        }
                    }
                )

            if app == "About":
                About.app()  # Call the application function from About.py
            elif app == "Analisis":
                analisis.app()  # Call the application function from analisis.py
            elif app == "Prediksi":
                prediksi.app()  # Call the application function from prediksi.py
            elif app == "Logout":
                st.session_state.username = ''
                st.session_state.useremail = ''
                st.session_state.dashboard = False
                st.rerun()

    multi_app = MultiApp()
    multi_app.run()
