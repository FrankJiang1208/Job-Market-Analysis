from flask import Flask, render_template, redirect
from flask import request
import pandas as pd
import numpy as np
import re
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import joblib




app = Flask(__name__)

@app.route("/")
def index():
    listings = {'_id':'615f3911a6d569a7cd86c945',
 'url': 'https://www.sportspromedia.com/news/nfl-data-analytics-excitement-engagement-paul-ballew/',
 'img': 'https://dd20lazkioz9n.cloudfront.net/wp-content/uploads/2021/11/NFL-Data-NEWS.jpg',
 'title': 'NFL using data analytics to monitor excitement level of each game'}
    return render_template("index.html",listings=listings)

@app.route("/slides")
def slides():
    return render_template("slides.html")

@app.route("/job_cat")
def jm():
    return render_template("jobs_by_category_mw.html")
    

@app.route("/job_market")
def jc():
    return render_template("job_market_map_visual_mw.html")
    

@app.route("/salary")
def sa():
    return render_template("as_charts.html")

@app.route("/employment_info")
def ei():
    return render_template("as_map.html")

@app.route("/skill")
def sk():
    return render_template("job_desc_skills_mw.html")

@app.route("/gov_job")
def gj():
    return render_template("cpj_gov_jobs.html")


# @app.route('/salary_prediction',methods=['GET', 'POST'])
# def sp():
#     if request.method == 'POST':
#         names = request.form.to_dict()
#         skill=skill_check(names)
#         job=job_title(names["titles"])
#         cat=category(names["industry"])
#         state=state1(names["state"])
#         sen=seniority(names["seniority"])
#         input=list(skill.values())+list(job.values())+list(cat.values())+list(state.values())+list(sen.values())
#         df=pd.DataFrame([input],columns=column_list)
#         pred=salary_category( model.predict(df)[0])
#         return render_template('salary_prediction_sj.html',pred=pred)
#     elif request.method=='GET':
#         return render_template('salary_prediction_sj.html')
#     else:
#         return render_template('salary_prediction_sj.html')


if __name__ == "__main__":
    app.run(debug=True)
