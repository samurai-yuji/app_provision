# coding: utf-8

import tornado.ioloop
import tornado.web
import os
import json

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class PostHandler(tornado.web.RequestHandler):

    def provisioning(self,router):
        # Do whatever about provisioning!!
        return True

    def post(self):
        result = {}
        data = json.loads(self.get_argument("json"))
        for router,is_target in data.items():
            if is_target:
                result[router] = self.provisioning(router)
        self.write(json.dumps(result))

application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/post", PostHandler)
    ],
    template_path=os.path.join(os.getcwd(),  "templates"),
    static_path=os.path.join(os.getcwd(),  "static")
    )

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

