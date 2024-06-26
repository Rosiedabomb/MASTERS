import pandas as pd
import numpy as np
import xgboost as xgb
#importing numpy libraries

# this file will contain functions to calculate the input values from the
def extract_peak_values(path):
    '''Extract peak kinematics (linear acceleration, rotational acceleration and rotational velocity
    values from csv file containing time series.
    Returns: a tuple containing peak rotational velocity, peak linear acceleration, and peak rotational acceleration 
    '''
    #if path is not csv say 'not correct file type', please use csv
    #open csv, convert to dataframe
    df = pd.read_csv(path)
    la_r = df['la_r'].values
    ra_r = df['ra_r'].values
    rv_r = df['rv_r'].values

    #search for peak values
    peak_lin_acc = la_r[(np.abs(la_r)).argmax()] #peak searched value from csv
    peak_rot_vel = rv_r[(np.abs(rv_r)).argmax()] #peak searched value from csv
    peak_rot_acc = ra_r[(np.abs(ra_r)).argmax()] #peak searched value from csv

    return peak_lin_acc, peak_rot_acc, peak_rot_vel

#predicting strain
def predict_strain_90th(peak_lin_acc, peak_rot_acc, peak_rot_vel,):
    '''
    predict 90th percentile strain based on peak values of kinematics
    parameters: peak kinematics (maximum magnitude)
    returns: predicted 90th percentile strain
    '''
    loaded_model = xgb.XGBRegressor()
    loaded_model.load_model('G:/MASTERS/resultant_strain_xgb.json') # load the saved/pretrained model
    #['peak rot acc resultant','peak lin acc resultant','peak rot vel resultant',]
    #'make inputs into correct format.
    input_df = pd.DataFrame([[peak_rot_acc, peak_lin_acc, peak_rot_vel]], 
                            columns=['peak rot acc resultant', 'peak lin acc resultant', 'peak rot vel resultant'])
    prediction = loaded_model.predict(input_df) #xgboost prediction
    return prediction

def predict_strainrate_90th(peak_lin_acc, peak_rot_acc, peak_rot_vel,):
    '''
    predict 90th percentile strain based on peak values of kinematics
    parameters: peak kinematics (maximum magnitude)
    returns: predicted 90th percentile strainrate
    '''
    # Load model from file
    loaded_model = xgb.XGBRegressor()
    loaded_model.load_model('G:/MASTERS/resultant_strainrate_xgb.json') # load the saved/pretrained model
    #['peak rot acc resultant','peak lin acc resultant','peak rot vel resultant',]
    #'make inputs into correct format.
    input_df = pd.DataFrame([[peak_rot_acc, peak_lin_acc, peak_rot_vel]], 
                            columns=['peak rot acc resultant', 'peak lin acc resultant', 'peak rot vel resultant'])
    prediction = loaded_model.predict(input_df) #xgboost prediction
    return prediction
