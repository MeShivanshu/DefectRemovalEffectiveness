import json

data = '''
{
    "Requirements" : [{
        "Requirements" : 81,
        "Analysis" : 21,
        "Design" : 17,
        "Coding" : 36,
        "Unit Testing" : 12,
        "Intergration Testing" : 7,
        "System Testing" : 14,
        "Field" : 3
        
    }],
    "Analysis": [{
        "Requirements" : null,
        "Analysis" : 29,
        "Design" : 17,
        "Coding" : 19,
        "Unit Testing" : 35,
        "Intergration Testing" : 15,
        "System Testing" : 39,
        "Field" : 2
        
    }],
    "Design": [{
        "Requirements" : null,
        "Analysis" : null,
        "Design" : 102,
        "Coding" : 55,
        "Unit Testing" : 8,
        "Intergration Testing" : 7,
        "System Testing" : 5,
        "Field" : 2             
        
    }],
    "Coding": [{
        "Requirements" : null,
        "Analysis" : null,
        "Design" : null,
        "Coding" : 402,
        "Unit Testing" : 156,
        "Intergration Testing" : 27,
        "System Testing" : 23,
        "Field" : 7       
        
    }],
    "Unit Testing": [{
        "Requirements" : null,
        "Analysis" : null,
        "Design" : null,
        "Coding" : null,
        "Unit Testing" : 51,
        "Intergration Testing" : null,
        "System Testing" : null,
        "Field" : null 
        
    }],
    "Integration Testing": [{
        "Requirements" : null,
        "Analysis" : null,
        "Design" : null,
        "Coding" : null,
        "Unit Testing" : null,
        "Intergration Testing" : 3,
        "System Testing" : null,
        "Field" : null 
        
    }],
    "System Testing": [{
        "Requirements" : null,
        "Analysis" : null,
        "Design" : null,
        "Coding" : null,
        "Unit Testing" : null,
        "Intergration Testing" : null,
        "System Testing" : 3,
        "Field" : null 
        
    }],
    "Field": [{
        "Requirements" : null,
        "Analysis" : null,
        "Design" : null,
        "Coding" : null,
        "Unit Testing" : null,
        "Intergration Testing" : null,
        "System Testing" : null,
        "Field" : 7
        
    }]
}
'''

count = sum(map(lambda x: int(x['Requirements']), json.loads(data)['Requirements']))

print(count)