import pandas as pd
import numpy as np
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
import src.config as cfg

# TODO is pool

def preprocess_new_col(df : pd.DataFrame) -> pd.DataFrame:
    df = df.fillna(value=0)
    df = df.astype(np.int8)
    return df


def add_bstmqual_norm(df : pd.DataFrame) -> pd.DataFrame:
    qual = {'Po': 1, 'Fa': 2,'TA': 3, 'Gd': 4, 'Ex': 5}
    df['BsmtQualNorm'] = df['BsmtQual'].astype('string').map(qual)
    df['BsmtQualNorm'] = preprocess_new_col(df['BsmtQualNorm'])
    return df

def add_bstmcond_norm(df : pd.DataFrame) -> pd.DataFrame:
    qual = {'Po': 1, 'Fa': 2,'TA': 3, 'Gd': 4, 'Ex': 5}
    df['BsmtCondNorm'] = df['BsmtCond'].astype('string').map(qual)
    df['BsmtCondNorm'] = preprocess_new_col(df['BsmtCondNorm'])
    return df

def add_heatingqc_norm(df : pd.DataFrame) -> pd.DataFrame:
    qual = {'Po': 1, 'Fa': 2,'TA': 3, 'Gd': 4, 'Ex': 5}
    df['HeatingQCNorm'] = df['HeatingQC'].astype('string').map(qual)
    df['HeatingQCNorm'] = preprocess_new_col(df['HeatingQCNorm'])
    return df

def add_kitchenqual_norm(df : pd.DataFrame) -> pd.DataFrame:
    qual = {'Po': 1, 'Fa': 2,'TA': 3, 'Gd': 4, 'Ex': 5}
    df['KitchenQualNorm'] = df['KitchenQual'].astype('string').map(qual)
    df['KitchenQualNorm'] = preprocess_new_col(df['KitchenQualNorm'])
    return df

def add_fireplacequ_norm(df : pd.DataFrame) -> pd.DataFrame:
    qual = {'Po': 1, 'Fa': 2,'TA': 3, 'Gd': 4, 'Ex': 5}
    df['FireplaceQuNorm'] = df['FireplaceQu'].astype('string').map(qual)
    df['FireplaceQuNorm'] = preprocess_new_col(df['FireplaceQuNorm'])
    return df

def add_bsmtfintype1_norm(df : pd.DataFrame) -> pd.DataFrame:
    qual = {'Unf': 1, 'LwQ': 2,'Rec': 3, 'BLQ': 4, 'ALQ': 5, 'GLQ': 6}
    df['BsmtFinType1Norm'] = df['BsmtFinType1'].astype('string').map(qual)
    df['BsmtFinType1Norm'] = preprocess_new_col(df['BsmtFinType1Norm'])
    return df


def feature_gen(df : pd.DataFrame) -> pd.DataFrame:
    df = add_bstmqual_norm(df)
    df = add_bstmcond_norm(df)
    df = add_heatingqc_norm(df)
    df = add_kitchenqual_norm(df)
    # df = add_fireplacequ_norm(df)
    df = add_bsmtfintype1_norm(df)
    return df