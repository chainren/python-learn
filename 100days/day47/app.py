from flask import Flask, request

from flask_restful import Api, Resource, reqparse

app = Flask(__name__)

# 初始化restful
api = Api(app)

# 定义全局的解析实体
parser = reqparse.RequestParser()
# 定义参数 id，类型必须是整数
parser.add_argument('id', type=int, help='必段提供参数id')
parser.add_argument('name', request=True)


# 定义资源
class HelloRESTful(Resource):
    def get(self):
        return {'greet': 'Hello Flask RESTful!'}


# 给资源绑定URI
api.add_resource(HelloRESTful, '/')


# 初始化待办列表
todos = {
    'todo_1': "读《程序员的自我修养》",
    'todo_2': "买点吃的",
    'todo_3': "去看星星"
}


# 资源是 Resource 类的子类，以请求方法( GET、POST 等)名称的小写形式定义的方法，能对对应方法的请求作出相应
class Todo(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}


api.add_resource(Todo, '/todo/<string:todo_id>/')

class Reqparser(Resource):
    def get(self):
        args = parser.parse_args() # 获取解析器中定义的参数 并校验
        return args

# 指定路由
api.add_resource(Reqparser, '/reqparser')       

if __name__ == '__main__':
    app.run(port=8888, debug=True)
