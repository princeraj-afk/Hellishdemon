import pickle
# import requests
# url='http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
# respons=requests.get(url)
# respons_text=respons.text
# data=respons_text.splitlines()
# read=[[i] for i in data]
# print("\n")
# #pickling the python object
# fileobj=open('irisData2.pkl','wb')
# pickle.dump(data,fileobj)
# fileobj.close()

# #Reading Of Pickel file
fileobj=open('irisData2.pkl','rb')
data=pickle.load(fileobj)
print(data)