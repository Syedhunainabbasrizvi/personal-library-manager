import streamlit as st

# to check password letters(capatilization, lower case and etc.)
import re

st.set_page_config(page_title="🔐 Password Strenght Checker")

st.title("🔐Password Strength Checker")

st.markdown("""
### Welcome to SafeGuard,  
###    Your Personal Password Strength Checker!

Ensure your passwords are **strong and secure** before using them.  
This tool will analyze your password and give you instant feedback  
on its strength based on length, complexity, and character variety.

💡 Stay safe. Stay secure. Let's check that password!
""")

# password input
password = st.text_input("**Enter your password:**", type="password")

feedback =[]

score = 0

if password:
    if len(password) >=8:
     score += 1
    else:
       feedback.append("❌ Password should be atleast 8 character long.")

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
       score += 1
    else:
       feedback.append("❌ Password should contain upper and lower case characters") 

    if re.search(r'[\d]', password):
       score += 1
    else:
       feedback.append("❌ Password should contain atleast one digit")      

    if re.search(r'[!@$#%^&~]', password):
       score += 1
    else:
       feedback.append("❌ Password should contain atleast one special character.")
    if score == 4:
        feedback.append("✅ Your password is strong!")
    elif score == 3:
       feedback.append("✅ Your password is medium strength, It could be stronger")
    else:
       feedback.append("🔴 Your Password is Week, Please make it stronger!")       
    

    if feedback:
       st.markdown("## Improvemnet Suggestion")
       for tip in feedback:
          st.write(tip)

else:
   st.info("Please enter your password to get started!")
 