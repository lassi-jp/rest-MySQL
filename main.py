from flask import Flask, request, jsonify
import mysql.connector
app = Flask(__name__)


@app.route('/get-item/<key>', methods=['GET'])
def get_single_item(key):
    key = str(key)
    sql = f'SELECT body FROM `sample`.`restDB` WHERE itemKey = \"{key}\"'
    print(sql)
    result = execute_sql(sql)
    if check_uni_key(key):
        return 'Invalid data'
    else:
        return result[0][0]

@app.route('/delete-item/<key>', methods=['DELETE'])
def delete_single_item(key):
    key = str(key)
    sql = f'DELETE FROM restDB WHERE itemKey = \"{key}\"'
    try:
        execute_sql(sql)
        return jsonify({'success': True}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400


@app.route('/create-item/', methods=['POST'])
def create_single_item():
    try:
        request_json = request.json
        key = str(request_json.get('key'))
        body = request_json.get('body')
        if check_uni_key(key):
            sql = f'INSERT INTO `restDB` (`itemKey`,`body`) VALUE(\"{key}\",\"{body}\")'
            execute_sql(sql)
            return jsonify({'success': True}), 200
        else:
            return jsonify({'success': False, 'error': 'Key already exists!'}), 403
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

def conn_db():
    conn = mysql.connector.connect(
        host='127.0.0.1',
        port='23306',
        user='root',
        passwd='new_root_password',
        db='sample'
    )
    return conn


def execute_sql(sql):
    global rows
    try:
        conn = conn_db()
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
    except:
        print('DB connection Error.')
        return False
    return rows


def check_uni_key(key):
    key = str(key)
    sql = f'SELECT id FROM `sample`.`restDB` WHERE itemKey = \"{key}\"'
    conn = conn_db()
    cur = conn.cursor()
    cur.execute(sql)
    row = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    num_rows = len(row)
    if num_rows < 1:
        return True
    else:
        return False

if __name__ == '__main__':
    app.run()
