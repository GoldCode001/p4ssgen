import streamlit as st
import random
import string

# Define the password generator function
def generate_password(length, lowercase, uppercase, numbers, symbols):
    # Define the characters to be used in the password
    letters = ""
    if lowercase:
        letters += string.ascii_lowercase
    if uppercase:
        letters += string.ascii_uppercase
    if numbers:
        letters += string.digits
    if symbols:
        letters += string.punctuation

    # Generate a password
    password = ''.join(random.choice(letters) for i in range(length))
    return password


# Create a Streamlit app
def main():
    # Set Streamlit options
    st.set_page_config(page_title="Password Generator", page_icon="🔒")
    #st.set_option('browser.serverAddress', '0.0.0.0')
    #st.set_option('server.enableCORS', False)
    #st.set_option('server.enableXsrfProtection', False)

    # Hide menu, footer and header
    hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """
    st.markdown(hide_menu_style, unsafe_allow_html=True)

    st.title("Password Generator")

    # Define the input fields
    length = st.slider("Password length", 6, 20, 10)
    lowercase = st.checkbox("Include lowercase letters")
    uppercase = st.checkbox("Include uppercase letters")
    numbers = st.checkbox("Include numbers")
    symbols = st.checkbox("Include symbols")

    # Generate a password and display it
    if st.button("Generate Password"):
        password = generate_password(length, lowercase, uppercase, numbers, symbols)
        st.write("Your password is:")
        st.write(password)

if __name__ == "__main__":
    main()
