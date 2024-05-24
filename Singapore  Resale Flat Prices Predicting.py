import numpy as np
import pickle
import streamlit as st
from PIL import Image

def load_model():
    with open("Resale_Flat_Prices_Model_1.pkl", "rb") as f:
        return pickle.load(f)

def town_mapping(town):
    town_map = {
        'ANG MO KIO': 0, 'BEDOK': 1, 'BISHAN': 2, 'BUKIT BATOK': 3, 'BUKIT MERAH': 4,
        'BUKIT PANJANG': 5, 'BUKIT TIMAH': 6, 'CENTRAL AREA': 7, 'CHOA CHU KANG': 8,
        'CLEMENTI': 9, 'GEYLANG': 10, 'HOUGANG': 11, 'JURONG EAST': 12, 'JURONG WEST': 13,
        'KALLANG/WHAMPOA': 14, 'MARINE PARADE': 15, 'PASIR RIS': 16, 'PUNGGOL': 17,
        'QUEENSTOWN': 18, 'SEMBAWANG': 19, 'SENGKANG': 20, 'SERANGOON': 21, 'TAMPINES': 22,
        'TOA PAYOH': 23, 'WOODLANDS': 24, 'YISHUN': 25
    }
    return town_map.get(town, -1)

def flat_type_mapping(flat_type):
    flat_map = {
        '3 ROOM': 2, '4 ROOM': 3, '5 ROOM': 4, '2 ROOM': 1, 'EXECUTIVE': 5,
        '1 ROOM': 0, 'MULTI-GENERATION': 6
    }
    return flat_map.get(flat_type, -1)

def flat_model_mapping(flat_model):
    model_map = {
        'Improved': 5, 'New Generation': 12, 'Model A': 8, 'Standard': 17, 'Simplified': 16,
        'Premium Apartment': 13, 'Maisonette': 7, 'Apartment': 3, 'Model A2': 10, 'Type S1': 19,
        'Type S2': 20, 'Adjoined flat': 2, 'Terrace': 18, 'DBSS': 4, 'Model A-Maisonette': 9,
        'Premium Maisonette': 15, 'Multi Generation': 11, 'Premium Apartment Loft': 14,
        'Improved-Maisonette': 6, '2-room': 0, '3Gen': 1
    }
    return model_map.get(flat_model, -1)

def predict_price(year, town, flat_type, flr_area_sqm, flat_model,
                  stry_start, stry_end, re_les_year, re_les_month, les_coms_dt):
    try:
        model = load_model()
        town_1 = town_mapping(town)
        flat_type_1 = flat_type_mapping(flat_type)
        flat_model_1 = flat_model_mapping(flat_model)
        str_str = np.log(stry_start)
        str_end = np.log(stry_end)

        user_data = np.array([[int(year), town_1, flat_type_1, int(flr_area_sqm),
                                flat_model_1, str_str, str_end, int(re_les_year),
                                int(re_les_month), int(les_coms_dt)]])
        predicted_price = np.exp(model.predict(user_data))[0]

        return round(predicted_price, 2)

    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

st.set_page_config(layout="wide")
st.title("SINGAPORE RESALE FLAT PRICES PREDICTING")
st.write("")

with st.sidebar:
    select = st.radio("MAIN MENU", ["Home", "Price Prediction", "About"])

if select == "Home":
    img = Image.open("0_hn4nICHk9Cq-tugt.jpg")
    st.image(img)
    
    st.write('''The majority of Singaporeans live in public housing provided by the HDB.
    HDB flats can be purchased either directly from the HDB as a new unit or through the resale market from existing owners.''')
    
    st.header(":blue[Resale Process:]")
    st.write('''In the resale market, buyers purchase flats from existing flat owners, and the transactions are facilitated through the HDB resale process.
    The process involves a series of steps, including valuation, negotiations, and the submission of necessary documents.''')
    
    st.header(":blue[Valuation:]")
    st.write('''The HDB conducts a valuation of the flat to determine its market value. 
             This is important for both buyers and sellers in negotiating a fair price.''')
    
    st.header(":blue[Eligibility Criteria:]")
    st.write('''Buyers and sellers in the resale market must meet certain eligibility criteria, 
             including citizenship requirements and income ceilings.''')
    
    st.header(":blue[Resale Levy:]")
    st.write('''For buyers who have previously purchased a subsidized flat from the HDB, 
             there might be a resale levy imposed when they purchase another flat from the HDB resale market.''')
    
    st.header(":blue[Grant Schemes:]")
    st.write('''There are various housing grant schemes available to eligible buyers, 
             such as the CPF Housing Grant, which provides financial assistance for the purchase of resale flats.''')
    
    st.header(":blue[HDB Loan and Bank Loan:]")
    st.write('''Buyers can choose to finance their flat purchase through an HDB loan or a bank loan. 
             HDB loans are provided by the HDB, while bank loans are obtained from commercial banks.''')
    
    st.header(":blue[Market Trends:]")
    st.write('''The resale market is influenced by various factors such as economic conditions, interest rates, and government policies. 
             Property prices in Singapore can fluctuate based on these factors.''')
    
    st.header(":blue[Online Platforms:]")
    st.write("There are online platforms and portals where sellers can list their resale flats, and buyers can browse available options.")

    

elif select == "Price Prediction":

    col1,col2= st.columns(2)
    with col1:

        year= st.selectbox("Select the Year",["2015", "2016", "2017", "2018", "2019", "2020", "2021",
                           "2022", "2023", "2024"])
        
        town= st.selectbox("Select the Town", ['ANG MO KIO', 'BEDOK', 'BISHAN', 'BUKIT BATOK', 'BUKIT MERAH',
                                            'BUKIT PANJANG', 'BUKIT TIMAH', 'CENTRAL AREA', 'CHOA CHU KANG',
                                            'CLEMENTI', 'GEYLANG', 'HOUGANG', 'JURONG EAST', 'JURONG WEST',
                                            'KALLANG/WHAMPOA', 'MARINE PARADE', 'PASIR RIS', 'PUNGGOL',
                                            'QUEENSTOWN', 'SEMBAWANG', 'SENGKANG', 'SERANGOON', 'TAMPINES',
                                            'TOA PAYOH', 'WOODLANDS', 'YISHUN'])
        
        flat_type= st.selectbox("Select the Flat Type", ['3 ROOM', '4 ROOM', '5 ROOM', '2 ROOM', 'EXECUTIVE', '1 ROOM',
                                                        'MULTI-GENERATION'])
        
        flr_area_sqm= st.number_input("Enter the Value of Floor Area sqm (Min: 31 / Max: 280")

        flat_model= st.selectbox("Select the Flat Model", ['Improved', 'New Generation', 'Model A', 'Standard', 'Simplified',
                                                        'Premium Apartment', 'Maisonette', 'Apartment', 'Model A2',
                                                        'Type S1', 'Type S2', 'Adjoined flat', 'Terrace', 'DBSS',
                                                        'Model A-Maisonette', 'Premium Maisonette', 'Multi Generation',
                                                        'Premium Apartment Loft', 'Improved-Maisonette', '2-room', '3Gen'])
        
    with col2:

        stry_start= st.number_input("Enter the Value of Storey Start")

        stry_end= st.number_input("Enter the Value of Storey End")

        re_les_year= st.number_input("Enter the Value of Remaining Lease Year (Min: 42 / Max: 97)")

        re_les_month= st.number_input("Enter the Value of Remaining Lease Month (Min: 0 / Max: 11)")
        
        les_coms_dt= st.selectbox("Select the Lease_Commence_Date", [str(i) for i in range(1966,2023)])

    button= st.button("Predict the Price", use_container_width= True)

    if button:

            
        pre_price= predict_price(year, town, flat_type, flr_area_sqm, flat_model,
                        stry_start, stry_end, re_les_year, re_les_month, les_coms_dt)

        st.write("## :green[**The Predicted Price is :**]",pre_price)

elif select == "About":
    # Add content for about page
    st.write("Data Collection and Preprocessing... ")
    
    st.header(":blue[Data Collection and Preprocessing:]")
    st.write("Gather a dataset of resale flat transactions from the Singapore Housing and Development Board (HDB) spanning from 1990 to the present.")
    st.write("Preprocess the data to cleanse and structure it in a format suitable for machine learning analysis.")

    st.header(":blue[Feature Engineering:]")
    st.write("Identify and extract pertinent features from the dataset, such as town, flat type, storey range, floor area, flat model, and lease commencement date.")
    st.write("Introduce any supplementary features that could augment prediction accuracy.")
    
    st.header(":blue[Model Selection and Training:]")
    st.write("Choose an appropriate regression-based machine learning model, such as linear regression, decision trees, or random forests.")
    st.write("Train the selected model using historical data, utilizing a segment of the dataset for training purposes.")

    st.header(":blue[Model Evaluation:]")
    st.write('''Assess the predictive capability of the trained model through various regression metrics, 
             including Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and R2 Score.''')
    
    st.header(":blue[Streamlit Web Application:]")
    st.write("Develop a user-friendly web application using Streamlit, enabling users to input flat details like town, flat type, storey range, etc.")
    st.write("Utilize the trained machine learning model within the application to predict the resale price based on user-provided inputs.")
    
    st.header(":blue[Deployment on Render:]")
    st.write("Deploy the Streamlit application on the Render platform to ensure accessibility to users via the internet.")
    
    st.header(":blue[Testing and Validation:]")
    st.write("Conduct comprehensive testing of the deployed application to validate its functionality and ensure accurate predictions are delivered.")