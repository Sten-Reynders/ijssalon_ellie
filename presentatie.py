def presenteer(mijn_dict, totaal):
    for key,value in mijn_dict.items(): 
        print(f"{key} : {value} euro")

    print ("==========================")
    print(f"totaal : {totaal} euro")
    
'''
mijn_dict = {
    'vis' : 10,
    'vlees' : 25,
    'overige' : 15
}

totaal = 50

presenteer (mijn_dict, totaal)
'''