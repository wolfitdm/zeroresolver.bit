import json 

import requests    

def instruct_wallet(method, params):
    url = "http://127.0.0.1:8336/"
    payload = json.dumps({"method": method, "params": params})
    headers = {'content-type': "application/json", 'cache-control': "no-cache"}
    rpc_user = "PLACEHOLDER"
    rpc_password = "PLACEHOLDER"
    try:
        response = requests.request("POST", url, data=payload, headers=headers, auth=(rpc_user, rpc_password))
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print(e)
    except:
        print ('No response from Wallet, check Bitcoin is running on this machine')

def op_coin(name, value): 
    answer = instruct_wallet(name, [value])
    if answer['error'] != None:
       print (answer['error'])
       return True
    else:
       print (answer['result'])
       return False
    
file="./names.json"
with open(file) as f:
     data = json.load(f)
     new_dict = {}
     values_ = data.values()
     keys_ = data.keys()
     i = 0
     new_keys_ = []
     for k in keys_:
         k = k.replace(".bit", "")
         new_keys_.append(k)
     keys_ = new_keys_
     for v in values_:
         new_dict[v] = keys_[i]
         i = i + 1
     
     values_ = new_dict.keys()
     new_array = {}
     for v in values_:
         vlen = len(v)
         if not v.startswith("1") or vlen <= 3 or vlen > 40:
            continue
         
         if op_coin("name_new", v):
            new_array[v] = new_dict[v]
  
     with open('keys.json', 'w') as fe:
          fe.write(json.dumps(new_array, indent=2, sort_keys=True))
          
          
