# -*- coding: utf-8 -*-
import click
import logging
import sys
import os
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
from sklearn.model_selection import GridSearchCV
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from src.utils import load_pickle, save_as_pickle
import pandas as pd
import json

@click.command()
@click.argument('input_data_filepath', type=click.Path(exists=True))
@click.argument('input_catboost_filepath', type=click.Path(exists=True))
@click.argument('input_hgbr_filepath', type=click.Path(exists=True))
@click.argument('output_catboost_predict_filepath', type=click.Path())
@click.argument('output_hgbr_predict_filepath', type=click.Path())
def main(input_data_filepath, input_catboost_filepath, input_hgbr_filepath, output_catboost_predict_filepath, output_hgbr_predict_filepath):

    logger = logging.getLogger(__name__)
    logger.info('model inference...')

    df = pd.read_pickle(input_data_filepath)
    catboost = load_pickle(input_catboost_filepath)
    HGBR = load_pickle(input_hgbr_filepath)
    
    catboost_pred = catboost.predict(df)
    HGBR_pred = HGBR.predict(df)
    save_as_pickle(catboost_pred, output_catboost_predict_filepath)
    save_as_pickle(HGBR_pred, output_hgbr_predict_filepath)
    


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()