import streamlit as st




# Base Class
class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email


# Intermediate Class (Inheritance from Person)
class Applicant(Person):
    def __init__(self, name, age, email, qualification, skills):
        super().__init__(name, age, email)
        self.qualification = qualification
        self.skills = skills

# Final Class in Multi-Level Inheritance (Inheritance from Applicant)
class DataAnalystApplicant(Applicant):
    def __init__(self, name, age, email, qualification, skills, experience, tools):
        super().__init__(name, age, email, qualification, skills)
        self.experience = experience
        self.tools = tools


# Function to determine eligibility
def check_eligibility(applicant):
    if applicant.experience >= 1 and "Excel" in applicant.tools and "Python" in applicant.tools:
        return "Eligible for Data Analyst Interview"
    else:
        return "Not Eligible"


# Streamlit UI
st.title("Data Analyst Job Appointment ")


st.header("Enter Applicant Details")


name = st.text_input("Name")
age = st.number_input("Age", min_value=18, max_value=60)
email = st.text_input("Email")
qualification = st.selectbox("Qualification", ["BSc", "BCA", "B.Tech", "MSc", "MCA", "MBA","Diploma"])
skills = st.text_area("Skills (comma separated)")
experience = st.number_input("Years of Experience", min_value=1, max_value=20)
tools = st.multiselect("Tools Known", ["Excel", "Python", "Power BI", "Tableau", "SQL", "NumPy", "Pandas"])


if st.button("Check Eligibility"):
    skills_list = [s.strip() for s in skills.split(",") if s.strip()]
    applicant = DataAnalystApplicant(name, age, email, qualification, skills_list, experience, tools)
    result = check_eligibility(applicant)


    st.subheader("Applicant Details:")
    st.write(f"Name: {applicant.name}")
    st.write(f"Age: {applicant.age}")
    st.write(f"Email: {applicant.email}")
    st.write(f"Qualification: {applicant.qualification}")
    st.write(f"Skills: {', '.join(applicant.skills)}")
    st.write(f"Experience: {applicant.experience} years")
    st.write(f"Tools Known: {', '.join(applicant.tools)}")
    
    
    

    st.subheader("Eligibility Result:")
    if result == "Eligible for Data Analyst Interview":
        st.success(result)
    else:
        st.error(result)
        

        
    