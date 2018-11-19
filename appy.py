import pymysql
from bottle import *
from bottle import route, run, template
@get('/')
def index():
    return template('Static/index')

@route('/donyskra', method='POST')
def nyr():
    u = request.forms.get('user')
    p = request.forms.get('pass')
    n = request.forms.get('nafn')

    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='2507002960', passwd='mypassword',db='2704982729_Verkefni7')
    cur = conn.cursor()

    cur.execute("SELECT count(*) From 2704982729_Verkefni7.user where user=%s",(u))
    result = cur.fetchone()

    if result[0] == 0:
        cur.execute("Insert into 2704982729_Verkefni7.user Values(%s,%s,%s)", (u,p,n))
        conn.commit()
        cur.close()
        conn.close()
        return u, " hefur verið skráður <br><a href='/'>Heim</a>"
    else:
        return u, " frátekið notendanafn, reyndu aftur <br><a href='/#ny'>Nyskra</a>"

@route('/doinnskra', method='POST')
def doinn():
    u = request.forms.get('user')
    p = request.forms.get('pass')

    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='2704982729', passwd='mypassword',db='2704982729_Verkefni7')
    cur = conn.cursor()

    cur.execute("SELECT count(*) From 2704982729_Verkefni7.user where user=%s and pass=%s",(u,p))
    result = cur.fetchone()
    print(result)

    if result[0] == 1:
        cur.close()
        conn.close()
        return template('Static/leyni',u=u)
    else:
        return template('Static/ekkileyni')

@route('/members')
def member():
    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='2507002960', passwd='mypassword',db='2704982729_Verkefni7')
    cur = conn.cursor()
    cur.execute("SELECT nafn From 2704982729_Verkefni7.user")
    result = cur.fetchall()
    cur.close()
    output = template('Static/members', rows=result)
    return output



run(host='localhost', port=8080)

