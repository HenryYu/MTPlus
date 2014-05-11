__author__ = 'yuziyuan'

from functools import wraps

def except_happen(event):
    def _except_happen(view_func):
        def _decorator(*args, **kwargs):
            if(event == ' world1'):
                return
            else:
                print 'before ' + event
            response = view_func(*args, **kwargs)
            # print 'after' + event
            return response
        return wraps(view_func)(_decorator)
    return _except_happen

@except_happen(' world')
@except_happen(' world1')
@except_happen(' world2')
def test(request = ' world'):
    print 'hello' + request

test(' henry')