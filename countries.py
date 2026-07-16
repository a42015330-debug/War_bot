# countries.py


COUNTRIES = {


"ایران":
{
"population":85000000,
"power":70,
"oil":500
},


"آمریکا":
{
"population":330000000,
"power":95,
"oil":800
},


"روسیه":
{
"population":145000000,
"power":90,
"oil":900
},


"چین":
{
"population":1400000000,
"power":92,
"oil":700
},


"آلمان":
{
"population":83000000,
"power":80,
"oil":200
},


"ژاپن":
{
"population":125000000,
"power":82,
"oil":150
},


"ترکیه":
{
"population":85000000,
"power":75,
"oil":300
},


"انگلیس":
{
"population":67000000,
"power":85,
"oil":250
}


}



def get_country(name):

    return COUNTRIES.get(name)



def country_list():

    return list(COUNTRIES.keys())
