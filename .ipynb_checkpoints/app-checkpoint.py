import pickle
from flask import Flask, render_template, request

app = Flask(__name__)
model = pickle.load(open('job.pkl','rb'))
@app.route('/', methods = ['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route("/predict", methods = ['Post'])
def predict():
    if request.method == 'POST':
    #jobs
        if(request.form['jobs']=='Bartender'):
             chef = 0
             cook = 0
             event_coordinator = 0
             hospitality = 0
             managerial = 0
             receptionist = 0
             waiter = 0
        elif(request.form['jobs']=='Chef'):
             chef = 1
             cook = 0
             event_coordinator = 0
             hospitality = 0
             managerial = 0
             receptionist = 0
             waiter = 0
        elif(request.form['jobs']=='Cook'):
             chef = 0
             cook = 1
             event_coordinator = 0
             hospitality = 0
             managerial = 0
             receptionist = 0
             waiter = 0
        elif(request.form['jobs']=='Event Coordinator'):
             chef = 0
             cook = 0
             event_coordinator = 1
             hospitality = 0
             managerial = 0
             receptionist = 0
             waiter = 0
        elif(request.form['jobs']=='Hospitality'):
             chef = 0
             cook = 0
             event_coordinator = 0
             hospitality = 1
             managerial = 0
             receptionist = 0
             waiter = 0
        elif(request.form['jobs']=='Managerial'):
             chef = 0
             cook = 0
             event_coordinator = 0
             hospitality = 0
             managerial = 1
             receptionist = 0
             waiter = 0
        elif(request.form['jobs']=='Receptionist'):
             chef = 0
             cook = 0
             event_coordinator = 0
             hospitality = 0
             managerial = 0
             receptionist = 1
             waiter = 0
        else:
             chef = 0
             cook = 0
             event_coordinator = 0
             hospitality = 0
             managerial = 0
             receptionist = 0
             waiter = 1
#job type
        if(request.form['job_type']=='Contract'):
            permanent = 0
            temporary = 0
        elif(request.form['job_type']=='Permanent'):
            permanent = 1
            temporary = 0
        else:
            permanent = 0
            temporary = 1
#job nature
        if(request.form['job_nature']=='Full Time'):
            full_o_part = 0
            part_time = 0
        elif(request.form['job_nature']=='Full Time or Part Time'):
            full_o_part = 1
            part_time = 0
        else:
            full_o_part = 0
            part_time = 1

#region
        if(request.form['region']=='Channel Islands'):
             east_england = 0
             east_midlands = 0
             greater_london = 0
             north_east_england = 0
             north_west_england = 0
             northern_ireland = 0
             scotland = 0
             south_east_england = 0
             south_west_england = 0
             wales = 0
             west_midland = 0
             yorkshire_and_humber = 0
        elif(request.form['region']=='East England'):
              east_england = 1
              east_midlands = 0
              greater_london = 0
              north_east_england = 0
              north_west_england = 0
              northern_ireland = 0
              scotland = 0
              south_east_england = 0
              south_west_england = 0
              wales = 0
              west_midland = 0
              yorkshire_and_humber = 0
        elif(request.form['region']=='East Midlands'):
             east_england = 0
             east_midlands = 1
             greater_london = 0
             north_east_england = 0
             north_west_england = 0
             northern_ireland = 0
             scotland = 0
             south_east_england = 0
             south_west_england = 0
             wales = 0
             west_midland = 0
             yorkshire_and_humber = 0
        elif(request.form['region']=='Greater London'):
             east_england = 0
             east_midlands = 0
             greater_london = 1
             north_east_england = 0
             north_west_england = 0
             northern_ireland = 0
             scotland = 0
             south_east_england = 0
             south_west_england = 0
             wales = 0
             west_midland = 0
             yorkshire_and_humber = 0
        elif(request.form['region']=='North East England'):
              east_england = 0
              east_midlands = 0
              greater_london = 0
              north_east_england = 1
              north_west_england = 0
              northern_ireland = 0
              scotland = 0
              south_east_england = 0
              south_west_england = 0
              wales = 0
              west_midland = 0
              yorkshire_and_humber = 0
        elif(request.form['region']=='North West England'):
             east_england = 0
             east_midlands = 0
             greater_london = 0
             north_east_england = 0
             north_west_england = 1
             northern_ireland = 0
             scotland = 0
             south_east_england = 0
             south_west_england = 0
             wales = 0
             west_midland = 0
             yorkshire_and_humber = 0
        elif(request.form['region']=='Northern Ireland'):
              east_england = 0
              east_midlands = 0
              greater_london = 0
              north_east_england = 0
              north_west_england = 0
              northern_ireland = 1
              scotland = 0
              south_east_england = 0
              south_west_england = 0
              wales = 0
              west_midland = 0
              yorkshire_and_humber = 0
        elif(request.form['region']=='Scotland'):
              east_england = 0
              east_midlands = 0
              greater_london = 0
              north_east_england = 0
              north_west_england = 0
              northern_ireland = 0
              scotland = 1
              south_east_england = 0
              south_west_england = 0
              wales = 0
              west_midland = 0
              yorkshire_and_humber = 0
        elif(request.form['region']=='South East England'):
              east_england = 0
              east_midlands = 0
              greater_london = 0
              north_east_england = 0
              north_west_england = 0
              northern_ireland = 0
              scotland = 0
              south_east_england = 1
              south_west_england = 0
              wales = 0
              west_midland = 0
              yorkshire_and_humber = 0
        elif(request.form['region']=='South West England'):
              east_england = 0
              east_midlands = 0
              greater_london = 0
              north_east_england = 0
              north_west_england = 0
              northern_ireland = 0
              scotland = 0
              south_east_england = 0
              south_west_england = 1
              wales = 0
              west_midland = 0
              yorkshire_and_humber = 0
        elif(request.form['region']=='Wales'):
              east_england = 0
              east_midlands = 0
              greater_london = 0
              north_east_england = 0
              north_west_england = 0
              northern_ireland = 0
              scotland = 0
              south_east_england = 0
              south_west_england = 0
              wales = 1
              west_midland = 0
              yorkshire_and_humber = 0
        elif(request.form['region']=='West Midland'):
              east_england = 0
              east_midlands = 0
              greater_london = 0
              north_east_england = 0
              north_west_england = 0
              northern_ireland = 0
              scotland = 0
              south_east_england = 0
              south_west_england = 0
              wales = 0
              west_midland = 1
              yorkshire_and_humber = 0
        else:
              east_england = 0
              east_midlands = 0
              greater_london = 0
              north_east_england = 0
              north_west_england = 0
              northern_ireland = 0
              scotland = 0
              south_east_england = 0
              south_west_england = 0
              wales = 0
              west_midland = 0
              yorkshire_and_humber = 1
        #

        

        if(request.form['experience']=='Yes'):
            experience = 1
        else:
            experience = 0
            
        prediction = model.predict([[chef,cook,event_coordinator,hospitality,managerial,receptionist,waiter,permanent,temporary,full_o_part,part_time,east_england,east_midlands,greater_london,north_east_england,north_west_england,northern_ireland,scotland,south_east_england,south_west_england,wales,west_midland,yorkshire_and_humber,experience]])
        output = round(prediction[0],2)
        if output < 0:

            return render_template('prediction.html', prediction_texts = "sorry can't find the result")
           
        else:
            job_p = request.form['jobs']
            job_ty_p = request.form['job_type']
            job_nat_p = request.form['job_nature']
            region_p = request.form['region']
            exp_p = request.form['experience']


            return render_template('prediction.html', job_p =job_p, job_ty_p=job_ty_p, job_nat_p=job_nat_p, region_p=region_p, exp_p=exp_p, prediction_texts = "Predicted salary is {} ".format(output))
            
    else:
        return render_template('prediction.html',prediction_texts = 'Sorry! Invalid Entry')   


if __name__=='__main__':
    app.run(debug=True)       