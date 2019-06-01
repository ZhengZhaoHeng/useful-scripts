# Author: Zhaoheng Zheng
# zhaoheng.zheng@usc.edu
# Write HTML for visualization

from html_writer import Html
import datetime
import os

video_list = os.listdir('videos')

video_ids = [s.strip().split('.')[0] for s in video_list]

head = Html()
head.self_close_tag('meta', attributes=dict(charset='utf-8'))
body = Html()
count = 0
with body.tag('table', attributes=dict(border='1')):
    with body.tag('tr'):
        for opt in ['id', 'color', 'depth', 'normal']:
            with body.tag('th') as h:
                h += opt
    for idx in video_ids:
        count += 1
        with body.tag('tr'):
            with body.tag('td') as h:
                h += idx
            for opt in ['color', 'depth', 'normal']:
                with body.tag('td'):
                    with body.tag('video', attributes={'height': '256', 'width':'256', 'controls':1}) as h:
                        h.self_close_tag('source', 
                            attributes={
                                'src': os.path.join('videos', idx, '{}_{}.mp4'.format(idx, opt)),
                                'type' : 'video/mp4'
                            }
                        )
        if count > 10:
            break

with open("test.html", "w") as fp:
    fp.write(Html.html_template(head, body).to_raw_html(indent_size=2))
