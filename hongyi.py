#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/8 16:10
# @Author  : dx
# @File    : hongyi.py

from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def hello_world():
    return 'Hello Flask!'


@app.route('/v1/menu/<action>', methods=["GET", "POST"])
def menulist(action):
    if request.method == "GET":
        menus = [
            {'key': '/app/dashboard/index', 'title': u'首页', 'icon': 'mobile', },
            {
                'key': '/app/ui', 'title': 'UI', 'icon': 'scan',
                'sub': [
                    {'key': '/app/ui/buttons', 'title': u'按钮', 'icon': '', },
                    {'key': '/app/ui/icons', 'title': u'图标', 'icon': '', },
                    {'key': '/app/ui/spins', 'title': u'加载中', 'icon': '', },
                    {'key': '/app/ui/modals', 'title': u'对话框', 'icon': '', },
                    {'key': '/app/ui/notifications', 'title': u'通知提醒框', 'icon': '', },
                    {'key': '/app/ui/tabs', 'title': u'标签页', 'icon': '', },
                    {'key': '/app/ui/banners', 'title': u'轮播图', 'icon': '', },
                    {'key': '/app/ui/wysiwyg', 'title': u'富文本', 'icon': '', },
                    {'key': '/app/ui/drags', 'title': u'拖拽', 'icon': '', },
                    {'key': '/app/ui/gallery', 'title': u'画廊', 'icon': '', },
                    {'key': '/app/ui/map', 'title': u'地图'},
                ],
            },
        ]
        return jsonify(menus)
    else:
        res = {"res": "failed"}
        return jsonify(res)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
