import  json

people_string = '''
{ 
 "people":[
  {
  "name" : "pratik yadav",
  "phone" : "9451444601",
  "Email" : ["pratiiikyadav@gmail.com" , "pratiiik1991@gmail.com"],
  "Adhar_card" : "True"
  },
  {
   "name" : "pragya yadav",
  "phone" : "9456789107",
  "Email" : ["pratiiikyadav@gmail.com" , "pratiiik1991@gmail.com"],
  "Adhar_card" : "True"
  }
 ]
}
'''

data = json.loads(people_string)
'''
json.load -- loads file into python object.
json.loads --- loads string into python 0bject

'''
print('{}\n'.format(data))
print('{}\n'.format(data['people']))

for i in data['people']:
    print(i)
    del i['Email'][1]
    print(i)
    i['Email'] = ''.join(i['Email'])
    print("\nAfter list key is converted to string: {}\n>>>>>>>>>>>>>".format(i))

#print(data)

new_data = json.dumps(data, indent=2, sort_keys=True)
print(new_data)
print("*********************************************************")
with open('jsonfile.json') as f:
    data = json.load(f)
    f.close()

for j in data:
    del j['xp']

print(data)

with open('newjson.json', 'w') as g:
    json.dump(data, g, indent= 2)

