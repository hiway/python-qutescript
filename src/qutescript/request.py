# coding=utf-8


class Request(object):
    def __init__(self):
        self.mode = None
        self.user_agent = None
        self.fifo = None
        self.html = None
        self.text = None
        self.config_dir = None
        self.data_dir = None
        self.download_dir = None
        self.commandline_text = None
        self.url = None
        self.title = None
        self.selected_text = None
        self.selected_html = None

    def dump(self):
        return {
            'mode': self.mode,
            'user_agent': self.user_agent,
            'fifo': self.fifo,
            'html': self.html,
            'text': self.text,
            'config_dir': self.config_dir,
            'data_dir': self.data_dir,
            'download_dir': self.download_dir,
            'commandline_text': self.commandline_text,
            'url': self.url,
            'title': self.title,
            'selected_text': self.selected_text,
            'selected_html': self.selected_html,
        }


def build_request():
    import os
    request = Request()
    request.mode = os.getenv('QUTE_MODE')
    request.user_agent = os.getenv('QUTE_USER_AGENT')
    request.fifo = os.getenv('QUTE_FIFO')
    request.html = os.getenv('QUTE_HTML')
    request.text = os.getenv('QUTE_TEXT')
    request.config_dir = os.getenv('QUTE_CONFIG_DIR')
    request.data_dir = os.getenv('QUTE_DATA_DIR')
    request.download_dir = os.getenv('QUTE_DOWNLOAD_DIR')
    request.commandline_text = os.getenv('QUTE_COMMANDLINE_TEXT')
    request.url = os.getenv('QUTE_URL')
    request.title = os.getenv('QUTE_TITLE')
    request.selected_text = os.getenv('QUTE_SELECTED_TEXT')
    request.selected_html = os.getenv('QUTE_SELECTED_HTML')
    if not request.mode:
        raise AssertionError('Unable to read environment variables, did you pass `:spawn --userscript` ?')
    return request
