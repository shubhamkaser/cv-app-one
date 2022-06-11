import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Shubham Kaser
##### Lead Business Analyst
##### *Resume* 
''')

image = Image.open('profpic.jpg')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- 4.5 years experienced Business Analyst armed with a Post Graduate Diploma in Data Science with a passion to solve real-world business challenges. Skilled at deploying machine learning and statistical modelling algorithms/techniques to identify patterns, extract valuable insights and predict business outcomes. Experienced in managing end-to-end life-cycle of product development across the blockchain, ICO (Initial Coin Offering), education domain and Retail.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="" target="_blank">Shubham Kaser</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')

txt('**Post Graduation Diploma in Data Science**, *IIT Bangalore*',
'2019-2020')
st.markdown('''
- GPA: `3.65`

''')

# - Research thesis entitled `Computer-aided molecular design for biological and chemical applications : Quantum chemical and machine learning approach`.
# - Received Royal Golden Jubilee Ph.D. Scholarship of `2.152 million THB` covering tuition and stipend.
# - Thesis awarded `1st` Prize by the National Research Council of Thailand.

txt('**Bachelors of Technology** (Biotechnology), *National Institute of Technology*, Raipur',
'2013-2017')
st.markdown('''
- CGPA: `7.46`
- Research thesis entitled `Homology Modeling and Molecular Docking Studies of Bacillomycin and Iturin Synthetases with Novel Ligands for the Production of Therapeutic Lipopeptides`.
''')

#####################
st.markdown('''
## Work Experience
''')

txt('**Senior Business Analyst**, Ugam Solutions PVT LTD',
'Dec 20-Present')
st.markdown('''
- **Market Mix Modelling for 360i:**
  - Built appropriate models to sufficiently capture historical data including the COVID effect on sales and used these models to evaluate the contribution of each media channel to drive revenue
  - Also used S and C curves to determine advertising spend saturation and hence calculated the point of highest ROI for each media channel

- **Media Spend Forecasting for iProspect:**
  - Generated forecast reports for media spending across all advertising channels for multiple clients that used this as a baseline for their budget planning.
  - Also developed an optimiser/scenario planner wherein the budgets across media channels were optimised to maximise a particular KPI.
''')

txt('**Business Analyst**, Collegedunia',
'Jul 19-Dec 20')
st.markdown('''
- Successfully planned and deployed a machine learning model to predict lead score from users' behaviour for different clients that changed the lead delivery system completely saving manpower of about 12 and increasing the CR by 25% for our top revenue generating clients.
- Analysed visitors' behaviour with Google Analytics and Amazon Redshift to take key decisions like new feature implementation on website to provide better user experience that effectively increased Average Session Duration of the website by 13%
''')

txt('**Business Analyst**, Ultratech India Limited',
'Jun 18-Jul 19')
st.markdown('''
- Managed end-to-end life-cycle of technical development (software & website) & did the digital marketing for projects across the block-chain and ICO (initial coin offering) industries.
- Performed a wide range of people management functions from recruiting through goal setting, training, resource utilisation/ allocation, building advisory board from the budget allocated etc.
- Strategically planned and analysed the basic requirements in setting up the technical infrastructure of the project while reviewing the project proposals.
- Devised strategies for Bounty, Airdrop, Social Media, PR & Other Digital Marketing Platform.
- Liaised with PR & listing website and exchanges.
''')


# #####################
# st.markdown('''
# ## Bioinformatics Tools
# ''')
# txt4('ABCpred', 'A web server for the discovery of acetyl- and butyryl-cholinesterase inhibitors', 'http://codes.bio/abcpred/')
# txt4('AutoWeka', 'An automated data mining software based on Weka', 'http://www.mt.mahidol.ac.th/autoweka/')
# txt4('ACPred', 'A computational tool for the prediction and analysis of anticancer peptides','http://codes.bio/acpred/')
# txt4('BioCurator', 'A web server for curating ChEMBL bioactivity data', 'http://codes.bio/biocurator/')
# txt4('CryoProtect', 'A web server for classifying antifreeze proteins from non-antifreeze proteins','http://codes.bio/cryoprotect/')
# txt4('ERpred', 'A web server for the prediction of subtype-specific estrogen receptor antagonists', 'http://codes.bio/erpred')
# txt4('HCVpred', 'A web server for predicting the bioactivity of Hepatitis C virus NS5B inhibitors', 'http://codes.bio/hemopred/')
# txt4('HemoPred', 'A web server for predicting the hemolytic activity of peptides', 'http://codes.bio/hemopred/')
# txt4('iQSP', 'A sequence-based tool for the prediction and analysis of quorum sensing peptides', 'http://codes.bio/iqsp/')
# txt4('Meta-iAVP', 'A sequence-based meta-predictor for improving the prediction of antiviral peptides', 'http://codes.bio/meta-iavp/')
# txt4('osFP', 'A web server for predicting the oligomeric state of fluorescent proteins', 'http://codes.bio/osfp/')
# txt4('PAAP', 'A web server for predicting antihypertensive activity of peptides', 'http://codes.bio/paap/')
# txt4('PepBio', 'A web server for predicting the bioactivity of host defense peptide', 'http://codes.bio/pepbio')
# txt4('PyBact', 'Open source software written in Python for bacterial identification', 'https://sourceforge.net/projects/pybact/')
# txt4('TargetAntiAngio', 'A sequence-based tool for the prediction and analysis of anti-angiogenic peptides','http://codes.bio/targetantiangio/')
# txt4('ThalPred', 'Development of decision model for discriminating Thalassemia trait and Iron deficiency anemia','http://codes.bio/thalpred/')
# txt4('THPep', 'A web server for predicting tumor homing peptides','http://codes.bio/thpep/')


#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `R`, `Linux`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`, `altair`, `ggplot2`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Deep Learning', '`TensorFlow`')
txt3('Web development', '`Flask`, `HTML`, `CSS`')
txt3('Model deployment', '`streamlit`, `gradio`, `R Shiny`, `Heroku`, `AWS`, `Digital Ocean`')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/shubhamkaser')
txt2('Twitter', 'https://twitter.com/kzr_sk')
txt2('GitHub', 'https://github.com/shubhamkaser/')
txt2('Instagram', 'https://instagram.com/kzr_sk')