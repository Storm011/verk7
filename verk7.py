import pymysql
from bottle import *

@get('/')
def index():
    return template('index')

@route('/donyskra', method='POST')
def nyr():
    u = request.forms.get('user')
    p = request.forms.get('pass')
    n = request.forms.get('nafn')

    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='2608012360',passwd='mypassword', db='2608012360_verk7')
    cur = conn.cursor()

    cur.execute('SELECT count(*) FROM 2608012360_verk7.users where user=%s',(u))
    result = cur.fetchone()

    if result[0] == 0:
        cur.execute('INSERT INTO 2608012360_verk7.users Values(%s,%s,%s)',(u,p,n))
        conn.commit()
        cur.close()
        conn.close()
        return u," hefur verið skráður <br><a href='/'>Heim</a>"

    else:
        return u,"er frátekið notendanafn, reyndu aftur <br><a href='/#ny'>Nýskrá</a>"

@route('/doinnskra', method='POST')
def doinn():
    u = request.forms.get('user')
    p = request.forms.get('pass')

    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='2608012360',passwd='mypassword', db='2608012360_verk7')
    cur = conn.cursor()

    cur.execute('SELECT count(*) FROM 2608012360_verk7.users where user=%s and pass=%s',(u,p))
    result = cur.fetchone()
    print(result)

    if result[0]== 1:

        cur.close()
        conn.close()
        return template('leyni',u=u)
    else:
        return template('Ekkileyni')

@route('/members')
def member():
    conn = pymysql.connect(host="tsuts.tskoli.is",port=3306,user="2608012360",password="mypassword", db='2608012360_verk7')
    c = conn.cursor()
    c.execute("SELECT user FROM 2608012360_verk7.users")
    result = c.fetchall()
    c.close()
    output = template('members',rows = result)
    return output

try:
    run(host="0.0.0.0", port=os.environ.get('PORT'))
except:
    run(host='localhost', port= 7000, debug=True)
