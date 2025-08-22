import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from streamlit_card import card
from streamlit_extras.grid import grid
from streamlit_extras.stylable_container import stylable_container

# Page configuration
st.set_page_config(
    page_title="Awais Ishtiaq - Resume",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for 3D effects and styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    .main-header {
        font-size: 3.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0px 4px 15px rgba(106, 17, 203, 0.3);
        margin-bottom: 0;
    }
    
    .sub-header {
        font-size: 1.5rem;
        color: #636363;
        margin-top: 0;
    }
    
    .section-header {
        font-size: 2rem;
        font-weight: 600;
        color: #2575fc;
        border-left: 5px solid #6a11cb;
        padding-left: 15px;
        margin: 2rem 0 1rem 0;
    }
    
    .card {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 8px 32px rgba(106, 17, 203, 0.2);
        backdrop-filter: blur(4px);
        -webkit-backdrop-filter: blur(4px);
        border: 1px solid rgba(255, 255, 255, 0.18);
        transition: transform 0.3s ease;
        margin-bottom: 20px;
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(106, 17, 203, 0.3);
    }
    
    .skill-pill {
        display: inline-block;
        padding: 8px 15px;
        margin: 5px;
        border-radius: 20px;
        background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%);
        color: white;
        font-size: 0.9rem;
        box-shadow: 0 4px 10px rgba(106, 17, 203, 0.2);
    }
    
    .timeline {
        border-left: 3px solid #6a11cb;
        border-bottom-right-radius: 4px;
        border-top-right-radius: 4px;
        position: relative;
        margin: 20px 0;
        padding: 0 0 0 30px;
    }
    
    .timeline-item {
        margin-bottom: 20px;
        position: relative;
    }
    
    .timeline-item:before {
        content: "";
        position: absolute;
        width: 15px;
        height: 15px;
        border-radius: 50%;
        background: #6a11cb;
        left: -39px;
        top: 5px;
        border: 3px solid #fff;
        box-shadow: 0 0 0 3px #6a11cb;
    }
    
    .contact-info {
        display: flex;
        align-items: center;
        margin: 10px 0;
    }
    
    .contact-icon {
        margin-right: 15px;
        font-size: 1.2rem;
        color: #6a11cb;
    }
            
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
</style>
""", unsafe_allow_html=True)

# Header Section
col1, col2 = st.columns([2, 1])
with col1:
    st.markdown('<h1 class="main-header">AWAIS ISHTIAQ</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Business Finance Graduate & AI Developer</p>', unsafe_allow_html=True)
    
    # Contact info
    st.markdown(
        """
        <div class="contact-info">
            <span class="contact-icon">📱</span> +973 36974120
        </div>
        <div class="contact-info">
            <span class="contact-icon">📧</span> awais.ishtiaq08@gmail.com
        </div>
        <div class="contact-info">
            <span class="contact-icon">📍</span> Manama, Bahrain
        </div>
        <div class="contact-info">
            <span class="contact-icon">🔗</span> 
            <a href="https://linkedin.com/in/awais-ishtiaq" target="_blank">LinkedIn</a> | 
            <a href="https://github.com/AwaisIshtiaq" target="_blank">GitHub</a>
        </div>
        """, 
        unsafe_allow_html=True
    )

with col2:
    # You could add a profile picture here if available
    # st.image("https://via.placeholder.com/150/6a11cb/ffffff?text=AI", width=150)
    pass

# Objective Section
st.markdown('<h2 class="section-header">Objective</h2>', unsafe_allow_html=True)
st.markdown("""
<div class="card">
    Accomplished Business Finance graduate with proven expertise at the intersection of finance and advanced technol
ogy. Skilled Python and Django developer with strong capabilities in Artificial Intelligence and Machine Learning,
 leveraging these tools to design intelligent, data-driven systems that optimize financial operations, accelerate decision
making, and deliver measurable business value. Adept at building scalable web applications, automation pipelines,
 and predictive models that enhance efficiency and strategic insight. Passionate about transforming financial ecosys
tems through innovative software engineering, precision analytics, and AI-powered solutions. Committed to delivering
 excellence in environments where finance, technology, and strategic vision converge.
</div>
""", unsafe_allow_html=True)

# Skills Section
st.markdown('<h2 class="section-header">Technical Skills</h2>', unsafe_allow_html=True)

# Create a grid for skills
st.markdown("""
    <style>
    .skill-container {
        display: flex;
        justify-content: center; /* center horizontally */
        align-items: center;
        flex-wrap: wrap;
        gap: 12px;
        margin: 10px 0;
        text-align: center;
    }
    .skill-pill {
        display: inline-block;
        background-color: #f0f2f6;
        padding: 8px 16px;
        border-radius: 20px;
        font-size: 14px;
        font-weight: 500;
        box-shadow: 0px 2px 6px rgba(0,0,0,0.1);
        margin: 4px;
    }
    </style>
""", unsafe_allow_html=True)

# Create 8-column grid
skill_grid = grid(8, vertical_align="center")

# --- Grid 1 ---
with skill_grid.container():
    st.markdown("**Programming Languages**")
    st.markdown(
        '<div class="skill-container">'
        '<div class="skill-pill">Python</div>'
        '<div class="skill-pill">PHP</div>'
        '<div class="skill-pill">JavaScript</div>'
        '<div class="skill-pill">Kotlin</div>'
        '<div class="skill-pill">HTML</div>'
        '<div class="skill-pill">CSS</div>'
        '</div>', unsafe_allow_html=True
    )

# --- Grid 2 ---
with skill_grid.container():
    st.markdown("**Frameworks**")
    st.markdown(
        '<div class="skill-container">'
        '<div class="skill-pill">Django</div>'
        '<div class="skill-pill">Flask</div>'
        '<div class="skill-pill">Laravel</div>'
        '<div class="skill-pill">Streamlit</div>'
        '</div>', unsafe_allow_html=True
    )

# --- Grid 3 ---
with skill_grid.container():
    st.markdown("**Libraries**")
    st.markdown(
        '<div class="skill-container">'
        '<div class="skill-pill">NumPy</div>'
        '<div class="skill-pill">Pandas</div>'
        '<div class="skill-pill">Scikit-learn</div>'
        '<div class="skill-pill">TensorFlow</div>'
        '<div class="skill-pill">Keras</div>'
        '</div>', unsafe_allow_html=True
    )

# --- Grid 4 ---
with skill_grid.container():
    st.markdown("**Artificial Intelligence**")
    st.markdown(
        '<div class="skill-container">'
        '<div class="skill-pill">Data Science</div>'
        '<div class="skill-pill">Machine Learning</div>'
        '<div class="skill-pill">Generative AI</div>'
        '</div>', unsafe_allow_html=True
    )

# --- Grid 5 ---
with skill_grid.container():
    st.markdown("**Platforms**")
    st.markdown(
        '<div class="skill-container">'
        '<div class="skill-pill">PyCharm</div>'
        '<div class="skill-pill">Jupyter</div>'
        '<div class="skill-pill">VS Code</div>'
        '</div>', unsafe_allow_html=True
    )

# --- Grid 6 ---
with skill_grid.container():
    st.markdown("**Tools**")
    st.markdown(
        '<div class="skill-container">'
        '<div class="skill-pill">Git</div>'
        '<div class="skill-pill">Tableau</div>'
        '</div>', unsafe_allow_html=True
    )

# --- Grid 7 ---
with skill_grid.container():
    st.markdown("**Databases**")
    st.markdown(
        '<div class="skill-container">'
        '<div class="skill-pill">MySQL</div>'
        '<div class="skill-pill">PostgreSQL</div>'
        '<div class="skill-pill">MongoDB</div>'
        '</div>', unsafe_allow_html=True
    )

# --- Grid 8 ---
with skill_grid.container():
    st.markdown("**Cloud & Deployment**")
    st.markdown(
        '<div class="skill-container">'
        '<div class="skill-pill">AWS</div>'
        '<div class="skill-pill">Docker</div>'
        '<div class="skill-pill">Heroku</div>'
        '</div>', unsafe_allow_html=True
    )

# Experience Section
st.markdown('<h2 class="section-header">Professional Experience</h2>', unsafe_allow_html=True)

exp_col1, exp_col2 = st.columns(2)

with exp_col1:
    st.markdown("""
    <div class="card">
        <h3>Django Developer</h3>
        <p><strong>Trolink Software House</strong> | Aug 2024 - Feb 2025</p>
        <ul>
            <li>Designed, developed, and maintained scalable Django-based web applications</li>
            <li>Integrated machine learning models into production environments</li>
            <li>Developed and optimized RESTful APIs for seamless data exchange</li>
            <li>Built dynamic, data-driven dashboards using Django and JavaScript</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with exp_col2:
    st.markdown("""
    <div class="card">
        <h3>E-Commerce Operations Manager</h3>
        <p><strong>Leopards Courier Services Pvt ltd</strong> | Feb 2020 - Jul 2024</p>
        <ul>
            <li>Managed e-commerce portals and API integrations</li>
            <li>Handled cash on delivery accounts and tracked sales goals</li>
            <li>Developed dynamic dashboards for company and vendor analysis</li>
            <li>Enhanced sales through effective service promotion</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Education and Certifications
st.markdown('<h2 class="section-header">Education & Certifications</h2>', unsafe_allow_html=True)

edu_col1, edu_col2 = st.columns(2)

with edu_col1:
    st.markdown("""
    <div class="card">
        <h3>Bachelor in Business Studies</h3>
        <p><strong>Hazara University</strong> | 2016</p>
        <p>Major: Finance</p>
    </div>
    """, unsafe_allow_html=True)

with edu_col2:
    st.markdown("""
    <div class="card">
        <h3>Certifications</h3>
        <ul>
            <li>Certified Artificial Intelligence Developer (PIAIC) - 2020-2023</li>
            <li>Python Development (IEC) - 2023</li>
            <li>Programming Essentials in Python (OpenEDG) - 2022</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Projects Section
st.markdown('<h2 class="section-header">Projects</h2>', unsafe_allow_html=True)

# Create tabs for different project categories
tab1, tab2, tab3, tab4 = st.tabs(["Machine Learning", "Django", "Finance", "Python"])

with tab1:
    st.markdown("""
    <div class="card">
        <h3>Heart Disease Prediction</h3>
        <p>Machine learning model with 98% accuracy using RandomForestClassifier</p>
        <span class="skill-pill">Scikit-learn</span>
        <span class="skill-pill">Pandas</span>
        <span class="skill-pill">Numpy</span>
        <span class="skill-pill">Random Forest Classifier</span>
        
        
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
        <h3>Resume Analyzer NLP Project</h3>
        <p>NLP application for skill extraction and job category prediction</p>
        <span class="skill-pill">NLP</span>
        <span class="skill-pill">NLTK</span>
        <span class="skill-pill">Scikit-learn</span>
        <span class="skill-pill">TF-IDF</span>
        
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h3>Churn Prediction </h3>
        <p>Deep Learning </p>
        <span class="skill-pill">Scikit-learn</span>
        <span class="skill-pill">Pandas</span>
        <span class="skill-pill">Numpy</span>
        <span class="skill-pill">TensorFlow</span>
        <span class="skill-pill">ANN</span>
        
        
        
    </div>
    """, unsafe_allow_html=True)
    

with tab2:
    st.markdown("""
    <div class="card">
        <h3>Link Shortener App</h3>
        <p>URL shortening service with tracking functionality</p>
        <p><h6>Store long URLs with short, easy-to-remember slugs, Automatic or custom slug generation, Track how
             many times each shortened URL has been accessed, Admin interface to manage all URLs and view click counts</h6></p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h3>CarZone App </h3>
        <p>CarZone - Buy & Rent with Ease</p>
        <p><h6>CarZone is a car dealership web application built using Django. It allows users to browse, search,
         and inquire about cars, while admins can manage car listings, brands, and user inquiries through a powerful
         admin interface.</h6></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
        <h3>Online Job Portal</h3>
        <p>Platform connecting companies with job seekers</p>
        <p><h6>Register and log in :Post job openings :View list of applicants per job. For
             Candidates : Register and log in :View available jobs :Upload resume/CV : Apply to jobs with one click :Manage
             applied jobs</h6></p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
        <div class="card">
            <h3>ToDo-app</h3>
            <p>Simple To-Do & Daily Tasks</p>
            <p><h6>A simple and efficient Django-based ToDo application where users can: Add tasks with descriptions,
                 Search tasks, Delete tasks, View all added tasks.</h6></p>
        </div>
    """, unsafe_allow_html=True)



with tab3:
    st.markdown("""
    <div class="card">
        <h3>Stock Price Prediction</h3>
        <p>Fama-French Three-Factor Model implementation in Excel</p>
        <ul>
            <li>Developed a predictive model in Excel using the Fama-French Three-Factor Model, incorporating Market Risk
             Premium, SMB (Small Minus Big), and HML (High Minus Low) factors to estimate expected stock returns.</li>
            <li>Gathered historical stock data from Yahoo Finance and factor data from the Kenneth French Data Library.</li>
            <li>Performed multiple linear regression analysis using Excel’s Data Analysis Toolpak to calculate factor sensitivities
                (betas) and determine their influence on stock returns.</li>
            <li>Created visualizations and charts to display the relationship between factor exposures and predicted vs actual
                stock performance.</li>
            <li>Used the model to analyze different stocks and evaluate the effectiveness of factor-based prediction in investment
            decision making.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
        <h3>CAPM Analysis</h3>
        <p>Capital Asset Pricing Model for stock return analysis</p>
        <ul>
            <li>Applied the Capital Asset Pricing Model to estimate the expected return of individual stocks based on their
                 systematic risk (beta) relative to the overall market.</li>
            <li>Collected historical price data for selected stocks and market indices (e.g., SP 500) using Yahoo Finance and
                 calculated monthly returns in Excel.</li>
            <li>Conducted regression analysis to estimate beta coefficients, compare predicted vs actual returns, and assess
                     stock risk relative to the market.</li>
            <li>Calculated risk-free rate, market premium, and applied the CAPM formula to determine fair value and assess
                 overvalued/undervalued stocks.</li>
            <li>Created interactive dashboards and charts in Excel to visualize stock performance, beta sensitivity, and CAPM
                 results for investment decision-making</li>        
        </ul>
    </div>
    """, unsafe_allow_html=True)

with tab4:
    st.markdown("""
    <div class="card">
        <h3>ATM Simulation</h3>
        <p>Python application simulating banking operations</p>
        <p><h6>Automatic Teller Machine Using Python: Simulated ATM system for basic banking operations.</h6></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
        <h3>Web Scraping Tool</h3>
        <p>Data extraction from websites using BeautifulSoup</p>
        <p><h6>Crawl/Scrape ODI Records Using Beautiful Soup: Web scraper for extracting ODI cricket records from CricInfo.</h6></p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <h3> BMI Calculator</h3>
        <p>Python application Calculating BMI</p>
        <p><h6>Python application to calculate and categorize BMI.</h6></p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <h3>Terminal-based “Quiz Game” Using Python</h3>
        <p>Pytho Quiz Game </p>
        <p><h6>Terminal-based “Quiz Game” Using Python: Interactive quiz game using text files for questions and answers.</h6></p>
    </div>
    """, unsafe_allow_html=True)
    
   

# Footer
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: #636363;">
        <p>© 2024 Awais Ishtiaq | 
        <a href="mailto:awais.ishtiaq08@gmail.com">Email</a> | 
        <a href="https://linkedin.com/in/awais-ishtiaq">LinkedIn</a> | 
        <a href="https://github.com/AwaisIshtiaq">GitHub</a></p>
    </div>
    """, 
    unsafe_allow_html=True
)