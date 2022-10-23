from sklearn.utils.fixes import sklearn
import src.config as cfg
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import HistGradientBoostingRegressor
from catboost import CatBoostRegressor
from sklearn.pipeline import Pipeline

cat_pipe = Pipeline([
    ('ohe', OneHotEncoder(handle_unknown='ignore', sparse=False))
])

real_pipe = Pipeline([
    ('scaler', StandardScaler()),
])

preprocess_pipe = ColumnTransformer(transformers=[
    ('real_cols', real_pipe, cfg.REAL_COLS),
    ('cat_cols', cat_pipe, cfg.CAT_COLS),
])

HGBR = Pipeline([
    ('preprocess', preprocess_pipe),
    ('lr', HistGradientBoostingRegressor())
])

cb = CatBoostRegressor(iterations=100, cat_features=cfg.CAT_COLS, random_seed=cfg.RS)

