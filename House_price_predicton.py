import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer

train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

X = train[['LotArea', 'BsmtFinSF1', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF', '1stFlrSF', '2ndFlrSF',
           'LowQualFinSF', 'GrLivArea', 'FullBath', 'HalfBath', 'BedroomAbvGr', 'GarageArea', 'WoodDeckSF',
           'OpenPorchSF', 'EnclosedPorch', '3SsnPorch', 'ScreenPorch', 'PoolArea']]
y = train['SalePrice']
Xtest = test[['LotArea', 'BsmtFinSF1', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF', '1stFlrSF', '2ndFlrSF',
              'LowQualFinSF', 'GrLivArea', 'FullBath', 'HalfBath', 'BedroomAbvGr', 'GarageArea', 'WoodDeckSF',
              'OpenPorchSF', 'EnclosedPorch', '3SsnPorch', 'ScreenPorch', 'PoolArea']]

model = LinearRegression()

imput = SimpleImputer(strategy='mean')
X = imput.fit_transform(X)
Xtest = imput.transform(Xtest)

model.fit(X, y)
pred = model.predict(Xtest)
output = pd.DataFrame({'Id': test['Id'], 'SalePrice': pred})
output.to_csv('predictions.xlsx', index=False)
print(output)