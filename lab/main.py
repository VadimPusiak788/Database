import cx_Oracle
import re
import chart_studio.plotly as py
import plotly.graph_objs as go
import chart_studio.dashboard_objs as dashboard
import chart_studio


username = 'hr'
password = '11'
database = 'localhost/ORCL'


def fileId_url(url):
    raw_filed = re.findall("~[A-z.]+/[0-9]+", url)[0][1:]
    return raw_filed.replace("/", ":")


connection = cx_Oracle.connect(username, password, database)

cursor = connection.cursor()

query1 = """select positions, count(player_name) as count_pos
from NBA_star
GROUP BY positions
order by count_pos DESC
"""

cursor.execute(query1)

dat = {}
for row in cursor:
    if row[0] in dat.keys():
        dat[row[0]] += int(row[1])
    else:
        dat[row[0]] = int(row[1])

data = [go.Bar(

    x=list(dat.keys()),
    y=list(dat.values())

)]

layout = go.Layout(
    xaxis=dict(
        titlefont=dict(
            family="monospace",
            size=18
        )
    ),
    yaxis=dict(
        autorange=True,
        rangemode="nonnegative",
        titlefont=dict(
            family="monospace",
            size=18
        )
    )
)

fig = go.Figure(data=data, layout=layout)

position_url = py.plot(fig, filename="first_url")

query2 = """select  round((count(player_name)/14) * 100, 2) as rate
    ,NVL(team, 0) as teams
from NBA_star
GROUP by NVL(team, 0)
order by teams DESC
"""
cursor.execute(query2)

teams = dict()

for row in cursor:
    teams[row[0]] = row[1]

team = go.Scatter(
    y=list(teams.keys()),
    x=list(teams.values())
)
data_about = [team]

tems_star_players_url = py.plot(data_about, filename='star_teams')

cursor.execute(query3)

years_star = dict()

for raw in cursor:
    years_star[raw[0]] = raw[1]

years_star_dynamic = go.Scatter(
    x=list(years_star.keys()),
    y=list(years_star.values())
)
data = [years_star_dynamic]
years_star_dunamic_url = py.plot(data, filename='years_star_dynamic')

my_dboard = dashboard.Dashboard()

x = fileId_url(position_url)
y = fileId_url(tems_star_players_url)
z = fileId_url(years_star_dunamic_url)

box_1 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': x,
    'title': 'Amount players on position'
}

box_2 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': y,
    'title': 'Amount star player in teams'
}

box_3 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': z,
    'title': 'Amount of star player for year'
}

my_dboard.insert(box_1)
my_dboard.insert(box_2, 'below', 1)
my_dboard.insert(box_3, 'left', 2)

py.dashboard_ops.upload(my_dboard, 'Dashboard for DB')

cursor.close()
connection.close()
