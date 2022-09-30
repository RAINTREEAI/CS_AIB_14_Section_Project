from sklearn.model_selection import train_test_split
import readDB
import xgboost
import pickle


df = readDB.read_qvuafktk_DB()
df['pubDate'] = df['pubDate'].apply(lambda x: x.strftime('%Y%m%d'))
df['pubDate'] = df['pubDate'].str[:4].astype('int64')
df.drop(df[df['ReviewRank'] == 0].index, inplace=True)
index1 = df[df['priceSales'] > df['priceStandard']].index
df.drop(index1, inplace=True)
index2 = df[df['bestRank'] != 0].index
df.drop(index2, inplace=True)
target = 'priceSales'
X = df[['pubDate', 'priceStandard', 'ReviewRank']]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.80, test_size=0.20, random_state=2)
train_X = X_train.values
test_X = X_test.values


print('X_train shape', X_train.shape)
print('y_train shape', y_train.shape)
print('X_test shape', X_test.shape)
print('y_test shape', y_test.shape)

model = xgboost.XGBRegressor(n_estimators=100, learning_rate=0.08, gamma=0, subsample=0.75, colsample_bytree=1, max_depth=7)
model.fit(train_X, y_train)

with open('used_book_price/model_pickle/model.pkl','wb') as pickle_file:
    pickle.dump(model, pickle_file)