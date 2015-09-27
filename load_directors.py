__author__ = 'michalmucha'

from graph_zinoplex.models import GraphNode
from display.models import Profile, PPI_scorecard, WorkExperience, Company
from datetime import date, datetime
import pandas

def create_director(director_id, f_name, last_name, m_name=None, honor=None, degree=None, dob=None):
    g = GraphNode()
    g.save()
    p = Profile(first_name=f_name, last_name=last_name, director_id=director_id, graph_node=g)

    if pandas.notnull(honor):
        if honor not in ['Mr', 'Ms', 'Mrs', 'Unknown']:
            p.honor = honor

    if pandas.notnull(degree):
        p.degree = degree

    if pandas.notnull(m_name):
        p.middle_name = m_name

    if pandas.notnull(dob):
        try:
            p.birth_date = date(dob.year, dob.month, dob.day)
        except:
            pass

    p.save()
    g.save()

def create_work_experience(director_id, company_name, position, ddate):
    p = Profile.objects.get(director_id=int(director_id))
    c, created = Company.objects.get_or_create(name=str(company_name))

    w = WorkExperience(user_profile=p, company=c)
    if pandas.notnull(position):
        w.position = position
    if pandas.notnull(ddate):
        try:
            if isinstance(ddate, datetime):
                w.date_ended = date(ddate.year, ddate.month, ddate.day)
            else:
                w.date_ended = date(int(ddate), 7, 1)
        except:
            pass

    w.save()

def create_PPI(director_id, b, c, d ,e):
    p = Profile.objects.get(director_id=director_id)
    sc = PPI_scorecard(user_profile=p, index_b=b, index_c=c, index_d=d, index_e=e)

    sc.save()

def load_directors():
    d_dob = pandas.read_excel('director_data/director DOB.xlsx')
    for index, row in d_dob.iterrows():
    # for index, row in list(d_dob.iterrows())[:10]:
        try:
            create_director(row.DirectorID, row.Forename1, row.Surname, row.Forename2, row.Title, row.SuffixTitle, row.DOB)
        except Exception as e:
            print('Failed creating director', row, '\n', e)

def load_work_exp():
    all_ed = pandas.read_excel('director_data/all education.xlsx')
    for index, row in all_ed.iterrows():
    # for index, row in list(all_ed.iterrows())[:10]:
        try:
            create_work_experience(row.DirectorID, row.CompanyName, row.Qualification, row.AwardDate)
        except Exception as e:
            print('Failed creating experience:', row, '\n', e)

def load_ppi():
    nodes = pandas.read_csv('director_data/nodes-utf8.csv', delimiter=';')
    for index, row in nodes.iterrows():
    # for index, row in list(nodes.iterrows())[:10]:
        try:
            create_PPI(row.v, row.index_b, row.index_c, row.index_d, row.index_e)
        except Exception as e:
            print('Failed creating PPI scorecard:', row,'\n',e)