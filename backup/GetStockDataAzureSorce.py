#https://funcinsalways.scm.azurewebsites.net/DebugConsole

# import os
# import json
# import platform
# from pandas_datareader import data

# postreqdata = json.loads(open(os.environ['req']).read())
# response = open(os.environ['res'], 'w')

# itemCode = postreqdata['itemcode']

# df = data.DataReader("KRX:" + itemCode,"google" )

# df.index = df.index.strftime('%Y-%m-%d')

# df = df.drop('Open',1)
# df = df.drop('High',1)
# df = df.drop('Low',1)
# df = df.drop('Volume',1)

# response.write(df.to_json())
# response.close()

#==============================================================================================================================================================================
# import os
# import json

# postreqdata = json.loads(open(os.environ['req']).read())
# response = open(os.environ['res'], 'w')

# name = postreqdata[0]['name']
# code = postreqdata[0]['code']


# response.write("name : "+ name + " code : " + code)
# response.close()


# [
#     {
#         "code":"1", "name": "테스트"
#     },
#     {
#         "code":"2", "name": "테스트2"
#     }
# ]

#==============================================================================================================================================================================
# https://myfunctiontest01.scm.azurewebsites.net/DebugConsole

# import os
# import json
# import platform
# from pandas_datareader import data

# postreqdata = json.loads(open(os.environ['req']).read())
# response = open(os.environ['res'], 'w')

# itemCode = postreqdata['itemcode']

# df = data.DataReader("KRX:" + itemCode,"google" )

# df.index = df.index.strftime('%Y-%m-%d')

# df = df.drop('Open',1)
# df = df.drop('High',1)
# df = df.drop('Low',1)
# df = df.drop('Volume',1)

# response.write(df.to_json())
# response.close()


# {
#     "itemcode" : "005930"
# }

#==============================================================================================================================================================================
# https://myfunctiontest01.scm.azurewebsites.net/DebugConsole

# import os
# import json
# import platform
# from pandas_datareader import data
# from collections import OrderedDict

# postreqdata = json.loads(open(os.environ['req']).read())
# response = open(os.environ['res'], 'w')

# re = OrderedDict()

# for item in postreqdata['item']:
#     df = data.DataReader("KRX:" + item,"google" )
#     df.index = df.index.strftime('%Y-%m-%d')
#     re[item] = df.to_dict()["Close"]
    
# response.write(json.dumps(re))
# response.close()

# {
#     "item": ["005930","066570"]
# }
