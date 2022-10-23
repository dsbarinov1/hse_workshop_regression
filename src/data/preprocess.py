import pandas as pd
import numpy as np
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
import src.config as cfg

def drop_cols(df : pd.DataFrame, cols : list) -> pd.DataFrame:
    for col in cols:
        if col in df.columns:
           df =  df.drop(col, axis=1)
    return df


def cast_types(df: pd.DataFrame) -> pd.DataFrame:
    df[cfg.CAT_COLS] = df[cfg.CAT_COLS].astype('object')
    df[cfg.INT_COLS] = df[cfg.INT_COLS].astype(np.int32)
    df[cfg.REAL_COLS] = df[cfg.REAL_COLS].astype(np.float32)
    return df


def set_idx(df: pd.DataFrame, idx_col: str) -> pd.DataFrame:
    df = df.set_index(idx_col)
    return df

def fill_nan_categories(df: pd.DataFrame) -> pd.DataFrame:
    for category in cfg.CAT_COLS:
        df[category] = df[category].fillna(' ')
    return df


def fill_nan_integers(df: pd.DataFrame) -> pd.DataFrame:
    for integer in cfg.INT_COLS:
        df[integer] = df[integer].fillna(0)
    return df
    

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    df = set_idx(df, cfg.ID_COL)
    df = drop_cols(df, cfg.DROP_COLS)
    df = fill_nan_integers(df)
    df = fill_nan_categories(df)
    df = cast_types(df)
    return df


def preprocess_target(df: pd.DataFrame) -> pd.DataFrame:
    df = df.astype(np.int32)
    return df


def extract_target(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    df, target = df.drop(cfg.TARGET_COL, axis=1), df[cfg.TARGET_COL].copy()
    return df, target
