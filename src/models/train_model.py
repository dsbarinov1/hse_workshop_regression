# -*- coding: utf-8 -*-
import click
import logging
import os
import sys
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
from sklearn.model_selection import GridSearchCV
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from src.utils import save_as_pickle
import pandas as pd
from train import cb, HGBR


@click.command()
@click.argument('input_train_data_filepath', type=click.Path(exists=True))
@click.argument('input_train_target_filepath', type=click.Path(exists=True))
@click.argument('output_catboost_filepath', type=click.Path())
@click.argument('output_hgbr_filepath', type=click.Path())
def main(input_train_data_filepath, input_train_target_filepath, output_catboost_filepath, output_hgbr_filepath):

    logger = logging.getLogger(__name__)
    logger.info('training model...')

    train = pd.read_pickle(input_train_data_filepath)
    target = pd.read_pickle(input_train_target_filepath)

    cbr = cb.fit(train, target)
    HGBR_model= HGBR.fit(train, target)
    
    save_as_pickle(cbr, output_catboost_filepath)
    save_as_pickle(HGBR_model, output_hgbr_filepath)


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()