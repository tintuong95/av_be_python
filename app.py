from flask import Flask, jsonify, request
from flaskext.mysql import MySQL
from flask_restful import Resource, Api
from flask_cors import CORS
# Khởi tạo  Flask
app = Flask(__name__)
CORS(app)
# Khởi tạo MySQL
mysql = MySQL()

# Khởi tạo Flask RESTful API
api = Api(app)

# Kết nối cơ sở dữ liệu với backend
app.config['MYSQL_DATABASE_USER'] = 'paoquvvjdq7t9syi'
app.config['MYSQL_DATABASE_PASSWORD'] = 'bbfil4ptq4cg1qim'
app.config['MYSQL_DATABASE_DB'] = 'krl4un16ywb4ycgs'
app.config['MYSQL_DATABASE_HOST'] = 'bmlx3df4ma7r1yh4.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'

# Khởi tạo MySQL extension
mysql.init_app(app)



class DanhSachThietBi(Resource):
    #Lấy tất cả thiet bi
    def get(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("""SELECT * FROM `thietbi`""")
            rows = cursor.fetchall()
            return jsonify(rows)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()    
    #Tạo phường
    def post(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            _tenthietbi = str(request.form['tenthietbi'])
            _ngaynhap = str(request.form['ngaynhap'])
            _ngaysx = str(request.form['ngaysx'])
            _hsx = str(request.form['hsx'])
            _loai = str(request.form['loai'])
            _giaban = str(request.form['giaban'])
            _soluong = str(request.form['soluong'])
            # _daban = str(request.form['daban'])
          
            taoThietBiCmd = """INSERT INTO `thietbi`( `tenthietbi`, `ngaynhap`, `ngaysx`, `hsx`, `loai`, `giaban`, `soluong`, `daban`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
            cursor.execute(taoThietBiCmd, (
                _tenthietbi, _ngaynhap,_ngaysx,_hsx,_loai,_giaban,_soluong,0))
            conn.commit()
            response = jsonify(
                message='Created successfully!', id=cursor.lastrowid)
           
            response.status_code = 201
        except Exception as e:
            print(e)
            response = jsonify('Created failture!')
            response.status_code = 400
        finally:
            cursor.close()
            conn.close()
            return (response)


class ThietBi(Resource):
    # Lấy thiet bi theo id
    def get(self, thietbi_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                """SELECT * FROM `thietbi` WHERE `id`=%s""", (thietbi_id))
            rows = cursor.fetchall()
            return jsonify(rows)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    # Chỉnh sửa thiet bi theo id
    def put(self, thietbi_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            _tenthietbi = str(request.form['tenthietbi'])
            _ngaynhap = str(request.form['ngaynhap'])
            _ngaysx = str(request.form['ngaysx'])
            _hsx = str(request.form['hsx'])
            _loai = str(request.form['loai'])
            _giaban = str(request.form['giaban'])
            _soluong = str(request.form['soluong'])
            _daban = str(request.form['daban'])
            update_ThietBi_cmd = """UPDATE `thietbi` SET `tenthietbi`=%s,`ngaynhap`=%s,`ngaysx`=%s,`hsx`=%s,`loai`=%s,`giaban`=%s,`soluong`=%s,`daban`=%s WHERE `id`=%s"""
            cursor.execute(update_ThietBi_cmd, (_tenthietbi, _ngaynhap,_ngaysx,_hsx,_loai,_giaban,_soluong ,_daban,thietbi_id))
            conn.commit()
            response = jsonify('Updated successfully.')
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify('Updated failture.')
            response.status_code = 400
        finally:
            cursor.close()
            conn.close()
            return (response)
        
    # Delete thiet bi theo id
    def delete(self, thietbi_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                """DELETE FROM `thietbi` WHERE `id`=%s""", (thietbi_id))
            conn.commit()
            response = jsonify('deleted successfully.')
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify('Failed delete.')
            response.status_code = 400
        finally:
            cursor.close()
            conn.close()
            return (response)

class DanhSachDanhMuc(Resource):
    # Lấy tất cả danh muc
    def get(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("""SELECT * FROM `danhmuc`""")
            rows = cursor.fetchall()
            return jsonify(rows)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
    
    # Tạo danh muc moi
    def post(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            _ten = str(request.form['ten'])
            _mota = str(request.form['mota'])
            _trangthai = str(request.form['trangthai'])

            create_class_cmd = """INSERT INTO `danhmuc`( `ten`, `mota`, `trangthai`) VALUES (%s,%s,%s)"""
            cursor.execute(create_class_cmd, (
                _ten, _mota, _trangthai))
            conn.commit()
            response = jsonify(
                message='place added successfully.', id=cursor.lastrowid)
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify('Failed to add place.')
            response.status_code = 400
        finally:
            cursor.close()
            conn.close()
            return (response)



class DanhMuc(Resource):
    # lấy danh muc theo id
    def get(self, danhmuc_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                """SELECT * FROM `danhmuc` WHERE `id`=%s""", (danhmuc_id))
            rows = cursor.fetchall()
            return jsonify(rows)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    #Cập nhật danh muc theo id
    def put(self, danhmuc_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            _ten = str(request.form['ten'])
            _mota = str(request.form['mota'])
            _trangthai = str(request.form['trangthai'])

            update_user_cmd = """UPDATE `danhmuc` SET `ten`=%s,`mota`=%s,`trangthai`=%s WHERE `id`=%s"""
            cursor.execute(update_user_cmd, (_ten, _mota,
                           _trangthai,danhmuc_id))
            conn.commit()
            response = jsonify('place updated successfully.')
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify('Failed to update place.')
            response.status_code = 400
        finally:
            cursor.close()
            conn.close()
            return (response)
        
    #Xóa danh muc theo id
    def delete(self, danhmuc_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                """DELETE FROM `danhmuc` WHERE `id`=%s""", (danhmuc_id))
            conn.commit()
            response = jsonify('place deleted successfully.')
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify('Failed to delete place.')
            response.status_code = 400
        finally:
            cursor.close()
            conn.close()
            return (response)


# Danh sách routers
api.add_resource(DanhSachThietBi, '/danhsachthietbi', endpoint='danhsachthietbi')
api.add_resource(ThietBi, '/thietbi/<int:thietbi_id>', endpoint='thietbi')
api.add_resource(DanhSachDanhMuc, '/danhsachdanhmuc', endpoint='danhsachdanhmuc')
api.add_resource(DanhMuc, '/danhmuc/<int:danhmuc_id>', endpoint='danhmuc')

#Chạy applications
if __name__ == "__main__":
    app.run(debug=True)
